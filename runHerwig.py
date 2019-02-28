
"""
runHerwig.py

Creates .in-files for Herwig for the combinations in simSettings.py and then runs through them.

"""


import os
import subprocess
import sys
import time
import math
import glob
import errno
import multiprocessing as mp 
import simSettings as sets 

def get_abspath(path):
   """
   Returns absolute path of input path.
   """
   if path.startswith("~"):
      return os.path.expanduser(path)
   else:
      return os.path.abspath(path)

def run_herwig(infile,nAnn,annCh,sun=False):
	"""
	Runs Herwig on the provided infile and puts results for the run in outDir.
	Input: infile - a .in-file to be run as "Herwig read infile"
	       nAnn - number of annihilations
	       annCh - the annihilation channel
	       sun - whether to set up for the sun or not (default is halo)
	Returns: path to infile, error code, time spent (s)
	"""
	start=time.time()
	if os.path.split(os.getcwd())[1]!="Herwig":
		os.chdir(os.path.join(os.getcwd(),"Herwig"))
	with open(infile[:-3]+".log","w") as log:
		print "\tStarting %s" % (os.path.split(infile)[1])
		p=subprocess.Popen(["Herwig","read",infile],stdout=log,stderr=log)
		returnCode=p.wait()
	end=time.time()

	return (infile,returnCode,end-start)

def write_infile(nAnn,fileDir,resDir,mwimp,annCh,sun):
	"""
	Writes the infile for input arguments
	Input: outDir - the directory to put results for this run in
	       nAnn - number of annihilations
	       annCh - the annihilation channel
	       sun - whether to set up for the sun or not (default is halo)
	Returns: path to infile
	"""
	if sun==False:
		fileName=os.path.join(fileDir,"da-her7-m"+str(mwimp)+"-"+annCh+"-halo.in")
	else:
		fileName=os.path.join(fileDir,"da-her7-m"+str(mwimp)+"-"+annCh+"-sun.in")
	
	with open(fileName,"w") as f:
		f.write("# "+fileName+"\n# -*- ThePEG-repository -*-\n")
		f.write("# DMann input file for Herwig runs\n\n")
		f.write("# Read in FR model file, include charge conservation etc.\n")
		f.write("read FRModel.model\n")
		f.write("read Matchbox/StandardModelLike.in\n\n")
		f.write("# Beam settings, e+e- collider at E=2*mX, unpolarised\n")
		f.write("read snippets/EECollider.in\n")
		f.write("cd /Herwig/EventHandlers\n")
		f.write("set EventHandler:LuminosityFunction:Energy "+str(2*mwimp)+"*GeV\n")
		f.write("set EventHandler:Cuts:MHatMin 0.0*GeV\n")
		f.write("set /Herwig/Particles/e-:PDF /Herwig/Partons/NoPDF\n") # Turn off ISR for e+ e- collision
		f.write("set /Herwig/Particles/e+:PDF /Herwig/Partons/NoPDF\n")
		f.write("cd /Herwig/FRModel\n")
		f.write("set FRModel:gSe 1.0\n")
		f.write("set FRModel:gPe 0.0\n\n")
		f.write("# Set up process and final state polarisation\n")
		f.write("cd /Herwig/NewPhysics\n")
		f.write("insert ResConstructor:Incoming 0 /Herwig/Particles/e+\n")
		f.write("insert ResConstructor:Incoming 0 /Herwig/Particles/e-\n")
		f.write("insert ResConstructor:Intermediates 0 /Herwig/FRModel/Particles/Y0\n")
		# Set final state and couplings 
		if annCh=="uu":
			f.write("insert ResConstructor:Outgoing 0 /Herwig/Particles/u\n")
			f.write("insert ResConstructor:Outgoing 0 /Herwig/Particles/ubar\n")
			f.write("cd /Herwig/FRModel\n")
			f.write("set FRModel:gSu11 1.0 \n")
			f.write("set FRModel:gPu11 0.0\n")
		if annCh=="dd":
			f.write("insert ResConstructor:Outgoing 0 /Herwig/Particles/d\n")
			f.write("insert ResConstructor:Outgoing 0 /Herwig/Particles/dbar\n")
			f.write("cd /Herwig/FRModel\n")
			f.write("set FRModel:gSd11 1.0 \n")
			f.write("set FRModel:gPd11 0.0\n")
		if annCh=="cc":
			f.write("insert ResConstructor:Outgoing 0 /Herwig/Particles/c\n")
			f.write("insert ResConstructor:Outgoing 0 /Herwig/Particles/cbar\n")
			f.write("cd /Herwig/FRModel\n")
			f.write("set FRModel:gSu22 1.0 \n")
			f.write("set FRModel:gPu22 0.0\n")
		if annCh=="ss":
			f.write("insert ResConstructor:Outgoing 0 /Herwig/Particles/s\n")
			f.write("insert ResConstructor:Outgoing 0 /Herwig/Particles/sbar\n")
			f.write("cd /Herwig/FRModel\n")
			f.write("set FRModel:gSd22 1.0 \n")
			f.write("set FRModel:gPd22 0.0\n")
		if annCh=="tLtL": 
			f.write("insert ResConstructor:Outgoing 0 /Herwig/Particles/t\n")
			f.write("insert ResConstructor:Outgoing 0 /Herwig/Particles/tbar\n")
			f.write("cd /Herwig/FRModel\n")
			f.write("set FRModel:gSu33 1.0 \n")
			f.write("set FRModel:gPu33 -1.0\n")
		if annCh=="tRtR":
			f.write("insert ResConstructor:Outgoing 0 /Herwig/Particles/t\n")
			f.write("insert ResConstructor:Outgoing 0 /Herwig/Particles/tbar\n")
			f.write("cd /Herwig/FRModel\n")
			f.write("set FRModel:gSu33 1.0 \n")
			f.write("set FRModel:gPu33 1.0\n")
		if annCh=="bb":
			f.write("insert ResConstructor:Outgoing 0 /Herwig/Particles/b\n")
			f.write("insert ResConstructor:Outgoing 0 /Herwig/Particles/bbar\n")
			f.write("cd /Herwig/FRModel\n")
			f.write("set FRModel:gSd33 1.0 \n")
			f.write("set FRModel:gPd33 0.0\n")
		if annCh=="taLtaL":
			f.write("insert ResConstructor:Outgoing 0 /Herwig/Particles/tau+\n")
			f.write("insert ResConstructor:Outgoing 0 /Herwig/Particles/tau-\n")
			f.write("cd /Herwig/FRModel\n")
			f.write("set FRModel:gSta 1.0 \n")
			f.write("set FRModel:gPta -1.0\n")
		if annCh=="taRtaR":
			f.write("insert ResConstructor:Outgoing 0 /Herwig/Particles/tau+\n")
			f.write("insert ResConstructor:Outgoing 0 /Herwig/Particles/tau-\n")
			f.write("cd /Herwig/FRModel\n")
			f.write("set FRModel:gSta 1.0 \n")
			f.write("set FRModel:gPta 1.0\n")
		if annCh=="muLmuL":
			f.write("insert ResConstructor:Outgoing 0 /Herwig/Particles/mu+\n")
			f.write("insert ResConstructor:Outgoing 0 /Herwig/Particles/mu-\n")
			f.write("cd /Herwig/FRModel\n")
			f.write("set FRModel:gSmm 1.0 \n")
			f.write("set FRModel:gPmm -1.0\n")
		if annCh=="muRmuR":
			f.write("insert ResConstructor:Outgoing 0 /Herwig/Particles/mu+\n")
			f.write("insert ResConstructor:Outgoing 0 /Herwig/Particles/mu-\n")
			f.write("cd /Herwig/FRModel\n")
			f.write("set FRModel:gSmm 1.0 \n")
			f.write("set FRModel:gPmm 1.0\n")
		if annCh=="ee":
			f.write("insert ResConstructor:Outgoing 0 /Herwig/Particles/e+\n")
			f.write("insert ResConstructor:Outgoing 0 /Herwig/Particles/e-\n")
			f.write("cd /Herwig/FRModel\n")
			f.write("set FRModel:gSe 1.0 \n")
			f.write("set FRModel:gPe 0.0\n")
		if annCh=="WLWL":
			f.write("insert ResConstructor:Outgoing 0 /Herwig/Particles/W+\n")
			f.write("insert ResConstructor:Outgoing 0 /Herwig/Particles/W-\n")
			f.write("cd /Herwig/FRModel\n")
			f.write("set FRModel:gSWL 1.0 \n")
			f.write("set FRModel:gSBL 1.0\n")
		if annCh=="WTWT":
			f.write("insert ResConstructor:Outgoing 0 /Herwig/Particles/W+\n")
			f.write("insert ResConstructor:Outgoing 0 /Herwig/Particles/W-\n")
			f.write("cd /Herwig/FRModel\n")
			f.write("set FRModel:gSWT 1.0 \n")
			f.write("set FRModel:gSBT 1.0\n")
		if annCh=="ZLZL":
			f.write("insert ResConstructor:Outgoing 0 /Herwig/Particles/Z0\n")
			f.write("insert ResConstructor:Outgoing 0 /Herwig/Particles/Z0\n")
			f.write("cd /Herwig/FRModel\n")
			f.write("set FRModel:gSWL 1.0 \n")
			f.write("set FRModel:gSBL 1.0\n")
		if annCh=="ZTZT":
			f.write("insert ResConstructor:Outgoing 0 /Herwig/Particles/Z0\n")
			f.write("insert ResConstructor:Outgoing 0 /Herwig/Particles/Z0\n")
			f.write("cd /Herwig/FRModel\n")
			f.write("set FRModel:gSWT 1.0 \n")
			f.write("set FRModel:gSBT 1.0\n")
		if annCh=="hh":
			f.write("insert ResConstructor:Outgoing 0 /Herwig/Particles/h0\n")
			f.write("insert ResConstructor:Outgoing 0 /Herwig/Particles/h0\n")
			f.write("cd /Herwig/FRModel\n")
			f.write("set FRModel:gSh1 1.0 \n")
			f.write("set FRModel:gSh2 1.0\n")
		f.write("set /Herwig/NewPhysics/ResConstructor:Processes Exclusive\n")
		f.write("## Special settings required for on-shell production of top, W, Z and H\n")
		f.write("read Matchbox/OnShellTopProduction.in\n")
		f.write("read Matchbox/OnShellWProduction.in\n")
		f.write("read Matchbox/OnShellZProduction.in\n")
		f.write("read Matchbox/OnShellHProduction.in\n\n")
		f.write("# Scale choice\n")
		f.write("cd /Herwig/MatrixElements/Matchbox\n")
		f.write("set Factory:ScaleChoice /Herwig/MatrixElements/Matchbox/Scales/SHatScale\n")
		f.write("# Do not apply profile scales for LEP as hard\n")
		f.write("# scale coincides with kinematic limit\n")
		f.write("set /Herwig/Shower/ShowerHandler:HardScaleProfile NULL\n")
		f.write("set /Herwig/DipoleShower/DipoleShowerHandler:HardScaleProfile NULL\n\n")
		f.write("# Shower choice \n")
		f.write("read Matchbox/MCatNLO-DefaultShower.in\n\n")
		f.write("# Make usually stable particles decay\n")
		if sun==False:
			f.write("set /Herwig/Particles/pi+:Stable Unstable\n")
			f.write("set /Herwig/Particles/K+:Stable Unstable\n")
			f.write("set /Herwig/Particles/K_L0:Stable Unstable\n")
			f.write("set /Herwig/Particles/mu+:Stable Unstable\n")
			f.write("set /Herwig/Particles/n0:Stable Unstable\n\n")
		f.write("# Analysis of multiplicity\n")
		f.write("cd /Herwig/Analysis\n")
		f.write("create DMann::DMannYields DMannYields DMannYields.so\n")
		f.write("insert /Herwig/Generators/EventGenerator:AnalysisHandlers 0 DMannYields\n")
		f.write("set DMannYields:MassDM "+str(mwimp)+"\n")
		f.write("set DMannYields:NEvent "+str(nAnn)+"\n")
		f.write("set DMannYields:AnnState "+annCh+"\n")
		if len(resDir)>0:
			f.write("set DMannYields:OutDir "+resDir+"\n")
		f.write("insert DMannYields:ParticleCodes[0] -12\n")
		f.write("insert DMannYields:ParticleCodes[0] 12\n")
		f.write("insert DMannYields:ParticleCodes[0] -14\n")
		f.write("insert DMannYields:ParticleCodes[0] 14\n")
		f.write("insert DMannYields:ParticleCodes[0] -16\n")
		f.write("insert DMannYields:ParticleCodes[0] 16\n")
		f.write("insert DMannYields:ParticleCodes[0] -11\n")
		f.write("insert DMannYields:ParticleCodes[0] 11\n")
		f.write("insert DMannYields:ParticleCodes[0] -2212\n")
		f.write("insert DMannYields:ParticleCodes[0] 22\n\n")
		f.write("# Save and run the generator\n")
		f.write("do /Herwig/MatrixElements/Matchbox/Factory:ProductionMode\n")
		f.write("cd /Herwig/Generators\n")
		f.write("set EventGenerator:NumberOfEvents "+str(nAnn)+"\n")
		f.write("run "+os.path.split(fileName)[1][:-3]+" EventGenerator\n")
	return fileName


def mkdir_p(path):
   """
   Creates directory path only if nonexistent.
   """
   try:
      os.makedirs(path)
   except OSError as exc:  # Python >2.5
      if exc.errno == errno.EEXIST and os.path.isdir(path):
         pass
      else:
         raise

def collect_result(res):
   """
   A callback function needed to collect results in apply_async call 
   """
   global results
   results.append(res)

# The threshold in GeV that the WIMP mass has to exceed for annihilations to be possible
annThresholds={"WLWL" : 80.4, "WTWT" : 80.4, "ZLZL" : 91.2, "ZTZT" : 91.2, "hh" : 125.2, 
               "taLtaL" : 1.8, "taRtaR" : 1.8, "muLmuL" : 0.11, "muRmuR" : 0.11, "ee" : 5.2e-6, 
               "tLtL" : 173., "tRtR" : 173., "bb" : 4.8, "cc" : 1.3, "ss" : 0.1, "uu" : 2.6e-3, "dd" : 5.1e-3}


if __name__=="__main__":
	"Create Herwig .in-files from all combinations in simSettings and run through them in parallell."
	
	print "Starting Herwig7 runs ..."
	allstart=time.time()
	infileDir=get_abspath(os.path.join(os.getcwd(),"Herwig","Runs_"+sets.RUN_TAG))
	try:
		os.makedirs(infileDir)
	except OSError as exc: #if directory exists, clear it of old in-files
		if exc.errno==errno.EEXIST and os.path.isdir(infileDir):
			oldFiles=glob.glob(os.path.join(infileDir,"*.in"))
			delCmd=["rm","-f"]
			for f in oldFiles:
				delCmd.append(f)
			subprocess.call(delCmd)

	pool=mp.Pool(processes=mp.cpu_count())
	results=[]
	for annCh in sets.ANN_CHANNELS:
		for mWIMP in sets.WIMP_MASSES:
			if annThresholds[annCh] < mWIMP:
				resDir=os.path.join(get_abspath(sets.DMANN_OUT_DIR),"Herwig",annCh+"-m"+str(mWIMP))
				mkdir_p(resDir)
				infilePath=get_abspath(write_infile(sets.N_ANN,infileDir,resDir,mWIMP,annCh,False))
				pool.apply_async(run_herwig,args=(infilePath,sets.N_ANN,annCh,False),callback=collect_result)
			else:
				print "\tWarning: m_WIMP = %5.3f GeV too small for annihilation channel %s, skipping" % (mWIMP,annCh)
         	continue # skip to next mwimp value
	pool.close()
	pool.join()	
	allend=time.time()
	print "Done! Total time: %i h, %i min, %i s" % (int(math.floor(math.floor((allend-allstart)/60)/60)),
	                                                          int(math.floor((allend-allstart)/60)%60),
	                                                          int((allend-allstart)%60))

	print "Have run Herwig7 on following files:"
	print "%-30s%-19s%-14s" % ("in-file","Return code","Time spent [s]")
	for infile,ret,delta in results:
		print "%-35s\t%-2i\t%15.1f" % (os.path.relpath(infile,start=get_abspath(os.path.join(os.getcwd(),"Herwig",infileDir))),ret,delta)


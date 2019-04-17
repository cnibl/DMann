
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
import MGfunctions as mgf
import random
import psutil

def get_abspath(path):
   """
   Returns absolute path of input path.
   """
   if path.startswith("~"):
      return os.path.expanduser(path)
   else:
      return os.path.abspath(path)

def run_herwig(infile,suffix=""):
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

	logFile=get_abspath(os.path.join(sets.DMANN_OUTDIR,"Herwig"+suffix,
		      os.path.split(infile)[1][:-3]+".log"))	
	with open(logFile,"w") as log:
		print "\tStarting %s" % (os.path.split(infile)[1])
		p=subprocess.Popen(["Herwig","read",infile],stdout=log,stderr=log)
		returnCode=p.wait()
	end=time.time()

	return (infile,returnCode,end-start)

def write_infile(nAnn,fileDir,resDir,mwimp,annCh,seed,sun=False):
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
		f.write("read Matchbox/NonDiagonalCKM.in\n")
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
		if annCh in ("WLWL", "WTWT", "ZLZL", "ZTZT", "tLtL", "tRtR", "bb", "taLtaL", "taRtaR", 
			          "muLmuL", "muRmuR", "ee", "hh","uu", "dd", "cc", "ss"):
			f.write("insert ResConstructor:Intermediates 0 /Herwig/FRModel/Particles/Y0\n")
		elif annCh in ("taLtaR","taRtaL","tLtR","tRtL","muLmuR","muRmuL"):
			f.write("insert ResConstructor:Intermediates 0 /Herwig/FRModel/Particles/Y1\n")
		# Set final state and couplings 
		if annCh=="uu":
			f.write("insert ResConstructor:Outgoing 0 /Herwig/Particles/u\n")
			f.write("insert ResConstructor:Outgoing 0 /Herwig/Particles/ubar\n")
			f.write("cd /Herwig/FRModel\n")
			f.write("set FRModel:gSu11 1.0 \n")
			f.write("set FRModel:gPu11 0.0\n")
		elif annCh=="dd":
			f.write("insert ResConstructor:Outgoing 0 /Herwig/Particles/d\n")
			f.write("insert ResConstructor:Outgoing 0 /Herwig/Particles/dbar\n")
			f.write("cd /Herwig/FRModel\n")
			f.write("set FRModel:gSd11 1.0 \n")
			f.write("set FRModel:gPd11 0.0\n")
		elif annCh=="cc":
			f.write("insert ResConstructor:Outgoing 0 /Herwig/Particles/c\n")
			f.write("insert ResConstructor:Outgoing 0 /Herwig/Particles/cbar\n")
			f.write("cd /Herwig/FRModel\n")
			f.write("set FRModel:gSu22 1.0 \n")
			f.write("set FRModel:gPu22 0.0\n")
		elif annCh=="ss":
			f.write("insert ResConstructor:Outgoing 0 /Herwig/Particles/s\n")
			f.write("insert ResConstructor:Outgoing 0 /Herwig/Particles/sbar\n")
			f.write("cd /Herwig/FRModel\n")
			f.write("set FRModel:gSd22 1.0 \n")
			f.write("set FRModel:gPd22 0.0\n")
		elif annCh=="tLtL": 
			f.write("insert ResConstructor:Outgoing 0 /Herwig/Particles/t\n")
			f.write("insert ResConstructor:Outgoing 0 /Herwig/Particles/tbar\n")
			f.write("cd /Herwig/FRModel\n")
			f.write("set FRModel:gSu33 1.0 \n")
			f.write("set FRModel:gPu33 -1.0\n")
		elif annCh=="tRtR":
			f.write("insert ResConstructor:Outgoing 0 /Herwig/Particles/t\n")
			f.write("insert ResConstructor:Outgoing 0 /Herwig/Particles/tbar\n")
			f.write("cd /Herwig/FRModel\n")
			f.write("set FRModel:gSu33 1.0 \n")
			f.write("set FRModel:gPu33 1.0\n")
		elif annCh=="tLtR":
			f.write("insert ResConstructor:Outgoing 0 /Herwig/Particles/t\n")
			f.write("insert ResConstructor:Outgoing 0 /Herwig/Particles/tbar\n")
			f.write("cd /Herwig/FRModel\n")
			f.write("set FRModel:gVu33 1.0 \n")
			f.write("set FRModel:gAu33 -1.0\n")
		elif annCh=="tRtL":
			f.write("insert ResConstructor:Outgoing 0 /Herwig/Particles/t\n")
			f.write("insert ResConstructor:Outgoing 0 /Herwig/Particles/tbar\n")
			f.write("cd /Herwig/FRModel\n")
			f.write("set FRModel:gVu33 1.0 \n")
			f.write("set FRModel:gAu33 1.0\n")
		elif annCh=="bb":
			f.write("insert ResConstructor:Outgoing 0 /Herwig/Particles/b\n")
			f.write("insert ResConstructor:Outgoing 0 /Herwig/Particles/bbar\n")
			f.write("cd /Herwig/FRModel\n")
			f.write("set FRModel:gSd33 1.0 \n")
			f.write("set FRModel:gPd33 0.0\n")
		elif annCh=="taLtaL":
			f.write("insert ResConstructor:Outgoing 0 /Herwig/Particles/tau+\n")
			f.write("insert ResConstructor:Outgoing 0 /Herwig/Particles/tau-\n")
			f.write("cd /Herwig/FRModel\n")
			f.write("set FRModel:gSta 1.0 \n")
			f.write("set FRModel:gPta -1.0\n")
		elif annCh=="taRtaR":
			f.write("insert ResConstructor:Outgoing 0 /Herwig/Particles/tau+\n")
			f.write("insert ResConstructor:Outgoing 0 /Herwig/Particles/tau-\n")
			f.write("cd /Herwig/FRModel\n")
			f.write("set FRModel:gSta 1.0 \n")
			f.write("set FRModel:gPta 1.0\n")
		elif annCh=="taLtaR":
			f.write("insert ResConstructor:Outgoing 0 /Herwig/Particles/tau+\n")
			f.write("insert ResConstructor:Outgoing 0 /Herwig/Particles/tau-\n")
			f.write("cd /Herwig/FRModel\n")
			f.write("set FRModel:gVta 1.0 \n")
			f.write("set FRModel:gAta -1.0\n")
		elif annCh=="taRtaL":
			f.write("insert ResConstructor:Outgoing 0 /Herwig/Particles/tau+\n")
			f.write("insert ResConstructor:Outgoing 0 /Herwig/Particles/tau-\n")
			f.write("cd /Herwig/FRModel\n")
			f.write("set FRModel:gVta 1.0 \n")
			f.write("set FRModel:gAta 1.0\n")
		elif annCh=="muLmuL":
			f.write("insert ResConstructor:Outgoing 0 /Herwig/Particles/mu+\n")
			f.write("insert ResConstructor:Outgoing 0 /Herwig/Particles/mu-\n")
			f.write("cd /Herwig/FRModel\n")
			f.write("set FRModel:gSmm 1.0 \n")
			f.write("set FRModel:gPmm -1.0\n")
		elif annCh=="muRmuR":
			f.write("insert ResConstructor:Outgoing 0 /Herwig/Particles/mu+\n")
			f.write("insert ResConstructor:Outgoing 0 /Herwig/Particles/mu-\n")
			f.write("cd /Herwig/FRModel\n")
			f.write("set FRModel:gSmm 1.0 \n")
			f.write("set FRModel:gPmm 1.0\n")
		elif annCh=="muLmuR":
			f.write("insert ResConstructor:Outgoing 0 /Herwig/Particles/mu+\n")
			f.write("insert ResConstructor:Outgoing 0 /Herwig/Particles/mu-\n")
			f.write("cd /Herwig/FRModel\n")
			f.write("set FRModel:gVmm 1.0 \n")
			f.write("set FRModel:gAmm -1.0\n")
		elif annCh=="muRmuL":
			f.write("insert ResConstructor:Outgoing 0 /Herwig/Particles/mu+\n")
			f.write("insert ResConstructor:Outgoing 0 /Herwig/Particles/mu-\n")
			f.write("cd /Herwig/FRModel\n")
			f.write("set FRModel:gVmm 1.0 \n")
			f.write("set FRModel:gAmm 1.0\n")
		elif annCh=="ee":
			f.write("insert ResConstructor:Outgoing 0 /Herwig/Particles/e+\n")
			f.write("insert ResConstructor:Outgoing 0 /Herwig/Particles/e-\n")
			f.write("cd /Herwig/FRModel\n")
			f.write("set FRModel:gSe 1.0 \n")
			f.write("set FRModel:gPe 0.0\n")
		elif annCh=="WLWL":
			f.write("insert ResConstructor:Outgoing 0 /Herwig/Particles/W+\n")
			f.write("insert ResConstructor:Outgoing 0 /Herwig/Particles/W-\n")
			f.write("cd /Herwig/FRModel\n")
			f.write("set FRModel:gSWL 1.0 \n")
			f.write("set FRModel:gSBL 1.0\n")
			f.write("set FRModel:gSWT 0.0 \n")
			f.write("set FRModel:gSBT 0.0\n")
			f.write("set FRModel:gPWT 0.0 \n")
			f.write("set FRModel:gPBT 0.0\n")
		elif annCh=="WTWT":
			f.write("insert ResConstructor:Outgoing 0 /Herwig/Particles/W+\n")
			f.write("insert ResConstructor:Outgoing 0 /Herwig/Particles/W-\n")
			f.write("cd /Herwig/FRModel\n")
			f.write("set FRModel:gSWL 0.0 \n")
			f.write("set FRModel:gSBL 0.0\n")
			f.write("set FRModel:gSWT 1.0 \n")
			f.write("set FRModel:gSBT 1.0\n")
			f.write("set FRModel:gPWT 1.0 \n")
			f.write("set FRModel:gPBT 1.0\n")
		elif annCh=="ZLZL":
			f.write("insert ResConstructor:Outgoing 0 /Herwig/Particles/Z0\n")
			f.write("insert ResConstructor:Outgoing 0 /Herwig/Particles/Z0\n")
			f.write("cd /Herwig/FRModel\n")
			f.write("set FRModel:gSWL 1.0 \n")
			f.write("set FRModel:gSBL 1.0\n")
			f.write("set FRModel:gSWT 0.0 \n")
			f.write("set FRModel:gSBT 0.0\n")
			f.write("set FRModel:gPWT 0.0 \n")
			f.write("set FRModel:gPBT 0.0\n")
		elif annCh=="ZTZT":
			f.write("insert ResConstructor:Outgoing 0 /Herwig/Particles/Z0\n")
			f.write("insert ResConstructor:Outgoing 0 /Herwig/Particles/Z0\n")
			f.write("cd /Herwig/FRModel\n")
			f.write("set FRModel:gSWL 0.0 \n")
			f.write("set FRModel:gSBL 0.0\n")
			f.write("set FRModel:gSWT 1.0 \n")
			f.write("set FRModel:gSBT 1.0\n")
			f.write("set FRModel:gPWT 1.0 \n")
			f.write("set FRModel:gPBT 1.0\n")
		elif annCh=="hh":
			f.write("insert ResConstructor:Outgoing 0 /Herwig/Particles/h0\n")
			f.write("insert ResConstructor:Outgoing 0 /Herwig/Particles/h0\n")
			f.write("cd /Herwig/FRModel\n")
			f.write("set FRModel:gSh1 1.0 \n")
			f.write("set FRModel:gSh2 1.0\n")
		else:
			sys.exit("ERROR: unknown annihilation channel: %s" % annCh)
		f.write("set /Herwig/NewPhysics/ResConstructor:Processes Exclusive\n")
		f.write("## Special settings required for on-shell production of top, W, Z and H\n")
		f.write("read Matchbox/OnShellTopProduction.in\n")
		f.write("read Matchbox/OnShellWProduction.in\n")
		f.write("read Matchbox/OnShellZProduction.in\n")
		f.write("read Matchbox/OnShellHProduction.in\n\n")

		#print "Trying to turn off EvtGen by commenting out line 32 in ~/Herwig7/share/Herwig/defaults/Decays.in ... check if works"
		if sets.HER_EVTGEN==False:
			f.write("## Reinitialise decays to turn off EvtGen usage\n")
			f.write("cd /Herwig/Particles\n")
			f.write("# switch off current modes\n")
			f.write("do B0:SelectDecayModes none\n")
			f.write("do Bbar0:SelectDecayModes none\n")
			f.write("do B+:SelectDecayModes none\n")
			f.write("do B-:SelectDecayModes none\n")
			f.write("do B_s0:SelectDecayModes none\n")
			f.write("do B_sbar0:SelectDecayModes none\n")
			f.write("do D0:SelectDecayModes none\n")
			f.write("do Dbar0:SelectDecayModes none\n")
			f.write("do D+:SelectDecayModes none\n")
			f.write("do D-:SelectDecayModes none\n")
			f.write("do D_s+:SelectDecayModes none\n")
			f.write("do D_s-:SelectDecayModes none\n")
			f.write("## Read in Herwig default B decays instead of EvtGen\n")
			f.write("read defaults/HerwigBDecays.in\n")

		f.write("# Scale choice\n")
		f.write("cd /Herwig/MatrixElements/Matchbox\n")
		f.write("set Factory:ScaleChoice /Herwig/MatrixElements/Matchbox/Scales/SHatScale\n")
		f.write("# Do not apply profile scales for LEP as hard\n")
		f.write("# scale coincides with kinematic limit\n")
		f.write("set /Herwig/Shower/ShowerHandler:HardScaleProfile NULL\n")
		f.write("set /Herwig/DipoleShower/DipoleShowerHandler:HardScaleProfile NULL\n\n")
		
		f.write("# Shower choice \n")
		f.write("cd /Herwig/EventHandlers\n")
		f.write("set EventHandler:CascadeHandler /Herwig/Shower/ShowerHandler # default\n") 
		f.write("#read Matchbox/MCatNLO-DefaultShower.in\n\n")

		if sets.HER_QRH==True:
			f.write("# QED radiation in particle decays (Q: don't use both QEDRadiationHandler and ShowerHandler:Interactions QCDandQED at the same time?)\n")
			f.write("cd /Herwig/EventHandlers\n")
			f.write("insert EventHandler:PostSubProcessHandlers 0 /Herwig/QEDRadiation/QEDRadiationHandler\n")
			for i in (1,2,3,4,5,6,11,13,15,23,-24,24):
				f.write("insert /Herwig/QEDRadiation/QEDRadiationHandler:DecayProducts[0] "+str(i)+"\n")
				f.write("insert /Herwig/QEDRadiation/QEDRadiationHandler:DecayProducts[0] "+str(-i)+"\n")   
			if annCh not in ("taLtaR","taRtaL","tRtL","tLtR","muLmuR","muRmuL"):
				f.write("insert /Herwig/QEDRadiation/QEDRadiationHandler:DecayingParticles[0] 9000006\n")
			else:
				f.write("insert /Herwig/QEDRadiation/QEDRadiationHandler:DecayingParticles[0] 9000007\n")
			f.write("set /Herwig/Shower/ShowerHandler:Interactions QCD\n") 
		else:
			f.write("set /Herwig/Shower/ShowerHandler:Interactions QCDandQED\n")
		
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
		f.write("set EventGenerator:RandomNumberGenerator:Seed "+str(seed)+"\n")
		f.write("set EventGenerator:Path "+fileDir+"\n")
		f.write("run "+os.path.split(fileName)[1][:-3]+" EventGenerator")
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

if __name__=="__main__":
	"""
	Create Herwig .in-files from all combinations in simSettings and run through them in parallell.
	"""

	if sets.N_ANN < 100000:
		nRuns=1
	else:
		nRuns=int(sets.N_ANN/100000) #sets.N_ANN must be multiple of 100k 

	for i in range(1,nRuns+1):

		print "Starting Herwig7 run %i of %i ..." % (i,nRuns)
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
		runResults=[]
		for mWIMP in sets.WIMP_MASSES:
			for annCh in sets.ANN_CHANNELS:
				testFile=os.path.join(sets.DMANN_OUTDIR,"Herwig_"+str(i),annCh+"_m"+str(mWIMP),"da-her7-mx"+str(mWIMP)+"-"+annCh+"-y14.dat","XXXXXX")
				if mgf.annThresholds[annCh] < mWIMP:
					if os.path.exists(testFile):
						continue
					else:
						#seed=random.randint(1,100000)
						seed=i
						resDir=os.path.join(get_abspath(sets.DMANN_OUTDIR),"Herwig_"+str(i),annCh+"_m"+str(mWIMP))
						mkdir_p(resDir)
						if sets.N_ANN < 100000:
							nAnn=sets.N_ANN
						else:
							nAnn=100000
						infilePath=get_abspath(write_infile(nAnn,infileDir,resDir,mWIMP,annCh,seed,sets.SUN))
						suffix="_"+str(i)
						result=pool.apply_async(run_herwig,args=(infilePath,suffix),callback=collect_result)
						runResults.append((result,annCh,mWIMP))
				else:
					print "\tWarning: m_WIMP = %5.3f GeV too small for annihilation channel %s, skipping" % (mWIMP,annCh)
		      	continue # skip to next mwimp value
		
		for runRes in runResults:
			try:
				runRes[0].get(timeout=20000) # no result in 20000 seconds triggers TimeoutError
				#runRes[0].wait()
			#may finish anyway if it is an early case in the run, continues until whole 100k run is looped through
			except mp.TimeoutError:
				print "\tWarning: %s, m=%5.1f might not have finished before timeout" % (runRes[1],runRes[2])
				continue

		pool.terminate()
		pool.join()
		
		# clean up and kill all Herwig processes to begin next 100k events clean
		for proc in psutil.process_iter():
			# check whether the process name matches
			if proc.name() == "Herwig":
				proc.kill()

		allend=time.time()
		if len(results)!=0:
			print "\tDone! Total time: %i h, %i min, %i s" % (int(math.floor(math.floor((allend-allstart)/60)/60)),
		                                                          int(math.floor((allend-allstart)/60)%60),
		                                                          int((allend-allstart)%60))
			print "\tHave run Herwig7 on following files:"
			print "\t%-30s%-19s%-14s" % ("in-file","Return code","Time spent [s]")
			for infile,ret,delta in results:
				print "\t%-35s\t%-2i\t%15.1f" % (os.path.relpath(infile,start=get_abspath(os.path.join(os.getcwd(),"Herwig",infileDir))),ret,delta)

		"""
		gzip all the event files created to save space   
		"""
		if sets.GZIP_EVTFILE==True:
			print "\tNow gzipping event files ... "
			zipstart=time.time()
			for annCh in sets.ANN_CHANNELS:
				for mX in sets.WIMP_MASSES:
					if mgf.annThresholds[annCh] < mX:
						suffix="_"+str(i)
						eventFile=os.path.join(sets.DMANN_OUTDIR,"Herwig"+suffix,
								annCh+"_m"+str(mX),"da-her7-mx"+str(mX)+"-"+annCh+"-events.dat")
						if os.path.exists(get_abspath(eventFile)):
							subprocess.call(["gzip","-f",get_abspath(eventFile)]) #overwrites any existing file
						else:
							"\tWarning: no event file for %s, m=%5.3f" % (annCh,mX)
			zipend=time.time()
			print "\tDone gzipping. Took %i h, %i min, %i s" % (int(math.floor(math.floor((zipend-zipstart)/60)/60)),
																				int(math.floor((zipend-zipstart)/60)%60),
																				int((zipend-zipstart)%60))      


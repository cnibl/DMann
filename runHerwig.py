
"""
runHerwig.py

Creates .in-files for Herwig for the combinations in simSettings.py and then runs through them.

"""


import os
import subprocess
import sys
import multiprocessing as mp 
import simSettings as sets 
import time
import math


def get_abspath(path):
   """
   Returns absolute path of input path.
   """
   if path.startswith("~"):
      return os.path.expanduser(path)
   else:
      return os.path.abspath(path)

def run_herwig(infile,outDir,nAnn,annCh,sun=False):
	"""
	Runs Herwig on the provided infile and puts results for the run in outDir.
	Input: infile - a .in-file to be run as "Herwig read infile"
	       outDir - the directory to put results for this run in
	       nAnn - number of annihilations
	       annCh - the annihilation channel
	       sun - whether to set up for the sun or not (default is halo)
	Returns: path to infile, error code
	"""


def write_infile(nAnn,outDir,mwimp,annCh,sun):
	"""
	Writes the infile for input arguments
	Input: outDir - the directory to put results for this run in
	       nAnn - number of annihilations
	       annCh - the annihilation channel
	       sun - whether to set up for the sun or not (default is halo)
	Returns: path to infile
	"""
	if sun==False:
		fileName=outDir+"da-her7-m"+str(mwimp)+"-"+annCh+"-halo.in"
	else:
		fileName=outDir+"da-her7-m"+str(mwimp)+"-"+annCh+"-sun.in"
	
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
		if len(outDir)>0:
			f.write("set DMannYields:OutDir "+outDir+"\n")
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
		f.write("run "+fileName+" EventGenerator\n")
	return fileName

def mk_outdir():
	pass



if __name__=="__main__":
	"Do stuff"
	pass

	#chdir(./Herwig)
	#for combinations in simSettings:
	#   create in-file
	#   apply_async(run_her,args=(),callback=)
	#pool.close
	#pool.join 
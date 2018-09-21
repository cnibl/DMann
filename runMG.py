import subprocess
import sys
import os
import matplotlib.pyplot as plt 
from runMG_helpfunctions import *
"""
A script that runs MadGraph with Pythia for a process.
The process is defined in write_madgraphscript.
The settings for the run (masses, beam energies etc.) are defined in the routines write_paramcard, write_runcard and write_pythiacard.
"""

def ann_mass(annPDG):
	"""
	Returns mass of particle with PDG code annPDG.
	"""
	masses = {5: 4.8, 6: 175., 15: 1.7, 24: 80.5}
	return masses[annPDG]

def readhepmc(HEPMCfilename,yieldPDG):
	"""
	Reads a specified HEPMC file and searches for energies of final state particles with codes in the list yieldPDG.
	"""
	try:
		energies = {y : [] for y in yieldPDG}
	except TypeError:
		energies = {y : [] for y in [yieldPDG]}

	with open(HEPMCfilename,"r") as infile:
		for line in infile:
			if line.startswith("P"): # corresponds to particle lines
				vals = line.split()
				if int(vals[8])==1 and int(vals[2]) in yieldPDG: # vals[8]=status, vals[2]=pdgID
					energies[int(vals[2])].append(float(vals[6]))
	return energies

currentdir = r"%s" % os.getcwd()
homedir = r"%s" % os.path.expanduser("~")
mgdir = "/".join((homedir,"MG5_aMC_v2_6_3_2"))
datadir = "/".join((currentdir,"Misc"))

nann = 10
a = 24
rundir = "/".join((mgdir,"DMannRuns_annPDG"+str(a))) # the directory for the MadGraph output
try: # delete rundir if exists already
	subprocess.call(["rm","-rf",rundir])
except OSError:
	pass
subprocess.call(["mkdir",rundir])

"""
Now run MadGraph for the specified final state to generate the output directory.
"""
mgscriptpath = write_madgraphscript(annPDG=a,run_dir=rundir)
print "Now running MadGraph with annihilation pdg %s..." % str(a)
with open("madgraph.log","w") as outfile:
	subprocess.call(["./bin/mg5_aMC","/".join((currentdir,mgscriptpath))],cwd=mgdir,stdout=outfile)
print "Done!"
"""
Specify WIMP masses to use and which yield particles to look for.
"""
wimpmasses = [200,1000,10000] 
yieldPDGs = [-11,-14,14,22,-2212]

for mwimp in wimpmasses:
	if mwimp > ann_mass(a):
		for c in ["run","param","pythia8"]:
			try:
				os.remove("/".join((currentdir,c+"_card.dat")))
				print "Removed %s" % c+"_card.dat"
			except OSError:
				pass
		"""
		Write the specific settings to cards and move to the MadGraph output directory
		"""
		pa = write_paramcard(mX=mwimp,mgoutput_path=rundir)
		ru = write_runcard(nAnn=nann,mX=mwimp,mgoutput_path=rundir)
		(py,hepmcfile) = write_pythiacard(mgoutput_path=rundir,HEPMCfilename="".join(("pyt8evts_y0med_mX",str(mwimp),"_a",str(a),".hepmc")))
	
		subprocess.call(["rm","/".join((rundir,"Cards",pa))])
		subprocess.call(["rm","/".join((rundir,"Cards",ru))])
		subprocess.call(["mv",pa,"/".join((rundir,"Cards",pa))])
		subprocess.call(["mv",ru,"/".join((rundir,"Cards",ru))])
		subprocess.call(["mv",py,"/".join((rundir,"Cards",py))])
		
		"""
		Now run MadEvent with the settings specified in madeventscript (typically Pythia8 showering)
		"""
		runtag = "".join(("ann",str(int(a)),"_mx",str(int(mwimp))))
		mescriptpath = write_madeventscript(run_tag=runtag)
		print "Now running MadEvent with %s annihilations..." % str(nann)
		with open("madevent.log","w") as outfile:
			subprocess.call(["./bin/madevent","/".join((currentdir,mescriptpath))],cwd=rundir,stdout=outfile)
		print "Done!"
		subprocess.call(["mkdir","-p","Misc"])
		subprocess.call(["mv","/".join((rundir,"Events",runtag,hepmcfile)),"/".join((datadir,hepmcfile))])
		print "".join(("Moved ",hepmcfile," to ",datadir))
	#
		"""
		Read the produced HEPMC file and store yield particle energies in the dictionary energies
		"""
		energies = readhepmc("/".join((datadir,hepmcfile)),yieldPDGs)
#
		"""
		Plot histograms
		"""
		for y in yieldPDGs:
			fig,ax = plt.subplots()
			ax.hist(energies[y],bins=100,histtype='step',linewidth=2,density=True)
			ax.hist(energies[y],bins=100,histtype='stepfilled',color='blue',alpha=0.2,density=True)
			ax.set_yscale('log')
			#ax.set_xlim(0,500)
			ax.set_ylim(1e-6,1e-1)
			fig.savefig(''.join(("Misc/y0med_energy_y",str(y),"_mx",str(int(mwimp)),".pdf")))		
			plt.close()
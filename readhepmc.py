"""
readhepmc.py contains functions for reading files in the HEPMC format and picking out particle properties from the event
"""


#def readfile(path,filename):
#	if path[-1]=="/":
#		fullPath = ''.join((path,filename)
#	else:
#		fullPath = '/'.join((path,filename))
#


yieldPdgs = [-11,-14,14,22,-2212]
energies = {id: [] for id in yieldPdgs}
e_numu = []
with open("tag_1_pythia8_events.hepmc","r") as infile:
	for line in infile:
		if line.startswith("P"):
			vals = line.split()
			if int(vals[8])==1 and int(vals[2]) in yieldPdgs: # vals[8]=status, vals[2]=pdgID
				energies[int(vals[2])].append(float(vals[6]))


for y in yieldPdgs:
	fig,ax = plt.subplots()
	ax.hist(energies[y],bins=100,histtype='step',linewidth=2,density=True)
	ax.hist(energies[y],bins=100,histtype='stepfilled',color='blue',alpha=0.2,density=True)
	ax.set_yscale('log')
	ax.set_xlim(0,200)
	ax.set_ylim(1e-6,1e-1)
	fig.savefig(''.join(("energy_",str(y),".pdf")))
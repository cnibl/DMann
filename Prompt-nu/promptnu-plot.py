"""
wnuplot.py
Plot only w-neutrinos.
"""

import numpy as np
import matplotlib.pyplot as plt
import subprocess

pyt8Dir = "data-Pythia8-promptnu/"
herDir  = "Herwig-promptnu/Herwig7DataPromptNu/"
plotdir = "plots-promptnu/"
subprocess.call(["mkdir","-p",plotdir[:-1]])  

eCM   = 400
nEvtHer   = 100000
PDG = [14,-14]
annPdg = 24

labels  = ["WW, H", "WW, P8"]
#colors  = plt.cm.Dark2(np.linspace(0,1,len(massX)))
colors = ["red","blue","black","green"]

Her = True
Pyt8 = True

for p in PDG:
	print p
	"""Herwig"""
	if Her:
		fName = herDir+"pnu-her7-e"+str(int(eCM))+"-p"+str(p)+".dat"
		print "Plotting ",fName
		dataHer = np.genfromtxt(open(fName,"r"),skip_header=10) # E_low, E_high, normY, N_part
		binWidths = dataHer[:,1]-dataHer[:,0]
		xaxis = (dataHer[:,0]+dataHer[:,1])/2.
		yaxis = np.divide(dataHer[:,3],binWidths)
		plt.plot(xaxis,yaxis,color=colors[0],label=labels[0])
		yaxis_h = yaxis
   
	"""Pythia 8"""
	if Pyt8:
		fName = pyt8Dir+"da-pyt8-mx"+str(int(eCM/2.))+"-ch24-int"+str(p)+".dat"
		print "Plotting ",fName
		dataPyt8 = np.genfromtxt(open(fName,"r"),skip_header=8) # E_kin, yield
		xaxis = dataPyt8[:,0]
		yaxis = np.divide(dataPyt8[:,1],binWidths)
		plt.plot(xaxis,yaxis,'--',color=colors[1],label=labels[1])
		yaxis_p8 = yaxis


	"""Plot settings"""
	plt.title(r"W decay neutrinos")
	plt.xlabel(r"$E_{\rm kin}$")
	plt.ylabel(r"$(1/N_{evt}) dN/dE$")
	#plt.gca().set_xscale("log")
	plt.gca().set_yscale("log")
	#plt.xlim(0,eCM/2.)
	plt.ylim(1e-6,1e-1)
	plt.legend(loc="lower center",ncol=2)
  
	fName = plotdir+"pnu_dNdE_lin_p"+str(p)+".pdf"
	print "Saving ",fName
	plt.savefig(fName)
	plt.close()
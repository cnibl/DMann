"""
plotyields.py

Script to make simple plots of Herwig and Pythia data
"""

import numpy as np
import matplotlib.pyplot as plt
import subprocess

pdgnames = {r"e^+": -11,r"e^-": 11,r"\bar{p}": -2212,r"\nu_\mu": 14,r"\bar{\nu}_\mu": -14,r"\gamma": 22,r"b": 5,r"t": 6,r"\tau^-": 15,"W^-": 24}
def pdg2name(pdg):
  for name, p in pdgnames.items():
    if p==pdg:
      return str(name)
  sys.exit("pdg2name: particle with PDG code "+str(p)+" not available")
  return "ERROR"
  
def name2pdg(name):
  if name in pdgnames:
    return pdg
  else:
    sys.exit("name2pdg: particle with name "+str(name)+" not available")
    return "ERROR"
  
pyt8Dir = "Pythia/Pythia8Data/"
pyt6Dir = "Pythia/Pythia6Data/"
herDir  = "Herwig/Herwig7Data/data_ref/"
plotdir = "plots/"
subprocess.call(["mkdir","-p",plotdir[:-1]])  

massX 	= 200.0
nEvt 	= 100000
yieldPdgs = [22, -11, -2212, 14]
annPdgs = [5, 6, 15, 24]
labels 	= [[r"$"+pdg2name(p)+"$"+", H", r"$"+pdg2name(p)+"$"+", P8", r"$"+pdg2name(p)+"$"+", P6"] for p in annPdgs]
colors 	= ["red","blue","black","green"]

for y in yieldPdgs:
  for i, a in zip(range(len(annPdgs)),annPdgs): 
    """Herwig"""
#    fName = herDir+"da-her7-mx"+str(int(massX))+"-ch"+str(a)+"-int"+str(y)+".dat"
#    dataHer = np.genfromtxt(open(fName,"r"),skip_header=10) # E_low, E_high, normY, N_part
#    if y==14: # nu and nubar fluxes are separate in Herwig, need to add numubar to numu 
#    	fName = herDir+"da-her7-mx"+str(int(massX))+"-ch"+str(a)+"-int"+str(-y)+".dat"
#    	dataHer[:,3] += np.genfromtxt(open(fName,"r"),skip_header=10)[:,3] # E_low, E_high, normY, N_part
#    logBinWidths = np.diff(np.log10(dataHer[:,0]))[0]
#    xaxis = (dataHer[:,0]+dataHer[:,1])/2.
#    yaxis = dataHer[:,3]/nEvt/logBinWidths
#    plt.plot(xaxis,yaxis,color=colors[i],label=labels[i][0])
    
    """Pythia 8"""
    fName = pyt8Dir+"da-pyt8-mx"+str(int(massX))+"-ch"+str(a)+"-int"+str(y)+".dat"
    dataPyt8 = np.genfromtxt(open(fName,"r"),skip_header=8) # E_kin, yield
    if y==14: # nu and nubar fluxes are separate, need to add numubar to numu 
      fName = pyt8Dir+"da-pyt8-mx"+str(int(massX))+"-ch"+str(a)+"-int"+str(-y)+".dat"
      dataPyt8[:,1] += np.genfromtxt(open(fName,"r"),skip_header=8)[:,1] # E_kin, yield
    logBinWidths = np.diff(np.log10(dataPyt8[:,0]))[0]
    xaxis = dataPyt8[:,0]
    yaxis = dataPyt8[:,1]/logBinWidths
    plt.plot(xaxis,yaxis,linestyle="dashdot",color=colors[i],label=labels[i][1])
    
    """Pythia 6"""
    fName = pyt6Dir+"da-pyt6-mx"+str(int(massX))+"-ch"+str(a)+"-int"+str(y)+".dat"
    dataPyt6 = np.genfromtxt(open(fName,"r"),skip_header=1) # i, E_kin, yield
    xaxis = dataPyt6[:,1]
    yaxis = np.multiply(dataPyt6[:,2],np.log(10)*dataPyt6[:,1])
    plt.plot(xaxis,yaxis,linestyle="dashed",color=colors[i],label=labels[i][2])	
    
    """Plot settings"""
    plt.title(r"$"+pdg2name(y)+"$")
    plt.xlabel(r"$E_{\rm kin}$")
    plt.ylabel(r"$dN/d(\log E)$")
    plt.gca().set_xscale("log")
    plt.gca().set_yscale("log")
    plt.xlim(massX*1e-10,massX)
    plt.ylim(1e-2,1e2)
    plt.legend(loc="best")
    
  plt.savefig(plotdir+"dNdlogE_yieldPdg"+str(y)+".pdf")
  plt.close()
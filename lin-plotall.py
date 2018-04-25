"""
plotall-lin.py

Script to make simple plots of Herwig and Pythia dN/dE, linear
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
herDir  = "Herwig/Herwig7Data/TEST-"
plotdir = "plots/"
subprocess.call(["mkdir","-p",plotdir[:-1]])  

massX   = 200.
#massX = 10000.0
nEvtHer   = 1000000
yieldPdgs = [22, -11, -2212, 14]
annPdgs = [5, 6, 15, 24]
yieldPdgs = [14]
annPdgs = [24]

#annPdgs = [15]
labels  = [[r"$"+pdg2name(p)+"$"+", H", r"$"+pdg2name(p)+"$"+", P8", r"$"+pdg2name(p)+"$"+", P6"] for p in annPdgs]
colors  = ["red","blue","black","green"]

Pyt6 = False
Pyt8 = True
Her = True

for y in yieldPdgs:
  for i, a in zip(range(len(annPdgs)),annPdgs): 
    """Herwig"""
    #if a==24 and y==14:
    # herDir += "TEST-"
    # nEvtHer = 100000
    if Her:
      fName = herDir+"da-her7-mx"+str(int(massX))+"-ch"+str(a)+"-int"+str(y)+".dat"
      print "Plotting ",fName
      dataHer = np.genfromtxt(open(fName,"r"),skip_header=10) # E_low, E_high, normY, N_part
      if y==14: # nu and nubar fluxes are separate, need to add numubar to numu 
        fName = herDir+"da-her7-mx"+str(int(massX))+"-ch"+str(a)+"-int"+str(-y)+".dat"
        dataHer[:,3] += np.genfromtxt(open(fName,"r"),skip_header=10)[:,3] # E_low, E_high, normY, N_part
        if a==24: 
          nEvtHer = 100000
          #dataHer[:,3] /= 10.
      binWidths = dataHer[:,1]-dataHer[:,0]
      xaxis = (dataHer[:,0]+dataHer[:,1])/2.
      yaxis = np.divide(dataHer[:,3]/nEvtHer,binWidths)
      plt.plot(xaxis,yaxis,'-.',color=colors[i],label=labels[i][0])
      yaxis_h = yaxis
    
    """Pythia 8"""
    if Pyt8:
      fName = pyt8Dir+"da-pyt8-mx"+str(int(massX))+"-ch"+str(a)+"-int"+str(y)+".dat"
      if abs(y)==14 and a==24:
        pyt8Dir = "Pythia/TEST-pythia8/"
        fName = pyt8Dir+"da-pyt8-mx"+str(int(massX))+"-ch"+str(a)+"-int"+str(y)+".dat"
      print "Plotting ",fName
      dataPyt8 = np.genfromtxt(open(fName,"r"),skip_header=8) # E_kin, yield
      if y==14: # nu and nubar fluxes are separate, need to add numubar to numu 
        fName = pyt8Dir+"da-pyt8-mx"+str(int(massX))+"-ch"+str(a)+"-int"+str(-y)+".dat"
        dataPyt8[:,1] += np.genfromtxt(open(fName,"r"),skip_header=8)[:,1] # E_kin, yield
      xaxis = dataPyt8[:,0]
      yaxis = np.divide(dataPyt8[:,1],binWidths)
      plt.plot(xaxis,yaxis,color=colors[i],label=labels[i][1])
      yaxis_p8 = yaxis
          
    """Pythia 6"""
    if Pyt6:
      fName = pyt6Dir+"da-pyt6-mx"+str(int(massX))+"-ch"+str(a)+"-int"+str(y)+".dat"
      print "Plotting ",fName
      dataPyt6 = np.genfromtxt(open(fName,"r"),skip_header=1) # i, E_kin, yield
      xaxis = dataPyt6[:,1]
      yaxis = np.multiply(dataPyt6[:,2],np.log(10)*dataPyt6[:,1]) # what to have here for lin dNdE plot ???
      plt.plot(xaxis,yaxis,linestyle="dashed",color=colors[i],label=labels[i][2]) 
      yaxis_p6 = yaxis
        
    """Comparison"""    
    if Pyt6 and Pyt8:
      plt.fill_between(xaxis,yaxis_p6,yaxis_p8,alpha=0.5,color=colors[i])
    elif Pyt6 and Her:
      plt.fill_between(xaxis,yaxis_p6,yaxis_h,alpha=0.5,color=colors[i])
    elif Her and Pyt8:
      plt.fill_between(xaxis,yaxis_h,yaxis_p8,alpha=0.5,color=colors[i])
    
    """Plot settings"""
    plt.title(r"$"+pdg2name(y)+"$")
    plt.xlabel(r"$E_{\rm kin}$")
    plt.ylabel(r"$dN/dE$")
    #plt.gca().set_xscale("log")
    plt.gca().set_yscale("log")
    plt.xlim(0,200)
    plt.ylim(0,0.05)
    plt.legend(loc="best")
  
  if Pyt6 and Pyt8:
    fName = plotdir+"dNdE_lin_P6vsP8_yieldPdg"+str(y)+".pdf"
    print "Saving ",fName
    plt.savefig(fName)
  elif Pyt6 and Her:
    fName = plotdir+"dNdE_lin_P6vsH_yieldPdg"+str(y)+".pdf"
    print "Saving ",fName
    plt.savefig(fName)
  elif Her and Pyt8:
    fName = plotdir+"dNdE_lin_HvsP8_yieldPdg"+str(y)+".pdf"
    print "Saving ",fName
    plt.savefig(fName)
  else:
    fName = plotdir+"dNdE_lin_yieldPdg"+str(y)+".pdf"
    print "Saving ",fName
    plt.savefig(fName)
  plt.close()
"""
read and process PPPC data files and pickle dump 
"""
try:
   import cPickle as pickle
except:
   import pickle
import numpy as np
import os
import sys


def annChColumn(annCh):
  """
  returns column in PPPC data file corresponding to input annCh
  """
  if annCh=="tata":
    return 4
  elif annCh=="bb":
    return 7
  elif annCh=="tt":
    return 8
  elif annCh=="WW":
    return 9
  elif annCh=="ZZ":
    return 10
  else:
    sys.exit("Error: incorrect annCh in annChColumn function")
  

if __name__=="__main__":
  
  yields=("gammas","antiprotons","neutrinos_e","neutrinos_mu",
          "neutrinos_tau","positrons","antideuterons")
  annChannels=("tata","bb","tt","WW","ZZ")
  xVals=np.array([10.**expo for expo in np.arange(-8.95,0.05,0.05)])
  masses=(5,6,8,10,15,20,25,30,40,50,60,70,80,90,100,110,120,
          130,140,150,160,180,200,220,240,260,280,300,330,360,
          400,450,500,550,600650,700,750,800,900,1000,1100,1200,
          1300,1500,1700,2000,2500,3000,4000,5000,6000,7000,
          8000,9000,10000,12000,15000,20000,30000,50000,100000)
  
  #if len(sys.argv)==1:
  #  print "Using default out directory ~/DMann/PPPC4DMID/PPPC_plotfiles"
  #  outDir=os.path.expanduser("~/DMann/PPPC4DMID/PPPC_plotfiles")
  #elif len(sys.argv)==2:
  #  outDir=sys.argv[1]
  #  try:
  #    if outDir.startswith("~"):
  #      outDir=os.path.expanduser(outDir)
  #    else:
  #      outDir=os.path.abspath(outDir)
  #    os.makedirs(outDir)
  #  except OSError:
  #    print "Warning: plot directory exists, using existing directory."
  #else:
  #  sys.exit("Error: function called incorrectly, maximum one argument allowed.")
    
  
  
  PPPC_all={"xVals": xVals}
  for y in yields:
    for annCh in annChannels:
      for ew in ("","NoEW"):
      # Read in PPPC data 
        with open(os.path.expanduser("~/DMann/PPPC4DMID/AtProduction"+ew+"_all/AtProduction"+ew+"_"+y+".dat"),"r") as f:
          PPPCdata=np.genfromtxt(f,skip_header=1)
        
        # Make out directory for yield particle
        #try:
        #  os.makedirs(os.path.join(outDir,ew+"_"+y))
        #except:
        #  pass #if folder already exists, do nothing
        #
        for i in range(len(masses)):
          
          dNdlogx=PPPCdata[i*180:(i+1)*180,annChColumn(annCh)]
          PPPC_all["dNdlog10x_"+str(masses[i])+"_"+y+"_"+annCh]=dNdlogx
  
  with open("PPPCdata.pickle","w") as f:
    pickle.dump(PPPC_all,f)
  
  
  import matplotlib.pyplot as plt
  
  with open("PPPCdata.pickle","r") as f:
    PPPCdata=pickle.load(f)
  
  fig,ax=plt.subplots()
  x=PPPCdata["xVals"]
  y=PPPCdata["dNdlog10x_1000_gammas_tt"]
  ax.plot(x,y)
  ax.set_yscale("log")
  ax.set_ylim(1e-5,100)
  #ax.set_xlim(0,1)
  plt.show()
  

  
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


def annChColumn(annCh,ew):
  """
  returns column in PPPC data file corresponding to input annCh
  """
  if annCh=="ee":
    if ew:
      return 4
    else:
      return 2
  if annCh=="mumu":
    if ew:
      return 7
    else:
      return 3
  if annCh=="tata":
    if ew:
      return 10
    else:
      return 4
  elif annCh=="qq":
    if ew:
      return 11
    else:
      return 5
  elif annCh=="cc":
    if ew:
      return 12
    else:
      return 6
  elif annCh=="bb":
    if ew:
      return 13
    else:
      return 7
  elif annCh=="tt":
    if ew:
      return 14
    else:
      return 8
  elif annCh=="WW":
    if ew:
      return 17
    else:
      return 9
  elif annCh=="ZZ":
    if ew:
      return 20
    else:
      return 10
  elif annCh=="gg":
    if ew:
      return 21
    else:
      return 11
  elif annCh=="gaga":
    if ew:
      return 22
    else:
      return 12
  elif annCh=="hh":
    if ew:
      return 23
    else:
      return 13
  else:
    sys.exit("Error: incorrect annCh in annChColumn function")
  

if __name__=="__main__":
  
  yields=("gammas","antiprotons","neutrinos_e","neutrinos_mu",
          "neutrinos_tau","positrons","antideuterons")
  annChannels=("tata","bb","tt","WW","ZZ","qq","cc")
  masses=(5,6,8,10,15,20,25,30,40,50,60,70,80,90,100,110,120,
          130,140,150,160,180,200,220,240,260,280,300,330,360,
          400,450,500,550,600,650,700,750,800,900,1000,1100,1200,
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
    
  
  xVals={True: np.array([10.**(expo-0.025) for expo in np.arange(-8.9,0.05,0.05)]),
         False: np.array([10.**(expo-0.025) for expo in np.arange(-8.95,0.05,0.05)])}
  print xVals[False]
  ewStr={True: "", False: "NoEW"}
  maxIndex={True: 179, False: 180}
  PPPC_all={}
  for ew in (True,False):
    for y in yields:
      for annCh in annChannels:
         for mX in masses:
            key="dNdlog10x"+ewStr[ew]+"_"+str(mX)+"_"+y+"_"+annCh
            PPPC_all[key]=[]
         
  for ew in (True,False):
    PPPC_all["xVals"+ewStr[ew]]=xVals[ew]
    for y in yields:
      for annCh in annChannels:
          # Read in PPPC data 
          with open(os.path.expanduser("~/DMann/PPPC4DMID/AtProduction"
                                       +ewStr[ew]+"_all/AtProduction"
                                       +ewStr[ew]+"_"+y+".dat"),"r") as f:
            for line in f:
               entries=line.split()
               if entries[0]=="mDM":
                  continue
               else:
                  key="dNdlog10x"+ewStr[ew]+"_"+entries[0]+"_"+y+"_"+annCh
                  yieldVal=float(entries[annChColumn(annCh,ew)])
                  PPPC_all[key].append(yieldVal)
            
            #PPPCdata=np.genfromtxt(f,skip_header=1)
          
          #for i in range(len(masses)):    
            #dNdlogx=PPPCdata[i*maxIndex[ew]:(i+1)*maxIndex[ew],annChColumn(annCh,ew)]
            #PPPC_all["dNdlog10x"+ewStr[ew]+"_"+str(masses[i])+"_"+y+"_"+annCh]=dNdlogx


  with open("PPPCdata.pickle","w") as f:
    pickle.dump(PPPC_all,f)
  
  """
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
  """

  
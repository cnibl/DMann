# Makes plots that compare Herwig and Pythia data.
# Usage: python plotCombined.py HERDIR PYTDIR OUTDIR
#
# Command line input arguments:
# HERDIR - a folder with Herwig data files (as e.g. created with combineRuns.py)
# PYTDIR - a folder with Pythia data files (as e.g. created with combineRuns.py)
# OUTDIR - output directory where plots will be placed (created if non-existing)


import os
import sys
import numpy as np
import matplotlib.pyplot as plt

# parameters deciding what to plot and how
annChannels=("tLtR","tRtL","bb","WLWL","WTWT","ZLZL","ZTZT","taLtaR","taRtaL")
WIMPMasses=(10,100,1000,10000)
#annChannels=("taRtaL","taLtaR","taLtaL","taRtaR")
#WIMPMasses=(1000,)
yieldParticles=(-11,11,-14,14,22,-12,12,-14,14,-16,16,22,-2212)
annThresholds={"WLWL" : 80.4, "WTWT" : 80.4, "ZLZL" : 91.2, "ZTZT" : 91.2, "hh" : 125.2, 
               "taLtaL" : 1.8, "taRtaR" : 1.8, "taLtaR" : 1.8, "taRtaL" : 1.8, 
               "muLmuL" : 0.11, "muRmuR" : 0.11, "muLmuR" : 0.11, "muRmuL" : 0.11, "ee" : 5.2e-6, 
               "tLtL" : 173., "tRtR" : 173., "tLtR" : 173., "tRtL" : 173., "bb" : 4.8, 
               "cc" : 1.3, "ss" : 0.1, "uu" : 2.6e-3, "dd" : 5.1e-3}
colors=plt.cm.rainbow(np.linspace(0,1,len(yieldParticles)))
yieldColors={y: colors[i] for (y,i) in zip(yieldParticles,range(len(yieldParticles)))}
lineStyle={"Herwig": "--", "Pythia": "-"}
  
def reBin(x,y,factor):
  """
  Rebins input arrays x,y to fewer bins, the new number of bins is the old number divided by input factor. Assumes linear bins, not log.
  """
  if len(x)!=len(y):
    print "Error in reBin: input x and y have different lengths"
    return -1
  nBinsOld=len(x)
  nBinsNew=nBinsOld/factor
  if nBinsNew-np.floor(nBinsNew)!=0:
    print "Error in reBin: input factor results in non-integer number of new bins"
    return -1
  xNew=np.zeros(nBinsNew)
  yNew=np.zeros(nBinsNew)
  for i in range(0,nBinsNew):
    xNew[i]=0
    yNew[i]=0
    for j in range(0,factor):
      xNew[i]+=x[factor*i+j]/factor
      yNew[i]+=y[factor*i+j]/factor
  return (xNew,yNew)
  
if __name__=="__main__":

  #input checks and assigning some directory variables
  if len(sys.argv)!=4:
    sys.error("ERROR: incorrect usage, usage is 'python plotCombined.py HERDIR PYTDIR OUTDIR'")
  for i in range(1,3):
    if not os.path.exists(sys.argv[i]):
      sys.exit("ERROR: provided directory %s does not exist." % sys.argv[i]) 
  inDir={"Herwig": "", "Pythia": ""}
  if sys.argv[1].startswith("~"):
    inDir["Herwig"]=os.path.expanduser(sys.argv[1])
  else:
    inDir["Herwig"]=os.path.abspath(sys.argv[1])
  if sys.argv[2].startswith("~"):
    inDir["Pythia"]=os.path.expanduser(sys.argv[2])
  else:
    inDir["Pythia"]=os.path.abspath(sys.argv[2])
  if sys.argv[3].startswith("~"):
    outDir=os.path.expanduser(sys.argv[3])
  else:
    outDir=os.path.abspath(sys.argv[3])
  if not os.path.exists(outDir):
    os.makedirs(outDir)
  
  for annCh in annChannels: 
      for mX in WIMPMasses: 
        if annThresholds[annCh] < mX: 
          fig,ax=plt.subplots() 
          for y in yieldParticles:
            for code in ("Herwig","Pythia"):  
              dNdx=[]
              x=[]
              if code=="Herwig":
                dataFile=os.path.abspath(os.path.join(inDir[code],annCh+"_m"+str(mX),
                         "da-her7-mx"+str(mX)+"-"+annCh+"-y"+str(y)+".dat"))
              elif code=="Pythia":
                dataFile=os.path.abspath(os.path.join(inDir[code],annCh+"_m"+str(mX),
                         "da-pyt8-mx"+str(mX)+"-"+annCh+"-y"+str(y)+".dat"))
              if os.path.exists(dataFile):
                with open(dataFile,"r") as f:
                  data=np.genfromtxt(f,skip_header=8)
                x=data[:,0] #assumed to be x=E_kin/mX
                dNdx=data[:,1] #assumed to be dNdx [ann^-1]
                (x,dNdx)=reBin(x,dNdx,4)
                ax.plot(x,dNdx,lineStyle[code],color=yieldColors[y],label="y="+str(y)+", "+code[0])
                
                if code=="Herwig":
                  dNdxH=dNdx
                elif code=="Pythia":
                  dNdxP=dNdx  
            ax.fill_between(x,dNdxH,dNdxP,color=yieldColors[y],alpha=0.5)  
          ax.legend(ncol=2)
          ax.set_xlim(0,1)
          ax.set_ylim(1e-3,1e2)
          ax.set_yscale("log")
          ax.set_xlabel(r"$x$")
          ax.set_ylabel(r"$dN/dx$ [ann.$^{-1}$]")
          ax.set_title(annCh+r", $m_\chi="+str(mX)+"$ GeV")
          plotFileName=os.path.abspath(os.path.join(outDir,annCh+"_m"+str(mX)+".pdf"))
          plt.savefig(plotFileName)
          plt.close()
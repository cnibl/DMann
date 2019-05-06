# A script that takes a DMann results directory as command line argument
# and combines all subruns for Herwig and Pythia in that directory. Puts
# the combined data in the given results directory. Ignores event files.

import os
import sys
import glob
import numpy as np
import datetime
import matplotlib.pyplot as plt

if len(sys.argv)>3:
  sys.exit("ERROR: correct usage is python combine_runs.py RESDIR (plot) \
           for some DMann results directory RESDIR with optional argument plot.")
if len(sys.argv)==3 and sys.argv[2]=="plot":
  plot=True
  print "Will make plots of combined data"
else:
  plot=False

if sys.argv[1].startswith("~"):
  resDir=os.path.expanduser(sys.argv[1])
else:
  resDir=os.path.abspath(sys.argv[1])
if not os.path.exists(resDir):
  sys.exit("ERROR: provided DMann results directory does not exist.")

annChannels=("tLtR","tRtL","bb","WLWL","WTWT","ZLZL","ZTZT","taLtaR","taRtaL")
WIMPMasses=(10,100,1000,10000)
yieldParticles=(-11,11,-14,14,-12,12,-14,14,-16,16,22,-2212)

annThresholds={"WLWL" : 80.4, "WTWT" : 80.4, "ZLZL" : 91.2, "ZTZT" : 91.2, "hh" : 125.2, 
               "taLtaL" : 1.8, "taRtaR" : 1.8, "taLtaR" : 1.8, "taRtaL" : 1.8, 
               "muLmuL" : 0.11, "muRmuR" : 0.11, "muLmuR" : 0.11, "muRmuL" : 0.11, "ee" : 5.2e-6, 
               "tLtL" : 173., "tRtR" : 173., "tLtR" : 173., "tRtL" : 173., "bb" : 4.8, 
               "cc" : 1.3, "ss" : 0.1, "uu" : 2.6e-3, "dd" : 5.1e-3}
colors=plt.cm.rainbow(np.linspace(0,1,len(yieldParticles)))
yieldColors={y: colors[i] for (y,i) in zip(yieldParticles,range(len(yieldParticles)))}
lineStyle={"Herwig": "--", "Pythia": "-"}

if __name__=="__main__":
      
  for annCh in annChannels:
    for mX in WIMPMasses:
      if annThresholds[annCh] < mX:
        if plot:
          fig,ax=plt.subplots()
        for code in ("Herwig","Pythia"):
          # List subrun directories w glob
          if code=="Herwig":
            dataDirs=glob.glob(os.path.join(resDir,"Herwig_*"))
            try: 
              dataDirs.remove(os.path.join(resDir,"Herwig_combined"))
            except:
              pass #not necessary to remove if not in list
          else:
            dataDirs=glob.glob(os.path.join(resDir,"Pythia_*"))
            try:
              dataDirs.remove(os.path.join(resDir,"Pythia_combined"))
            except:
              pass #not necessary to remove if not in list
      
          # If there are directories, go through ann channels, masses and yield particles and
          # read and add together data
          if len(dataDirs)>0:
            if code=="Herwig":
              try:
                os.makedirs(os.path.join(resDir,"Herwig_combined",annCh+"_m"+str(mX)))
              except:
                pass # don't need to do anything if directory exists
            else:
              try:
                os.makedirs(os.path.join(resDir,"Pythia_combined",annCh+"_m"+str(mX)))
              except:
                pass # don't need to do anything if directory exists
            for y in yieldParticles:
              for log in ("","-log"):
                dNdx=[] # =dNdlog10x if log=="-log"
                x=[]
                nFiles=0 #tracks number of events, 100k per increment
                for dDir in dataDirs:
                  if code=="Herwig":
                    dataFile=os.path.abspath(os.path.join(resDir,dDir,annCh+"_m"+str(mX),
                           "da-her7-mx"+str(mX)+"-"+annCh+"-y"+str(y)+log+".dat"))
                  else:
                    dataFile=os.path.abspath(os.path.join(resDir,dDir,annCh+"_m"+str(mX),
                           "da-pyt8-mx"+str(mX)+"-"+annCh+"-y"+str(y)+log+".dat"))
                  if os.path.exists(dataFile):
                    with open(dataFile,"r") as f:
                      if code=="Herwig" and log=="-log":
                        data=np.genfromtxt(f,skip_header=10)
                      else:
                        data=np.genfromtxt(f,skip_header=8)
                    
                    if log!="-log":
                      binWid=np.diff(data[:,0])[0]
                      #binWid*=mX #for Herwig runs from before Apr 23
                      if nFiles==0:
                        x=data[:,0]/mX #note: Herwig runs from before April 23 have x, not E, in dataFile
                        dNdx=data[:,1]*mX/binWid
                      else:
                        dNdx+=data[:,1]*mX/binWid

                    else: #logarithmic file
                      xEdges=np.logspace(-10,0,251) # in x
                      binWidths=np.diff(xEdges)
                      if code=="Herwig": #columns are binLow-binHigh-norm-counts/nAnn 
                        xCenters=(data[:,0]+data[:,1])/2./mX
                      else:
                        xCenters=[(xEdges[i+1]+xEdges[i])/2. for i in range(len(xEdges)-1)]
                      if nFiles==0:
                        x=xCenters
                        if code=="Herwig":
                          dNdx=np.divide(data[:,3],binWidths)*mX/np.log(10.)
                        else:
                          dNdx=np.divide(data[:,1],binWidths)*mX/np.log(10.)
                      else:
                        if code=="Herwig":
                          dNdx+=np.divide(data[:,3],binWidths)*mX/np.log(10.)
                        else:
                          dNdx+=np.divide(data[:,1],binWidths)*mX/np.log(10.)
                    nFiles+=1
                currentDT=datetime.datetime.now()
                headText="\n".join(("Combined data file for DMann with x=E_kin/mX vs dNdx",
                                    "Created: "+currentDT.strftime("%Y-%m-%d %H:%M:%S"),
                                    "Number of events in file: "+str(nFiles*100000),
                                    "WIMP mass: "+str(mX),
                                    "Annihilation channel: "+annCh,
                                    "PDG code of yield particle: "+str(y),
                                    "",
                                    "x             dNdx [ann.^-1] "))
                if code=="Herwig":
                  fileName=os.path.abspath(os.path.join(resDir,"Herwig_combined",annCh+"_m"+str(mX),
                           "da-her7-mx"+str(mX)+"-"+annCh+"-y"+str(y)+log+".dat"))
                else:
                  fileName=os.path.abspath(os.path.join(resDir,"Pythia_combined",annCh+"_m"+str(mX),
                           "da-pyt8-mx"+str(mX)+"-"+annCh+"-y"+str(y)+log+".dat"))
                if nFiles!=0:
                  dNdx/=nFiles #normalize to total no. of annihilations
                  with open(fileName,"w") as f:
                    np.savetxt(fname=f,X=np.array(zip(x,dNdx)),fmt="%-12.5e    %-12.5e",header=headText)
                # if desired, make plots
                if plot:
                  ax.plot(x,dNdx,lineStyle[code],color=yieldColors[y],label="y="+str(y)+", "+code[0])
                
        if plot:      
          ax.legend(ncol=2)
          ax.set_xlim(0,1)
          ax.set_ylim(1e-3,1e2)
          ax.set_yscale("log")
          ax.set_xlabel(r"$x$")
          ax.set_ylabel(r"$dN/dx$ [ann.$^{-1}$]")
          ax.set_title(annCh+r", $m_\chi="+str(mX)+"$ GeV")
          try: 
            os.makedirs(os.path.abspath(os.path.join(resDir,"Plots_combined")))
          except:
            pass
          plotFileName=os.path.abspath(os.path.join(resDir,"Plots_combined",annCh+"_m"+str(mX)+".pdf"))
          plt.savefig(plotFileName)
          plt.close()


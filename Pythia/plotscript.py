# plotscript.py
# script for plotting the pythia8 data files

import numpy as np
import subprocess
import matplotlib.pyplot as plt
import sys

if "testmode" in sys.argv:
  testmode = True

if len(sys.argv) < 2: # note that "plotscript.py" is the sys.argv[0] 
  errormsg = "ERROR: usage is 'python plotscript.py plotmode linlog'"
  errormsg += "\nplotmode = "
  errormsg += "\n\tann: same annihilation channel, different yield particles in same plot"
  errormsg += "\n\tyield: same yield particle, different annihilation channels in same plot"  
  errormsg += "\nlinlog = "
  errormsg += "\n\tlin: linear x-axis"
  errormsg += "\n\telse defaults to logarithmic x-axis"
  sys.exit(errormsg)
plotmode = str(sys.argv[1])

datadir = "pythia8data"
plotsdir = "plots"
if testmode == True:
  datadir = "TEST-pythia8"
  plotdir = "TEST-plots"

proc = subprocess.Popen(["ls",datadir+"/"], stdout=subprocess.PIPE)
filelist = proc.stdout.readlines()
filelist = [str(f.rstrip()) for f in filelist]
filelist = [(datadir+"/"+"{0}").format(f) for f in filelist]
subprocess.call(["mkdir","-p",plotdir])  

annch = ["$\\tau^+ \\tau^-$","$W^+W^-$","$b\\bar{b}$","$t\\bar{t}$"]
yieldch = ["$e^+$","$\\bar{p}$","$\\nu_{\mu}+ \\bar{\\nu}_{\mu}$","$\gamma$"]
"""
plotmode = "ann": plot with same annihilation channel, different yield particles in one plot  
plotmode = "yield": plot with same yield particle, different annihilation channel in one plot  
""" 
for i in range(4):
  plt.figure(i)
  if plotmode == "ann":
    plt.title(annch[i])  
    j=0
    for f in filelist[i*4:i*4+4]:
      datafile = open(f,'r')
      data = np.genfromtxt(datafile,skip_header=8)
      plt.plot(data[:,0], data[:,1], label=yieldch[j])
      plt.legend(loc = "best")
      plt.xlabel("$E_{{\\rm kin}}/m_\chi=(E-m)/m_\chi$")
      plt.ylabel("$dN/dE$")
      plt.gca().set_xscale("log") #change filename if removing log scale
      plt.gca().set_yscale("log")  
      plt.xlim(1e-5,1)
      plt.ylim(1e-5,1e1)            
      datafile.close()
      j += 1
    plotfiles = ["tautau","WW","bbbar","ttbar"]
    if testmode == True:
      plotfiles = ["{0}-TEST".format(f) for f in plotfiles]
    plotfiles = [(plotdir+"/da-m200-n1e6-ann-{0}.pdf").format(f) for f in plotfiles] #change filename if removing log scale
    plt.savefig(plotfiles[i])
  elif plotmode == "yield":
    plt.title(yieldch[i])
    for j in range(i,16,4):
      datafile = open(filelist[j],'r')
      data = np.genfromtxt(datafile,skip_header=8)
      plt.plot(data[:,0], data[:,1], label=annch[j/4])
      plt.legend(loc = "best")
      plt.xlabel("$E_{{\\rm kin}}/m_\chi=(E-m)/m_\chi$")
      plt.ylabel("$dN/dE$")
      plt.gca().set_xscale("log") #change filename if removing log scale 
      plt.gca().set_yscale("log")  
      plt.xlim(1e-5,1)
      plt.ylim(1e-5,1e1)      
#      plt.ylim(0,2)
      datafile.close()
    plotfiles = ["e+","pbar","numu","gamma"]    
    if testmode == True:
      plotfiles = ["{0}-TEST".format(f) for f in plotfiles]
    plotfiles = [(plotdir+"/da-m200-n1e6-yield-{0}.pdf").format(f) for f in plotfiles] #change filename if removing log scale  
    plt.savefig(plotfiles[i])


for i in range(4):
  plt.figure(i)
  plt.close()

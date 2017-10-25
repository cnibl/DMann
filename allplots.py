# allplots.py
# Script that plots all the data files (.dat) in a given directory
#
# Usage: python allplots.py datadir plotdir
# datadir: the directory where the data files are
# plotdir: the directory where the plots will end up

import numpy as np
import subprocess
import matplotlib.pyplot as plt
import sys


if len(sys.argv) < 3: # note that "plotscript.py" is the sys.argv[0] 
  errormsg = "ERROR: usage is 'python allplots.py datadir plotdir'"
  errormsg += "\ndatadir: the directory where the data files are"
  errormsg += "\nplotdir: the directory where the plots will end up"
  sys.exit(errormsg)
datadir = argv[1]
plotdir = argv[2]

proc = subprocess.Popen(["ls",datadir+"/"], stdout=subprocess.PIPE)
filelist = proc.stdout.readlines()
filelist = [str(f.rstrip()) for f in filelist]
plotfilenames = [f.split('.')[0] for f in filelist]
filelist = [(datadir+"/"+"{0}").format(f) for f in filelist]
subprocess.call(["mkdir","-p",plotdir])  

"""
Loop through all data files and plot them with filename 
""" 
for i in range(len(filelist)):
  plt.figure(i)
  plt.title(plotfilenames[i])
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
  plt.savefig(plotfilenames[i]+".pdf")
  plt.close()
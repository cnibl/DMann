# plotscript.py
# script for plotting the pythia8 data files

import numpy as np
import subprocess
import matplotlib.pyplot as plt

proc = subprocess.Popen(["ls","pythia8data/"], stdout=subprocess.PIPE)
filelist = proc.stdout.readlines()
filelist = [str(f.rstrip()) for f in filelist]
filelist = ["pythia8data/{0}".format(f) for f in filelist]

titles = ["$\\tau^+ \\tau^-$","$W^+W^-$","$b\\bar{b}$","$t\\bar{t}$"]
keys = ["$e^+$","$\\bar{p}$","$\\nu_{\mu}/\\bar{\\nu}_{\mu}$","$\gamma$"]
for i in range(4):
  plt.figure(i)
  plt.title(titles[i])
  j=0
  for f in filelist[i*4:i*4+4]:
    datafile = open(f,'r')
    data = np.genfromtxt(datafile)
    plt.plot(data[:,0], data[:,1], label=keys[j])
    plt.legend(loc = "best")
    plt.xlabel("$E_{{\\rm kin}}/m_\chi=(E-m)/m_\chi$")
    plt.ylabel("$dN/dE$")
    plt.gca().set_xscale("log")
    plt.gca().set_yscale("log")  
    datafile.close()
    j += 1
  
subprocess.call(["mkdir","-p","plots"])  
plotfiles = ["tautau","WW","bbbar","ttbar"]
plotfiles = ["plots/da-m200-n1e6-{0}.pdf".format(f) for f in plotfiles]
for i in range(4):
  plt.figure(i)
  plt.savefig(plotfiles[i])
  plt.close()

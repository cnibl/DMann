# plotscript.py
# script for plotting the pythia8 data files

import numpy as np
import subprocess
import matplotlib.pyplot as plt

proc = subprocess.Popen(["ls","pythia8data/"], stdout=subprocess.PIPE)
filelist = proc.stdout.readlines()
filelist = [str(f.rstrip()) for f in filelist]
filelist = ["pythia8data/{0}".format(f) for f in filelist]

i=0
for f in filelist:
  i += 1
  datafile = open(f,'r')
  data = np.genfromtxt(datafile)
  plt.plot(data[:,0], data[:,1], label=i)
  plt.legend(loc = "best")
  plt.gca().set_xscale("log")
  plt.gca().set_yscale("log")  
  datafile.close()
plt.show()
plt.close()

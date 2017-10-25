# plotyields.py 
#
# Plot yields of a particle for different annihilation channels

import numpy as np
import matplotlib.pyplot as plt
import sys

pdgyield = 22
pdgann = [15,6,5,24]
mx = 200

datadir = "TEST-pythia8"
plotdir = "TEST-plots"

pdgnames = {"e+": -11,"e-": 11,"pbar": -2212,"numu": 14,"numubar": -14,"gamma": 22,"b": 5,"t": 6,"tau-": 15,"W-": 24}
def pdg2name(pdg):
  for name, p in pdgnames.items():
    if p==pdg:
      return str(name)
  sys.exit("pdg2pname: particle with PDG code "+str(p)+" not available")
  return "ERROR"
  
def name2pdg(name):
  if name in pdgnames:
    return pdg
  else:
    sys.exit("name2pdg: particle with name "+str(name)+" not available")
    return "ERROR"

#logarithmic bin sizes
binedges = np.logspace(-10,0,251,base=10.0) # 251 logarithmically spaced bins from 10^-10 to 10^0 (same as imported data)
binwidths = np.diff(binedges) 
bincenters = np.zeros(len(binwidths))
for i in range(len(binwidths)):
  bincenters[i] = binedges[i] + (binedges[i+1]-binedges[i])/2.

plt.figure()
for p in pdgann:
  fname = datadir+"/da-mx"+str(mx)+"-ch"+str(p)+"-int"+str(pdgyield)+".dat"
  data = np.genfromtxt(open(fname,"r"),skip_header=8)
  xaxis = mx*data[:,0]
  yaxis = np.log10(np.exp(1.))*np.multiply(data[:,1],np.divide(data[:,0],binwidths)) # gives correct units (?)
  print np.trapz(yaxis,xaxis)
  plt.plot(xaxis,yaxis,label=pdg2name(p))
  plt.legend(loc="best")
  plt.title(pdg2name(pdgyield))
  plt.xlabel("E")
  plt.ylabel("dN/dE")
  plt.gca().set_xscale("log")
  plt.xlim(mx/1e5,mx)

plt.show()
plt.close()
  
# plotyields.py 
#
# Plot yields of a particle for different annihilation channels

import numpy as np
import matplotlib.pyplot as plt
import sys

pdgyield = 14
pdgann = [15,6,5,24]
mx = 200

data_p8dir = "pythia8data"
data_p6dir = "pythia6data"
plotdir = "plots"

pdgnames = {"e^+": -11,"e^-": 11,"\\bar{p}": -2212,"\\nu_\mu": 14,"\\bar{\\nu}_\mu": -14,"\gamma": 22,"b": 5,"t": 6,r"\tau^-": 15,"W^-": 24}
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
  
#logarithmic bin sizes
binedges = mx*np.logspace(-10,0,251,base=10.0) # 251 logarithmically spaced binedges from 10^-10*mx to 10^0*mx
binwidths = np.diff(binedges) 
bincenters = np.zeros(len(binwidths)) # now matches imported data below
for i in range(len(binwidths)):
  bincenters[i] = binedges[i] + (binedges[i+1]-binedges[i])/2.

cl = ["red","blue","black","green"]
labels = [["$"+pdg2name(p)+"$"+", Pyt6","$"+pdg2name(p)+"$"+", Pyt8"] for p in pdgann]
plt.figure()
for p,i in zip(pdgann,range(4)):
  fname = data_p8dir+"/da-mx"+str(int(mx))+"-ch"+str(p)+"-int"+str(pdgyield)+".dat"
#  fname = data_p8dir+"/histdata-mx"+str(int(mx))+"-ch"+str(p)+"-int"+str(pdgyield)+".dat"  
  data_p8 = np.genfromtxt(open(fname,"r"),skip_header=8) # x, yield
  fname = data_p6dir+"/da-pyt6-mx"+str(int(mx))+"-ch"+str(p)+"-int"+str(pdgyield)+".dat"
  data_p6 = np.genfromtxt(open(fname,"r"),skip_header=1) # i, E, yield
  xaxis_p8 = mx*data_p8[:,0]
  xaxis_p8 *= 1./mx # Depending on if energies or x=E_kin/mX are used in histogram
  xaxis_p6 = data_p6[:,1]
#  yaxis_p8 = np.log(10.)*np.multiply(data_p8[:,1],np.divide(data_p8[:,0],binwidths)) # gives correct units (?)
  yaxis_p8 = data_p8[:,1]
  yaxis_p8 /= (np.diff(np.log10(binwidths))[0])
  yaxis_p6 = data_p6[:,2]
  yaxis_p6 = np.multiply(yaxis_p6,np.log(10)*xaxis_p6)  

  print "Pythia8: ",np.trapz(yaxis_p8,np.log10(xaxis_p8)),"Pythia6: ",np.trapz(yaxis_p6,np.log10(xaxis_p6))
  plt.plot(xaxis_p6,yaxis_p6,label=labels[i][0],color=cl[i],linewidth=1,linestyle="dashed")
  plt.plot(xaxis_p8,yaxis_p8,label=labels[i][1],color=cl[i],linewidth=1) 
  plt.fill_between(xaxis_p6,yaxis_p6,yaxis_p8,alpha=0.5,color=cl[i])
  plt.legend(loc="best")
  plt.title("$"+pdg2name(pdgyield)+"$")
  plt.xlabel(r"$E_{\rm kin}$")
  plt.ylabel(r"$dN/d(\log E)$")
  plt.xlim(mx*1e-8,mx)
  plt.ylim(1e-2,100) # for log
#  plt.ylim(0,40) # for lin
  plt.gca().set_xscale("log")
  plt.gca().set_yscale("log")
#  plt.gca().grid(linestyle="-",which="minor", linewidth=.1,alpha=.5)


#plt.figure(2)
#plt.plot(xaxis_p6,np.multiply(data_p6[:,2],xaxis_p6)/data_p8[:,1])
plt.savefig("dNdlogE_p6vsp8_pdgyield"+str(pdgyield)+".pdf")
plt.close()
  

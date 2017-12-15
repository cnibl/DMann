"""
Plotting PPPC fluxes
"""

import numpy as np
import matplotlib.pyplot as plt

noEW = False
if noEW:
  fName = open("PPPC4DMID/AtProductionNoEW_all/AtProductionNoEW_antiprotons.dat","r")
else:
  fName = open("PPPC4DMID/AtProduction_all/AtProduction_antiprotons.dat","r")  
data = np.genfromtxt(fName,skip_header=1) # data matrix

xaxis = np.array([ 10.**exp for exp in np.unique(data[:,1]) ])
xaxis *= 200.
index200 = np.where(data[:,0]==200) # rows in data matrix for 200 GeV DM mass
anncodes = [15,5,6,24]
yaxis200 = np.zeros((len(anncodes),len(xaxis)))
"""
Fluxes for various annihilation channels, dN/dlog10(x) where x=E_kin/mX
"""
if noEW:
  yaxis200[0] = data[index200,4] # tau tau 
  yaxis200[1] = data[index200,7] # b bbar
  yaxis200[2] = data[index200,8] # t tbar
  yaxis200[3] = data[index200,9] # W W
else:
  yaxis200[0] = data[index200,10] # tau tau 
  yaxis200[1] = data[index200,13] # b bbar
  yaxis200[2] = data[index200,14] # t tbar
  yaxis200[3] = data[index200,17] # W W

means = [np.mean(yaxis200[i]) for i in range(4)]
colors = ["black","red","blue","green"]
fig, ax = plt.subplots()
for i, p in zip(range(len(anncodes)),anncodes):
  ax.plot(xaxis, yaxis200[i], label=str(p), color=colors[i])

ax.set_ylim(1e-2,1e2)
ax.set_xlim(2e-8,2e2)
ax.set_xlabel(r"$E_{\rm kin}$")
ax.set_ylabel(r"$dN/d\log E_{\rm kin}$")
ax.set_xscale("log")
ax.set_yscale("log")    
ax.legend(loc="best")
plt.show()
plt.close()
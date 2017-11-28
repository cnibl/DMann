# herwigplot.py
#
# Script to make simple plots of Herwig data

import numpy as np
import matplotlib.pyplot as plt

massX = 200.0
yieldPdgs = [22, -11, -2212, 14]
labels = [r"$\gamma$",r"$e^+$",r"$\bar{p}$",r"$\nu_\mu$"]
nEvt = 10000
colors = ["green","red","black","blue"]

for i, p in zip(range(len(yieldPdgs)),yieldPdgs):
	fName = "DMann-" + str(p) + ".mult"
	data = np.genfromtxt(open(fName,"r"),skip_header=2)
	logBinWidths = np.diff(np.log10(data[:,0]))[0]
	xaxis = (data[:,0]+data[:,1])/2.
	yaxis = data[:,3]/nEvt/logBinWidths
	plt.plot(xaxis,yaxis,color=colors[i],label=labels[i])
	plt.gca().set_xscale("log")
	plt.gca().set_yscale("log")
	plt.xlim(massX*1e-10,massX)
	plt.ylim(1e-2,1e2)
	plt.legend(loc="best")

plt.show()
plt.close()
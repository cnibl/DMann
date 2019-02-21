#!/Users/carlniblaeus/anaconda/bin/python
"""
runMG.py

Script that runs MadGraph for the DMann folders set up with setupMG.py. Simulations settings are set in simSettings.py

Usage: ./runMG.py  

"""

import os
import sys
import subprocess
import glob
import simSettings as sets
import MGfunctions as mgf
import time
import math

"""
First check that everything is set up properly
"""
if sets.MG_DIR.startswith("~"):
   absMGdir=os.path.expanduser(sets.MG_DIR)
else:
   absMGdir=os.path.abspath(sets.MG_DIR)
if not os.path.exists(absMGdir):
   sys.exit("ERROR: The MadGraph directory provided does not exist")
for ann in sets.ANN_CHANNELS:
   if not os.path.exists(os.path.join(absMGdir,"DMann_"+ann)):
      sys.exit("ERROR: No folder exists for %s, run setupMG.py" % ann)
      
# The threshold in GeV that the WIMP mass has to exceed for annihilations to be possible
annThresholds={"WLWL" : 80.4, "WTWT" : 80.4, "ZLZL" : 91.2, "ZTZT" : 91.2, "hh" : 125.2, 
               "taLtaL" : 1.8, "taRtaR" : 1.8, "muLmuL" : 0.11, "muRmuR" : 0.11, "ee" : 5.2e-6, 
               "tLtL" : 173., "tRtR" : 173., "bb" : 4.8, "cc" : 1.3, "ss" : 0.1, "uu" : 2.6e-3, "dd" : 5.1e-3}

if __name__=="__main__":
   """
   Go to MG directory and go down in directories corresponding to all annihilation channels and run MG for each WIMP mass.
   """
   allstart=time.time()
   for ann in sets.ANN_CHANNELS:
      print "Running MadGraph for %s ... " % ann
      os.chdir(os.path.join(absMGdir,"DMann_"+ann))
      mgf.set_n_ann(sets.N_ANN)
      for mwimp in sets.WIMP_MASSES:
         print "\tRunning with mWIMP = %5.3f ... " % mwimp
         start=time.time()
         if annThresholds[ann] > mwimp:
            print "\tWarning: m_WIMP = %5.3f GeV too small for annihilation channel %s" % (mwimp,ann)
            continue # skip to next mwimp value
         mgf.set_run_tag(sets.RUN_TAG+"_m"+str(mwimp))
         mgf.set_wimp_mass(mwimp)
         fileName=mgf.write_MG_runscript(ann,sets.N_ANN,sets.RUN_TAG,mwimp)
         with open("".join(("DMann_runMG_",ann,"_mwimp",str(int(mwimp)),".log")),"w") as log:
            proc=subprocess.Popen(["./bin/madevent",fileName],stdout=log,stderr=log)
            proc.wait()
         end=time.time()
         if ((end-start)/60) > 60:
            print "\tTook %i h, %i min, %i s" % (int(math.floor(math.floor((end-start)/60)/60)),
                                                             int(math.floor((end-start)/60)%60),
                                                             int((end-start)%60))
         else:
            print "\tTook %i min, %i s" % (int(math.floor((end-start)/60)),int((end-start)%60))
   end=time.time()
   print "Done! Took %i h, %i min, %i s" % (int(math.floor(math.floor((end-allstart)/60)/60)),
                                                             int(math.floor((end-allstart)/60)%60),
                                                             int((end-allstart)%60))      
         
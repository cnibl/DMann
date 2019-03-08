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
import time
import math
import multiprocessing as mp
import simSettings as sets
import MGfunctions as mgf

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
   for mX in sets.WIMP_MASSES:
      if not os.path.exists(os.path.join(absMGdir,"DMann_"+sets.RUN_TAG+"_"+ann+"_m"+str(mX))):
         sys.exit("ERROR: No folder exists for %s, run setupMG.py" % ann)
      
# The threshold in GeV that the WIMP mass has to exceed for annihilations to be possible
annThresholds={"WLWL" : 80.4, "WTWT" : 80.4, "ZLZL" : 91.2, "ZTZT" : 91.2, "hh" : 125.2, 
               "taLtaL" : 1.8, "taRtaR" : 1.8, "muLmuL" : 0.11, "muRmuR" : 0.11, "ee" : 5.2e-6, 
               "tLtL" : 173., "tRtR" : 173., "bb" : 4.8, "cc" : 1.3, "ss" : 0.1, "uu" : 2.6e-3, "dd" : 5.1e-3}

def run_MG(annCh,mWimp,runTag,nAnn,nCores):
   """
   Runs MadGraph for given input
   Input: annCh - the annihilation channel 
          mWimp - the WIMP mass
          runTag - the run_tag for the run
          nAnn - number of annihilations
          nCores - number of cores to use per MG run
   Returns: the scenario, return code from madevent and time spent
   """
   start=time.time()
   """
   Set no. of ann., runtag, WIMP mass, couplings corresponding to polarization in param_card, couplings and properties of beams, reset all cuts and set up madspin_card if necessary
   """
   os.chdir(os.path.join(absMGdir,"DMann_"+sets.RUN_TAG+"_"+annCh+"_m"+str(mWimp)))   
   mgf.set_n_ann(nAnn)
   mgf.set_run_tag(runTag)
   mgf.set_couplings(annCh) 
   mgf.set_wimp_mass(mWimp)
   mgf.set_beam_particles()
   mgf.reset_cuts()
   if annCh in ["WLWL","WTWT","ZLZL","ZTZT","tLtL","tRtR"]:
      mgf.set_madspin_card(annCh) 
   fileName=mgf.write_MG_runscript(annCh,nAnn,runTag,mWimp,nCores)
   print "Starting MadGraph run for %s, mWIMP=%5.1f" % (annCh,mWimp)
   logFile=os.path.join(absMGdir,"log_DMann","DMann_runMG_"+sets.RUN_TAG+"_"+annCh+"_m"+str(int(mWimp))+".log")
   with open(logFile,"w") as log:
      proc=subprocess.Popen(["./bin/madevent",fileName],stdout=log,stderr=log)
      returnCode=proc.wait()
   end=time.time()
   global totalRuns
   with nCur.get_lock():
      nCur.value+=1
   print "Finished run %i of %i" % (nCur.value,totalRuns)
   return (annCh+", m="+str(mWimp),returnCode,end-start)

def collect_result(res):
   """
   Callback function that collect results in apply_async call.
   """
   global results
   results.append(res)
   return
   
if __name__=="__main__":
   """
   Go to MG directory and go down in directories corresponding to all annihilation channels and WIMP masses and run MG for all combinations in a parallellised way.
   """
   nCur=mp.Value('i',0) #integer shared between processes to count current run, initialised at 0
   totalRuns=len(sets.WIMP_MASSES)*len(sets.ANN_CHANNELS)
   allstart=time.time()
   results=[]
   cpus=mp.cpu_count()
   pool=mp.Pool(processes=sets.MG_PAR) #processes=number of parallell MG runs to do
   if not os.path.exists(os.path.join(absMGdir,"log_DMann")):
      os.makedirs(os.path.join(absMGdir,"log_DMann"))
   for annCh in sets.ANN_CHANNELS:
      for mwimp in sets.WIMP_MASSES:
         if annThresholds[annCh] > mwimp:
            print "Note: m_WIMP = %5.3f GeV too small for annihilation channel %s, skipping" % (mwimp,annCh)
            continue # skip to next mwimp value
         pool.apply_async(run_MG,args=(annCh,mwimp,sets.RUN_TAG,sets.N_ANN,sets.MG_CORES),callback=collect_result)
   
   pool.close()
   pool.join()
   end=time.time()
   print "===================================================="
   print "Done! Took %i h, %i min, %i s" % (int(math.floor(math.floor((end-allstart)/60)/60)),
                                                             int(math.floor((end-allstart)/60)%60),
                                                             int((end-allstart)%60))      
   print "Have run MadGraph for the following combinations: " 
   print "Run\t\tErrorcode\tTime spent[sec]"
   for res in results:
      print "%s\t\t%i\t%15.1f" % (res[0],res[1],res[2])
   
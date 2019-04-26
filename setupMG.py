#!/Users/carlniblaeus/anaconda/bin/python
"""
setupMG.py

Script to set up the folder structure for the various annihilation channel, sets couplings to get the right polarization. Creates folders in the MadGraph directory provided. All functions are defined in the library MGfunctions.py. Simulations settings are set in simSettings.py

Usage: ./setupMG.py  

"""

import os
import sys
import subprocess
import glob
import multiprocessing as mp
import simSettings as sets
import MGfunctions as mgf

if sets.MG_DIR.startswith("~"):
   absMGdir=os.path.expanduser(sets.MG_DIR)
else:
   absMGdir=os.path.abspath(sets.MG_DIR)
if not os.path.exists(absMGdir):
   sys.exit("ERROR: The MadGraph directory provided does not exist")


def setup_MG(annCh,mX,runTag,madspin):
   """
   Go to MG directory and run mg5_aMC to create directories for all annihilation channels and WIMP masses
   """
   os.chdir(absMGdir)
   fileName=mgf.write_MG_setupscript(annCh,mX,runTag,madspin)
   print "Setting up %s, mX = %-5.0f..." % (annCh,mX)
   with open("".join(("log_DMann/DMann_setupMG_",runTag,"_",annCh,"_m",str(mX),".log")),"w") as log:
      proc=subprocess.Popen(["./bin/mg5_aMC",fileName],stdout=log,stderr=log)
      proc.wait()
      

def collect_result(res):
   """
   A callback function needed to collect results in apply_async call 
   """
   global results
   results.append(res)
   
      
if __name__=="__main__":
   """
   Setup the MG folders for each annihilation channel and WIMP mass in parallell.
   """
   cpus=mp.cpu_count()
   pool=mp.Pool(cpus)
   results=[]
   if not os.path.exists(os.path.join(absMGdir,"log_DMann")):
      os.makedirs(os.path.join(absMGdir,"log_DMann"))
   for annCh in sets.ANN_CHANNELS:
      for mX in sets.WIMP_MASSES:
         if mgf.annThresholds[annCh] > mX:
            print "Note: m_WIMP = %5.3f GeV too small for annihilation channel %s, skipping" % (mX,annCh)
            continue # skip to next mwimp value
         pool.apply_async(setup_MG,args=(annCh,mX,sets.RUN_TAG,sets.MADSPIN),callback=collect_result)
         
   pool.close()
   pool.join()
         

         
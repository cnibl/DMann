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
import simSettings as sets
import MGfunctions as mgf

if sets.MG_DIR.startswith("~"):
   absMGdir=os.path.expanduser(sets.MG_DIR)
else:
   absMGdir=os.path.abspath(sets.MG_DIR)
if not os.path.exists(absMGdir):
   sys.exit("ERROR: The MadGraph directory provided does not exist")

if __name__=="__main__":
   """
   Go to MG directory and run mg5_aMC to create directories for all annihilation channels 
   """
   for ann in sets.ANN_CHANNELS:
      os.chdir(absMGdir)
      fileName=mgf.write_MG_setupscript(annch=ann)
      print "Setting up %s ..." % ann
      with open("".join(("DMann_setupMG_",ann,".log")),"w") as log:
         proc=subprocess.Popen(["./bin/mg5_aMC",fileName],stdout=log,stderr=log)
         proc.wait()
      """
      Set couplings corresponding to polarization in param_card, and set up madspin_card if necessary
      """
      os.chdir(os.path.join(absMGdir,"DMann_"+ann))         
      mgf.set_couplings(annch=ann) #use default value for WIMP mass 
      mgf.set_beam_particles()
      if ann in ["WLWL","WTWT","ZLZL","ZTZT","tLtL","tRtR"]:
         mgf.set_madspin_card(annch=ann) 

         
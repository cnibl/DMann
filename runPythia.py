
"""
runPythia.py

Script that runs Pythia for a given LHEF created with setup/runMG scripts.

"""

import subprocess
import os
import sys
import re
import simSettings as sets
import multiprocessing as mp
import time
import math

#if len(sys.argv)!=2:
#   sys.exit("ERROR: correct usage is python runPythia.py LHEPATH where LHEPATH is a path to an LHEF.")

def get_abspath(path):
   """
   Returns absolute path of input path.
   """
   if path.startswith("~"):
      return os.path.expanduser(path)
   else:
      return os.path.abspath(path)
   
def run_pythia(lhef,outDir,nAnn,annCh,sun=False):
   """
   Runs pythia on the provided LHE file and places output in outDir
   Input: lhef - path to the LHE file with events
          outDir - directory to put results for this run in
          nAnn - number of events in file
          annCh - annihilation channel (string)
          sun - whether to set up Pythia for annihilations in the Sun (default is halo)
   """
   
   with open(lhef,"r") as f:
      for line in f:
         if "Number of Events" in line:
            entries=line.split()
            try:
               nAnn_file=int(entries[5])
            except:
               print "Warning: could not identify nAnn in LHEF, file may be faulty. Using nAnn provided."
               nAnn_file=nAnn
               break
   if nAnn_file!=nAnn:
      print "Warning: nAnn provided does not agree with that in LHEF, using nAnn from LHEF."
      nAnn=nAnn_file
   absCmndPath=get_abspath(write_cmnd_file(nAnn,annCh,sun))
   absOutDir=get_abspath(outDir)
   absLHEF=get_abspath(lhef)
   logname=os.path.dirname(absLHEF).split("/")[-1]
   with open(os.path.join(absOutDir,logname+".log"),"w") as log:
      if os.path.split(os.getcwd())[-1]!="Pythia":
         scrDir=os.path.dirname(get_abspath(sys.argv[0]))
         os.chdir(os.path.join(scrDir,"Pythia")) 
      print "Starting ",lhef
      start=time.time()
      p=subprocess.Popen(["./DMannPythia8LHE",absCmndPath,absLHEF,annCh,absOutDir],stdout=log,stderr=log)
      returnCode=p.wait()

      end=time.time()
      #print "Finished %s with returncode %d" % (lhef,returnCode)
   
   return (lhef,returnCode,end-start)
   
def write_cmnd_file(nAnn,annCh,sun):
   if not sun:
      cmndFileName="DMann_P8_halo_n"+str(nAnn)+"_"+annCh+".cmnd"
   else: 
      cmndFileName="DMann_P8_sun_n"+str(nAnn)+"_"+annCh+".cmnd"
   with open(cmndFileName,"w") as f:
      f.write("# This file contains commands to be read in for a Pythia8 run.\n")
      f.write("# Lines not beginning with a letter or digit are comments.\n")
      f.write("# Set up for Pythia8 runs of DM annihilation in the halo.\n")
      f.write("\n")
      f.write("# 1) General settings for run, output etc.\n")
      if annCh not in ["WLWL","WTWT","ZLZL","ZTZT","tRtR","tLtL"]:
         f.write("Main:numberOfEvents = "+str(nAnn)+"        ! number of events to generate SYNC TO SIMSETTINGS.PY!\n")
      else:
         f.write("Main:numberOfEvents = 100000        ! number of events to generate\n")
      f.write("Main:timesAllowErrors = 10          ! allow a few failures before quitting\n")
      f.write("Init:showChangedSettings = on       ! list changed settings\n")
      f.write("Init:showChangedParticleData = off  ! list changed particle data\n")
      f.write("Next:numberCount = 10000            ! print message every n events\n")
      f.write("\n")
      f.write("# 2) Incoming beam settings\n")
      f.write("LesHouches:idRenameBeams = 9000008\n")
      f.write("PartonLevel:ISR = off\n")
      f.write("PartonLevel:MPI = off\n")
      f.write("\n")
      f.write("# 3) Set stable particles to decay (note: different for Sun/halo)\n")
      if not sun:
         f.write("13:mayDecay   = true                ! mu+-\n")
         f.write("211:mayDecay  = true                ! pi+-\n")
         f.write("321:mayDecay  = true                ! K+-\n")
         f.write("130:mayDecay  = true                ! K0_L\n")
         f.write("2112:mayDecay = true                ! n\n")
      else:
         f.write("13:mayDecay   = false               ! mu+-\n")         
         f.write("xxx:mayDecay  = false               ! pi0\n")
         f.write("xxx:mayDecay  = false               ! K0_S\n")
         f.write("321:mayDecay  = false               ! K+-\n")
      f.write("\n")
      if annCh in ["taLtaL","taRtaR"]:
         f.write("# 4) Settings for tau decay, use SPINUP for external taus (not produced internally in Pythia)\n")
         f.write("!TauDecays:externalMode = 0\n")
   
   return cmndFileName
   
def mk_outdir(lhef):
   """
   Creates the output directory where Pythia output is placed by identifying the necessary parameters in the LHEF filename.
   Input: lhef - path to an LHEF file, should be constructed with the setupMG+runMG pipeline
   """
   absLHEF=get_abspath(lhef)
   res=re.search(r"DMann_(\w+)",absLHEF)
   annch=res.groups(1)[0]
   res=re.search(r"run_(.+)_m\d+",absLHEF)
   runName=res.groups(1)[0]
   if len(annch)==0:
      print "Warning: could not find annihilation channel in LHEF path."
      annch="XX"
   if len(runName)==0:
      print "Warning: could not find run_tag in LHEF path."
      runName=""
   runDir=os.path.split(os.path.dirname(lhef))[-1]
   outDir=os.path.join(os.path.expanduser("~"),"DMann","Pythia","DMann_P8_"+annch+"_"+runDir)

   #outDir=os.path.join(os.path.dirname(get_abspath(sys.argv[0])),"Pythia","DMann_P8_"+runName+"_"+annch)
   if not os.path.exists(outDir):
      subprocess.call(["mkdir",get_abspath(outDir)])
   return get_abspath(outDir) 
         
def get_nAnn(lhef):
   """
   Finds the number of events in an LHEF.
   Input: lhef - path to an LHEF file
   """
   absLHEF=get_abspath(lhef)
   with open(absLHEF,"r") as f:
      res=re.search(r"Number of Events\s*:\s*(\d+)",f.read())
   try:
      return int(res.groups(1)[0])
   except:
      sys.exit("ERROR: could not identify nAnn in LHEF provided.")
   
def get_annch(lhef):
   """
   Finds the name of the annihilation channel from an LHEF path.
   Input: lhef - path to an LHEF file, should be constructed with the setupMG+runMG pipeline
   """
   absLHEF=get_abspath(lhef)
   res=re.search(r"DMann_(\w+)",absLHEF)
   annch=res.groups(1)[0]
   if len(annch)==0:
      print "Warning: could not find annihilation channel in LHEF path."
      return "XX"
   else:
      return annch

def collect_result(res):
   """
   A callback function needed to collect results in apply_async call 
   """
   global results
   results.append(res)
   

# The threshold in GeV that the WIMP mass has to exceed for annihilations to be possible
annThresholds={"WLWL" : 80.4, "WTWT" : 80.4, "ZLZL" : 91.2, "ZTZT" : 91.2, "hh" : 125.2, 
               "taLtaL" : 1.8, "taRtaR" : 1.8, "muLmuL" : 0.11, "muRmuR" : 0.11, "ee" : 5.2e-6, 
               "tLtL" : 173., "tRtR" : 173., "bb" : 4.8, "cc" : 1.3, "ss" : 0.1, "uu" : 2.6e-3, "dd" : 5.1e-3}

if __name__=="__main__":
   """
   Set up and run Pythia8 for all the combinations in simSettings, parallellised.
   """
   
   
   LHEfiles=[]
   for mx in sets.WIMP_MASSES:
      for annCh in sets.ANN_CHANNELS:
         if annThresholds[annCh] < mx:
            if annCh not in ["WLWL","WTWT","ZLZL","ZTZT","tRtR","tLtL"]:
               lhePath=os.path.join(get_abspath(sets.MG_DIR),
                                 "DMann_"+annCh,"Events",
                                 "run_"+sets.RUN_TAG+"_m"+str(mx),
                                 "unweighted_events.lhe")
               LHEfiles.append(lhePath)
            else:
               if sets.N_ANN < 100000:
                  suffix=[]
               else:
                  suffix=[]
                  for i in range(sets.N_ANN/100000):
                     suffix.append("_"+str(i))
               for s in suffix:
                  lhePath=os.path.join(get_abspath(sets.MG_DIR),
                                 "DMann_"+annCh,"Events",
                                 "run_"+sets.RUN_TAG+"_m"+str(mx)+s+"_decayed_1",
                                 "unweighted_events.lhe")
                  LHEfiles.append(lhePath)
      
#   LHEfiles=[os.path.join(get_abspath(sets.MG_DIR),"DMann_tLtL","Events",
#                          "run_190218_m500_decayed_"+str(i),"unweighted_events.lhe") for i in range(1,3)]
#   for hel in ("L","R"):
#      LHEfiles.append(os.path.join(get_abspath(sets.MG_DIR),"DMann_mu"+hel+"mu"+hel,"Events",
#                          "run_190218_m200","unweighted_events.lhe"))
#      LHEfiles.append(os.path.join(get_abspath(sets.MG_DIR),"DMann_ta"+hel+"ta"+hel,"Events",
#                          "run_190220_m1000","unweighted_events.lhe"))

   results=[]
   pool=mp.Pool(processes=mp.cpu_count()) #processes defaults to #cpus
   print "Starting Pythia8 runs ..."
   allstart=time.time()
   for lhef in LHEfiles:

      absLHEpath=get_abspath(lhef)
      if os.path.exists(absLHEpath+".gz")==False and os.path.exists(absLHEpath)==False:
         print "Warning: LHEF (or .gz) does not exist. Skipping."
         continue
      if not os.path.exists(absLHEpath):
         subprocess.call(["gunzip","-k",absLHEpath+".gz"])

      outDir=mk_outdir(absLHEpath)
      nAnn=get_nAnn(absLHEpath)
      annch=get_annch(absLHEpath)  

      pool.apply_async(run_pythia,args=(absLHEpath,outDir,nAnn,annch),callback=collect_result) # run run_pythia for #cpu processes in parallel until LHEF list exhausted
   pool.close()
   pool.join()
   allend=time.time()
   print "Done! Total time: %i h, %i min, %i s" % (int(math.floor(math.floor((allend-allstart)/60)/60)),
                                                             int(math.floor((allend-allstart)/60)%60),
                                                             int((allend-allstart)%60))
   print "Have run Pythia8 on following files:"
   print "LHEF path\t\tReturn code\t\tTime spent [s]"
   for lhef,ret,delta in results:
      print "MG_DIR/"+os.path.relpath(lhef,start=get_abspath(sets.MG_DIR))
                  +"\t\t"+ret+"\t\t"+delta
   
   


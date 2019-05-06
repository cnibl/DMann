
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
import MGfunctions as mgf

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
   
def run_pythia(lhef,outDir,nAnn,annCh,suffix=None,sun=False):
   """
   Runs pythia on the provided LHE file and places output in outDir
   Input: lhef - path to the LHE file with events
          outDir - directory to put results for this run in
          nAnn - number of events in file
          annCh - annihilation channel (string)
          suffix - a suffix that gives the number of the run when separating runs in 100k at a time
          sun - whether to set up Pythia for annihilations in the Sun (default is halo)
   """

   absCmndPath=get_abspath(write_cmnd_file(nAnn,annCh,sun))
   absOutDir=get_abspath(outDir)
   absLHEF=get_abspath(lhef)
   res=re.search(r"m(\d+\.?\d*)",lhef)
   mX=res.groups()[0]
   logname=os.path.dirname(absLHEF).split("/")[-1]
   with open(os.path.join(absOutDir,logname+".log"),"w") as log:
      if os.path.split(os.getcwd())[-1]!="Pythia":
         scrDir=os.path.dirname(get_abspath(sys.argv[0]))
         os.chdir(os.path.join(scrDir,"Pythia"))       
      if len(suffix)>0:
         print "Starting %s, m_WIMP = %-s, run %s ... " % (annCh,mX,str(int(suffix[1:])+1))
      else:
         print "Starting %s, m_WIMP = %-s ... " % (annCh,mX)
      start=time.time()
      p=subprocess.Popen(["./DMannPythia8LHE",absCmndPath,absLHEF,annCh,absOutDir],stdout=log,stderr=log)
      returnCode=p.wait()
   end=time.time()
   global totalRuns
   with nCur.get_lock():
      nCur.value+=1
   print "Finished run %i of %i" % (nCur.value,totalRuns)
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
      if nAnn < 100000:
         f.write("Main:numberOfEvents = "+str(nAnn)+"        ! number of events to generate\n")
         f.write("Main:timesAllowErrors = "+str(nAnn/10)+"       ! allow a few failures before quitting\n")
      else:   
         f.write("Main:numberOfEvents = 100000        ! number of events to generate\n")
         f.write("Main:timesAllowErrors = 10000       ! allow a few failures before quitting\n")
      f.write("Init:showChangedSettings = on       ! list changed settings\n")
      f.write("Init:showChangedParticleData = on  ! list changed particle data\n")
      f.write("Next:numberCount = 10000            ! print message every n events\n")
      """
      # Tolerated energy/mom mismatch before errors/warnings occur:
      errTol=0.01
      warnTol=0.1
      f.write("Check:epTolErr = "+str(errTol)+"\n")
      f.write("Check:epTolWarn = "+str(warnTol)+"\n")
      f.write("Check:mTolErr = "+str(errTol)+"\n")
      f.write("Check:mTolWarn = "+str(warnTol)+"\n")            
      f.write("LesHouches:matchInOut = off") #off because MG messes things up with energy-mom in MadSpin decays
      """
      f.write("Next:numberShowEvent = 1000\n")
#      f.write("Next:showScaleAndVertex = on\n")
      f.write("\n")
      f.write("# 2) Incoming beam settings\n")
      if annCh not in ("taLtaR","taRtaL","tRtL","tLtR","muRmuL","muLmuR"):
         f.write("LesHouches:idRenameBeams = 9000008\n")
      else:
         f.write("LesHouches:idRenameBeams = 9000010\n")
      f.write("PartonLevel:ISR = off\n")
      f.write("PartonLevel:MPI = off\n")
      f.write("SpaceShower:QEDShowerByL = off\n")
      f.write("PDF:lepton = off\n\n")
      
      f.write("\n")
      f.write("# 3) Set stable particles to decay (note: different for Sun/halo)\n")
      
      if not sun:
         f.write("13:mayDecay   = true                ! mu+-\n")
         f.write("211:mayDecay  = true                ! pi+-\n")
         f.write("321:mayDecay  = true                ! K+-\n")
         f.write("130:mayDecay  = true                ! K0_L\n")
         f.write("2112:mayDecay = true                ! n\n")
      else:
         f.write("13:mayDecay   = false                ! mu+-\n")
         f.write("211:mayDecay  = false                ! pi+-\n")
         f.write("321:mayDecay  = false                ! K+-\n")
         f.write("130:mayDecay  = false                ! K0_L\n")
         f.write("2112:mayDecay = false                ! n\n")
      
      if annCh in ["taLtaL","taRtaR","taLtaR","taRtaL"]:
         f.write("# 4) Settings for tau decay, use SPINUP for external taus (not produced internally in Pythia)\n")
         f.write("TauDecays:externalMode = 0\n\n") #suggested as best by Philip Ilten
         #f.write("TauDecays:mode=3\n")
         #f.write("TauDecays:tauPolarization=1\n")     
         #f.write("15:0:meMode = 1531\n") # sometimes needed for sophisticated tau decays 
         
      if sets.PYT_EWRAD:
        f.write("# 5) Settings for EW radiation\n")
        f.write("TimeShower:weakShower = on\n")
        if annCh in ("tLtR","tRtL","tLtL","tRtR","muLmuR","muRmuL","muLmuL","muRmuR"):
          f.write("TimeShower:weakShowerMode = 2 #only include Z branchings for this ann. ch.\n")      
            
         
   return cmndFileName
   
def mk_outdir(lhef,suffix=None):
   """
   Creates the output directory where Pythia output is placed by identifying the necessary parameters in the LHEF filename.
   Input: lhef - path to an LHEF file, should be constructed with the setupMG+runMG pipeline
          suffix - the suffix for this run of 100k events (if less than 100k events, should be "" (length zero))
   """
   absLHEF=get_abspath(lhef)
   res=re.search(r"DMann_([^_]*)_(\w{2,6})_m(\d+)",absLHEF) 
   runName=res.groups()[0]
   annch=res.groups()[1]
   mWIMP=res.groups()[2]
   if len(annch)==0:
      print "Warning: could not find annihilation channel in LHEF path."
      annch="XX"
   if len(runName)==0:
      print "Warning: could not find run_tag in LHEF path."
      runName=""
   runDir=os.path.split(os.path.dirname(lhef))[-1]
   if len(suffix)==0:
      pytDir="Pythia"
   else:
      pytDir="Pythia_"+str(int(suffix[1:])+1)
   outDir=os.path.join(get_abspath(sets.DMANN_OUTDIR),pytDir,annch+"_m"+str(mWIMP))
   if not os.path.exists(outDir):
      subprocess.call(["mkdir","-p",get_abspath(outDir)])
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
   #res=re.search(r"_(\w{2,6})_m\d+",absLHEF) # proper one
   res=re.search(r"DMann_[^_]*_(\w{2,6})_m\d+",absLHEF) # proper one
   annch=res.groups()[0]
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

def unzip(lhef):
   """
   unzips gzipped file, keeps gz file
   """
   print "Unzipping %s.gz ..." % lhef
   subprocess.call(["gunzip","-k",get_abspath(lhef)+".gz"]) 
   return

def setup_LHEF(suffixes,wimpMasses,annChannels,):
   """
   Sets up a list of all the LHEF to process, along with the corresponding folder suffix for each file.
   Input: suffixes - a list of suffixes in the form "_i" where i is an integer signifying which 100k events that are simulated, suffixes is just [""] for less than 100k events
          wimpMasses - a list of WIMP masses to consider
          annChannels - a list of annihilation channels to consider
   """
   LHEfiles=[]
   LHEsuffixes={}
   for s in suffixes:
      for mx in wimpMasses:
         for annCh in annChannels:
            if mgf.annThresholds[annCh] < mx:
               madSpinChannels=("WLWL","WTWT","ZLZL","ZTZT","tRtL","tLtR","tLtL","tRtR")
               if sets.MADSPIN==False or annCh not in madSpinChannels: #all except MadSpin runs
                  lhePath=os.path.join(get_abspath(sets.MG_DIR),
                                 "DMann_"+sets.RUN_TAG+"_"+annCh+"_m"+str(mx),"Events",
                                 "run_"+sets.RUN_TAG+s,
                                 "unweighted_events.lhe.gz")
                  LHEfiles.append(lhePath)
                  LHEsuffixes[lhePath]=s
               elif sets.MADSPIN==True and annCh in madSpinChannels: #MadSpin runs              
                  lhePath=os.path.join(get_abspath(sets.MG_DIR),
                                 "DMann_"+sets.RUN_TAG+"_"+annCh+"_m"+str(mx),"Events",
                                 "run_"+sets.RUN_TAG+s+"_decayed_1",
                                 "unweighted_events.lhe.gz")
                  LHEfiles.append(lhePath)
                  LHEsuffixes[lhePath]=s
               else:
                  print annCh,sets.MADSPIN
   return LHEfiles,LHEsuffixes
   

if __name__=="__main__":
   """
   Set up and run Pythia8 for all the combinations in simSettings, parallellised.
   """
   

   """
   If >100k events, run 100k events at a time and put in folders Pythia+suffix (Pythia_1, Pythia_2 etc.), suffixes is a list with elements "_i" where i runs from 0 to nAnn/100000 
   """
   if sets.N_ANN < 100000:
      suffix=["_0"]
   else:
      suffix=[]
      for i in range(sets.N_ANN/100000):
         suffix.append("_"+str(i))
   """
   Begin by setting up a list of all the LHE files to shower
   """
   (LHEfiles,LHEsuffixes)=setup_LHEF(suffix,wimpMasses=sets.WIMP_MASSES,annChannels=sets.ANN_CHANNELS)
   
   """
   Run DMannPythia8LHE on all LHEF in parallell               
   """
   
   results=[]
   nCur=mp.Value('i',0) #integer shared between processes to count current run, initialised at 0
   totalRuns=len(LHEfiles)   
   pool=mp.Pool(processes=mp.cpu_count()) #processes defaults to #cpus
   print "Starting Pythia8 runs ..."
   allstart=time.time()
   for lhef in LHEfiles:
      absLHEpath=get_abspath(lhef)
      if os.path.exists(absLHEpath+".gz")==False and os.path.exists(absLHEpath)==False:
         print "Warning: LHEF does not exist. Skipping. File name:"
         print absLHEpath
         continue
      suffix=LHEsuffixes[lhef]
      outDir=mk_outdir(absLHEpath,suffix)
      if sets.N_ANN < 100000:
         nAnn=sets.N_ANN
      else:
         nAnn=100000
      annCh=get_annch(absLHEpath)  
      pool.apply_async(run_pythia,args=(absLHEpath,outDir,nAnn,annCh,suffix),callback=collect_result) # run run_pythia for #cpu processes in parallel until LHEF list exhausted
   pool.close()
   pool.join()

   end=time.time()
   print "========================================================================================================================="
   print "Done! Took %i h, %i min, %i s" % (int(math.floor(math.floor((end-allstart)/60)/60)),
                                                             int(math.floor((end-allstart)/60)%60),
                                                             int((end-allstart)%60))      
   print "Have run Pythia8 on following files:"
   print "LHEF path\t\tReturn code\t\tTime spent [s]"
   for res in results:
      print "%s\t\t%i\t%15.1f" % ("MG_DIR/"+os.path.relpath(res[0],start=get_abspath(sets.MG_DIR)),res[1],res[2])
   
   """
   gzip all the event files created to save space   
   """
   if sets.GZIP_EVTFILE==True:
      print "Now gzipping event files ... "
      zipstart=time.time()
      if sets.N_ANN >= 100000:
         suffixes=["_"+str(i) for i in range(1,sets.N_ANN/100000+1)]
      else:
         suffixes=["_1"]
      for s in suffixes:
         for annCh in sets.ANN_CHANNELS:
            for mX in sets.WIMP_MASSES:
               if mgf.annThresholds[annCh] < mX:
                  if len(s)>0:
                     eventFile=os.path.join(sets.DMANN_OUTDIR,"Pythia"+s,
                            annCh+"_m"+str(mX),"da-pyt8-mx"+str(mX)+"-"+annCh+"-events.dat")
                  else:
                     eventFile=os.path.join(sets.DMANN_OUTDIR,"Pythia",
                            annCh+"_m"+str(mX),"da-pyt8-mx"+str(mX)+"-"+annCh+"-events.dat")
                  subprocess.call(["gzip","-f",get_abspath(eventFile)]) #overwrites any existing file
      zipend=time.time()
      print "Done gzipping. Took %i h, %i min, %i s" % (int(math.floor(math.floor((zipend-zipstart)/60)/60)),
                                                             int(math.floor((zipend-zipstart)/60)%60),
                                                             int((zipend-zipstart)%60))      

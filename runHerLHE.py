
"""
runHerLHE.py

Script that runs Herwig7 on a set of LHEF created with setup/runMG scripts.

"""
import multiprocessing as mp
import time
import math
import os
import subprocess

import simSettings as sets
import MGfunctions as mgf
import LHEfunctions as lhf

def collect_result(res):
   """
   A callback function needed to collect results in apply_async call 
   """
   global results
   results.append(res)

if __name__=="__main__":
   """
   Set up and run Herwig7 for all the combinations in simSettings, parallellised.
   """
   
   """
   If >100k events, run 100k events at a time and put in folders Herwig+suffix (Herwig_1, Herwig_2 etc.), suffixes is a list with elements "_i" where i runs from 0 to nAnn/100000 
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
   (LHEfiles,LHEsuffixes)=lhf.setup_LHEF(suffix,wimpMasses=sets.WIMP_MASSES,annChannels=sets.ANN_CHANNELS)
   
   """
   Run Herwig7 on all LHEF in parallell               
   """
   results=[]
   runResults=[]
   nCur=mp.Value('i',0) #integer shared between processes to count current run, initialised at 0
   totalRuns=len(LHEfiles)   
   pool=mp.Pool(processes=mp.cpu_count()) #processes defaults to #cpus
   print "Starting Herwig7 runs ..."
   allstart=time.time()
   for lhef in LHEfiles:
      absLHEpath=lhf.get_abspath(lhef)
      if os.path.exists(absLHEpath+".gz")==False and os.path.exists(absLHEpath)==False:
         print "Warning: LHEF does not exist. Skipping. File name:"
         print absLHEpath
         continue
      
      #seed=random.randint(1,100000)
      seed=int(LHEsuffixes[lhef][1:])
      annCh=lhf.get_annch(absLHEpath)
      mWIMP=lhf.get_mWIMP(absLHEpath)
      suffix=LHEsuffixes[lhef]
      outDir=lhf.mk_outdir(absLHEpath,"Herwig",suffix)
      
      if sets.N_ANN < 100000:
      	nAnn=sets.N_ANN
      else:
      	nAnn=100000
      infilePath=lhf.get_abspath(lhf.write_infileLHE(nAnn,absLHEpath,outDir,mWIMP,annCh,seed,sets.SUN))
      result=pool.apply_async(lhf.run_herwigLHE,args=(infilePath,outDir,suffix),callback=collect_result) # run run_herwig for #cpu processes in parallel until LHEF list exhausted
      runResults.append((result,annCh,mWIMP))
      
   pool.close()
   pool.join()
   
   end=time.time()
   print "========================================================================================================================="
   print "Done! Took %i h, %i min, %i s" % (int(math.floor(math.floor((end-allstart)/60)/60)),
                                                             int(math.floor((end-allstart)/60)%60),
                                                             int((end-allstart)%60))      
   print "Have run Herwig7 on following files:"
   print "LHEF path\t\tReturn code\t\tTime spent [s]"
   for res in results:
      print "%s\t\t%i\t%15.1f" % ("MG_DIR/"+os.path.relpath(res[0],start=lhf.get_abspath(sets.MG_DIR)),res[1],res[2])
   
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
                     eventFile=os.path.join(sets.DMANN_OUTDIR,"Herwig"+s,
                            annCh+"_m"+str(mX),"da-her7-mx"+str(int(mX))+"-"+annCh+"-events.dat")
                  else:
                     eventFile=os.path.join(sets.DMANN_OUTDIR,"Herwig",
                            annCh+"_m"+str(mX),"da-her7-mx"+str(int(mX))+"-"+annCh+"-events.dat")
                  subprocess.call(["gzip","-f",lhf.get_abspath(eventFile)]) #overwrites any existing file
      zipend=time.time()
      print "Done gzipping. Took %i h, %i min, %i s" % (int(math.floor(math.floor((zipend-zipstart)/60)/60)),
                                                             int(math.floor((zipend-zipstart)/60)%60),
                                                             int((zipend-zipstart)%60))      
   
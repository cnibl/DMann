"""
A library that contains functions used in the runHerLHE and runPythia scripts.
"""
import os
import sys
import re
import subprocess
import time
import MGfunctions as mgf
import simSettings as sets


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
   res=re.search(r"_m(\d+\.?\d*)",lhef)
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

def run_herwigLHE(infile,outDir,suffix=""):
   """
   Runs Herwig on the provided LHE file and places output in outDir
   Input: lhef - path to the LHE file with events
          outDir - directory to put results for this run in
          nAnn - number of events in file
          annCh - annihilation channel (string)
          suffix - a suffix that gives the number of the run when separating runs in 100k at a time
          sun - whether to set up Herwig for annihilations in the Sun (default is halo)
   """
   start=time.time()
   if os.path.split(os.getcwd())[1]!="Herwig":
      os.chdir(os.path.join(os.getcwd(),"Herwig"))
   logFile=os.path.dirname(infile).split("/")[-1]
   absOutDir=get_abspath(outDir)
   #get_abspath(os.path.join(sets.DMANN_OUTDIR,"Herwig"+suffix,
   #         os.path.split(infile)[1][:-3]+".log"))	
   with open(os.path.join(absOutDir,logFile+".log"),"w") as log:
      print "\tStarting %s" % (os.path.split(infile)[1])
      p=subprocess.Popen(["Herwig","read",infile],stdout=log,stderr=log)
      returnCode=p.wait()
   end=time.time()

   return (infile,returnCode,end-start)

   
def get_abspath(path):
   """
   Returns absolute path of input path.
   """
   if path.startswith("~"):
      return os.path.expanduser(path)
   else:
      return os.path.abspath(path)
      
def mk_outdir(lhef,code,suffix=None):
   """
   Creates the output directory where Pythia output is placed by identifying the necessary parameters in the LHEF filename.
   Input: lhef - path to an LHEF file, should be constructed with the setupMG+runMG pipeline
          code - string giving code used, either "Pythia" or "Herwig
          suffix - the suffix for this run of 100k events (if less than 100k events, should be "" (length zero))
   """
   if code not in ("Pythia","Herwig"):
      sys.exit("ERROR: mk_outdir in LHEfunctions called with code %d" % str(code))
   absLHEF=get_abspath(lhef)
   res=re.search(r"DMann_([^_]*)_(\w{2,6})_m(\d+\.?\d+)/Events",absLHEF) 
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
      codeDir=code
   else:
      codeDir=code+"_"+str(int(suffix[1:])+1)
   outDir=os.path.join(get_abspath(sets.DMANN_OUTDIR),codeDir,annch+"_mx"+str(mWIMP))
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

def get_mWIMP(lhef):
   """
   Finds the WIMP mass from an LHEF filename
   Input: lhef - path to an LHEF file
   """
   absLHEF=get_abspath(lhef)
   res=re.search(r"DMann_.*_m(\d+\.?\d+)/Events",absLHEF) 
   mWIMP=res.groups()[0]
   try:
      if "." in mWIMP:
         return float(mWIMP)
      else:
         return int(mWIMP)
   except:
      sys.exit("ERROR: could not identify mWIMP in LHEF path provided.")
         
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
         

def write_infileLHE(nAnn,LHEpath,resDir,mwimp,annCh,seed,sun=False):
   """
   Writes the infile for input arguments
   Input: resDir - the directory to put results for this run in
          nAnn - number of annihilations
          annCh - the annihilation channel
          sun - whether to set up for the sun or not (default is halo)
   Returns: path to infile
   """
   
   if sun==False:
      fileName=os.path.join(resDir,"da-her7-mx"+str(mwimp)+"-"+annCh+"-halo.in")
   else:
      fileName=os.path.join(resDir,"da-her7-mx"+str(mwimp)+"-"+annCh+"-sun.in")
   
   with open(fileName,"w") as f:
      f.write("# "+fileName+"\n# -*- ThePEG-repository -*-\n")
      f.write("# DMann input file for Herwig runs\n\n")
      f.write("# Read in FR model file, include charge conservation etc.\n")
      f.write("read FRModel.model\n")
      f.write("read Matchbox/NonDiagonalCKM.in\n")
      f.write("read Matchbox/StandardModelLike.in\n\n")
      
      #Create the LHEF reader and set LHEF path
      f.write("#Create the LHEF reader and set LHEF path\n")
      f.write("library LesHouches.so\n")
      f.write("library MadGraphReader.so\n")
      f.write("cd /Herwig/EventHandlers\n")
      f.write("create ThePEG::MadGraphReader LHReader\n")
      #f.write("create ThePEG::LesHouchesFileReader LHReader\n")
      f.write("set LHReader:FileName "+LHEpath+"\n")
      f.write("set LHReader:CacheFileName cache.tmp\n")
      
      f.write("# Beam settings, x x collisions at E=2*mX, unpolarised\n")
      f.write("set LHReader:InitPDFs 0\n")
      if annCh not in ("taLtaR","taRtaL","tRtL","tLtR","muRmuL","muLmuR"): #scalar states
         f.write("set LHReader:BeamA /Herwig/FRModel/Particles/Xr\n")
         f.write("set LHReader:BeamB /Herwig/FRModel/Particles/Xr\n")
         f.write("set LHReader:PDFA /Herwig/Partons/NoPDF\n") # Turn off ISR for e+ e- collision
         f.write("set LHReader:PDFB /Herwig/Partons/NoPDF\n")
      else: #vector states
         f.write("set LHReader:BeamA /Herwig/FRModel/Particles/Xd\n")
         f.write("set LHReader:BeamA /Herwig/FRModel/Particles/Xd~\n")
         f.write("set LHReader:PDFA /Herwig/Partons/NoPDF\n") # Turn off ISR for e+ e- collision
         f.write("set LHReader:PDFB /Herwig/Partons/NoPDF\n")
      f.write("set LHReader:EBeamA "+str(mwimp)+"*GeV\n")
      f.write("set LHReader:EBeamB "+str(mwimp)+"*GeV\n")      
      #f.write("read snippets/EECollider.in\n")
      f.write("create ThePEG::Cuts NoCuts\n")
      f.write("set LHReader:Cuts NoCuts\n")
      f.write("set LHReader:Decayer /Herwig/Decays/Mambo\n")
      
      f.write("cd /Herwig/EventHandlers\n")
      f.write("create ThePEG::LesHouchesEventHandler LHHandler\n")
      #f.write("set LHHandler:LuminosityFunction:Energy "+str(2*mwimp)+"*GeV\n")
      #f.write("set LHHandler:Cuts:MHatMin 0.0*GeV\n")
      f.write("set LHHandler:HadronizationHandler /Herwig/Hadronization/ClusterHadHandler\n")
      f.write("set LHHandler:DecayHandler /Herwig/Decays/DecayHandler\n")
      f.write("set LHHandler:CascadeHandler /Herwig/Shower/ShowerHandler # default\n")
      f.write("set LHHandler:PartonExtractor /Herwig/Partons/EEExtractor\n")
      f.write("set LHHandler:CascadeHandler:MPIHandler NULL\n")
      f.write("insert LHHandler:PreCascadeHandlers 0 /Herwig/Decays/DecayHandler\n")
      
      #Set event handler to read events from LHEF
      f.write("#Set event handler to read events from LHEF\n")
      f.write("insert LHHandler:LesHouchesReaders[0] LHReader\n")
      
      #f.write("set /Herwig/Particles/e-:LongitudinalPolarization -1\n") # set beam polarization
      #f.write("set /Herwig/Particles/e+:LongitudinalPolarization -1\n")
      
      f.write("## Special settings required for on-shell production of top, W, Z and H\n")
      f.write("read Matchbox/OnShellTopProduction.in\n")
      f.write("read Matchbox/OnShellWProduction.in\n")
      f.write("read Matchbox/OnShellZProduction.in\n")
      f.write("read Matchbox/OnShellHProduction.in\n\n")
      
      if sets.HER_EVTGEN==False:
      	f.write("## Reinitialise decays to turn off EvtGen usage\n")
      	f.write("cd /Herwig/Particles\n")
      	f.write("# switch off current modes\n")
      	f.write("do B0:SelectDecayModes none\n")
      	f.write("do Bbar0:SelectDecayModes none\n")
      	f.write("do B+:SelectDecayModes none\n")
      	f.write("do B-:SelectDecayModes none\n")
      	f.write("do B_s0:SelectDecayModes none\n")
      	f.write("do B_sbar0:SelectDecayModes none\n")
      	f.write("do D0:SelectDecayModes none\n")
      	f.write("do Dbar0:SelectDecayModes none\n")
      	f.write("do D+:SelectDecayModes none\n")
      	f.write("do D-:SelectDecayModes none\n")
      	f.write("do D_s+:SelectDecayModes none\n")
      	f.write("do D_s-:SelectDecayModes none\n")
      	f.write("## Read in Herwig default B decays instead of EvtGen\n")
      	f.write("read defaults/HerwigBDecays.in\n")
      
      f.write("# Scale choice\n")
      f.write("cd /Herwig/MatrixElements/Matchbox\n")
      f.write("set Factory:ScaleChoice /Herwig/MatrixElements/Matchbox/Scales/SHatScale\n")
      f.write("# Do not apply profile scales for LEP as hard\n")
      f.write("# scale coincides with kinematic limit\n")
      f.write("set /Herwig/Shower/ShowerHandler:HardScaleProfile NULL\n")
      f.write("set /Herwig/DipoleShower/DipoleShowerHandler:HardScaleProfile NULL\n\n")
      
      
      if sets.HER_QRH==True:
      	f.write("# QED radiation in particle decays (Q: don't use both QEDRadiationHandler and ShowerHandler:Interactions QCDandQED at the same time?)\n")
      	f.write("cd /Herwig/EventHandlers\n")
      	f.write("insert EventHandler:PostSubProcessHandlers 0 /Herwig/QEDRadiation/QEDRadiationHandler\n")
      	for i in (1,2,3,4,5,6,11,13,15,23,-24,24):
      		f.write("insert /Herwig/QEDRadiation/QEDRadiationHandler:DecayProducts[0] "+str(i)+"\n")
      		f.write("insert /Herwig/QEDRadiation/QEDRadiationHandler:DecayProducts[0] "+str(-i)+"\n")   
      	if annCh not in ("taLtaR","taRtaL","tRtL","tLtR","muLmuR","muRmuL"):
      		f.write("insert /Herwig/QEDRadiation/QEDRadiationHandler:DecayingParticles[0] 9000006\n")
      	else:
      		f.write("insert /Herwig/QEDRadiation/QEDRadiationHandler:DecayingParticles[0] 9000007\n")
      	#f.write("set /Herwig/Shower/ShowerHandler:Interactions QCD\n") 
      else:
      	f.write("set /Herwig/Shower/ShowerHandler:Interactions QCDandQED\n")
      
      f.write("# Make usually stable particles decay\n")
      if sun==False:
      	f.write("set /Herwig/Particles/pi+:Stable Unstable\n")
      	f.write("set /Herwig/Particles/K+:Stable Unstable\n")
      	f.write("set /Herwig/Particles/K_L0:Stable Unstable\n")
      	f.write("set /Herwig/Particles/mu+:Stable Unstable\n")
      	f.write("set /Herwig/Particles/n0:Stable Unstable\n\n")
      f.write("# Analysis of multiplicity\n")
      f.write("cd /Herwig/Analysis\n")
      f.write("create DMann::DMannYields DMannYields DMannYields.so\n")
      f.write("insert /Herwig/Generators/EventGenerator:AnalysisHandlers 0 DMannYields\n")
      f.write("set DMannYields:MassDM "+str(mwimp)+"\n")
      f.write("set DMannYields:NEvent "+str(nAnn)+"\n")
      f.write("set DMannYields:AnnState "+annCh+"\n")
      if len(resDir)>0:
      	f.write("set DMannYields:OutDir "+resDir+"\n")
      f.write("insert DMannYields:ParticleCodes[0] -12\n")
      f.write("insert DMannYields:ParticleCodes[0] 12\n")
      f.write("insert DMannYields:ParticleCodes[0] -14\n")
      f.write("insert DMannYields:ParticleCodes[0] 14\n")
      f.write("insert DMannYields:ParticleCodes[0] -16\n")
      f.write("insert DMannYields:ParticleCodes[0] 16\n")
      f.write("insert DMannYields:ParticleCodes[0] -11\n")
      f.write("insert DMannYields:ParticleCodes[0] 11\n")
      f.write("insert DMannYields:ParticleCodes[0] -2212\n")
      f.write("insert DMannYields:ParticleCodes[0] 22\n\n")
      #Save and run
      f.write("# Save and run the generator\n")
      f.write("do /Herwig/MatrixElements/Matchbox/Factory:ProductionMode\n")
      f.write("cd /Herwig/Generators\n")
      f.write("cp EventGenerator LHGenerator\n")
      f.write("set LHGenerator:EventHandler /Herwig/EventHandlers/LHHandler\n")
      f.write("set LHGenerator:NumberOfEvents "+str(nAnn)+"\n")
      f.write("set LHGenerator:RandomNumberGenerator:Seed "+str(seed)+"\n")
      f.write("set LHGenerator:Path "+resDir+"\n")
      #f.write("set EventGenerator:DebugLevel 5\n")
      f.write("set EventGenerator:PrintEvent 100\n")
      f.write("run "+os.path.split(fileName)[1][:-3]+" LHGenerator")
      
   return fileName
      
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
      
      f.write("ParticleDecays:allowPhotonRadiation = on\n")
      
      #f.write("\n")          
      #f.write("StringZ:deriveBLund = on\n")
      #f.write("StringZ:aLund       = 0.5999 #0.80 #0.40\n")
      #f.write("StringZ:avgZLund    = 0.5278 #0.50 #0.55\n")
      #f.write("StringPT:Sigma      = 0.3174 #0.28 #0.36\n")
      
   return cmndFileName
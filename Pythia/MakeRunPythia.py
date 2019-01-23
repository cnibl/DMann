"""
MakeRunPythia.py
Constructs .cmnd-files intended to be read by PYTHIA8 for the generation of
production fluxes of secondary particles from DM annihilation. First defines
function that creates one runfile, then loops over parameter values to
create all runfiles 

mX = eCM/2: 
Mass of DM particle
goes from 10-25000 GeV

annPdg: 
Annihilation channel PDG code (of particle in particle/antiparticle pair)
=5 - b bbar
=24 - W+W- (W+ is particle, W- antiparticle)
=15 - tau-tau+ 
=6 - t tbar

yieldPdg:
Yield particle PDG code 
=22 - gamma
=-11 - e+
=-2212 - pbar
=14 - numu/numubar (abs. value)

nEvt:
Number of simulated events
"""

def makerunfile(mX,annPdg,yieldPdg,nEvt,test=False):
   if not test:
      filename = "da-pyt8-m"+str(int(mX))+"-ch"+str(annPdg)+".cmnd"
   else:
      filename = "TEST-da-pyt8-m"+str(int(mX))+"-ch"+str(annPdg)+"-int"+str(yieldPdg)+".cmnd"
   
   runfile = open("Runs-todo/"+filename,'w') 
   """ 
   Write all PYTHIA commands and parameters for a run into the runfile
   """
   runfile.write("! "+filename+".\n")
   runfile.write("! This file contains commands to be read in for a Pythia8 run.\n")
   runfile.write("! Lines not beginning with a letter or digit are comments.\n")
   runfile.write("\n")
   runfile.write("! 1) Settings used in the main program.\n")
   runfile.write("Main:numberOfEvents = "+str(nEvt)+"         ! number of events to generate\n")
   runfile.write("Main:timesAllowErrors = 5          ! allow a few failures before quitting\n")
   runfile.write("\n")
   runfile.write("! 2) Settings related to output in init(), next() and stat().\n")
   runfile.write("Init:showChangedSettings = on      ! list changed settings\n")
   runfile.write("Init:showChangedParticleData = on  ! list changed particle data\n")
   runfile.write("Next:numberCount = 1000            ! print message every n events\n")
   runfile.write("Next:numberShowInfo = 1            ! print event information n times\n")
   runfile.write("Next:numberShowProcess = 1         ! print process record n times\n")
   runfile.write("Next:numberShowEvent = 1           ! print event record n times\n")
   runfile.write("\n")
   runfile.write("! 3) Beam parameter settings. Incoming beams do not radiate.\n")
   runfile.write("Beams:idA = -11                    ! ficititious incoming e+\n")
   runfile.write("Beams:idB = 11                     ! ficititious incoming e-\n")
   runfile.write("PDF:lepton = off                   ! no radiation off ficititious e+e-\n")
   runfile.write("Beams:eCM = "+str(2*mX)+"                   ! CM energy of collision, 2 times WIMP mass\n")
   runfile.write("\n")
   runfile.write("! 4) Set up properties of the GeneralResonance and its decay channels.\n")
   runfile.write("! id:all = name antiName spinType chargeType colType m0 mWidth mMin mMax tau0\n")
   runfile.write("999999:all = GeneralResonance void 1 0 0 "+str(2*mX)+" 1. 0. 0. 0.\n")
   runfile.write("! id:addChannel = onMode bRatio meMode product1 product2 ...\n")
   runfile.write("! id:oneChannel = onMode bRatio meMode product1 product2 ...\n ")
   runfile.write("! Note: oneChannel sets all other BR:s to zero except the specified one")  
   runfile.write("! Note: sum of branching ratios automatically rescaled to 1.\n")
   runfile.write("999999:oneChannel = 1 1. 101 "+str(annPdg)+" "+str(-annPdg)+"   !  -> annPdg -annPdg\n") 
   #  if annPdg == 5: # oneChannel sets all other BR:s to zero 
   #    runfile.write("999999:oneChannel = 1 1. 101 5 -5   !  -> b bbar\n") 
   #  elif annPdg == 24:
   #    runfile.write("999999:oneChannel = 1 1. 101 24 -24 !  -> W+ W-\n")
   #  elif annPdg == 15:                          
   #    runfile.write("999999:oneChannel = 1 1. 101 15 -15 !  -> tau- tau+\n")
   #  elif annPdg == 6:                          
   #    runfile.write("999999:oneChannel = 1 1. 101 6 -6   !  -> t tbar\n")
   runfile.write("\n")
   runfile.write("! 5) Tell that also long-lived should decay.\n")
   runfile.write("13:mayDecay   = true                 ! mu+-\n")
   runfile.write("211:mayDecay  = true                 ! pi+-\n")
   runfile.write("321:mayDecay  = true                 ! K+-\n")
   runfile.write("130:mayDecay  = true                 ! K0_L\n")
   runfile.write("2112:mayDecay = true                 ! n\n")
    
   #CN: TEMPORARY STUFF, REMOVE LATER
   #  runfile.write("24:mayDecay = false                 ! n\n") # prevent W decays
    
   #Sophisticated tau decays including spin correlations:
   runfile.write("TauDecays:mode = 2                    ! set tau polarization manually \n")
   runfile.write("TauDecays:tauMother = 999999          ! set tau polarization manually \n")   
   runfile.write("TauDecays:tauPolarization = -1        ! LH tau polarisation \n")
   runfile.write("15:oneChannel = 1 1. 101 16 11 -12    !  only tau > e vt ve decays\n") 
   runfile.write("-15:oneChannel = 1 1. 101 -16 -11 12  !  only tau > e vt ve decays\n") 
   
   runfile.close()


"""
Loop over general data that changes for each run. Specification of secondary particle with part
currently has no effect since all particles are handled in one PYTHIA run (this may 
change in the future).
"""
import subprocess

subprocess.call(["mkdir","-p","Runs-todo"], stdout=subprocess.PIPE) # create Runs-todo if not already existing
m = 500.     # mass of DM particle in GeV
#c = 91        
y = 22      # the secondary particle of interest (e+, pbar, nu_l, gamma etc.)
n = 100000  # number of events to simulate
anncodes = [5,24,15,6] # the DM annihilation channel (b bbar, W+W- etc.)
anncodes = [15]
#yieldcodes = [22,-11,-2212,14] # the yield particle code (gamma,e+, pbar, nu_mu/nu_mubar,  etc.)
for a in anncodes:
   makerunfile(m,a,y,n,False) 

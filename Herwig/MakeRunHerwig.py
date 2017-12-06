"""
makerun.py
Constructs .cmnd-files intended to be read by PYTHIA8 for the generation of
production fluxes of secondary particles from DM annihilation. First defines
function that creates one runfile, then loops over parameter values to
create all runfiles 

mX = eCM/2: 
Mass of DM particle
goes from 10-25000 GeV

annpdg: 
Annihilation channel PDG code (of particle in particle/antiparticle pair)
=5 - b bbar
=24 - W+W- (W+ is particle, W- antiparticle)
=15 - tau-tau+ 
=6 - t tbar

part:
Yield particle PDG code 
=22 - gamma
=-11 - e+
=-2212 - pbar
=14 - numu/numubar (abs. value)

nEvt:
Number of simulated events
"""
import sys

def makerunfile(mX,annPdg,yieldPdg,nEvt,test=False):
  if not test:
    filename = "da-her7-m"+str(int(mX))+"-ch"+str(annPdg)+".in"
    runfile = open("Runs-todo/"+filename,'w') 
  else:
    filename = "TEST-da-her7-m"+str(int(mX))+"-ch"+str(annPdg)+".in"
    runfile = open("Runs-todo/"+filename,'w') 
  """ 
  Write all Herwig commands and parameters for a run into the runfile
  """
  runfile.write("# "+filename+".\n")
  runfile.write("# -*- ThePEG-repository -*-\n")
  runfile.write("\n")
  runfile.write("##################################################\n")
  runfile.write("## DMann input file for WIMP annihilation yields\n")
  runfile.write("##################################################\n")
  runfile.write("\n")
  runfile.write("##################################################\n")
  runfile.write("## Collider type\n")
  runfile.write("##################################################\n")
  runfile.write("read snippets/EECollider.in\n")
  runfile.write("\n")
  runfile.write("##################################################\n")
  runfile.write("## Beam energy sqrt(s) = 2*m_X\n")
  runfile.write("##################################################\n")
  runfile.write("\n")
  runfile.write("cd /Herwig/EventHandlers\n")
  runfile.write("set EventHandler:LuminosityFunction:Energy "+str(2*mX)+"*GeV\n")
  runfile.write("\n")
  runfile.write("##################################################\n")
  runfile.write("## Process selection\n")
  runfile.write("##################################################\n")
  runfile.write("\n")
  runfile.write("## Note that event generation may fail if no matching matrix element has\n")
  runfile.write("## been found.  Coupling orders are with respect to the Born process,\n")
  runfile.write("## i.e. NLO QCD does not require an additional power of alphas.\n")
  runfile.write("\n")
  runfile.write("## Model assumptions\n")
  runfile.write("read Matchbox/StandardModelLike.in\n")
  runfile.write("read Matchbox/DiagonalCKM.in\n")
  runfile.write("\n")
  runfile.write("## Set the order of the couplings\n")
  runfile.write("cd /Herwig/MatrixElements/Matchbox\n")
  runfile.write("set Factory:OrderInAlphaS 0\n")
  runfile.write("set Factory:OrderInAlphaEW 2\n")
  runfile.write("\n")
  runfile.write("## Select the process\n")
  runfile.write("## The simple way. You may use identifiers such as p, pbar, j, l, mu+, h0 etc.\n")
  runfile.write("#do Factory:Process e- e+ -> W+ W-\n")
  runfile.write("\n")
  runfile.write("## The tougher way, needed for MEs not in Matchbox. Method is to:\n")
  runfile.write("# - create your custom SubProcessHandler\n")
  runfile.write("# - insert the MEs you need\n")
  runfile.write("# - set your SubProcessHandler instead of the default (see HerwigDefaults.in)\n")
  runfile.write("##################################################\n")
  runfile.write("\n")
  runfile.write("##################################################\n")
  runfile.write("#  e+e- matrix elements\n")
  runfile.write("##################################################\n")
  runfile.write("cd /Herwig/MatrixElements\n")
  runfile.write("\n")
  if abs(annPdg) in range(1,6):  
    runfile.write("# e+e- > q qbar\n")
    runfile.write("create Herwig::MEee2gZ2qq MEqq\n")
    runfile.write("insert SubProcess:MatrixElements[0] MEqq\n")
    runfile.write("set MEqq:MinimumFlavour "+str(abs(annPdg))+"\n")
    runfile.write("set MEqq:MaximumFlavour "+str(abs(annPdg))+"\n")
    runfile.write("set MEqq:AlphaQCD /Herwig/Shower/AlphaQCD\n")
    runfile.write("set MEqq:AlphaQED /Herwig/Shower/AlphaQED\n")
  elif abs(annPdg)==6:
    runfile.write("# e+e- > t tbar\n")
    runfile.write("insert SubProcess:MatrixElements[0] MEee2gZ2qq\n")
    runfile.write("set MEee2gZ2qq:MinimumFlavour "+str(abs(annPdg))+"\n")
    runfile.write("set MEee2gZ2qq:MaximumFlavour "+str(abs(annPdg))+"\n")
    runfile.write("set MEee2gZ2qq:AlphaQCD /Herwig/Shower/AlphaQCD\n")
    runfile.write("set MEee2gZ2qq:AlphaQED /Herwig/Shower/AlphaQED\n")
  elif abs(annPdg) in [11,13,15]:
    runfile.write("# e+e- -> l+l-\n")
    runfile.write("create Herwig::MEee2gZ2ll MEll\n")
    runfile.write("insert SubProcess:MatrixElements[0] MEll\n")
    if annPdg==11:
      runfile.write("set MEll:Allowed Electron  	# options: All, Charged, Electron, Muon or Tau\n")
    elif annPdg==13:
      runfile.write("set MEll:Allowed Mu  	# options: All, Charged, Electron, Muon or Tau\n")
    else:
      runfile.write("set MEll:Allowed Tau  	# options: All, Charged, Electron, Muon or Tau\n")
    runfile.write("set MEll:AlphaQED /Herwig/Shower/AlphaQED\n")
  elif abs(annPdg) in [23,24]:
    runfile.write("# e+e- -> W+W- ZZ\n")
    runfile.write("create Herwig::MEee2VV MEVV\n")
    runfile.write("insert SubProcess:MatrixElements[0] MEVV\n")
    if abs(annPdg)==23:
      runfile.write("set MEVV:Process ZZ 	# options: WW, WZ (W+ or W-), ZZ, WpZ, WmZ \n")      
    elif abs(annPdg)==24:
      runfile.write("set MEVV:Process WW 	# options: WW, WZ (W+ or W-), ZZ, WpZ, WmZ \n")
  elif abs(annPdg)==2300:
    runfile.write("# e+e- -> ZH\n")
    runfile.write("create Herwig::MEee2ZH MEZH\n")
    runfile.write("insert SubProcess:MatrixElements[0] MEZH\n")
    runfile.write("set MEH:Coupling /Herwig/Shower/AlphaQCD\n")
  else:
    sys.exit("ERROR in MakeRunHerwig.py: Annihilation channel not available")
  runfile.write("\n")
  runfile.write("## Special settings required for on-shell production of unstable particles\n")
  runfile.write("## enable for on-shell top production\n")
  runfile.write("read Matchbox/OnShellTopProduction.in\n")
  runfile.write("## enable for on-shell W, Z or h production\n")
  runfile.write("read Matchbox/OnShellWProduction.in\n")
  runfile.write("read Matchbox/OnShellZProduction.in\n")
  runfile.write("# read Matchbox/OnShellHProduction.in\n") # CN: Keep this or not??
  runfile.write("\n")
  runfile.write("##################################################\n")
  runfile.write("## Scale choice\n")
  runfile.write("## See the documentation for more options\n")
  runfile.write("##################################################\n")
  runfile.write("\n")
  runfile.write("cd /Herwig/MatrixElements/Matchbox\n")
  runfile.write("set Factory:ScaleChoice /Herwig/MatrixElements/Matchbox/Scales/SHatScale\n")
  runfile.write("\n")
  runfile.write("##################################################\n")
  runfile.write("## Matching and shower selection\n")
  runfile.write("##################################################\n")
  runfile.write("\n")
  runfile.write("read Matchbox/MCatNLO-DefaultShower.in\n")
  runfile.write("#read Matchbox/Powheg-DefaultShower.in\n")
  runfile.write("## use for strict LO/NLO comparisons\n")
  runfile.write("#read Matchbox/MCatLO-DefaultShower.in\n")
  runfile.write("## use for improved LO showering\n")
  runfile.write("#read Matchbox/LO-DefaultShower.in\n")
  runfile.write("\n")
  runfile.write("#read Matchbox/MCatNLO-DipoleShower.in\n")
  runfile.write("#read Matchbox/Powheg-DipoleShower.in\n")
  runfile.write("## use for strict LO/NLO comparisons\n")
  runfile.write("#read Matchbox/MCatLO-DipoleShower.in\n")
  runfile.write("## use for improved LO showering\n")
  runfile.write("#read Matchbox/LO-DipoleShower.in\n")
  runfile.write("\n")
  runfile.write("#read Matchbox/LO-NoShower.in\n")
  runfile.write("\n")
  runfile.write("##################################################\n")
  runfile.write("## Turn off ISR for e+ e- collision\n")
  runfile.write("##################################################\n")
  runfile.write("set /Herwig/Particles/e-:PDF /Herwig/Partons/NoPDF\n")
  runfile.write("set /Herwig/Particles/e+:PDF /Herwig/Partons/NoPDF\n")
  runfile.write("\n")
  runfile.write("##################################################\n")
  runfile.write("## Make usually stable particles decay\n")
  runfile.write("##################################################\n")
  runfile.write("set /Herwig/Particles/pi+:Stable Unstable\n")
  runfile.write("set /Herwig/Particles/K+:Stable Unstable\n")
  runfile.write("set /Herwig/Particles/K_L0:Stable Unstable\n")
  runfile.write("set /Herwig/Particles/mu+:Stable Unstable\n")
  runfile.write("set /Herwig/Particles/n0:Stable Unstable	\n") # CN: how to do with this??
  runfile.write("\n")
  runfile.write("##################################################\n")
  runfile.write("## Scale uncertainties\n")
  runfile.write("##################################################\n")
  runfile.write("\n")
  runfile.write("# read Matchbox/MuDown.in\n")
  runfile.write("# read Matchbox/MuUp.in\n")
  runfile.write("\n")
  runfile.write("##################################################\n")
  runfile.write("## Shower scale uncertainties\n")
  runfile.write("##################################################\n")
  runfile.write("\n")
  runfile.write("# read Matchbox/MuQDown.in\n")
  runfile.write("# read Matchbox/MuQUp.in\n")
  runfile.write("\n")
  runfile.write("##################################################\n")
  runfile.write("## Analysis of multiplicity\n")
  runfile.write("##################################################\n")
  runfile.write("cd /Herwig/Analysis\n")
  runfile.write("create DMann::DMannYields DMannYields DMannYields.so\n")
  runfile.write("insert /Herwig/Generators/EventGenerator:AnalysisHandlers 0 DMannYields\n")
  runfile.write("set DMannYields:MassDM "+str(mX)+"\n")
  for p in yieldpdgs:
    runfile.write("insert DMannYields:ParticleCodes[0] "+str(p)+"\n")
  runfile.write("\n")
  runfile.write("##################################################\n")
  runfile.write("## Do not apply profile scales for LEP as hard\n")
  runfile.write("## scale coincides with kinematic limit\n") # CN: How to do with this??
  runfile.write("##################################################\n")
  runfile.write("\n")
  runfile.write("set /Herwig/Shower/ShowerHandler:HardScaleProfile NULL\n")
  runfile.write("set /Herwig/DipoleShower/DipoleShowerHandler:HardScaleProfile NULL\n")
  runfile.write("\n")
  runfile.write("##################################################\n")
  runfile.write("## Save the generator\n")
  runfile.write("##################################################\n")
  runfile.write("\n")
  runfile.write("do /Herwig/MatrixElements/Matchbox/Factory:ProductionMode\n") # CN: what is this?
  runfile.write("\n")
  runfile.write("cd /Herwig/Generators\n")
  runfile.write("set EventGenerator:NumberOfEvents "+str(nEvt)+"\n")
  runfile.write("run "+filename[:-3]+" EventGenerator\n")

  runfile.close()


"""
Loop over general data that changes for each run. 
"""
import subprocess

subprocess.call(["mkdir","-p","Runs-todo"], stdout=subprocess.PIPE) # create runs-todo if not already existing
m = 200.0     # mass of DM particle in GeV
#c = 91        
yieldpdgs = [22,-11,-14,14,-2212]      # the secondary particles of interest (e+, pbar, nu_l, gamma etc.)
n = 10000  # number of events to simulate
anncodes = [5,24,15,6] # the DM annihilation channel (b bbar, W+W- etc.)
#yieldcodes = [22,-11,-2212,14] # the yield particle code (gamma,e+, pbar, nu_mu/nu_mubar,  etc.)
for c in anncodes:
  makerunfile(m,c,yieldpdgs,n,False) 


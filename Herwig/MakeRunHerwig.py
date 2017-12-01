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

def makerunfile(mX,annPdg,yieldPdg,nEvt,test=False):
  if not test:
    filename = "da-her7-m"+str(int(mX))+"-ch"+str(annPdg)+"-int"+str(yieldPdg)+".in"
    runfile = open("runs-todo/"+filename,'w') 
  else:
    filename = "TEST-runs/TEST-da-m"+str(int(mX))+"-ch"+str(annPdg)+"-int"+str(yieldPdg)+".cmnd"
    runfile = open(filename,'w')
  """ 
  Write all PYTHIA commands and parameters for a run into the runfile
  """
  runfile.write("# "+filename+".\n")
  runfile.write("# -*- ThePEG-repository -*-")
  runfile.write("")
  runfile.write("##################################################")
  runfile.write("## DMann input file for WIMP annihilation yields")
  runfile.write("##################################################")
  runfile.write("")
  runfile.write("##################################################")
  runfile.write("## Collider type")
  runfile.write("##################################################")
  runfile.write("read snippets/EECollider.in")
  runfile.write("")
  runfile.write("##################################################")
  runfile.write("## Beam energy sqrt(s) = 2*m_X")
  runfile.write("##################################################")
  runfile.write("")
  runfile.write("cd /Herwig/EventHandlers")
  runfile.write("set EventHandler:LuminosityFunction:Energy "+str(mX)+"*GeV")
  runfile.write("")
  runfile.write("##################################################")
  runfile.write("## Process selection")
  runfile.write("##################################################")
  runfile.write("")
  runfile.write("## Note that event generation may fail if no matching matrix element has")
  runfile.write("## been found.  Coupling orders are with respect to the Born process,")
  runfile.write("## i.e. NLO QCD does not require an additional power of alphas.")
  runfile.write("")
  runfile.write("## Model assumptions")
  runfile.write("read Matchbox/StandardModelLike.in")
  runfile.write("read Matchbox/DiagonalCKM.in")
  runfile.write("")
  runfile.write("## Set the order of the couplings")
  runfile.write("cd /Herwig/MatrixElements/Matchbox")
  runfile.write("set Factory:OrderInAlphaS 0")
  runfile.write("set Factory:OrderInAlphaEW 2")
  runfile.write("")
  runfile.write("## Select the process")
  runfile.write("## The simple way. You may use identifiers such as p, pbar, j, l, mu+, h0 etc.")
  runfile.write("#do Factory:Process e- e+ -> W+ W-")
  runfile.write("")
  runfile.write("## The tougher way, needed for MEs not in Matchbox. Method is to:")
  runfile.write("# - create your custom SubProcessHandler")
  runfile.write("# - insert the MEs you need")
  runfile.write("# - set your SubProcessHandler instead of the default (see HerwigDefaults.in)")
  runfile.write("##############################################################################")
  runfile.write("")
  runfile.write("############################################################")
  runfile.write("#  e+e- matrix elements")
  runfile.write("############################################################")
  runfile.write("cd /Herwig/MatrixElements")
  runfile.write("")
  if abs(annPdg) in range(1,7):  
    runfile.write("# e+e- > q qbar")
    runfile.write("#create Herwig::MEee2gZ2qq MEqq")
    runfile.write("#insert SubProcess:MatrixElements[0] MEqq")
    runfile.write("#set MEqq:MinimumFlavour "+str(annPdg))
    runfile.write("#set MEqq:MaximumFlavour "+str(annPdg))
    runfile.write("#set MEqq:AlphaQCD /Herwig/Shower/AlphaQCD")
    runfile.write("#set MEqq:AlphaQED /Herwig/Shower/AlphaQED")
  elif abs(annPdg) in range(11,17):
    runfile.write("# e+e- -> l+l-")
    runfile.write("#create Herwig::MEee2gZ2ll MEll")
    runfile.write("#insert SubProcess:MatrixElements[0] MEll")
    runfile.write("#set MEll:Allowed Tau  	# options: All, Charged, Electron, Muon or Tau")
    runfile.write("#set MEll:AlphaQED /Herwig/Shower/AlphaQED")
  elif abs(annPdg) in [23,24]:
    runfile.write("# e+e- -> W+W- ZZ")
    runfile.write("create Herwig::MEee2VV MEVV")
    runfile.write("insert SubProcess:MatrixElements[0] MEVV")
    if abs(annPdg)==23:
      runfile.write("set MEVV:Process ZZ 	# options: WW, WZ (W+ or W-), ZZ, WpZ, WmZ ")      
    elif abs(annPdg)==24:
      runfile.write("set MEVV:Process WW 	# options: WW, WZ (W+ or W-), ZZ, WpZ, WmZ ")
  elif abs(annPdg)==2300:
    runfile.write("# e+e- -> ZH")
    runfile.write("#create Herwig::MEee2ZH MEZH")
    runfile.write("#insert SubProcess:MatrixElements[0] MEZH")
    runfile.write("#set MEH:Coupling /Herwig/Shower/AlphaQCD")
  runfile.write("")
  runfile.write("## Special settings required for on-shell production of unstable particles")
  runfile.write("## enable for on-shell top production")
  runfile.write("read Matchbox/OnShellTopProduction.in")
  runfile.write("## enable for on-shell W, Z or h production")
  runfile.write("read Matchbox/OnShellWProduction.in")
  runfile.write("read Matchbox/OnShellZProduction.in")
  runfile.write("# read Matchbox/OnShellHProduction.in") # CN: Keep this or not??
  runfile.write("")
  runfile.write("##################################################")
  runfile.write("## Scale choice")
  runfile.write("## See the documentation for more options")
  runfile.write("##################################################")
  runfile.write("")
  runfile.write("cd /Herwig/MatrixElements/Matchbox")
  runfile.write("set Factory:ScaleChoice /Herwig/MatrixElements/Matchbox/Scales/SHatScale")
  runfile.write("")
  runfile.write("##################################################")
  runfile.write("## Matching and shower selection")
  runfile.write("##################################################")
  runfile.write("")
  runfile.write("#read Matchbox/MCatNLO-DefaultShower.in")
  runfile.write("#read Matchbox/Powheg-DefaultShower.in")
  runfile.write("## use for strict LO/NLO comparisons")
  runfile.write("#read Matchbox/MCatLO-DefaultShower.in")
  runfile.write("## use for improved LO showering")
  runfile.write("read Matchbox/LO-DefaultShower.in")
  runfile.write("")
  runfile.write("#read Matchbox/MCatNLO-DipoleShower.in")
  runfile.write("#read Matchbox/Powheg-DipoleShower.in")
  runfile.write("## use for strict LO/NLO comparisons")
  runfile.write("#read Matchbox/MCatLO-DipoleShower.in")
  runfile.write("## use for improved LO showering")
  runfile.write("#read Matchbox/LO-DipoleShower.in")
  runfile.write("")
  runfile.write("#read Matchbox/LO-NoShower.in")
  runfile.write("")
  runfile.write("##################################################")
  runfile.write("## Turn off ISR for e+ e- collision")
  runfile.write("##################################################")
  runfile.write("set /Herwig/Particles/e-:PDF /Herwig/Partons/NoPDF")
  runfile.write("set /Herwig/Particles/e+:PDF /Herwig/Partons/NoPDF")
  runfile.write("")
  runfile.write("##################################################")
  runfile.write("## Make usually stable particles decay")
  runfile.write("##################################################")
  runfile.write("set /Herwig/Particles/pi+:Stable Unstable")
  runfile.write("set /Herwig/Particles/K+:Stable Unstable")
  runfile.write("set /Herwig/Particles/K_L0:Stable Unstable")
  runfile.write("set /Herwig/Particles/mu+:Stable Unstable")
  runfile.write("#set /Herwig/Particles/n0:Stable Unstable	# does not seem to work") # CN: how to do with this??
  runfile.write("")
  runfile.write("##################################################")
  runfile.write("## Scale uncertainties")
  runfile.write("##################################################")
  runfile.write("")
  runfile.write("# read Matchbox/MuDown.in")
  runfile.write("# read Matchbox/MuUp.in")
  runfile.write("")
  runfile.write("##################################################")
  runfile.write("## Shower scale uncertainties")
  runfile.write("##################################################")
  runfile.write("")
  runfile.write("# read Matchbox/MuQDown.in")
  runfile.write("# read Matchbox/MuQUp.in")
  runfile.write("")
  runfile.write("##################################################")
  runfile.write("## Analysis of multiplicity")
  runfile.write("##################################################")
  runfile.write("cd /Herwig/Analysis")
  runfile.write("create DMann::DMannYields DMannYields DMannYields.so")
  runfile.write("insert /Herwig/Generators/EventGenerator:AnalysisHandlers 0 DMannYields")
  runfile.write("set DMannYields:MassDM 200.0")
  runfile.write("insert DMannYields:ParticleCodes[0] 22 		# gamma")
  runfile.write("insert DMannYields:ParticleCodes[1] -2212	# pbar")
  runfile.write("insert DMannYields:ParticleCodes[2] -11		# e+")
  runfile.write("insert DMannYields:ParticleCodes[3] 14		# numu")
  runfile.write("insert DMannYields:ParticleCodes[4] -14		# numubar	")
  runfile.write("")
  runfile.write("##################################################")
  runfile.write("## Do not apply profile scales for LEP as hard")
  runfile.write("## scale coincides with kinematic limit") # CN: How to do with this??
  runfile.write("##################################################")
  runfile.write("")
  runfile.write("set /Herwig/Shower/ShowerHandler:HardScaleProfile NULL")
  runfile.write("set /Herwig/DipoleShower/DipoleShowerHandler:HardScaleProfile NULL")
  runfile.write("")
  runfile.write("##################################################")
  runfile.write("## Save the generator")
  runfile.write("##################################################")
  runfile.write("")
  runfile.write("do /Herwig/MatrixElements/Matchbox/Factory:ProductionMode") # CN: what is this?
  runfile.write("")
  runfile.write("cd /Herwig/Generators")
  runfile.write("saverun "+filename[:-3]+" EventGenerator")
  runfile.write("")
  runfile.write("set EventGenerator:NumberOfEvents "+str(nEvt))
  runfile.write("run DMann EventGenerator")

  runfile.close()


"""
Loop over general data that changes for each run. Specification of secondary particle with part
currently has no effect since all particles are handled in one PYTHIA run (this may 
change in the future).
"""
import subprocess

subprocess.call(["mkdir","-p","runs-todo"], stdout=subprocess.PIPE) # create runs-todo if not already existing
m = 200.     # mass of DM particle in GeV
#c = 91        
p = 22      # the secondary particle of interest (e+, pbar, nu_l, gamma etc.)
n = 1000000  # number of events to simulate
anncodes = [5,24,15,6] # the DM annihilation channel (b bbar, W+W- etc.)
#yieldcodes = [22,-11,-2212,14] # the yield particle code (gamma,e+, pbar, nu_mu/nu_mubar,  etc.)
for c in anncodes:
  makerunfile(m,c,p,n,False) 


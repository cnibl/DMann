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

def makerunfile(eCM,PDGs,nEvt,ResCon,FRMod):
  filename = "pnu-her7-e"+str(int(eCM))+".in"
  runfile = open("Runs/"+filename,'w') 
  """ 
  Write all Herwig commands and parameters for a run into the runfile
  """
  runfile.write("# "+filename+".\n")
  runfile.write("# -*- ThePEG-repository -*-\n")
  runfile.write("\n")
  runfile.write("##################################################\n")
  runfile.write("## Input file for prompt neutrino yields\n")
  runfile.write("##################################################\n")
  runfile.write("\n")
  if FRMod:
    runfile.write("##################################################\n")
    runfile.write("## Read in the FeynRules model file\n")
    runfile.write("##################################################\n")
    runfile.write("read ../FRModel.model\n")
    runfile.write("\n")
  runfile.write("###########################################################\n")
  runfile.write("## Change masses of gen. resonance and Z to match E_CM\n")
  runfile.write("###########################################################\n")
  runfile.write("\n")
  if FRMod:
    runfile.write("set /Herwig/FRModel/Particles/GR:NominalMass "+str(eCM)+"\n")
  runfile.write("set /Herwig/Particles/Z0:NominalMass "+str(eCM)+"\n")
  runfile.write("\n")
  runfile.write("##################################################\n")
  runfile.write("## Collider type\n")
  runfile.write("##################################################\n")
  runfile.write("read snippets/EECollider.in\n")
  runfile.write("\n")
  runfile.write("##################################################\n")
  runfile.write("## Beam energy sqrt(s)\n")
  runfile.write("##################################################\n")
  runfile.write("\n")
  runfile.write("cd /Herwig/EventHandlers\n")
  runfile.write("set EventHandler:LuminosityFunction:Energy "+str(eCM)+"*GeV\n")
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
  runfile.write("set Factory:OrderInAlphaEW 1\n")
  runfile.write("\n")
  runfile.write("##################################################\n")
  runfile.write("#  e+e- matrix elements\n")
  runfile.write("##################################################\n")
  if ResCon:
    runfile.write("##################################################\n")
    runfile.write("## Select the process\n")
    runfile.write("## Use the FeynRules UFO model with a simple general resonance (GR).\n")
    runfile.write("##################################################\n")
    runfile.write("\n")  
    runfile.write("cd /Herwig/NewPhysics\n")
    runfile.write("insert ResConstructor:Incoming 0 /Herwig/Particles/e-\n")
    runfile.write("insert ResConstructor:Incoming 0 /Herwig/Particles/e+\n")
    if FRMod:
      runfile.write("insert ResConstructor:Intermediates 0 /Herwig/FRModel/Particles/GR\n") 
    else:
      runfile.write("insert ResConstructor:Intermediates 0 /Herwig/FRModel/Particles/Z0\n")
    runfile.write("# e+e- -> W+W-\n")
    runfile.write("insert ResConstructor:Outgoing 0 /Herwig/Particles/W-\n")
    runfile.write("insert ResConstructor:Outgoing 0 /Herwig/Particles/W+\n")
    runfile.write("set ResConstructor:Process Exclusive")
    runfile.write("set ResConstructor:Processes Exclusive\n")    
  else:
    runfile.write("cd /Herwig/MatrixElements\n")
    runfile.write("# e+e- -> W+W- ZZ\n")
    runfile.write("create Herwig::MEee2VV MEVV\n")
    runfile.write("insert SubProcess:MatrixElements[0] MEVV\n")
    runfile.write("set MEVV:Process WW   # options: WW, WZ (W+ or W-), ZZ, WpZ, WmZ \n")
  runfile.write("\n")
  runfile.write("## Special settings required for on-shell production of unstable particles\n")
  runfile.write("## enable for on-shell top production\n")
  runfile.write("read Matchbox/OnShellTopProduction.in\n")
  runfile.write("## enable for on-shell W, Z or h production\n")
  runfile.write("read Matchbox/OnShellWProduction.in\n")
  runfile.write("read Matchbox/OnShellZProduction.in\n")
  runfile.write("# read Matchbox/OnShellHProduction.in\n") # CN: Keep this or not??
  runfile.write("\n")
  #runfile.write("##################################################\n")
  #runfile.write("## Scale choice\n")
  #runfile.write("## See the documentation for more options\n")
  #runfile.write("##################################################\n")
  #runfile.write("\n")
  #runfile.write("cd /Herwig/MatrixElements/Matchbox\n")
  #runfile.write("set Factory:ScaleChoice /Herwig/MatrixElements/Matchbox/Scales/SHatScale\n")
  #runfile.write("\n")
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
#  runfile.write("##################################################\n")
#  runfile.write("## Turn on QED radiation\n")
#  runfile.write("##################################################\n")  
#  runfile.write("# add QED radiation off W/Z decay products using YFS formalism\n")
#  runfile.write("cd /Herwig/EventHandlers\n")
#  runfile.write("insert EventHandler:PostSubProcessHandlers[0] /Herwig/QEDRadiation/QEDRadiationHandler\n")
#  for i in range(1,7):
#    runfile.write("insert /Herwig/QEDRadiation/QEDRadiationHandler:DecayProducts[0] "+str(i)+"\n")  
#  for i in range(10,17):
#    runfile.write("insert /Herwig/QEDRadiation/QEDRadiationHandler:DecayProducts[0] "+str(i)+"\n")     
#  runfile.write("insert /Herwig/QEDRadiation/QEDRadiationHandler:DecayProducts[0] 24\n")     
#  runfile.write("insert /Herwig/QEDRadiation/QEDRadiationHandler:DecayingParticles[0] "+str(annPdg)+"\n")    
#  runfile.write("set /Herwig/Shower/ShowerHandler:Interactions QCDandQED\n")
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
  #runfile.write("set /Herwig/Particles/mu+:Stable Unstable\n")
  runfile.write("set /Herwig/Particles/n0:Stable Unstable	\n") # CN: how to do with this??
  runfile.write("\n")
  runfile.write("##################################################\n")
  runfile.write("## Change W properties to get only prompt \n")
  runfile.write("## neutrinos from W decay \n")
  runfile.write("##################################################\n")
  runfile.write("do /Herwig/Particles/W+:PrintDecayModes\n")
  runfile.write("set /Herwig/Particles/W+:NominalMass 80.385\n")
  runfile.write("set /Herwig/Particles/W+:WidthCut 0.01\n")
  runfile.write("set /Herwig/Particles/W+:Width_generator:Initialize Yes\n")
  runfile.write("set /Herwig/Particles/W+:Mass_generator:Initialize Yes\n")
  runfile.write("set /Herwig/Decays/WDecayer:Initialize Yes\n")
  runfile.write("do /Herwig/Particles/W+:SelectDecayModes\n")
  runfile.write("do /Herwig/Particles/W+:SelectDecayModes W+->nu_mu,mu+;\n")
  runfile.write("set /Herwig/Particles/W+/W+->nu_mu,mu+;:BranchingRatio 1\n")
  runfile.write("do /Herwig/Particles/W+:PrintDecayModes\n")
  #runfile.write("#set /Herwig/Particles/W+/W+->nu_e,e+;:OnOff On\n")
  
  #runfile.write("##################################################\n")
  #runfile.write("## Scale uncertainties\n")
  #runfile.write("##################################################\n")
  #runfile.write("\n")
  #runfile.write("# read Matchbox/MuDown.in\n")
  #runfile.write("# read Matchbox/MuUp.in\n")
  #runfile.write("\n")
  #runfile.write("##################################################\n")
  #runfile.write("## Shower scale uncertainties\n")
  #runfile.write("##################################################\n")
  #runfile.write("\n")
  #runfile.write("# read Matchbox/MuQDown.in\n")
  #runfile.write("# read Matchbox/MuQUp.in\n")
  #runfile.write("\n")
  runfile.write("##################################################\n")
  runfile.write("## Analysis of multiplicity\n")
  runfile.write("##################################################\n")
  runfile.write("cd /Herwig/Analysis\n")
  runfile.write("create DMann::DMannYields DMannYields DMannYields.so\n")
  runfile.write("insert /Herwig/Generators/EventGenerator:AnalysisHandlers 0 DMannYields\n")
  runfile.write("set DMannYields:MassDM "+str(eCM/2.)+"\n")
  runfile.write("set DMannYields:NEvent "+str(nEvt)+"\n")
  for p in PDGs:
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
  runfile.write("## Set up some last things\n")
  runfile.write("##################################################\n")
  runfile.write("set /Herwig/Shower/ShowerHandler:Interactions QCD\n")

  runfile.write("cd /Herwig/EventHandlers\n")
  runfile.write("##set EventHandler:DecayHandler NULL\n")
  runfile.write("set EventHandler:HadronizationHandler NULL\n")
  runfile.write("#set EventHandler:CascadeHandler:MPIHandler NULL\n")
  runfile.write("#set EventHandler:CascadeHandler NULL\n")
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

subprocess.call(["mkdir","-p","Runs"], stdout=subprocess.PIPE) # create runs-todo if not already existing
e = 400.0     # mass of DM particle in GeV
pdgs = [-14,14]      # the secondary particles of interest (e+, pbar, nu_l, gamma etc.)
n = 100000  # number of events to simulate
rc = False
frm = False
makerunfile(e,pdgs,n,rc,frm) 


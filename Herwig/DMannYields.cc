// -*- C++ -*-
//
// This is the implementation of the non-inlined, non-templated member
// functions of the DMannYields class.
//

#include "DMannYields.h"
#include "ThePEG/Interface/ClassDocumentation.h"
#include "ThePEG/Interface/ParVector.h"
#include "ThePEG/Interface/Parameter.h"
#include "ThePEG/EventRecord/Particle.h"
#include "ThePEG/Repository/UseRandom.h"
#include "ThePEG/Repository/EventGenerator.h"
#include "ThePEG/Utilities/DescribeClass.h"

#include "ThePEG/Persistency/PersistentOStream.h"
#include "ThePEG/Persistency/PersistentIStream.h"

//#include "TH1F.h"
//#include "TCanvas.h"

using namespace DMann;
//histo(2.e-10.,200.,250)
DMannYields::DMannYields() : 
histo(Herwig::Histogram::LogBins(2.e-8,250,pow(10,0.04))), 
_yieldpdg(0),
_massdm(0.0),
_annpdg(0)
{}

DMannYields::~DMannYields() {}

#ifndef LWH_AIAnalysisFactory_H
#ifndef LWH 
#define LWH ThePEGLWH
#endif
#include "ThePEG/Analysis/LWH/AnalysisFactory.h"
#endif

void DMannYields::analyze(tEventPtr event, long ieve, int loop, int state) {
  AnalysisHandler::analyze(event, ieve, loop, state);
  // Rotate to CMS, extract final state particles and call analyze(particles).
  Lorentz5Momentum p;
  set<tcPPtr> particles;
  event->selectFinalState(inserter(particles));
//  if ( loop > 0 || state != 0 || !event ) return
 
  tSubProPtr sub = event->primarySubProcess();
  ParticleVector outPtr = sub->outgoing(); 
  _annpdg = abs((*(outPtr[0])).id());

  for(set<tcPPtr>::const_iterator it = particles.begin(); 
    it != particles.end(); ++it) {
    /** Check if particle id in list (i.e. (*it)->id()) equals any of yield particle IDs and fill histograms */
    for (std::vector<long>::iterator idPtr = _pdgvec.begin(); 
          idPtr != _pdgvec.end(); ++idPtr) {
      if ((*it)->id()==(*idPtr)) { 
        p = (*it)->momentum();
        _histograms[(*idPtr)] += (p.e()-p.mass())/GeV; // Fill histogram corresponding to yield ID
        //histo += p.e()/GeV;
      }
    } 
    /** Select only the gammas  */
    /*if((*it)->id()==ParticleID::gamma) {
      p = (*it)->momentum();
      //histograms[(*it)->id()] += p.e()/GeV;
      histo += p.e()/GeV;
    }*/
  }

}

LorentzRotation DMannYields::transform(tcEventPtr event) const {
  return LorentzRotation();
  // Return the Rotation to the frame in which you want to perform the analysis.
}

void DMannYields::analyze(const tPVector & particles, double weight) {
  AnalysisHandler::analyze(particles);
  // Calls analyze() for each particle.
}

void DMannYields::analyze(tPPtr, double weight) {}

void DMannYields::dofinish() {
  // *** ATTENTION *** Normalize and post-process histograms here.
  long nEvt = generator()->currentEventNumber() - 1;  
  for (std::vector<long>::iterator idPtr = _pdgvec.begin(); 
        idPtr != _pdgvec.end(); ++idPtr) {
    useMe();
    string filename = "Herwig7Data/da-her7-mx"+std::to_string((int)_massdm)+"-ch"+std::to_string(_annpdg)+"-int"+std::to_string(*idPtr)+".dat";
    //string filename = generator()->filename() + "-" + std::to_string((*idPtr)) +".mult";
    ofstream outfile(filename.c_str());
    outfile << "# DMann Herwig7 data file with counts/nAnn as function of E_kin (not divided by nAnn right now)\n";
    time_t rawtime;
    time(&rawtime);
    outfile << "# Created: " << ctime(&rawtime);
    outfile << "# Number of simulated events: " << std::to_string(nEvt) << "\n";
    outfile << "# WIMP mass: " << std::to_string((int)_massdm) << " GeV\n";
    outfile << "# PDG code of annihilation channel: " << std::to_string(_annpdg) << "\n"; 
    outfile << "# PDG code of yield particle: " << std::to_string((*idPtr)) << "\n";   
    outfile << "# \n";
    outfile << "# E_low\tE_high\tnorm\tcounts\n";  
    
    
    _histograms[(*idPtr)].simpleOutput(outfile, false, false);
    //_histograms[(*idPtr)].rivetOutput(outfile, "Multiplicity", "DMann", "Multiplicity", "E_{\\rm kin}", "dN/dE", false, 1./nEvt); //???
    outfile.close();
    AnalysisHandler::dofinish();
  }
}

void DMannYields::doinitrun() {
  AnalysisHandler::doinitrun();
  // *** ATTENTION *** histogramFactory().registerClient(this); // Initialize histograms.
  // *** ATTENTION *** histogramFactory().mkdirs("/SomeDir"); // Put histograms in specal directory.
  for (std::vector<long>::iterator idPtr = _pdgvec.begin(); 
        idPtr != _pdgvec.end(); ++idPtr) {
    _histograms.insert(make_pair((*idPtr),
      Herwig::Histogram(Herwig::Histogram::LogBins(1.e-10*_massdm,250,pow(10,0.04)))));    
  }
}


IBPtr DMannYields::clone() const {
  return new_ptr(*this);
}

IBPtr DMannYields::fullclone() const {
  return new_ptr(*this);
}


// If needed, insert default implementations of virtual function defined
// in the InterfacedBase class here (using ThePEG-interfaced-impl in Emacs).


void DMannYields::persistentOutput(PersistentOStream & os) const {
  // *** ATTENTION *** os << ; // Add all member variable which should be written persistently here.
  os << _yieldpdg << _massdm << _pdgvec;
}

void DMannYields::persistentInput(PersistentIStream & is, int) {
  // *** ATTENTION *** os << ; // Add all member variable which should be read persistently here.
  is >> _yieldpdg >> _massdm >> _pdgvec;
}

string library() { return "DMannYields.so"; }

// *** Attention *** The following static variable is needed for the type
// description system in ThePEG. Please check that the template arguments
// are correct (the class and its base class), and that the constructor
// arguments are correct (the class name and the name of the dynamically
// loadable library where the class implementation can be found).
DescribeClass<DMannYields,AnalysisHandler>
  describeDMannDMannYields("DMann::DMannYields", "DMannYields.so");

// Definition of the static class description member.
ClassDescription<DMannYields> DMannYields::initDMannYields;

void DMannYields::Init() {

  static Parameter<DMannYields,double> interfacemassdm
    ("MassDM",
     "The mass of the DM particle",
     &DMannYields::_massdm, 0, 0., 0., 100000.0, 
     false, false, Interface::limited);

  static Parameter<DMannYields,long> interfaceyieldpdg //OBSOLETE
    ("YieldPDG",
     "PDG code of the yield particle of interest (gamma, e+ etc.)",
     &DMannYields::_yieldpdg, 0, 0, 0, 100000, 
     false, false, Interface::limited);    

  static ParVector<DMannYields,long> interfacepdgvec
    ("ParticleCodes",
     "The PDG code for the particles",
     &DMannYields::_pdgvec,-1, 0l, -10000000l, 10000000l,
     false, false, Interface::limited);
     //0, 0, 0, -10000000, 10000000, false, false, Interface::nolimits);

  static ClassDocumentation<DMannYields> documentation
    ("There is no documentation for the DMannYields class");

}


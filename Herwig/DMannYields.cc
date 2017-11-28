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
_massdm(0.0)
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

  //map <long,long> eventcount;
//  if ( loop > 0 || state != 0 || !event ) return
  //tPVector particles = event->getFinalState();
 
  /** loop over all particles */
//  for (tPVector::const_iterator pit = particles.begin();
//    pit != particles.end(); ++pit){
  
  /*
  cout << "Mass DM " << _massdm << "\n";
  cout << "Yield PDG " << _yieldpdg << "\n\n";
  for (std::vector<int>::iterator it = _pdgvec.begin(); it != _pdgvec.end(); ++it) {
    cout << "PDGvec = " << (*it) << "\n";
  }
  cout << "\n";
  */

  for(set<tcPPtr>::const_iterator it = particles.begin(); 
    it != particles.end(); ++it) {
    /** Check if particle id ((*it)->id()) equals any of yield particle IDs and fill histograms */
    for (std::vector<int>::iterator idPtr = _pdgvec.begin(); 
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
  for (std::vector<int>::iterator idPtr = _pdgvec.begin(); 
        idPtr != _pdgvec.end(); ++idPtr) {
    useMe();
    string filename = generator()->filename() + "-" + std::to_string((*idPtr)) +".mult";
    ofstream outfile(filename.c_str());
    //using namespace Herwig::HistogramOptions;
    //histo.topdrawOutput(outfile,Frame|Ylog,"BLACK","title","",
    //         "N (200 bins)","","Photon energy [GeV]");
    //histo.simpleOutput(outfile, false, false);
    _histograms[(*idPtr)].simpleOutput(outfile, false, false);
    outfile.close();
    AnalysisHandler::dofinish();
  }
}

void DMannYields::doinitrun() {
  AnalysisHandler::doinitrun();
  // *** ATTENTION *** histogramFactory().registerClient(this); // Initialize histograms.
  // *** ATTENTION *** histogramFactory().mkdirs("/SomeDir"); // Put histograms in specal directory.
  for (std::vector<int>::iterator idPtr = _pdgvec.begin(); 
        idPtr != _pdgvec.end(); ++idPtr) {
    _histograms.insert(make_pair((*idPtr),
      Herwig::Histogram(Herwig::Histogram::LogBins(2.e-8,250,pow(10,0.04)))));
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

  static Parameter<DMannYields,int> interfaceyieldpdg
    ("YieldPDG",
     "PDG code of the yield particle of interest (gamma, e+ etc.)",
     &DMannYields::_yieldpdg, 0, 0, 0, 100000, 
     false, false, Interface::limited);    

  static ParVector<DMannYields,int> interfacepdgvec
    ("ParticleCodes",
     "The PDG code for the particles",
     &DMannYields::_pdgvec,-1, 0, -10000000, 10000000,
     false, false, Interface::limited);
     //0, 0, 0, -10000000, 10000000, false, false, Interface::nolimits);

  static ClassDocumentation<DMannYields> documentation
    ("There is no documentation for the DMannYields class");

}


// -*- C++ -*-
//
// This is the implementation of the non-inlined, non-templated member
// functions of the DMannYields class.
//

#include "DMannYields.h"
#include "ThePEG/Interface/ClassDocumentation.h"
#include "ThePEG/EventRecord/Particle.h"
#include "ThePEG/Repository/UseRandom.h"
#include "ThePEG/Repository/EventGenerator.h"
#include "ThePEG/Utilities/DescribeClass.h"
#include <iostream>
#include <sstream>
#include <fstream>

//#include "TH1F.h"
//#include "TCanvas.h"

using namespace DMann;
//histo(2.e-10.,200.,250)
DMannYields::DMannYields()  :  histo(Herwig::Histogram::LogBins(2.e-8,250,pow(10,0.04))) {}

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
  for(set<tcPPtr>::const_iterator it = particles.begin(); 
    it != particles.end(); ++it) {
    /** Select only the gammas  */
    if((*it)->id()==ParticleID::gamma) {
      p = (*it)->momentum();
      histo += p.e()/GeV;
    }
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
  useMe();
  string filename = generator()->filename() + ".mult";
  ofstream outfile(filename.c_str());
  //using namespace Herwig::HistogramOptions;
  //histo.topdrawOutput(outfile,Frame|Ylog,"BLACK","title","",
  //         "N (200 bins)","","Photon energy [GeV]");
  histo.simpleOutput(outfile, false, false);
  outfile.close();
  AnalysisHandler::dofinish();
}

void DMannYields::doinitrun() {
  AnalysisHandler::doinitrun();
  // *** ATTENTION *** histogramFactory().registerClient(this); // Initialize histograms.
  // *** ATTENTION *** histogramFactory().mkdirs("/SomeDir"); // Put histograms in specal directory.
  //Herwig::Histogram histo = Herwig::Histogram(0.,200., 100);
}


IBPtr DMannYields::clone() const {
  return new_ptr(*this);
}

IBPtr DMannYields::fullclone() const {
  return new_ptr(*this);
}


// If needed, insert default implementations of virtual function defined
// in the InterfacedBase class here (using ThePEG-interfaced-impl in Emacs).

//static string library() { return "DMannYields.so"; }

// *** Attention *** The following static variable is needed for the type
// description system in ThePEG. Please check that the template arguments
// are correct (the class and its base class), and that the constructor
// arguments are correct (the class name and the name of the dynamically
// loadable library where the class implementation can be found).
DescribeNoPIOClass<DMannYields,AnalysisHandler>
  describeDMannDMannYields("DMann::DMannYields", "DMannYields.so");

void DMannYields::Init() {

  static ClassDocumentation<DMannYields> documentation
    ("There is no documentation for the DMannYields class");

}


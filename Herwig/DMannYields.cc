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

#include "Herwig/Utilities/Histogram.h"

//#include "TH1F.h"
//#include "TFile.h"
//#include "TCanvas.h"

using namespace DMann;

//histo(2.e-10.,200.,250)
DMannYields::DMannYields() : 
 //histo(Herwig::Histogram::LogBins(2.e-8,250,pow(10,0.04))), 
_yieldpdg(0),
_massdm(0.0),
_annpdg(0),
_annstate(""),
_nevt(0),
_evtFile(true),
_lastEvt(false)
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
  //sub->printMe(cout); // print out hard process
  if (_evtFile==true) {
    string eventfilename = _outdir+"/da-her7-mx"+std::to_string((int)_massdm)+"-"+_annstate+"-events.dat";
    ofstream eventfile(eventfilename.c_str(),std::fstream::app);
    long nEvtCur = generator()->currentEventNumber();
    if (nEvtCur==_nevt) {
      _lastEvt=true;
    }
    eventfile << "# Event " << nEvtCur << endl;
    eventfile.close();
  }
  for(set<tcPPtr>::const_iterator it = particles.begin(); 
    it != particles.end(); ++it) {
    /** Check if particle id in list (i.e. (*it)->id()) equals any of yield particle IDs and fill histograms */
    for (std::vector<long>::const_iterator idPtr = _pdgvec.begin(); 
          idPtr != _pdgvec.end(); ++idPtr) {
      if ((*it)->id()==(*idPtr)) { 
        //if (abs((*it)->id())==14) {
        //  int parID = ((*it)->parents())[0]->id();
        //  if (abs(parID)==23 || abs(parID)==24) {
        //    ((*it)->parents())[0]->print(cout);
        //  }
        //}
        p = (*it)->momentum(); //the four-momentum
        _histogramslog[(*idPtr)].addWeighted( (p.e()-p.mass())/GeV, 1.0/(double)_nevt ); // Fill log histogram corresponding to yield ID, divided by number of events
        _histograms[(*idPtr)].addWeighted( (p.e()-p.mass())/GeV, 1.0/(double)_nevt ); // Fill histogram corresponding to yield ID, divided by number of events
        //_histogramsROOT[(*idPtr)]->Fill((p.e()-p.mass())/GeV);
        if (_evtFile==true) {
          string eventfilename = _outdir+"/da-her7-mx"+std::to_string((int)_massdm)+"-"+_annstate+"-events.dat";
          ofstream eventfile(eventfilename.c_str(),std::fstream::app);
          eventfile << setw(10) << left <<(*it)->id() 
                  << setw(15) << left << std::scientific << p.e()/GeV 
                  << setw(10) << left << ((*it)->parents())[0]->id() << endl;
          eventfile.close();
        }
      }
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
  long nEvt = generator()->currentEventNumber() - 1;  
  for (std::vector<long>::iterator idPtr = _pdgvec.begin(); 
        idPtr != _pdgvec.end(); ++idPtr) {
    useMe();
    //string filename = "Herwig7Data/da-her7-mx"+std::to_string((int)_massdm)+"-ch"+std::to_string(_annpdg)+"-y"+std::to_string(*idPtr)+".dat";
    string filename = _outdir+"/da-her7-mx"+std::to_string((int)_massdm)+"-"+_annstate+"-y"+std::to_string(*idPtr)+".dat";
    
    ofstream outfile(filename.c_str());
    outfile << "# DMann Herwig7 data file with counts/nAnn as function of E_kin\n";
    time_t rawtime;
    time(&rawtime);
    outfile << "# Created: " << ctime(&rawtime);
    outfile << "# Number of simulated events: " << std::to_string(nEvt) << "\n";
    outfile << "# WIMP mass: " << std::to_string((int)_massdm) << " GeV\n";
    outfile << "# Annihilation channel: " << _annstate << "\n"; 
    outfile << "# PDG code of yield particle: " << std::to_string((*idPtr)) << "\n";   
    outfile << "# \n";
    //outfile << "# E_low\tE_high\tnorm\tcounts\n";  
    outfile << "# E\t\tcounts/nAnn\n";  
    
    std::vector<double> binEntries = _histograms[(*idPtr)].dumpBins(); //note:first bin is underflow, last overflow
    double deltaBin = 1./_histograms[(*idPtr)].numberOfBins();
    for (unsigned int i=1; i != _histograms[(*idPtr)].numberOfBins()+1; ++i) { 
      outfile << _massdm*(1./_histograms[(*idPtr)].numberOfBins()/2.+(i-1)*deltaBin) << "\t\t" << binEntries[i] << endl;
    }
    //_histograms[(*idPtr)].simpleOutput(outfile, false, false);
    outfile.close();


    //Same for log histogram
    string filenamelog = _outdir+"/da-her7-mx"+std::to_string((int)_massdm)+"-"+_annstate+"-y"+std::to_string(*idPtr)+"-log.dat";
    
    ofstream outfilelog(filenamelog.c_str());
    outfilelog << "# DMann Herwig7 data file with counts/nAnn as function of E_kin, logarithmic bins\n";
    outfilelog << "# Created: " << ctime(&rawtime);
    outfilelog << "# Number of simulated events: " << std::to_string(nEvt) << "\n";
    outfilelog << "# WIMP mass: " << std::to_string((int)_massdm) << " GeV\n";
    outfilelog << "# Annihilation channel: " << _annstate << "\n"; 
    outfilelog << "# PDG code of yield particle: " << std::to_string((*idPtr)) << "\n";   
    outfilelog << "# \n";
    outfilelog << "# E_low\tE_high\tnorm\tcounts\n";  

    //vector<double> logbinedges = _histogramslog[(*idPtr)].LogBins()
    //for (unsigned int i=0; i != _histogramslog[(*idPtr)].numberOfBins (); ++i) {
    //  cout << logbinedges[i] << endl;
    //}

    _histogramslog[(*idPtr)].simpleOutput(outfilelog, false, false);
    outfilelog.close();

    //string fName = "yieldpdg_"+std::to_string(*idPtr)+".root";
    //TFile* outFile = new TFile(fName.c_str(), "RECREATE");
    //_histogramsROOT[(*idPtr)]->Write();
    //delete outFile;  

    
    if (_evtFile==true && _lastEvt==true) {
      string eventfilename = _outdir+"/da-her7-mx"+std::to_string((int)_massdm)+"-"+_annstate+"-events.dat";
      ofstream eventfile(eventfilename.c_str(),std::fstream::app);
      eventfile << "#END" << endl;
      eventfile.close();
    }

    AnalysisHandler::dofinish();

  }
}

void DMannYields::doinitrun() {
  AnalysisHandler::doinitrun();
  // *** ATTENTION *** histogramFactory().registerClient(this); // Initialize histograms.
  // *** ATTENTION *** histogramFactory().mkdirs("/SomeDir"); // Put histograms in specal directory.
  for (std::vector<long>::iterator idPtr = _pdgvec.begin(); 
        idPtr != _pdgvec.end(); ++idPtr) {
    _histogramslog.insert(make_pair((*idPtr),
      Herwig::Histogram(Herwig::Histogram::LogBins(1.e-10*_massdm,250,pow(10,0.04)))));     
    _histograms.insert(make_pair((*idPtr),
      Herwig::Histogram(0.,_massdm,200)));   

    //string histoname = std::to_string(*idPtr);
    //string histotitle = "Kinetic energy for yield PDG " + std::to_string(*idPtr);
    //TH1F * histoROOT = new TH1F("test",
    //                        "multiplicity",
    //                        200, 0., _massdm);
    //_histogramsROOT.insert(make_pair((*idPtr), histoROOT)); 
    if (_evtFile==true) {
      string eventfilename = _outdir+"/da-her7-mx"+std::to_string((int)_massdm)+"-"+_annstate+"-events.dat";
      ofstream eventfile(eventfilename.c_str(),std::fstream::trunc);
      time_t rawtime;
      time(&rawtime);
      eventfile << "# DMann Herwig7 event file with particles printed out" << endl;
      eventfile << "# Created: " << ctime(&rawtime);
      eventfile << "# Number of simulated events: " << std::to_string(_nevt) << endl;
      eventfile << "# WIMP mass: " << std::to_string((int)_massdm) << " GeV" << endl;
      eventfile << "# Annihilation channel: " << _annstate << endl; 
      eventfile << "# " << endl;
      eventfile << setw(10) << left << "# PDG" 
                << setw(15) << left << "E [GeV]" 
                << setw(10) << left << "MotherPDG" << endl;
      eventfile.close();
    }
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

  /*static Parameter<DMannYields,long> interfaceyieldpdg //OBSOLETE
    ("YieldPDG",
     "PDG code of the yield particle of interest (gamma, e+ etc.)",
     &DMannYields::_yieldpdg, 0, 0, 0, 100000, 
     false, false, Interface::limited);    */

  static ParVector<DMannYields,long> interfacepdgvec
    ("ParticleCodes",
     "The PDG code for the particles",
     &DMannYields::_pdgvec,-1, 0l, -10000000l, 10000000l,
     false, false, Interface::limited);
     //0, 0, 0, -10000000, 10000000, false, false, Interface::nolimits);

  static Parameter<DMannYields,long> interfacenevt
    ("NEvent",
     "The number of events to simulate",
     &DMannYields::_nevt, 0, 0., 0., 100000000.0, 
     false, false, Interface::limited);    

  static Parameter<DMannYields,string> interfaceannstate
    ("AnnState",
     "The name of the annihilation state",
     &DMannYields::_annstate,"", 
     false, false);    

  static Parameter<DMannYields,string> interfaceoutdir
    ("OutDir",
     "The directory to put output files in, must exist already.",
     &DMannYields::_outdir,"Herwig7Data", 
     false, false);    

//  static Parameter<MatchboxFactory,string> interfacePoleData
//    ("PoleData",
//     "Prefix for subtraction check data.",
//     &MatchboxFactory::thePoleData, "",
//     false, false);    

  static ClassDocumentation<DMannYields> documentation
    ("There is no documentation for the DMannYields class");

}


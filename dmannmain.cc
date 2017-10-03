// dmannmain.cc is a modified copy of main07.cc in the PYTHIA8 examples
// directory. See below for description of that program.

// main07.cc is a part of the PYTHIA event generator.
// Copyright (C) 2017 Torbjorn Sjostrand.
// PYTHIA is licenced under the GNU GPL version 2, see COPYING for details.
// Please respect the MCnet Guidelines, see GUIDELINES for details.

// Illustration how to generate various two-body channels from
// astroparticle processes, e.g. neutralino annihilation or decay.
// To this end a "blob" of energy is created with unit cross section,
// from the fictitious collision of two non-radiating incoming e+e-.
// In the accompanying .cmnd file the decay channels of this
// blob can be set up. Furthermore, only gamma, e+-, p/pbar and
// neutrinos are stable, everything else is set to decay.
// (The "single-particle gun" of main21.cc offers another possible
// approach to the same problem.)

// Stdlib header file for input and output.
#include <iostream>

// Header file to access Pythia 8 program elements.
#include "Pythia8/Pythia.h"
#include "Pythia8/ParticleDecays.h"
#include "Pythia8/ParticleData.h"

// ROOT, for histogramming.
#include "TH1.h"

// ROOT, for interactive graphics.
#include "TVirtualPad.h"
#include "TApplication.h"

// ROOT, for saving file.
#include "TFile.h"

using namespace Pythia8;

//==========================================================================

// A derived class for (e+ e- ->) GenericResonance -> various final states.

class Sigma1GenRes : public Sigma1Process {

public:

  // Constructor.
  Sigma1GenRes() {}

  // Evaluate sigmaHat(sHat): dummy unit cross section.
  virtual double sigmaHat() {return 1.;}

  // Select flavour. No colour or anticolour.
  virtual void setIdColAcol() {setId( -11, 11, 999999);
    setColAcol( 0, 0, 0, 0, 0, 0);}

  // Info on the subprocess.
  virtual string name()    const {return "GenericResonance";}
  virtual int    code()    const {return 9001;}
  virtual string inFlux()  const {return "ffbarSame";}

};

//==========================================================================

// A macro to make txt-files from ROOT TH1 histograms, modified from example 
// at https://root-forum.cern.ch/t/histogram-to-ascii/14080/5
void h12ascii (TH1* h, string filename) {
  ofstream outputfile;
  outputfile.open (filename);
  Int_t n = h->GetNbinsX();
  for (Int_t i=1; i<=n; i++) {
      outputfile << h->GetBinLowEdge(i)+h->GetBinWidth(i)/2;
      outputfile << "\t";
      outputfile << h->GetBinContent(i);
      outputfile << "\n";
  }
  outputfile.close();
}

//==========================================================================

// A macro to make it possible with log scale  in the histograms
// From https://root.cern.ch/root/roottalk/roottalk06/1213.html
void BinLogX(TH1*h) 
{

   TAxis *axis = h->GetXaxis(); 
   int bins = axis->GetNbins();

   Axis_t from = axis->GetXmin();
   Axis_t to = axis->GetXmax();
   Axis_t width = (to - from) / bins;
   Axis_t *new_bins = new Axis_t[bins + 1];

   for (int i = 0; i <= bins; i++) {
     new_bins[i] = pow(10, from + i * width);
   } 
   axis->Set(bins, new_bins); 
   delete new_bins; 
}

//==========================================================================
//Main program
int main(int argc, char* argv[]) {

  // Check that correct number of command-line arguments
  if (argc != 2) {
    cerr << " Unexpected number of command-line arguments. \n"
         << " You are expected to provide a file name and nothing else. \n"
         << " Program stopped! " << endl;
    return 1;
  }

  // Check that the provided file name corresponds to an existing file.
  ifstream is(argv[1]);
  if (!is) {
    cerr << " Command-line file " << argv[1] << " was not found. \n"
         << " Program stopped! " << endl;
    return 1;
  }

  // Confirm that external file will be used for settings..
  cout << " PYTHIA settings will be read from file " << argv[1] << endl;

  // A class to generate the fictitious resonance initial state.
  SigmaProcess* sigma1GenRes = new Sigma1GenRes();
  
  // Pythia generator.
  Pythia pythia;
  
  // Read in file from command line argument
  pythia.readFile(argv[1]);
//  pythia.readFile("dmannmain1.cmnd");
//  pythia.readFile("eg-m250-ch91-int91.cmnd");  
  
  // Create the ROOT application environment.
  TApplication theApp("hist", &argc, argv);

  // Hand pointer to Pythia.
  pythia.setSigmaPtr( sigma1GenRes);
    
  // Initialization.
  pythia.init();

  // Extract settings to be used in the main program.
  int nEvent  = pythia.mode("Main:numberOfEvents");
  int nAbort  = pythia.mode("Main:timesAllowErrors");
  double mX = 0.5*pythia.parm("Beams:eCM"); // WIMP mass
  //The following is a method to find the particle ID of the first decay product
  const DecayChannel& channel = pythia.particleData.particleDataEntryPtr(999999)->channel(0);
  int ch = channel.product(0); // ID of decay product;
//  int dcode = channel.product(0); // ID of decay product
//  if ( dcode == 5 || dcode == -5 )  ch = 91;  // b bbar
//  else if ( dcode == 24 || dcode == -24 )  ch = 92; // W+W-
//  else if ( dcode == 15 || dcode == -15 )  ch = 93; // tau-tau+
//  else if ( dcode == 6 || dcode == -6 )  ch = 94; // t tbar
//  else {
//    cout << "Error: Could not find decay product in prescribed list.";
//    return 1;
//  }
  
  // Create file where histogram can be saved and book histogram itself
//  TFile* outFile = new TFile("plot/eGa.root", "RECREATE");
  TH1F *eGamma = new TH1F("eGamma","Photon energy divided by WIMP mass", 250, -10, 0);
  TH1F *ePos = new TH1F("ePos","Positron energy divided by WIMP mass", 250, -10, 0);
  TH1F *ePbar = new TH1F("ePbar","Antiproton energy divided by WIMP mass", 250, -10, 0);
  TH1F *eNumu = new TH1F("eNumu","Muon neutrino energy divided by WIMP mass", 250, -10, 0);      
  BinLogX(eGamma);
  BinLogX(ePos);
  BinLogX(ePbar);
  BinLogX(eNumu);      
  
  // Histogram particle spectra.
//  Hist eGamma("energy spectrum of photons",        100, 0., 100.);
//  Hist eE(    "energy spectrum of e+ and e-",      100, 0., 100.);
//  Hist eP(    "energy spectrum of p and pbar",     100, 0., 100.);
//  Hist eNu(   "energy spectrum of neutrinos",      100, 0., 100.);
//  Hist eRest( "energy spectrum of rest particles", 100, 0., 100.);

  // Begin event loop.
  int iAbort = 0;
  for (int iEvent = 0; iEvent < nEvent; ++iEvent) {

    // Generate events. Quit if many failures.
    if (!pythia.next()) {
      if (++iAbort < nAbort) continue;
      cout << " Event generation aborted prematurely, owing to error!\n";
      break;
    }

    // Loop over all particles and analyze the final-state ones.
    for (int i = 0; i < pythia.event.size(); ++i) {
      if (pythia.event[i].isFinal()) {
        int id = pythia.event[i].id();
        int idAbs = pythia.event[i].idAbs();      
        double eI = pythia.event[i].e();
        // Fill histograms with weight 1/nEvent to get dN/dx
        if (id == 22) eGamma->Fill(eI/mX,1./nEvent); 
        else if (id == -11) ePos->Fill(eI/mX,1./nEvent); 
        else if (id == -2212) ePbar->Fill(eI/mX,1./nEvent); 
        else if (idAbs == 14) eNumu->Fill(eI/mX,1./nEvent); 
//      else {
//        eRest.fill(eI);
//        cout << " Error: stable id = " << pythia.event[i].id() << endl;
//      }
      }
    }

  // End of event loop.
  }
  
//  eGamma->Draw();
//  std::cout << "\nDouble click on the histogram window to quit.\n";
//  gPad->WaitPrimitive();

  // Save histogram on file and close file.
//  eGam->Write();
//  delete outFile;
  
  // Dump TH1 data in a text file with function h12ascii (from above)
  int yieldcodes [] = {22, -11, -2212, 14};
  int yieldpdg;
  int length = sizeof(yieldcodes)/sizeof(yieldcodes[0]); //The length of the yieldcodes array
  for (int i = 0; i < length; ++i) {
    yieldpdg = yieldcodes[i];
    string filename = "pythia8data/da-mx"+std::to_string((int)mX)+"-ch"+std::to_string(ch)+"-int"+std::to_string(yieldpdg)+".dat";
    if (i == 0) h12ascii(eGamma,filename);
    else if (i == 1) h12ascii(ePos,filename);
    else if (i == 2) h12ascii(ePbar,filename);
    else if (i == 3) h12ascii(eNumu,filename);        
  }
//  for (int i = 91; i < 95; ++i) {
//    string filename = "pythia8data/da-mx"+std::to_string((int)mX)+"-ch"+std::to_string(ch)+"-int"+std::to_string(i)+".dat";
//    if (i == 91) h12ascii(eGamma,filename);
//    else if (i == 92) h12ascii(ePos,filename);
//    else if (i == 93) h12ascii(ePbar,filename);
//    else if (i == 94) h12ascii(eNumu,filename);        
//  }  
  
  
//  // Save histograms to two column data files
//  eGamma.table("plot/eGamma.dat");
//  eE.table("plot/eE.dat");  
//  eP.table("plot/eP.dat");
//  eNu.table("plot/eNu.dat");
//  eRest.table("plot/eRest.dat");    
    
  // Final statistics and histograms.
  pythia.stat();
//  cout << eGamma << eE << eP << eNu << eRest;

  // Done.
  delete sigma1GenRes;
  return 0;
}

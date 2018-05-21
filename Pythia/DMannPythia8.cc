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

// Date and time (for headers in output files)
#include <time.h>

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
void h12ascii (TH1* h, double mX, int ch, int yieldpdg, int nEvent) {
  ofstream outputfile;
  string filename = "Pythia8Data/da-pyt8-mx"+std::to_string((int)mX)+"-ch"+std::to_string(ch)+"-int"+std::to_string(yieldpdg)+".dat";  
  outputfile.open (filename);
  // Header of file
//  outputfile << "# DMann data file with dN/dE_kin as function of x=E_kin/mX=(E-m)/mX\n";
  outputfile << "# DMann Pythia8 data file with counts/nAnn as function of E_kin\n";  
  time_t rawtime;
  time(&rawtime);
  outputfile << "# Created: " << ctime(&rawtime);
  outputfile << "# Number of simulated events: " << std::to_string(nEvent) << "\n";
  outputfile << "# WIMP mass: " << std::to_string((int)mX) << " GeV\n";
  outputfile << "# PDG code of annihilation channel: " << std::to_string(ch) << "\n";
  outputfile << "# PDG code of yield particle: " << std::to_string(yieldpdg) << "\n";   
  outputfile << "# \n";
//  outputfile << "# x\tdN/dE\n";
  outputfile << "# E\t\tcounts/nAnn\n";  
  // Print histogram data to file
  Int_t n = h->GetNbinsX();
  for (Int_t i=1; i<=n; i++) {
      outputfile << h->GetBinLowEdge(i)+h->GetBinWidth(i)/2;
      outputfile << "\t\t";
      outputfile << h->GetBinContent(i)/nEvent; //CN divide by Nevent here ??
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
  
  // Read in file from command line argument (read file name.cmnd with pythia.readFile("name.cmnd"))
  pythia.readFile(argv[1]);
  
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

  // Define the PDG codes of the final state particles to be histogrammed (yield particles)
  // NOTE: ADD/REMOVE HERE IF YOU WANT TO INCLUDE MORE/FEWER FINAL STATE PARTICLES
  vector<long> yieldpdgs;
  //yieldpdgs.push_back(-11l);  // e+
  //yieldpdgs.push_back(22l);   // gamma
  //yieldpdgs.push_back(-2212l);// pbar
  yieldpdgs.push_back(-14l);  // numubar
  yieldpdgs.push_back(14l);   // numu
  
  // Construct ROOT TH1F histogram for each yield particle with 250 logarithmic bins from mX*10^-10 to mX (25 bins per decade)
  map<long,TH1F*> histograms;
  for (std::vector<long>::iterator idPtr = yieldpdgs.begin(); 
        idPtr != yieldpdgs.end(); ++idPtr) {
      string histoname = std::to_string(*idPtr);
      string histotitle = "Kinetic energy for yield PDG "+std::to_string(*idPtr);
      TH1F * histo = new TH1F(histoname.c_str(),
                      histotitle.c_str(), 
                      250, -10+log10(mX), 0+log10(mX));
      
      histograms.insert(make_pair((*idPtr), histo));    
      BinLogX(histograms[*idPtr]); 
  }
   
  double me = 0.000511; // electron mass
  double mp = 0.938; // proton mass
  
  TH1F * histoTheta = new TH1F("histoTheta",
                      "Cos(theta) distribution of neutrino", 
                      50, -1.0, 1.0);
  
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
        double eID = pythia.event[i].e(); // total energy of particle 
        double mID = pythia.event[i].m0(); // particle mass       
        double cTh = pythia.event[i].pz()/eID; // cos(th) of (massless) particle
        // Fill histograms with E_kin = E - m. CN With weight 1/nEvent to get dN/dx??
        for (std::vector<long>::iterator idPtr = yieldpdgs.begin(); 
              idPtr != yieldpdgs.end(); ++idPtr) {
          if ( id==(*idPtr) ) {
            histograms[*idPtr]->Fill(eID-mID);
            if (id == 14) {
              histoTheta->Fill(cTh);
            }
          }
        }
      }
    }

  // End of event loop.
  }
  
//  eGamma->Draw();
//  std::cout << "\nDouble click on the histogram window to quit.\n";
//  gPad->WaitPrimitive();

  // Save histograms on files and close files.
  for (std::vector<long>::iterator idPtr = yieldpdgs.begin(); 
        idPtr != yieldpdgs.end(); ++idPtr) {
    string fName = "yieldpdg_"+std::to_string(*idPtr)+".root";
    TFile* outFile = new TFile(fName.c_str(), "RECREATE");
    histograms[(*idPtr)]->Write();
    delete outFile;    
    h12ascii(histograms[(*idPtr)],mX,ch,(*idPtr),nEvent);
  }
  
  //Save cos theta histogram to file
  ofstream outputfile;
  string filename = "da-pyt8-mx"+std::to_string((int)mX)+"-ch"+std::to_string(ch)+"-int"+std::to_string(14)+"-costh.dat";  
  outputfile.open (filename);
  // Header of file
//  outputfile << "# DMann data file with dN/dE_kin as function of x=E_kin/mX=(E-m)/mX\n";
  outputfile << "# DMann Pythia8 data file with counts/nAnn as function of cos theta for nu_mu\n";  
  time_t rawtime;
  time(&rawtime);
  outputfile << "# Created: " << ctime(&rawtime);
  outputfile << "# Number of simulated events: " << std::to_string(nEvent) << "\n";
  outputfile << "# WIMP mass: " << std::to_string((int)mX) << " GeV\n";
  outputfile << "# PDG code of annihilation channel: " << std::to_string(ch) << "\n";
  outputfile << "# \n";
//  outputfile << "# x\tdN/dE\n";
  outputfile << "# cosTh\t\tcounts/nAnn\n";  
  // Print histogram data to file
  Int_t n = histoTheta->GetNbinsX();
  for (Int_t i=1; i<=n; i++) {
      outputfile << histoTheta->GetBinLowEdge(i) + histoTheta->GetBinWidth(i)/2;
      outputfile << "\t\t";
      outputfile << histoTheta->GetBinContent(i)/nEvent; //CN divide by Nevent here ??
      outputfile << "\n";
  }
  outputfile.close();
  
  
  // Final statistics and histograms.
  pythia.stat();
  
  // Done.
  delete sigma1GenRes;
  return 0;
}

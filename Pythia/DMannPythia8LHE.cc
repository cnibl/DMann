// A Pythia8 program that takes a LHEF as input and hadronises. 
// When called, the user should supply the path to the LHE file, a .cmnd-file with 
// Pythia settings and a directory where the output will be placed.

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

// A macro to make txt-files from ROOT TH1 histograms, modified from example 
// at https://root-forum.cern.ch/t/histogram-to-ascii/14080/5
void h12ascii (TH1* h, double mX, std::string annCh, int yieldpdg, int nEvent, std::string outDir) {
  ofstream outputfile;
  string filename;
  if (h->GetNbinsX() == 200) {
    filename = outDir + "/da-pyt8-mx" 
                    + std::to_string((int)mX) 
                    + "-" + annCh 
                    + "-y" + std::to_string(yieldpdg) 
                    + ".dat";  
  }
  else {
    filename = outDir + "/da-pyt8-mx" 
                    + std::to_string((int)mX) 
                    + "-" + annCh 
                    + "-y" + std::to_string(yieldpdg) 
                    + "-log.dat";  
  }
  cout << filename << endl;
  outputfile.open (filename);

  // Header of file
  //  outputfile << "# DMann data file with dN/dE_kin as function of x=E_kin/mX=(E-m)/mX\n";
  outputfile << "# DMann Pythia8 data file with counts/nAnn as function of E_kin\n";  
  time_t rawtime;
  time(&rawtime);
  outputfile << "# Created: " << ctime(&rawtime);
  outputfile << "# Number of simulated events: " << std::to_string(nEvent) << "\n";
  outputfile << "# WIMP mass: " << std::to_string((int)mX) << " GeV\n";
  outputfile << "# Annihilation channel: " << annCh << "\n";
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
  if (argc != 5) {
    cerr << " Unexpected number of command-line arguments. \n"
         << " You are expected to provide \n" 
         << " 1. Input cmnd-file for settings \n"
         << " 2. Path to input LHE file \n"
         << " 3. Annihilation channel \n"
         << " 4. Output folder \n"
         << " Program stopped! " << endl;
    return 1;
  }

  // Check that the provided file names and folder correspond to existing files/folder.
  for (int i = 0; i <= 2; i++) {
    ifstream is(argv[i]);
    if (!is) {
      cerr << " Command-line file " << argv[i] << " was not found. \n"
           << " Program stopped! " << endl;
      return 1;
    }
  }
  
  // Pythia generator.
  Pythia pythia;
  
  // Input parameters:
  //  1. Input cmnd-file for settings
  //  2. Path to input LHE file
  //  3. Annihilation channel 
  //  4. Output folder
  string settingsFile = string(argv[1]);
  string LHEpath = string(argv[2]);
  string annCh = string(argv[3]);
  string outDir = string(argv[4]);

  // Confirm files to use
  cout << " PYTHIA settings will be read from file " << settingsFile << endl;
  cout << " PYTHIA will hadronise LHE file " << LHEpath << endl;
  cout << " Output will be placed in folder " << outDir << endl;

  // Read in ME configurations
  pythia.readString("Beams:frameType = 4");
  pythia.readString("Beams:LHEF = " + LHEpath);

  pythia.readFile(settingsFile); // read Pythia settings
    
  pythia.init();
  
  // Create the ROOT application environment.
  TApplication theApp("hist", &argc, argv);

  // Initialization.
  pythia.init();
  cout << " PYTHIA initialised. " << endl;
  
  // Extract settings to be used in the main program.
  int nEvent  = pythia.mode("Main:numberOfEvents");
  int nAbort  = pythia.mode("Main:timesAllowErrors");
  double mX = 0.5*pythia.particleData.m0(9000006); // WIMP mass
  //The following is a method to find the particle ID of the first decay product (does not work with LHE)
  //const DecayChannel& channel = pythia.particleData.particleDataEntryPtr(9000006)->channel(0);
  //int ch = channel.product(0); // ID of decay product;
  cout << "mWIMP = " << mX << endl;
  cout << "nEvents = " << nEvent << endl;
  cout << "Decay channel = " << annCh << endl;
  
  // Define the PDG codes of the final state particles to be histogrammed (yield particles)
  // NOTE: ADD/REMOVE HERE IF YOU WANT TO INCLUDE MORE/FEWER FINAL STATE PARTICLES
  vector<long> yieldpdgs;
  yieldpdgs.push_back(-11l);  // e+
  yieldpdgs.push_back(22l);   // gamma
  yieldpdgs.push_back(-2212l);// pbar
  yieldpdgs.push_back(-14l);  // numubar
  yieldpdgs.push_back(14l);   // numu
  
  yieldpdgs.push_back(11l);   // e-
  yieldpdgs.push_back(-12l);  // nuebar
  yieldpdgs.push_back(12l);   // nue
  yieldpdgs.push_back(-16l);  // nutaubar
  yieldpdgs.push_back(16l);   // nutau
  
  // Construct ROOT TH1F histogram for each yield particle with 250 logarithmic bins from mX*10^-10 to mX (25 bins per decade)
  map<long,TH1F*> histograms;
  map<long,TH1F*> histogramslog;
  for (std::vector<long>::iterator idPtr = yieldpdgs.begin(); 
        idPtr != yieldpdgs.end(); ++idPtr) {
      string histoname = std::to_string(*idPtr);
      string histotitle = "Kinetic energy for yield PDG " + std::to_string(*idPtr);
      TH1F * histo = new TH1F(histoname.c_str(),
                              histotitle.c_str(), 
                              200, 0., mX);
      histograms.insert(make_pair((*idPtr), histo));     

      string histonamelog = std::to_string(*idPtr)+"_log";
      string histotitlelog = "Kinetic energy for yield PDG " + std::to_string(*idPtr);
      TH1F * histolog = new TH1F(histonamelog.c_str(),
                      histotitlelog.c_str(), 
                      250, -10+log10(mX), 0+log10(mX));
      histogramslog.insert(make_pair((*idPtr), histolog));    
      BinLogX(histogramslog[*idPtr]); 
      
  }
  
  string eventFileName = outDir+"/da-pyt8-mx"+std::to_string((int)mX)+"-"+annCh+"-events.dat";
  ofstream eventFile(eventFileName.c_str(),std::fstream::trunc);
  time_t rawtime;
  time(&rawtime);
  eventFile << "# DMann Pythia8 event file with particles printed out" << endl;
  eventFile << "# Created: " << ctime(&rawtime);
  eventFile << "# Number of simulated events: " << std::to_string(nEvent) << endl;
  eventFile << "# WIMP mass: " << std::to_string((int)mX) << " GeV" << endl;
  eventFile << "# Annihilation channel: " << annCh << endl; 
  eventFile << "# " << endl;
  eventFile << setw(10) << left << "# PDG" 
            << setw(15) << left << "E [GeV]" 
            << setw(10) << left << "MotherPDG" << endl;
  eventFile.close();
  

  // Begin event loop.
  int iAbort = 0;
  for (int iEvent = 0; iEvent < nEvent ; ++iEvent ) {
    
//    double scale = mX/2.;
//    pythia.forceTimeShower( 1, 3, 100.);
    
    // Generate events. 
    if (!pythia.next()) {

      //pythia.event.list();

      // Quit if many failures.
      if (++iAbort < nAbort) continue;
      cout << " iEvent = " << iEvent << endl;
      cout << " Event generation aborted prematurely, owing to error!\n";
      break;
      
      
      // If failure because reached end of file then exit event loop.
      if (pythia.info.atEndOfFile()) break;
    }
    
    string eventFileName = outDir+"/da-pyt8-mx"+std::to_string((int)mX)+"-"+annCh+"-events.dat";
    ofstream eventFile(eventFileName.c_str(),std::fstream::app);
    int nEvtCur = iEvent + 1;
    eventFile << "# Event " << nEvtCur << endl;

    // Loop over all particles and analyze the final-state ones.
    for (int i = 0; i < pythia.event.size(); ++i) {
      if (pythia.event[i].isFinal()) {
        int id = pythia.event[i].id();
        int idAbs = pythia.event[i].idAbs();      
        double eID = pythia.event[i].e(); // total energy of particle 
        double mID = pythia.event[i].m0(); // particle mass       
        // Fill histograms with E_kin = E - m. CN With weight 1/nEvent to get dN/dx??
        for (std::vector<long>::iterator idPtr = yieldpdgs.begin(); 
              idPtr != yieldpdgs.end(); ++idPtr) {
          if ( (*idPtr)==pythia.event[i].id() ) {
            histograms[*idPtr]->Fill(eID-mID);
            histogramslog[*idPtr]->Fill(eID-mID);
            int mother = pythia.event[i].mother1();
            eventFile << setw(10) << left << pythia.event[i].id()
                      << setw(15) << left << std::scientific << eID
                      << setw(10) << left << pythia.event[mother].id() << endl;
          }
        }
      }
    }
    // End of event loop.
    eventFile.close();
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
    h12ascii(histograms[(*idPtr)],mX,annCh,(*idPtr),nEvent,outDir);
    h12ascii(histogramslog[(*idPtr)],mX,annCh,(*idPtr),nEvent,outDir);
  }

  ofstream eventFileEnd(eventFileName.c_str(),std::fstream::app);
  eventFileEnd << "#END" << endl;
  eventFileEnd.close();
  
  // Final statistics and histograms.
  pythia.stat();
  
  // Done.
  return 0;
}

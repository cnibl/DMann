
// -*- C++ -*-
#ifndef DMann_DMannYields_H
#define DMann_DMannYields_H
//
// This is the declaration of the DMannYields class.


#include "ThePEG/Handlers/AnalysisHandler.h"
#include "Herwig/Utilities/Histogram.h"

#include "ThePEG/EventRecord/Event.h"
#include "ThePEG/EventRecord/Particle.h"
#include "ThePEG/EventRecord/StandardSelectors.h"

//#include "TH1F.h"
//#include "TFile.h"
//#include "TCanvas.h"


namespace DMann {

using namespace ThePEG;

/**
 * Here is the documentation of the DMannYields class.
 *
 * @see \ref DMannYieldsInterfaces "The interfaces"
 * defined for DMannYields.
 */
class DMannYields: public AnalysisHandler {

public:

  /** @name Standard constructors and destructors. */
  //@{
  /**
   * The default constructor.
   */
  DMannYields();

  /**
   * The destructor.
   */
  virtual ~DMannYields();
  //@}

public:


  /** @name Virtual functions required by the AnalysisHandler class. */
  //@{
  /**
   * Analyze a given Event. Note that a fully generated event
   * may be presented several times, if it has been manipulated in
   * between. The default version of this function will call transform
   * to make a lorentz transformation of the whole event, then extract
   * all final state particles and call analyze(tPVector) of this
   * analysis object and those of all associated analysis objects. The
   * default version will not, however, do anything on events which
   * have not been fully generated, or have been manipulated in any
   * way.
   * @param event pointer to the Event to be analyzed.
   * @param ieve the event number.
   * @param loop the number of times this event has been presented.
   * If negative the event is now fully generated.
   * @param state a number different from zero if the event has been
   * manipulated in some way since it was last presented.
   */
  virtual void analyze(tEventPtr event, long ieve, int loop, int state);

  /**
   * Return a LorentzTransform which would put the event in the
   * desired Lorentz frame.
   * @param event a pointer to the Event to be considered.
   * @return the LorentzRotation used in the transformation.
   */
  virtual LorentzRotation transform(tcEventPtr event) const;

  /**
   * Analyze the given vector of particles. The default version calls
   * analyze(tPPtr) for each of the particles.
   * @param particles the vector of pointers to particles to be analyzed
   * @param weight the weight of the current event.
   */
  virtual void analyze(const tPVector & particles, double weight);

  /**
   * Analyze the given particle.
   * @param particle pointer to the particle to be analyzed.
   * @param weight the weight of the current event.
   */
  virtual void analyze(tPPtr particle, double weight);
  //@}

protected:

  /**
   * Initialize this object. Called in the run phase just before
   * a run begins.
   */
  virtual void doinitrun();

  /**
   * Finalize this object. Called in the run phase just after a
   * run has ended. Used eg. to write out statistics.
   */
  virtual void dofinish();


public:

  /** @name Functions used by the persistent I/O system. */
  //@{
  /**
   * Function used to write out object persistently.
   * @param os the persistent output stream written to.
   */
  void persistentOutput(PersistentOStream & os) const;

  /**
   * Function used to read in object persistently.
   * @param is the persistent input stream read from.
   * @param version the version number of the object when written.
   */
  void persistentInput(PersistentIStream & is, int version);
  //@}
  
  /**
   * The standard Init function used to initialize the interfaces.
   * Called exactly once for each class by the class description system
   * before the main function starts or
   * when this class is dynamically loaded.
   */
  static void Init();

protected:

  /** @name Clone Methods. */
  //@{
  /**
   * Make a simple clone of this object.
   * @return a pointer to the new object.
   */
  virtual IBPtr clone() const;

  /** Make a clone of this object, possibly modifying the cloned object
   * to make it sane.
   * @return a pointer to the new object.
   */
  virtual IBPtr fullclone() const;
  //@}


// If needed, insert declarations of virtual function defined in the
// InterfacedBase class here (using ThePEG-interfaced-decl in Emacs).

//private:
///**
//* A pointer to a Root histogram
//*/
//  TH1F* histo;

public:
  static string library();

private:
  /**
   * The static object used to initialize the description of this class.
   * Indicates that this is a concrete class with persistent data.
   */
  static ClassDescription<DMannYields> initDMannYields;

  /**
   * The assignment operator is private and must never be called.
   * In fact, it should not even be implemented.
   */
  DMannYields & operator=(const DMannYields &);

private:

  /**
   *  The histograms of dN/dE
   *  (the int is the PDG id)
   */
  map<long,Herwig::Histogram> _histograms;
  map<long,Herwig::Histogram> _histogramslog;
  //map<long,TH1F*> _histogramsROOT;

  /**
   *  The PDG code of the yield particle
   */
  long _yieldpdg;

  /**
   *  The WIMP mass
   */
  double _massdm;

  /**
   *  The PDG codes of the yield particles
   */
  vector<long> _pdgvec;
  
  /**
   *  Absolute value of PDG code of the 
   *  final state (i.e. DM ann. channel)
   */
  long _annpdg;

  /**
   *  The name of the final state
   */
  string _annstate;
  
  /**
   *  The name of the output directory
   */
  string _outdir;

  /**
   *  Number of simulated events
   */
  long _nevt;

};

}

#endif /* DMann_DMannYields_H */

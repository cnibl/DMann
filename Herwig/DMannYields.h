
// -*- C++ -*-
#ifndef DMann_DMannYields_H
#define DMann_DMannYields_H
//
// This is the declaration of the DMannYields class.
//
//#include "TH1F.h"
//#include "TCanvas.h"

#include "ThePEG/Handlers/AnalysisHandler.h"
#include "ThePEG/EventRecord/Event.h"
#include "ThePEG/EventRecord/Particle.h"
#include "ThePEG/Repository/Repository.h"
#include "ThePEG/PDT/ParticleData.h"
#include "ThePEG/EventRecord/StandardSelectors.h"

#include "Herwig/Utilities/Histogram.h"

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

  Herwig::Histogram histo;

  /**
   *  The PDG codes of the particles
   */
  vector<long> _particlecodes;

  /**
   * The multiplcity
   */
  vector<double> _multiplicity;

  /**
   * The error
   */
  vector<double> _error;

  /**
   * Species of particle
   */
  vector<unsigned int> _species;


 /// Histograms for cluster mass dependence
 map<long,Herwig::Histogram> _histograms;

 /**
  *  Histograms of the clusters after cluster splitting
  */
 map<int,Herwig::Histogram> _clusters;

 /**
  *  Histograms of the primary clusters
  */
 map<int,Herwig::Histogram> _primary;

  /**
   *  Map of number of final-state particles to PDG code
   */
  map<long,long> _finalstatecount;

  /**
   *  Particles in hard process
   */
  map<long,long> _collisioncount;

  /// Make histograms of cluster mass dependence
  bool _makeHistograms;


};

}


#endif /* DMann_DMannYields_H */

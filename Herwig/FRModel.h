// -*- C++ -*-
//
// FRModel.h is a part of Herwig - A multi-purpose Monte Carlo event generator
// Copyright (C) 2002-2013 The Herwig Collaboration
//
// Herwig is licenced under version 2 of the GPL, see COPYING for details.
// Please respect the MCnet academic guidelines, see GUIDELINES for details.
//
#ifndef HERWIG_FRModel_H
#define HERWIG_FRModel_H

// This is the declaration of the FRModel class.
#include "Herwig/Models/General/BSMModel.h"

namespace Herwig {
using namespace ThePEG;
using ThePEG::Constants::pi;

const Complex ii = Complex(0,1);

/** \ingroup Models
 *  
 *  This is the Herwig FRModel class which inherits from ThePEG 
 *  FeynRules Model class and implements additional FeynRules Model couplings, 
 *  access to vertices for helicity amplitude calculations etc.
 *
 *  @see BSMModel
 */
class FRModel: public BSMModel {

public:
  /// Default constructor
  FRModel();

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
   * Write out a UFO param_card.dat that matches the configured values
   */
  void writeParamCard() const;

  /**
   * Standard Init function used to initialize the interfaces.
   */
  static void Init();

protected:
  virtual bool registerDefaultVertices() const { return false; }

public:

  /**
   * Pointers to the objects handling the vertices.
   */
  //@{


  double ZERO() const { return ZERO_; }
  double cabi() const { return cabi_; }
  double gSf() const { return gSf_; }
  double Lambda() const { return Lambda_; }
  double gSEW() const { return gSEW_; }
  double gPg() const { return gPg_; }
  double aEWM1() const { return aEWM1_; }
  double Gf() const { return Gf_; }
  double aS() const { return aS_; }
  double ymdo() const { return ymdo_; }
  double ymup() const { return ymup_; }
  double yms() const { return yms_; }
  double ymc() const { return ymc_; }
  double ymb() const { return ymb_; }
  double ymt() const { return ymt_; }
  double yme() const { return yme_; }
  double ymm() const { return ymm_; }
  double ymtau() const { return ymtau_; }
  double MZ() const { return MZ_; }
  double Me() const { return Me_; }
  double MMU() const { return MMU_; }
  double MTA() const { return MTA_; }
  double MU() const { return MU_; }
  double MC() const { return MC_; }
  double MT() const { return MT_; }
  double MD() const { return MD_; }
  double MS() const { return MS_; }
  double MB() const { return MB_; }
  double MH() const { return MH_; }
  double MGR() const { return MGR_; }
  double WZ() const { return WZ_; }
  double WW() const { return WW_; }
  double WT() const { return WT_; }
  double WH() const { return WH_; }
  double WGR() const { return WGR_; }
  double aEW() const { return aEW_; }
  double G() const { return G_; }
  Complex CKM1x1() const { return CKM1x1_; }
  Complex CKM1x2() const { return CKM1x2_; }
  Complex CKM1x3() const { return CKM1x3_; }
  Complex CKM2x1() const { return CKM2x1_; }
  Complex CKM2x2() const { return CKM2x2_; }
  Complex CKM2x3() const { return CKM2x3_; }
  Complex CKM3x1() const { return CKM3x1_; }
  Complex CKM3x2() const { return CKM3x2_; }
  Complex CKM3x3() const { return CKM3x3_; }
  double MW() const { return MW_; }
  double ee() const { return ee_; }
  double sw2() const { return sw2_; }
  double cw() const { return cw_; }
  double sw() const { return sw_; }
  double g1() const { return g1_; }
  double gw() const { return gw_; }
  double vev() const { return vev_; }
  double lam() const { return lam_; }
  double yb() const { return yb_; }
  double yc() const { return yc_; }
  double ydo() const { return ydo_; }
  double ye() const { return ye_; }
  double ym() const { return ym_; }
  double ys() const { return ys_; }
  double yt() const { return yt_; }
  double ytau() const { return ytau_; }
  double yup() const { return yup_; }
  double muH() const { return muH_; }
  Complex I1b11() const { return I1b11_; }
  Complex I1b12() const { return I1b12_; }
  Complex I1b13() const { return I1b13_; }
  Complex I1b21() const { return I1b21_; }
  Complex I1b22() const { return I1b22_; }
  Complex I1b23() const { return I1b23_; }
  Complex I1b31() const { return I1b31_; }
  Complex I1b32() const { return I1b32_; }
  Complex I1b33() const { return I1b33_; }
  Complex I2b11() const { return I2b11_; }
  Complex I2b12() const { return I2b12_; }
  Complex I2b13() const { return I2b13_; }
  Complex I2b21() const { return I2b21_; }
  Complex I2b22() const { return I2b22_; }
  Complex I2b23() const { return I2b23_; }
  Complex I2b31() const { return I2b31_; }
  Complex I2b32() const { return I2b32_; }
  Complex I2b33() const { return I2b33_; }
  Complex I3b11() const { return I3b11_; }
  Complex I3b12() const { return I3b12_; }
  Complex I3b13() const { return I3b13_; }
  Complex I3b21() const { return I3b21_; }
  Complex I3b22() const { return I3b22_; }
  Complex I3b23() const { return I3b23_; }
  Complex I3b31() const { return I3b31_; }
  Complex I3b32() const { return I3b32_; }
  Complex I3b33() const { return I3b33_; }
  Complex I4b11() const { return I4b11_; }
  Complex I4b12() const { return I4b12_; }
  Complex I4b13() const { return I4b13_; }
  Complex I4b21() const { return I4b21_; }
  Complex I4b22() const { return I4b22_; }
  Complex I4b23() const { return I4b23_; }
  Complex I4b31() const { return I4b31_; }
  Complex I4b32() const { return I4b32_; }
  Complex I4b33() const { return I4b33_; }

  //@}  
  
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
  
protected:

  /**
   * Initialize this object after the setup phase before saving and
   * EventGenerator to disk.
   * @throws InitException if object could not be initialized properly.
   */
  virtual void doinit();

  /**
   * Initialize this object. Called in the run phase just before
   * a run begins.
   */
  virtual void doinitrun();
  //@}

private:
  
  /** 
   * Private and non-existent assignment operator.
   */
  FRModel & operator=(const FRModel &);

private:

  /**
   *  Helper functions for doinit
   */
  //@{


  //@}
  
private:

  /**
   * Pointers to the vertices for FRModel Model helicity amplitude
   * calculations.
   */
  //@{


  double ZERO_;
  double cabi_;
  double gSf_;
  double Lambda_;
  double gSEW_;
  double gPg_;
  double aEWM1_;
  double Gf_;
  double aS_;
  double ymdo_;
  double ymup_;
  double yms_;
  double ymc_;
  double ymb_;
  double ymt_;
  double yme_;
  double ymm_;
  double ymtau_;
  double MZ_;
  double Me_;
  double MMU_;
  double MTA_;
  double MU_;
  double MC_;
  double MT_;
  double MD_;
  double MS_;
  double MB_;
  double MH_;
  double MGR_;
  double WZ_;
  double WW_;
  double WT_;
  double WH_;
  double WGR_;
  double aEW_;
  double G_;
  Complex CKM1x1_;
  Complex CKM1x2_;
  Complex CKM1x3_;
  Complex CKM2x1_;
  Complex CKM2x2_;
  Complex CKM2x3_;
  Complex CKM3x1_;
  Complex CKM3x2_;
  Complex CKM3x3_;
  double MW_;
  double ee_;
  double sw2_;
  double cw_;
  double sw_;
  double g1_;
  double gw_;
  double vev_;
  double lam_;
  double yb_;
  double yc_;
  double ydo_;
  double ye_;
  double ym_;
  double ys_;
  double yt_;
  double ytau_;
  double yup_;
  double muH_;
  Complex I1b11_;
  Complex I1b12_;
  Complex I1b13_;
  Complex I1b21_;
  Complex I1b22_;
  Complex I1b23_;
  Complex I1b31_;
  Complex I1b32_;
  Complex I1b33_;
  Complex I2b11_;
  Complex I2b12_;
  Complex I2b13_;
  Complex I2b21_;
  Complex I2b22_;
  Complex I2b23_;
  Complex I2b31_;
  Complex I2b32_;
  Complex I2b33_;
  Complex I3b11_;
  Complex I3b12_;
  Complex I3b13_;
  Complex I3b21_;
  Complex I3b22_;
  Complex I3b23_;
  Complex I3b31_;
  Complex I3b32_;
  Complex I3b33_;
  Complex I4b11_;
  Complex I4b12_;
  Complex I4b13_;
  Complex I4b21_;
  Complex I4b22_;
  Complex I4b23_;
  Complex I4b31_;
  Complex I4b32_;
  Complex I4b33_;
  //@}
};

}

namespace ThePEG {
  ThePEG_DECLARE_POINTERS(Herwig::FRModel,HwFRModelPtr);
}


#endif /* HERWIG_FRModel_H */

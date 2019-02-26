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
  double gSh1() const { return gSh1_; }
  double gSh2() const { return gSh2_; }
  double gSWT() const { return gSWT_; }
  double gPWT() const { return gPWT_; }
  double gPBT() const { return gPBT_; }
  double gSBT() const { return gSBT_; }
  double gSWL() const { return gSWL_; }
  double gSBL() const { return gSBL_; }
  double gSg() const { return gSg_; }
  double gPg() const { return gPg_; }
  double gSd11() const { return gSd11_; }
  double gSu11() const { return gSu11_; }
  double gSd22() const { return gSd22_; }
  double gSu22() const { return gSu22_; }
  double gSd33() const { return gSd33_; }
  double gSu33() const { return gSu33_; }
  double gPd11() const { return gPd11_; }
  double gPu11() const { return gPu11_; }
  double gPd22() const { return gPd22_; }
  double gPu22() const { return gPu22_; }
  double gPd33() const { return gPd33_; }
  double gPu33() const { return gPu33_; }
  double gSe() const { return gSe_; }
  double gPe() const { return gPe_; }
  double gSmm() const { return gSmm_; }
  double gPmm() const { return gPmm_; }
  double gSta() const { return gSta_; }
  double gPta() const { return gPta_; }
  double gVd11() const { return gVd11_; }
  double gVu11() const { return gVu11_; }
  double gVd22() const { return gVd22_; }
  double gVu22() const { return gVu22_; }
  double gVd33() const { return gVd33_; }
  double gVu33() const { return gVu33_; }
  double gAd11() const { return gAd11_; }
  double gAu11() const { return gAu11_; }
  double gAd22() const { return gAd22_; }
  double gAu22() const { return gAu22_; }
  double gAd33() const { return gAd33_; }
  double gAu33() const { return gAu33_; }
  double gVe() const { return gVe_; }
  double gAe() const { return gAe_; }
  double gVmm() const { return gVmm_; }
  double gAmm() const { return gAmm_; }
  double gVta() const { return gVta_; }
  double gAta() const { return gAta_; }
  double gSXr() const { return gSXr_; }
  double gSXc() const { return gSXc_; }
  double gSXd() const { return gSXd_; }
  double gPXd() const { return gPXd_; }
  double gVXd() const { return gVXd_; }
  double gAXd() const { return gAXd_; }
  double Lambda() const { return Lambda_; }
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
  double MD0() const { return MD0_; }
  double MD1() const { return MD1_; }
  double MXr() const { return MXr_; }
  double MXc() const { return MXc_; }
  double MXd() const { return MXd_; }
  double WZ() const { return WZ_; }
  double WW() const { return WW_; }
  double WE() const { return WE_; }
  double WMU() const { return WMU_; }
  double WTA() const { return WTA_; }
  double WT() const { return WT_; }
  double WH() const { return WH_; }
  double WD0() const { return WD0_; }
  double WD1() const { return WD1_; }
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
  Complex I1a11() const { return I1a11_; }
  Complex I1a12() const { return I1a12_; }
  Complex I1a13() const { return I1a13_; }
  Complex I1a21() const { return I1a21_; }
  Complex I1a22() const { return I1a22_; }
  Complex I1a23() const { return I1a23_; }
  Complex I1a31() const { return I1a31_; }
  Complex I1a32() const { return I1a32_; }
  Complex I1a33() const { return I1a33_; }
  Complex I2a11() const { return I2a11_; }
  Complex I2a12() const { return I2a12_; }
  Complex I2a13() const { return I2a13_; }
  Complex I2a21() const { return I2a21_; }
  Complex I2a22() const { return I2a22_; }
  Complex I2a23() const { return I2a23_; }
  Complex I2a31() const { return I2a31_; }
  Complex I2a32() const { return I2a32_; }
  Complex I2a33() const { return I2a33_; }
  Complex I3a11() const { return I3a11_; }
  Complex I3a12() const { return I3a12_; }
  Complex I3a13() const { return I3a13_; }
  Complex I3a21() const { return I3a21_; }
  Complex I3a22() const { return I3a22_; }
  Complex I3a23() const { return I3a23_; }
  Complex I3a31() const { return I3a31_; }
  Complex I3a32() const { return I3a32_; }
  Complex I3a33() const { return I3a33_; }
  Complex I4a11() const { return I4a11_; }
  Complex I4a12() const { return I4a12_; }
  Complex I4a13() const { return I4a13_; }
  Complex I4a21() const { return I4a21_; }
  Complex I4a22() const { return I4a22_; }
  Complex I4a23() const { return I4a23_; }
  Complex I4a31() const { return I4a31_; }
  Complex I4a32() const { return I4a32_; }
  Complex I4a33() const { return I4a33_; }

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
  double gSh1_;
  double gSh2_;
  double gSWT_;
  double gPWT_;
  double gPBT_;
  double gSBT_;
  double gSWL_;
  double gSBL_;
  double gSg_;
  double gPg_;
  double gSd11_;
  double gSu11_;
  double gSd22_;
  double gSu22_;
  double gSd33_;
  double gSu33_;
  double gPd11_;
  double gPu11_;
  double gPd22_;
  double gPu22_;
  double gPd33_;
  double gPu33_;
  double gSe_;
  double gPe_;
  double gSmm_;
  double gPmm_;
  double gSta_;
  double gPta_;
  double gVd11_;
  double gVu11_;
  double gVd22_;
  double gVu22_;
  double gVd33_;
  double gVu33_;
  double gAd11_;
  double gAu11_;
  double gAd22_;
  double gAu22_;
  double gAd33_;
  double gAu33_;
  double gVe_;
  double gAe_;
  double gVmm_;
  double gAmm_;
  double gVta_;
  double gAta_;
  double gSXr_;
  double gSXc_;
  double gSXd_;
  double gPXd_;
  double gVXd_;
  double gAXd_;
  double Lambda_;
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
  double MD0_;
  double MD1_;
  double MXr_;
  double MXc_;
  double MXd_;
  double WZ_;
  double WW_;
  double WE_;
  double WMU_;
  double WTA_;
  double WT_;
  double WH_;
  double WD0_;
  double WD1_;
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
  Complex I1a11_;
  Complex I1a12_;
  Complex I1a13_;
  Complex I1a21_;
  Complex I1a22_;
  Complex I1a23_;
  Complex I1a31_;
  Complex I1a32_;
  Complex I1a33_;
  Complex I2a11_;
  Complex I2a12_;
  Complex I2a13_;
  Complex I2a21_;
  Complex I2a22_;
  Complex I2a23_;
  Complex I2a31_;
  Complex I2a32_;
  Complex I2a33_;
  Complex I3a11_;
  Complex I3a12_;
  Complex I3a13_;
  Complex I3a21_;
  Complex I3a22_;
  Complex I3a23_;
  Complex I3a31_;
  Complex I3a32_;
  Complex I3a33_;
  Complex I4a11_;
  Complex I4a12_;
  Complex I4a13_;
  Complex I4a21_;
  Complex I4a22_;
  Complex I4a23_;
  Complex I4a31_;
  Complex I4a32_;
  Complex I4a33_;
  //@}
};

}

namespace ThePEG {
  ThePEG_DECLARE_POINTERS(Herwig::FRModel,HwFRModelPtr);
}


#endif /* HERWIG_FRModel_H */

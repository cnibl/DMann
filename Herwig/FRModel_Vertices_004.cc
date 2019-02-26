// -*- C++ -*-
//
// FRModelV_V_100.cc is a part of Herwig - A multi-purpose Monte Carlo event generator
// Copyright (C) 2002-2007 The Herwig Collaboration
//
// Herwig is licenced under version 2 of the GPL, see COPYING for details.
// Please respect the MCnet academic guidelines, see GUIDELINES for details.

#include "FRModel.h"
#include "ThePEG/Helicity/Vertex/Scalar/FFSVertex.h"

#include "ThePEG/Utilities/DescribeClass.h"
#include "ThePEG/Persistency/PersistentOStream.h"
#include "ThePEG/Persistency/PersistentIStream.h"

namespace Herwig 
{
  using namespace ThePEG;
  using namespace ThePEG::Helicity;
  using ThePEG::Constants::pi;

  class FRModelV_V_76: public FFSVertex {
 public:
  FRModelV_V_76() {
    kinematics(false);
    addToList(-5,5,25);
  }
  void setCoupling(Energy2 ,tcPDPtr,tcPDPtr,tcPDPtr) {
    double yb = model_->yb();
    //    getParams(q2);
    norm(1.0);
    left(((((1.0*(-ii))*1.0)*1.0)*(-((ii*yb)/sqrt(2.0)))));
    right(((((1.0*(-ii))*1.0)*1.0)*(-((ii*yb)/sqrt(2.0)))));
    
  }
  void persistentOutput(PersistentOStream & os) const { os << model_; }
  void persistentInput(PersistentIStream & is, int) { is >> model_; }
  //  static void Init();
 protected:
  IBPtr clone() const { return new_ptr(*this); }
  IBPtr fullclone() const { return new_ptr(*this); }
  void doinit() {
    model_ = dynamic_ptr_cast<tcHwFRModelPtr>
	     (generator()->standardModel());
    assert(model_);
    //    getParams(q2);
    
    
    orderInGem(1);
    orderInGs(0);
    FFSVertex::doinit();
  }
  //    void getParams(Energy2);
 private:
  FRModelV_V_76 & operator=(const FRModelV_V_76 &);
  //    Complex leftval, rightval, normval;
  tcHwFRModelPtr model_;
};
DescribeClass<FRModelV_V_76,Helicity::FFSVertex>
describeHerwigFRModelV_V_76("Herwig::FRModelV_V_76",
				       "FRModel.so");
// void FRModelV_V_76::getParams(Energy2 ) {
// }

class FRModelV_V_83: public FFSVertex {
 public:
  FRModelV_V_83() {
    kinematics(false);
    addToList(-11,11,25);
  }
  void setCoupling(Energy2 ,tcPDPtr,tcPDPtr,tcPDPtr) {
    double ye = model_->ye();
    //    getParams(q2);
    norm(1.0);
    left(((((1.0*(-ii))*1.0)*1.0)*(-((ii*ye)/sqrt(2.0)))));
    right(((((1.0*(-ii))*1.0)*1.0)*(-((ii*ye)/sqrt(2.0)))));
    
  }
  void persistentOutput(PersistentOStream & os) const { os << model_; }
  void persistentInput(PersistentIStream & is, int) { is >> model_; }
  //  static void Init();
 protected:
  IBPtr clone() const { return new_ptr(*this); }
  IBPtr fullclone() const { return new_ptr(*this); }
  void doinit() {
    model_ = dynamic_ptr_cast<tcHwFRModelPtr>
	     (generator()->standardModel());
    assert(model_);
    //    getParams(q2);
    
    
    orderInGem(1);
    orderInGs(0);
    FFSVertex::doinit();
  }
  //    void getParams(Energy2);
 private:
  FRModelV_V_83 & operator=(const FRModelV_V_83 &);
  //    Complex leftval, rightval, normval;
  tcHwFRModelPtr model_;
};
DescribeClass<FRModelV_V_83,Helicity::FFSVertex>
describeHerwigFRModelV_V_83("Herwig::FRModelV_V_83",
				       "FRModel.so");
// void FRModelV_V_83::getParams(Energy2 ) {
// }

class FRModelV_V_84: public FFSVertex {
 public:
  FRModelV_V_84() {
    kinematics(false);
    addToList(-13,13,25);
  }
  void setCoupling(Energy2 ,tcPDPtr,tcPDPtr,tcPDPtr) {
    double ym = model_->ym();
    //    getParams(q2);
    norm(1.0);
    left(((((1.0*(-ii))*1.0)*1.0)*(-((ii*ym)/sqrt(2.0)))));
    right(((((1.0*(-ii))*1.0)*1.0)*(-((ii*ym)/sqrt(2.0)))));
    
  }
  void persistentOutput(PersistentOStream & os) const { os << model_; }
  void persistentInput(PersistentIStream & is, int) { is >> model_; }
  //  static void Init();
 protected:
  IBPtr clone() const { return new_ptr(*this); }
  IBPtr fullclone() const { return new_ptr(*this); }
  void doinit() {
    model_ = dynamic_ptr_cast<tcHwFRModelPtr>
	     (generator()->standardModel());
    assert(model_);
    //    getParams(q2);
    
    
    orderInGem(1);
    orderInGs(0);
    FFSVertex::doinit();
  }
  //    void getParams(Energy2);
 private:
  FRModelV_V_84 & operator=(const FRModelV_V_84 &);
  //    Complex leftval, rightval, normval;
  tcHwFRModelPtr model_;
};
DescribeClass<FRModelV_V_84,Helicity::FFSVertex>
describeHerwigFRModelV_V_84("Herwig::FRModelV_V_84",
				       "FRModel.so");
// void FRModelV_V_84::getParams(Energy2 ) {
// }

class FRModelV_V_85: public FFSVertex {
 public:
  FRModelV_V_85() {
    kinematics(false);
    addToList(-15,15,25);
  }
  void setCoupling(Energy2 ,tcPDPtr,tcPDPtr,tcPDPtr) {
    double ytau = model_->ytau();
    //    getParams(q2);
    norm(1.0);
    left(((((1.0*(-ii))*1.0)*1.0)*(-((ii*ytau)/sqrt(2.0)))));
    right(((((1.0*(-ii))*1.0)*1.0)*(-((ii*ytau)/sqrt(2.0)))));
    
  }
  void persistentOutput(PersistentOStream & os) const { os << model_; }
  void persistentInput(PersistentIStream & is, int) { is >> model_; }
  //  static void Init();
 protected:
  IBPtr clone() const { return new_ptr(*this); }
  IBPtr fullclone() const { return new_ptr(*this); }
  void doinit() {
    model_ = dynamic_ptr_cast<tcHwFRModelPtr>
	     (generator()->standardModel());
    assert(model_);
    //    getParams(q2);
    
    
    orderInGem(1);
    orderInGs(0);
    FFSVertex::doinit();
  }
  //    void getParams(Energy2);
 private:
  FRModelV_V_85 & operator=(const FRModelV_V_85 &);
  //    Complex leftval, rightval, normval;
  tcHwFRModelPtr model_;
};
DescribeClass<FRModelV_V_85,Helicity::FFSVertex>
describeHerwigFRModelV_V_85("Herwig::FRModelV_V_85",
				       "FRModel.so");
// void FRModelV_V_85::getParams(Energy2 ) {
// }

class FRModelV_V_98: public FFSVertex {
 public:
  FRModelV_V_98() {
    kinematics(false);
    addToList(-2,2,25);
  }
  void setCoupling(Energy2 ,tcPDPtr,tcPDPtr,tcPDPtr) {
    double yup = model_->yup();
    //    getParams(q2);
    norm(1.0);
    left(((((1.0*(-ii))*1.0)*1.0)*(-((ii*yup)/sqrt(2.0)))));
    right(((((1.0*(-ii))*1.0)*1.0)*(-((ii*yup)/sqrt(2.0)))));
    
  }
  void persistentOutput(PersistentOStream & os) const { os << model_; }
  void persistentInput(PersistentIStream & is, int) { is >> model_; }
  //  static void Init();
 protected:
  IBPtr clone() const { return new_ptr(*this); }
  IBPtr fullclone() const { return new_ptr(*this); }
  void doinit() {
    model_ = dynamic_ptr_cast<tcHwFRModelPtr>
	     (generator()->standardModel());
    assert(model_);
    //    getParams(q2);
    
    
    orderInGem(1);
    orderInGs(0);
    FFSVertex::doinit();
  }
  //    void getParams(Energy2);
 private:
  FRModelV_V_98 & operator=(const FRModelV_V_98 &);
  //    Complex leftval, rightval, normval;
  tcHwFRModelPtr model_;
};
DescribeClass<FRModelV_V_98,Helicity::FFSVertex>
describeHerwigFRModelV_V_98("Herwig::FRModelV_V_98",
				       "FRModel.so");
// void FRModelV_V_98::getParams(Energy2 ) {
// }

class FRModelV_V_99: public FFSVertex {
 public:
  FRModelV_V_99() {
    kinematics(false);
    addToList(-4,4,25);
  }
  void setCoupling(Energy2 ,tcPDPtr,tcPDPtr,tcPDPtr) {
    double yc = model_->yc();
    //    getParams(q2);
    norm(1.0);
    left(((((1.0*(-ii))*1.0)*1.0)*(-((ii*yc)/sqrt(2.0)))));
    right(((((1.0*(-ii))*1.0)*1.0)*(-((ii*yc)/sqrt(2.0)))));
    
  }
  void persistentOutput(PersistentOStream & os) const { os << model_; }
  void persistentInput(PersistentIStream & is, int) { is >> model_; }
  //  static void Init();
 protected:
  IBPtr clone() const { return new_ptr(*this); }
  IBPtr fullclone() const { return new_ptr(*this); }
  void doinit() {
    model_ = dynamic_ptr_cast<tcHwFRModelPtr>
	     (generator()->standardModel());
    assert(model_);
    //    getParams(q2);
    
    
    orderInGem(1);
    orderInGs(0);
    FFSVertex::doinit();
  }
  //    void getParams(Energy2);
 private:
  FRModelV_V_99 & operator=(const FRModelV_V_99 &);
  //    Complex leftval, rightval, normval;
  tcHwFRModelPtr model_;
};
DescribeClass<FRModelV_V_99,Helicity::FFSVertex>
describeHerwigFRModelV_V_99("Herwig::FRModelV_V_99",
				       "FRModel.so");
// void FRModelV_V_99::getParams(Energy2 ) {
// }

class FRModelV_V_100: public FFSVertex {
 public:
  FRModelV_V_100() {
    kinematics(false);
    addToList(-6,6,25);
  }
  void setCoupling(Energy2 ,tcPDPtr,tcPDPtr,tcPDPtr) {
    double yt = model_->yt();
    //    getParams(q2);
    norm(1.0);
    left(((((1.0*(-ii))*1.0)*1.0)*(-((ii*yt)/sqrt(2.0)))));
    right(((((1.0*(-ii))*1.0)*1.0)*(-((ii*yt)/sqrt(2.0)))));
    
  }
  void persistentOutput(PersistentOStream & os) const { os << model_; }
  void persistentInput(PersistentIStream & is, int) { is >> model_; }
  //  static void Init();
 protected:
  IBPtr clone() const { return new_ptr(*this); }
  IBPtr fullclone() const { return new_ptr(*this); }
  void doinit() {
    model_ = dynamic_ptr_cast<tcHwFRModelPtr>
	     (generator()->standardModel());
    assert(model_);
    //    getParams(q2);
    
    
    orderInGem(1);
    orderInGs(0);
    FFSVertex::doinit();
  }
  //    void getParams(Energy2);
 private:
  FRModelV_V_100 & operator=(const FRModelV_V_100 &);
  //    Complex leftval, rightval, normval;
  tcHwFRModelPtr model_;
};
DescribeClass<FRModelV_V_100,Helicity::FFSVertex>
describeHerwigFRModelV_V_100("Herwig::FRModelV_V_100",
				       "FRModel.so");
// void FRModelV_V_100::getParams(Energy2 ) {
// }

}

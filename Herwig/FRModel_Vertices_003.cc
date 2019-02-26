// -*- C++ -*-
//
// FRModelV_V_75.cc is a part of Herwig - A multi-purpose Monte Carlo event generator
// Copyright (C) 2002-2007 The Herwig Collaboration
//
// Herwig is licenced under version 2 of the GPL, see COPYING for details.
// Please respect the MCnet academic guidelines, see GUIDELINES for details.

#include "FRModel.h"
#include "ThePEG/Helicity/Vertex/Vector/VVVVVertex.h"
#include "ThePEG/Helicity/Vertex/Vector/VVVVertex.h"
#include "ThePEG/Helicity/Vertex/Scalar/FFSVertex.h"

#include "ThePEG/Utilities/DescribeClass.h"
#include "ThePEG/Persistency/PersistentOStream.h"
#include "ThePEG/Persistency/PersistentIStream.h"

namespace Herwig 
{
  using namespace ThePEG;
  using namespace ThePEG::Helicity;
  using ThePEG::Constants::pi;

  class FRModelV_V_51: public FFSVertex {
 public:
  FRModelV_V_51() {
    kinematics(false);
    addToList(-13,13,9000006);
  }
  void setCoupling(Energy2 ,tcPDPtr,tcPDPtr,tcPDPtr) {
    double gSmm = model_->gSmm();
    double gPmm = model_->gPmm();
    //    getParams(q2);
    norm(1.0);
    left((((((1.0*(-ii))*1.0)*1.0)*((ii*gSmm)/sqrt(2.0)))+((((1.0*(-ii))*1.0)*-1.0)*((ii*gPmm)/sqrt(2.0)))));
    right((((((1.0*(-ii))*1.0)*1.0)*((ii*gSmm)/sqrt(2.0)))+((((1.0*(-ii))*1.0)*1.0)*((ii*gPmm)/sqrt(2.0)))));
    
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
  FRModelV_V_51 & operator=(const FRModelV_V_51 &);
  //    Complex leftval, rightval, normval;
  tcHwFRModelPtr model_;
};
DescribeClass<FRModelV_V_51,Helicity::FFSVertex>
describeHerwigFRModelV_V_51("Herwig::FRModelV_V_51",
				       "FRModel.so");
// void FRModelV_V_51::getParams(Energy2 ) {
// }

class FRModelV_V_52: public FFSVertex {
 public:
  FRModelV_V_52() {
    kinematics(false);
    addToList(-3,3,9000006);
  }
  void setCoupling(Energy2 ,tcPDPtr,tcPDPtr,tcPDPtr) {
    double gPd22 = model_->gPd22();
    double gSd22 = model_->gSd22();
    //    getParams(q2);
    norm(1.0);
    left((((((1.0*(-ii))*1.0)*1.0)*((ii*gSd22)/sqrt(2.0)))+((((1.0*(-ii))*1.0)*-1.0)*((ii*gPd22)/sqrt(2.0)))));
    right((((((1.0*(-ii))*1.0)*1.0)*((ii*gSd22)/sqrt(2.0)))+((((1.0*(-ii))*1.0)*1.0)*((ii*gPd22)/sqrt(2.0)))));
    
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
  FRModelV_V_52 & operator=(const FRModelV_V_52 &);
  //    Complex leftval, rightval, normval;
  tcHwFRModelPtr model_;
};
DescribeClass<FRModelV_V_52,Helicity::FFSVertex>
describeHerwigFRModelV_V_52("Herwig::FRModelV_V_52",
				       "FRModel.so");
// void FRModelV_V_52::getParams(Energy2 ) {
// }

class FRModelV_V_53: public FFSVertex {
 public:
  FRModelV_V_53() {
    kinematics(false);
    addToList(-15,15,9000006);
  }
  void setCoupling(Energy2 ,tcPDPtr,tcPDPtr,tcPDPtr) {
    double gPta = model_->gPta();
    double gSta = model_->gSta();
    //    getParams(q2);
    norm(1.0);
    left((((((1.0*(-ii))*1.0)*1.0)*((ii*gSta)/sqrt(2.0)))+((((1.0*(-ii))*1.0)*-1.0)*((ii*gPta)/sqrt(2.0)))));
    right((((((1.0*(-ii))*1.0)*1.0)*((ii*gSta)/sqrt(2.0)))+((((1.0*(-ii))*1.0)*1.0)*((ii*gPta)/sqrt(2.0)))));
    
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
  FRModelV_V_53 & operator=(const FRModelV_V_53 &);
  //    Complex leftval, rightval, normval;
  tcHwFRModelPtr model_;
};
DescribeClass<FRModelV_V_53,Helicity::FFSVertex>
describeHerwigFRModelV_V_53("Herwig::FRModelV_V_53",
				       "FRModel.so");
// void FRModelV_V_53::getParams(Energy2 ) {
// }

class FRModelV_V_54: public FFSVertex {
 public:
  FRModelV_V_54() {
    kinematics(false);
    addToList(-6,6,9000006);
  }
  void setCoupling(Energy2 ,tcPDPtr,tcPDPtr,tcPDPtr) {
    double gPu33 = model_->gPu33();
    double gSu33 = model_->gSu33();
    //    getParams(q2);
    norm(1.0);
    left((((((1.0*(-ii))*1.0)*1.0)*((ii*gSu33)/sqrt(2.0)))+((((1.0*(-ii))*1.0)*-1.0)*((ii*gPu33)/sqrt(2.0)))));
    right((((((1.0*(-ii))*1.0)*1.0)*((ii*gSu33)/sqrt(2.0)))+((((1.0*(-ii))*1.0)*1.0)*((ii*gPu33)/sqrt(2.0)))));
    
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
  FRModelV_V_54 & operator=(const FRModelV_V_54 &);
  //    Complex leftval, rightval, normval;
  tcHwFRModelPtr model_;
};
DescribeClass<FRModelV_V_54,Helicity::FFSVertex>
describeHerwigFRModelV_V_54("Herwig::FRModelV_V_54",
				       "FRModel.so");
// void FRModelV_V_54::getParams(Energy2 ) {
// }

class FRModelV_V_55: public FFSVertex {
 public:
  FRModelV_V_55() {
    kinematics(false);
    addToList(-2,2,9000006);
  }
  void setCoupling(Energy2 ,tcPDPtr,tcPDPtr,tcPDPtr) {
    double gSu11 = model_->gSu11();
    double gPu11 = model_->gPu11();
    //    getParams(q2);
    norm(1.0);
    left((((((1.0*(-ii))*1.0)*1.0)*((ii*gSu11)/sqrt(2.0)))+((((1.0*(-ii))*1.0)*-1.0)*((ii*gPu11)/sqrt(2.0)))));
    right((((((1.0*(-ii))*1.0)*1.0)*((ii*gSu11)/sqrt(2.0)))+((((1.0*(-ii))*1.0)*1.0)*((ii*gPu11)/sqrt(2.0)))));
    
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
  FRModelV_V_55 & operator=(const FRModelV_V_55 &);
  //    Complex leftval, rightval, normval;
  tcHwFRModelPtr model_;
};
DescribeClass<FRModelV_V_55,Helicity::FFSVertex>
describeHerwigFRModelV_V_55("Herwig::FRModelV_V_55",
				       "FRModel.so");
// void FRModelV_V_55::getParams(Energy2 ) {
// }

class FRModelV_V_56: public FFSVertex {
 public:
  FRModelV_V_56() {
    kinematics(false);
    addToList(-9000010,9000010,9000006);
  }
  void setCoupling(Energy2 ,tcPDPtr,tcPDPtr,tcPDPtr) {
    double gPXd = model_->gPXd();
    double gSXd = model_->gSXd();
    //    getParams(q2);
    norm(1.0);
    left((((((1.0*(-ii))*1.0)*1.0)*(ii*gSXd))+((((1.0*(-ii))*1.0)*-1.0)*(-gPXd))));
    right((((((1.0*(-ii))*1.0)*1.0)*(ii*gSXd))+((((1.0*(-ii))*1.0)*1.0)*(-gPXd))));
    
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
  FRModelV_V_56 & operator=(const FRModelV_V_56 &);
  //    Complex leftval, rightval, normval;
  tcHwFRModelPtr model_;
};
DescribeClass<FRModelV_V_56,Helicity::FFSVertex>
describeHerwigFRModelV_V_56("Herwig::FRModelV_V_56",
				       "FRModel.so");
// void FRModelV_V_56::getParams(Energy2 ) {
// }

class FRModelV_V_58: public VVVVertex {
 public:
  FRModelV_V_58() {
    kinematics(false);
    addToList(21,21,21);
  }
  void setCoupling(Energy2 ,tcPDPtr,tcPDPtr,tcPDPtr) {
    double G = model_->G();
    //    getParams(q2);
    norm((((1.0*ii)*(-ii))*(-G)));
    
    
    
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
    
    
    orderInGem(0);
    orderInGs(1);
    VVVVertex::doinit();
  }
  //    void getParams(Energy2);
 private:
  FRModelV_V_58 & operator=(const FRModelV_V_58 &);
  //    Complex leftval, rightval, normval;
  tcHwFRModelPtr model_;
};
DescribeClass<FRModelV_V_58,Helicity::VVVVertex>
describeHerwigFRModelV_V_58("Herwig::FRModelV_V_58",
				       "FRModel.so");
// void FRModelV_V_58::getParams(Energy2 ) {
// }

class FRModelV_V_59: public VVVVVertex {
 public:
  FRModelV_V_59() {
    kinematics(false);
    addToList(21,21,21,21);
  }
  void setCoupling(Energy2 ,tcPDPtr,tcPDPtr,tcPDPtr,tcPDPtr) {
    double G = model_->G();
    //    getParams(q2);
    norm((((((1.0*ii)*(-1.0/3.0))*(ii*sqr(G)))+(((1.0*ii)*(-1.0/3.0))*(ii*sqr(G))))+(((1.0*ii)*(-1.0/3.0))*(ii*sqr(G)))));
    
    
    setType(1);
setOrder(0,1,2,3);
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
    
    
    orderInGem(0);
    orderInGs(2);
    VVVVVertex::doinit();
  }
  //    void getParams(Energy2);
 private:
  FRModelV_V_59 & operator=(const FRModelV_V_59 &);
  //    Complex leftval, rightval, normval;
  tcHwFRModelPtr model_;
};
DescribeClass<FRModelV_V_59,Helicity::VVVVVertex>
describeHerwigFRModelV_V_59("Herwig::FRModelV_V_59",
				       "FRModel.so");
// void FRModelV_V_59::getParams(Energy2 ) {
// }

class FRModelV_V_74: public FFSVertex {
 public:
  FRModelV_V_74() {
    kinematics(false);
    addToList(-1,1,25);
  }
  void setCoupling(Energy2 ,tcPDPtr,tcPDPtr,tcPDPtr) {
    double ydo = model_->ydo();
    //    getParams(q2);
    norm(1.0);
    left(((((1.0*(-ii))*1.0)*1.0)*(-((ii*ydo)/sqrt(2.0)))));
    right(((((1.0*(-ii))*1.0)*1.0)*(-((ii*ydo)/sqrt(2.0)))));
    
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
  FRModelV_V_74 & operator=(const FRModelV_V_74 &);
  //    Complex leftval, rightval, normval;
  tcHwFRModelPtr model_;
};
DescribeClass<FRModelV_V_74,Helicity::FFSVertex>
describeHerwigFRModelV_V_74("Herwig::FRModelV_V_74",
				       "FRModel.so");
// void FRModelV_V_74::getParams(Energy2 ) {
// }

class FRModelV_V_75: public FFSVertex {
 public:
  FRModelV_V_75() {
    kinematics(false);
    addToList(-3,3,25);
  }
  void setCoupling(Energy2 ,tcPDPtr,tcPDPtr,tcPDPtr) {
    double ys = model_->ys();
    //    getParams(q2);
    norm(1.0);
    left(((((1.0*(-ii))*1.0)*1.0)*(-((ii*ys)/sqrt(2.0)))));
    right(((((1.0*(-ii))*1.0)*1.0)*(-((ii*ys)/sqrt(2.0)))));
    
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
  FRModelV_V_75 & operator=(const FRModelV_V_75 &);
  //    Complex leftval, rightval, normval;
  tcHwFRModelPtr model_;
};
DescribeClass<FRModelV_V_75,Helicity::FFSVertex>
describeHerwigFRModelV_V_75("Herwig::FRModelV_V_75",
				       "FRModel.so");
// void FRModelV_V_75::getParams(Energy2 ) {
// }

}

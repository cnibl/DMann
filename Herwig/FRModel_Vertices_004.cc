// -*- C++ -*-
//
// FRModelV_V_100.cc is a part of Herwig - A multi-purpose Monte Carlo event generator
// Copyright (C) 2002-2007 The Herwig Collaboration
//
// Herwig is licenced under version 2 of the GPL, see COPYING for details.
// Please respect the MCnet academic guidelines, see GUIDELINES for details.

#include "FRModel.h"
#include "ThePEG/Helicity/Vertex/Scalar/SSSVertex.h"
#include "ThePEG/Helicity/Vertex/Scalar/SSSSVertex.h"
#include "ThePEG/Helicity/Vertex/Vector/VVVVVertex.h"
#include "ThePEG/Helicity/Vertex/Vector/VVVVertex.h"
#include "ThePEG/Helicity/Vertex/Scalar/VVSSVertex.h"
#include "ThePEG/Helicity/Vertex/Scalar/VVSVertex.h"
#include "ThePEG/Helicity/Vertex/Scalar/FFSVertex.h"

#include "ThePEG/Utilities/DescribeClass.h"
#include "ThePEG/Persistency/PersistentOStream.h"
#include "ThePEG/Persistency/PersistentIStream.h"

namespace Herwig 
{
  using namespace ThePEG;
  using namespace ThePEG::Helicity;
  using ThePEG::Constants::pi;

  class FRModelV_V_6: public SSSSVertex {
 public:
  FRModelV_V_6() {
    kinematics(false);
    addToList(25,25,25,25);
  }
  void setCoupling(Energy2 ,tcPDPtr,tcPDPtr,tcPDPtr,tcPDPtr) {
    double lam = model_->lam();
    //    getParams(q2);
    norm((((1.0*(-ii))*1.0)*((-6.0*ii)*lam)));
    
    
    
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
    
    
    orderInGem(2);
    orderInGs(0);
    SSSSVertex::doinit();
  }
  //    void getParams(Energy2);
 private:
  FRModelV_V_6 & operator=(const FRModelV_V_6 &);
  //    Complex leftval, rightval, normval;
  tcHwFRModelPtr model_;
};
DescribeClass<FRModelV_V_6,Helicity::SSSSVertex>
describeHerwigFRModelV_V_6("Herwig::FRModelV_V_6",
				       "FRModel.so");
// void FRModelV_V_6::getParams(Energy2 ) {
// }

class FRModelV_V_9: public SSSVertex {
 public:
  FRModelV_V_9() {
    kinematics(false);
    addToList(25,25,25);
  }
  void setCoupling(Energy2 ,tcPDPtr,tcPDPtr,tcPDPtr) {
    double vev = model_->vev();
    double lam = model_->lam();
    //    getParams(q2);
    norm(Complex(((((1.0*(-ii))*1.0)*(((-6.0*ii)*lam)*vev))) * GeV / UnitRemoval::E));
    
    
    
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
    SSSVertex::doinit();
  }
  //    void getParams(Energy2);
 private:
  FRModelV_V_9 & operator=(const FRModelV_V_9 &);
  //    Complex leftval, rightval, normval;
  tcHwFRModelPtr model_;
};
DescribeClass<FRModelV_V_9,Helicity::SSSVertex>
describeHerwigFRModelV_V_9("Herwig::FRModelV_V_9",
				       "FRModel.so");
// void FRModelV_V_9::getParams(Energy2 ) {
// }

class FRModelV_V_35: public FFSVertex {
 public:
  FRModelV_V_35() {
    kinematics(false);
    addToList(-5,5,999);
  }
  void setCoupling(Energy2 ,tcPDPtr,tcPDPtr,tcPDPtr) {
    double gSf = model_->gSf();
    //    getParams(q2);
    norm(1.0);
    left(((((1.0*(-ii))*1.0)*1.0)*(ii*gSf)));
    right(((((1.0*(-ii))*1.0)*1.0)*(ii*gSf)));
    
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
  FRModelV_V_35 & operator=(const FRModelV_V_35 &);
  //    Complex leftval, rightval, normval;
  tcHwFRModelPtr model_;
};
DescribeClass<FRModelV_V_35,Helicity::FFSVertex>
describeHerwigFRModelV_V_35("Herwig::FRModelV_V_35",
				       "FRModel.so");
// void FRModelV_V_35::getParams(Energy2 ) {
// }

class FRModelV_V_36: public FFSVertex {
 public:
  FRModelV_V_36() {
    kinematics(false);
    addToList(-4,4,999);
  }
  void setCoupling(Energy2 ,tcPDPtr,tcPDPtr,tcPDPtr) {
    double gSf = model_->gSf();
    //    getParams(q2);
    norm(1.0);
    left(((((1.0*(-ii))*1.0)*1.0)*(ii*gSf)));
    right(((((1.0*(-ii))*1.0)*1.0)*(ii*gSf)));
    
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
  FRModelV_V_36 & operator=(const FRModelV_V_36 &);
  //    Complex leftval, rightval, normval;
  tcHwFRModelPtr model_;
};
DescribeClass<FRModelV_V_36,Helicity::FFSVertex>
describeHerwigFRModelV_V_36("Herwig::FRModelV_V_36",
				       "FRModel.so");
// void FRModelV_V_36::getParams(Energy2 ) {
// }

class FRModelV_V_37: public FFSVertex {
 public:
  FRModelV_V_37() {
    kinematics(false);
    addToList(-1,1,999);
  }
  void setCoupling(Energy2 ,tcPDPtr,tcPDPtr,tcPDPtr) {
    double gSf = model_->gSf();
    //    getParams(q2);
    norm(1.0);
    left(((((1.0*(-ii))*1.0)*1.0)*(ii*gSf)));
    right(((((1.0*(-ii))*1.0)*1.0)*(ii*gSf)));
    
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
  FRModelV_V_37 & operator=(const FRModelV_V_37 &);
  //    Complex leftval, rightval, normval;
  tcHwFRModelPtr model_;
};
DescribeClass<FRModelV_V_37,Helicity::FFSVertex>
describeHerwigFRModelV_V_37("Herwig::FRModelV_V_37",
				       "FRModel.so");
// void FRModelV_V_37::getParams(Energy2 ) {
// }

class FRModelV_V_38: public FFSVertex {
 public:
  FRModelV_V_38() {
    kinematics(false);
    addToList(-11,11,999);
  }
  void setCoupling(Energy2 ,tcPDPtr,tcPDPtr,tcPDPtr) {
    double gSf = model_->gSf();
    //    getParams(q2);
    norm(1.0);
    left(((((1.0*(-ii))*1.0)*1.0)*(ii*gSf)));
    right(((((1.0*(-ii))*1.0)*1.0)*(ii*gSf)));
    
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
  FRModelV_V_38 & operator=(const FRModelV_V_38 &);
  //    Complex leftval, rightval, normval;
  tcHwFRModelPtr model_;
};
DescribeClass<FRModelV_V_38,Helicity::FFSVertex>
describeHerwigFRModelV_V_38("Herwig::FRModelV_V_38",
				       "FRModel.so");
// void FRModelV_V_38::getParams(Energy2 ) {
// }

class FRModelV_V_39: public FFSVertex {
 public:
  FRModelV_V_39() {
    kinematics(false);
    addToList(-13,13,999);
  }
  void setCoupling(Energy2 ,tcPDPtr,tcPDPtr,tcPDPtr) {
    double gSf = model_->gSf();
    //    getParams(q2);
    norm(1.0);
    left(((((1.0*(-ii))*1.0)*1.0)*(ii*gSf)));
    right(((((1.0*(-ii))*1.0)*1.0)*(ii*gSf)));
    
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
  FRModelV_V_39 & operator=(const FRModelV_V_39 &);
  //    Complex leftval, rightval, normval;
  tcHwFRModelPtr model_;
};
DescribeClass<FRModelV_V_39,Helicity::FFSVertex>
describeHerwigFRModelV_V_39("Herwig::FRModelV_V_39",
				       "FRModel.so");
// void FRModelV_V_39::getParams(Energy2 ) {
// }

class FRModelV_V_40: public FFSVertex {
 public:
  FRModelV_V_40() {
    kinematics(false);
    addToList(-3,3,999);
  }
  void setCoupling(Energy2 ,tcPDPtr,tcPDPtr,tcPDPtr) {
    double gSf = model_->gSf();
    //    getParams(q2);
    norm(1.0);
    left(((((1.0*(-ii))*1.0)*1.0)*(ii*gSf)));
    right(((((1.0*(-ii))*1.0)*1.0)*(ii*gSf)));
    
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
  FRModelV_V_40 & operator=(const FRModelV_V_40 &);
  //    Complex leftval, rightval, normval;
  tcHwFRModelPtr model_;
};
DescribeClass<FRModelV_V_40,Helicity::FFSVertex>
describeHerwigFRModelV_V_40("Herwig::FRModelV_V_40",
				       "FRModel.so");
// void FRModelV_V_40::getParams(Energy2 ) {
// }

class FRModelV_V_41: public FFSVertex {
 public:
  FRModelV_V_41() {
    kinematics(false);
    addToList(-15,15,999);
  }
  void setCoupling(Energy2 ,tcPDPtr,tcPDPtr,tcPDPtr) {
    double gSf = model_->gSf();
    //    getParams(q2);
    norm(1.0);
    left(((((1.0*(-ii))*1.0)*1.0)*(ii*gSf)));
    right(((((1.0*(-ii))*1.0)*1.0)*(ii*gSf)));
    
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
  FRModelV_V_41 & operator=(const FRModelV_V_41 &);
  //    Complex leftval, rightval, normval;
  tcHwFRModelPtr model_;
};
DescribeClass<FRModelV_V_41,Helicity::FFSVertex>
describeHerwigFRModelV_V_41("Herwig::FRModelV_V_41",
				       "FRModel.so");
// void FRModelV_V_41::getParams(Energy2 ) {
// }

class FRModelV_V_42: public FFSVertex {
 public:
  FRModelV_V_42() {
    kinematics(false);
    addToList(-6,6,999);
  }
  void setCoupling(Energy2 ,tcPDPtr,tcPDPtr,tcPDPtr) {
    double gSf = model_->gSf();
    //    getParams(q2);
    norm(1.0);
    left(((((1.0*(-ii))*1.0)*1.0)*(ii*gSf)));
    right(((((1.0*(-ii))*1.0)*1.0)*(ii*gSf)));
    
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
  FRModelV_V_42 & operator=(const FRModelV_V_42 &);
  //    Complex leftval, rightval, normval;
  tcHwFRModelPtr model_;
};
DescribeClass<FRModelV_V_42,Helicity::FFSVertex>
describeHerwigFRModelV_V_42("Herwig::FRModelV_V_42",
				       "FRModel.so");
// void FRModelV_V_42::getParams(Energy2 ) {
// }

class FRModelV_V_43: public FFSVertex {
 public:
  FRModelV_V_43() {
    kinematics(false);
    addToList(-2,2,999);
  }
  void setCoupling(Energy2 ,tcPDPtr,tcPDPtr,tcPDPtr) {
    double gSf = model_->gSf();
    //    getParams(q2);
    norm(1.0);
    left(((((1.0*(-ii))*1.0)*1.0)*(ii*gSf)));
    right(((((1.0*(-ii))*1.0)*1.0)*(ii*gSf)));
    
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
  FRModelV_V_43 & operator=(const FRModelV_V_43 &);
  //    Complex leftval, rightval, normval;
  tcHwFRModelPtr model_;
};
DescribeClass<FRModelV_V_43,Helicity::FFSVertex>
describeHerwigFRModelV_V_43("Herwig::FRModelV_V_43",
				       "FRModel.so");
// void FRModelV_V_43::getParams(Energy2 ) {
// }

class FRModelV_V_45: public VVVVertex {
 public:
  FRModelV_V_45() {
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
  FRModelV_V_45 & operator=(const FRModelV_V_45 &);
  //    Complex leftval, rightval, normval;
  tcHwFRModelPtr model_;
};
DescribeClass<FRModelV_V_45,Helicity::VVVVertex>
describeHerwigFRModelV_V_45("Herwig::FRModelV_V_45",
				       "FRModel.so");
// void FRModelV_V_45::getParams(Energy2 ) {
// }

class FRModelV_V_46: public VVVVVertex {
 public:
  FRModelV_V_46() {
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
  FRModelV_V_46 & operator=(const FRModelV_V_46 &);
  //    Complex leftval, rightval, normval;
  tcHwFRModelPtr model_;
};
DescribeClass<FRModelV_V_46,Helicity::VVVVVertex>
describeHerwigFRModelV_V_46("Herwig::FRModelV_V_46",
				       "FRModel.so");
// void FRModelV_V_46::getParams(Energy2 ) {
// }

class FRModelV_V_59: public FFSVertex {
 public:
  FRModelV_V_59() {
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
  FRModelV_V_59 & operator=(const FRModelV_V_59 &);
  //    Complex leftval, rightval, normval;
  tcHwFRModelPtr model_;
};
DescribeClass<FRModelV_V_59,Helicity::FFSVertex>
describeHerwigFRModelV_V_59("Herwig::FRModelV_V_59",
				       "FRModel.so");
// void FRModelV_V_59::getParams(Energy2 ) {
// }

class FRModelV_V_60: public FFSVertex {
 public:
  FRModelV_V_60() {
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
  FRModelV_V_60 & operator=(const FRModelV_V_60 &);
  //    Complex leftval, rightval, normval;
  tcHwFRModelPtr model_;
};
DescribeClass<FRModelV_V_60,Helicity::FFSVertex>
describeHerwigFRModelV_V_60("Herwig::FRModelV_V_60",
				       "FRModel.so");
// void FRModelV_V_60::getParams(Energy2 ) {
// }

class FRModelV_V_61: public FFSVertex {
 public:
  FRModelV_V_61() {
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
  FRModelV_V_61 & operator=(const FRModelV_V_61 &);
  //    Complex leftval, rightval, normval;
  tcHwFRModelPtr model_;
};
DescribeClass<FRModelV_V_61,Helicity::FFSVertex>
describeHerwigFRModelV_V_61("Herwig::FRModelV_V_61",
				       "FRModel.so");
// void FRModelV_V_61::getParams(Energy2 ) {
// }

class FRModelV_V_68: public FFSVertex {
 public:
  FRModelV_V_68() {
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
  FRModelV_V_68 & operator=(const FRModelV_V_68 &);
  //    Complex leftval, rightval, normval;
  tcHwFRModelPtr model_;
};
DescribeClass<FRModelV_V_68,Helicity::FFSVertex>
describeHerwigFRModelV_V_68("Herwig::FRModelV_V_68",
				       "FRModel.so");
// void FRModelV_V_68::getParams(Energy2 ) {
// }

class FRModelV_V_69: public FFSVertex {
 public:
  FRModelV_V_69() {
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
  FRModelV_V_69 & operator=(const FRModelV_V_69 &);
  //    Complex leftval, rightval, normval;
  tcHwFRModelPtr model_;
};
DescribeClass<FRModelV_V_69,Helicity::FFSVertex>
describeHerwigFRModelV_V_69("Herwig::FRModelV_V_69",
				       "FRModel.so");
// void FRModelV_V_69::getParams(Energy2 ) {
// }

class FRModelV_V_70: public FFSVertex {
 public:
  FRModelV_V_70() {
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
  FRModelV_V_70 & operator=(const FRModelV_V_70 &);
  //    Complex leftval, rightval, normval;
  tcHwFRModelPtr model_;
};
DescribeClass<FRModelV_V_70,Helicity::FFSVertex>
describeHerwigFRModelV_V_70("Herwig::FRModelV_V_70",
				       "FRModel.so");
// void FRModelV_V_70::getParams(Energy2 ) {
// }

class FRModelV_V_83: public FFSVertex {
 public:
  FRModelV_V_83() {
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
  FRModelV_V_85 & operator=(const FRModelV_V_85 &);
  //    Complex leftval, rightval, normval;
  tcHwFRModelPtr model_;
};
DescribeClass<FRModelV_V_85,Helicity::FFSVertex>
describeHerwigFRModelV_V_85("Herwig::FRModelV_V_85",
				       "FRModel.so");
// void FRModelV_V_85::getParams(Energy2 ) {
// }

class FRModelV_V_91: public VVVVertex {
 public:
  FRModelV_V_91() {
    kinematics(false);
    addToList(22,-24,24);
  }
  void setCoupling(Energy2 ,tcPDPtr p1,tcPDPtr p2,tcPDPtr p3) {
    double ee = model_->ee();
    //    getParams(q2);
    norm((((1.0*ii)*1.0)*(ee*ii)));
    
    
    if((p1->id()==-24&&p2->id()==22&&p3->id()==24)||(p1->id()==22&&p2->id()==24&&p3->id()==-24)||(p1->id()==24&&p2->id()==-24&&p3->id()==22)) {norm(-norm());}
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
    VVVVertex::doinit();
  }
  //    void getParams(Energy2);
 private:
  FRModelV_V_91 & operator=(const FRModelV_V_91 &);
  //    Complex leftval, rightval, normval;
  tcHwFRModelPtr model_;
};
DescribeClass<FRModelV_V_91,Helicity::VVVVertex>
describeHerwigFRModelV_V_91("Herwig::FRModelV_V_91",
				       "FRModel.so");
// void FRModelV_V_91::getParams(Energy2 ) {
// }

class FRModelV_V_97: public VVSVertex {
 public:
  FRModelV_V_97() {
    kinematics(false);
    addToList(-24,24,999);
  }
  void setCoupling(Energy2 ,tcPDPtr,tcPDPtr,tcPDPtr) {
    double gSEW = model_->gSEW();
    double Lambda = model_->Lambda();
    //    getParams(q2);
    norm(Complex((((((1.0*(-ii))*1.0)*((ii*gSEW)/Lambda))*1.0)) * GeV / UnitRemoval::E));
    
    
    
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
    VVSVertex::doinit();
  }
  //    void getParams(Energy2);
 private:
  FRModelV_V_97 & operator=(const FRModelV_V_97 &);
  //    Complex leftval, rightval, normval;
  tcHwFRModelPtr model_;
};
DescribeClass<FRModelV_V_97,Helicity::VVSVertex>
describeHerwigFRModelV_V_97("Herwig::FRModelV_V_97",
				       "FRModel.so");
// void FRModelV_V_97::getParams(Energy2 ) {
// }

class FRModelV_V_100: public VVSSVertex {
 public:
  FRModelV_V_100() {
    kinematics(false);
    addToList(-24,24,25,25);
  }
  void setCoupling(Energy2 ,tcPDPtr,tcPDPtr,tcPDPtr,tcPDPtr) {
    double ee = model_->ee();
    double sw = model_->sw();
    //    getParams(q2);
    norm((((1.0*(-ii))*1.0)*((sqr(ee)*ii)/(2.0*sqr(sw)))));
    
    
    
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
    
    
    orderInGem(2);
    orderInGs(0);
    VVSSVertex::doinit();
  }
  //    void getParams(Energy2);
 private:
  FRModelV_V_100 & operator=(const FRModelV_V_100 &);
  //    Complex leftval, rightval, normval;
  tcHwFRModelPtr model_;
};
DescribeClass<FRModelV_V_100,Helicity::VVSSVertex>
describeHerwigFRModelV_V_100("Herwig::FRModelV_V_100",
				       "FRModel.so");
// void FRModelV_V_100::getParams(Energy2 ) {
// }

}

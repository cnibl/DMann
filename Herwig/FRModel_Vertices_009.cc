// -*- C++ -*-
//
// FRModelV_V_225.cc is a part of Herwig - A multi-purpose Monte Carlo event generator
// Copyright (C) 2002-2007 The Herwig Collaboration
//
// Herwig is licenced under version 2 of the GPL, see COPYING for details.
// Please respect the MCnet academic guidelines, see GUIDELINES for details.

#include "FRModel.h"
#include "ThePEG/Helicity/Vertex/Vector/FFVVertex.h"

#include "ThePEG/Utilities/DescribeClass.h"
#include "ThePEG/Persistency/PersistentOStream.h"
#include "ThePEG/Persistency/PersistentIStream.h"

namespace Herwig 
{
  using namespace ThePEG;
  using namespace ThePEG::Helicity;
  using ThePEG::Constants::pi;

  class FRModelV_V_201: public FFVVertex {
 public:
  FRModelV_V_201() {
    kinematics(false);
    addToList(-1,4,-24);
  }
  void setCoupling(Energy2 ,tcPDPtr p1,tcPDPtr,tcPDPtr) {
    double ee = model_->ee();
    Complex CKM2x1 = model_->CKM2x1();
    double sw = model_->sw();
    //    getParams(q2);
    norm(1.0);
    left(((((1.0*(-ii))*1.0)*1.0)*(((CKM2x1*ee)*ii)/(sw*sqrt(2.0)))));
    right(0.0);
    if(p1->id()!=-1) {Complex ltemp=left(), rtemp=right(); left(-rtemp); right(-ltemp);}
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
    FFVVertex::doinit();
  }
  //    void getParams(Energy2);
 private:
  FRModelV_V_201 & operator=(const FRModelV_V_201 &);
  //    Complex leftval, rightval, normval;
  tcHwFRModelPtr model_;
};
DescribeClass<FRModelV_V_201,Helicity::FFVVertex>
describeHerwigFRModelV_V_201("Herwig::FRModelV_V_201",
				       "FRModel.so");
// void FRModelV_V_201::getParams(Energy2 ) {
// }

class FRModelV_V_202: public FFVVertex {
 public:
  FRModelV_V_202() {
    kinematics(false);
    addToList(-3,4,-24);
  }
  void setCoupling(Energy2 ,tcPDPtr p1,tcPDPtr,tcPDPtr) {
    double ee = model_->ee();
    double sw = model_->sw();
    Complex CKM2x2 = model_->CKM2x2();
    //    getParams(q2);
    norm(1.0);
    left(((((1.0*(-ii))*1.0)*1.0)*(((CKM2x2*ee)*ii)/(sw*sqrt(2.0)))));
    right(0.0);
    if(p1->id()!=-3) {Complex ltemp=left(), rtemp=right(); left(-rtemp); right(-ltemp);}
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
    FFVVertex::doinit();
  }
  //    void getParams(Energy2);
 private:
  FRModelV_V_202 & operator=(const FRModelV_V_202 &);
  //    Complex leftval, rightval, normval;
  tcHwFRModelPtr model_;
};
DescribeClass<FRModelV_V_202,Helicity::FFVVertex>
describeHerwigFRModelV_V_202("Herwig::FRModelV_V_202",
				       "FRModel.so");
// void FRModelV_V_202::getParams(Energy2 ) {
// }

class FRModelV_V_203: public FFVVertex {
 public:
  FRModelV_V_203() {
    kinematics(false);
    addToList(-5,4,-24);
  }
  void setCoupling(Energy2 ,tcPDPtr p1,tcPDPtr,tcPDPtr) {
    double ee = model_->ee();
    double sw = model_->sw();
    Complex CKM2x3 = model_->CKM2x3();
    //    getParams(q2);
    norm(1.0);
    left(((((1.0*(-ii))*1.0)*1.0)*(((CKM2x3*ee)*ii)/(sw*sqrt(2.0)))));
    right(0.0);
    if(p1->id()!=-5) {Complex ltemp=left(), rtemp=right(); left(-rtemp); right(-ltemp);}
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
    FFVVertex::doinit();
  }
  //    void getParams(Energy2);
 private:
  FRModelV_V_203 & operator=(const FRModelV_V_203 &);
  //    Complex leftval, rightval, normval;
  tcHwFRModelPtr model_;
};
DescribeClass<FRModelV_V_203,Helicity::FFVVertex>
describeHerwigFRModelV_V_203("Herwig::FRModelV_V_203",
				       "FRModel.so");
// void FRModelV_V_203::getParams(Energy2 ) {
// }

class FRModelV_V_204: public FFVVertex {
 public:
  FRModelV_V_204() {
    kinematics(false);
    addToList(-1,6,-24);
  }
  void setCoupling(Energy2 ,tcPDPtr p1,tcPDPtr,tcPDPtr) {
    double ee = model_->ee();
    double sw = model_->sw();
    Complex CKM3x1 = model_->CKM3x1();
    //    getParams(q2);
    norm(1.0);
    left(((((1.0*(-ii))*1.0)*1.0)*(((CKM3x1*ee)*ii)/(sw*sqrt(2.0)))));
    right(0.0);
    if(p1->id()!=-1) {Complex ltemp=left(), rtemp=right(); left(-rtemp); right(-ltemp);}
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
    FFVVertex::doinit();
  }
  //    void getParams(Energy2);
 private:
  FRModelV_V_204 & operator=(const FRModelV_V_204 &);
  //    Complex leftval, rightval, normval;
  tcHwFRModelPtr model_;
};
DescribeClass<FRModelV_V_204,Helicity::FFVVertex>
describeHerwigFRModelV_V_204("Herwig::FRModelV_V_204",
				       "FRModel.so");
// void FRModelV_V_204::getParams(Energy2 ) {
// }

class FRModelV_V_205: public FFVVertex {
 public:
  FRModelV_V_205() {
    kinematics(false);
    addToList(-3,6,-24);
  }
  void setCoupling(Energy2 ,tcPDPtr p1,tcPDPtr,tcPDPtr) {
    double ee = model_->ee();
    double sw = model_->sw();
    Complex CKM3x2 = model_->CKM3x2();
    //    getParams(q2);
    norm(1.0);
    left(((((1.0*(-ii))*1.0)*1.0)*(((CKM3x2*ee)*ii)/(sw*sqrt(2.0)))));
    right(0.0);
    if(p1->id()!=-3) {Complex ltemp=left(), rtemp=right(); left(-rtemp); right(-ltemp);}
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
    FFVVertex::doinit();
  }
  //    void getParams(Energy2);
 private:
  FRModelV_V_205 & operator=(const FRModelV_V_205 &);
  //    Complex leftval, rightval, normval;
  tcHwFRModelPtr model_;
};
DescribeClass<FRModelV_V_205,Helicity::FFVVertex>
describeHerwigFRModelV_V_205("Herwig::FRModelV_V_205",
				       "FRModel.so");
// void FRModelV_V_205::getParams(Energy2 ) {
// }

class FRModelV_V_206: public FFVVertex {
 public:
  FRModelV_V_206() {
    kinematics(false);
    addToList(-5,6,-24);
  }
  void setCoupling(Energy2 ,tcPDPtr p1,tcPDPtr,tcPDPtr) {
    double ee = model_->ee();
    double sw = model_->sw();
    Complex CKM3x3 = model_->CKM3x3();
    //    getParams(q2);
    norm(1.0);
    left(((((1.0*(-ii))*1.0)*1.0)*(((CKM3x3*ee)*ii)/(sw*sqrt(2.0)))));
    right(0.0);
    if(p1->id()!=-5) {Complex ltemp=left(), rtemp=right(); left(-rtemp); right(-ltemp);}
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
    FFVVertex::doinit();
  }
  //    void getParams(Energy2);
 private:
  FRModelV_V_206 & operator=(const FRModelV_V_206 &);
  //    Complex leftval, rightval, normval;
  tcHwFRModelPtr model_;
};
DescribeClass<FRModelV_V_206,Helicity::FFVVertex>
describeHerwigFRModelV_V_206("Herwig::FRModelV_V_206",
				       "FRModel.so");
// void FRModelV_V_206::getParams(Energy2 ) {
// }

class FRModelV_V_207: public FFVVertex {
 public:
  FRModelV_V_207() {
    kinematics(false);
    addToList(-2,1,24);
  }
  void setCoupling(Energy2 ,tcPDPtr p1,tcPDPtr,tcPDPtr) {
    double ee = model_->ee();
    double sw = model_->sw();
    Complex CKM1x1 = model_->CKM1x1();
    //    getParams(q2);
    norm(1.0);
    left(((((1.0*(-ii))*1.0)*1.0)*(((ee*ii)*conj(CKM1x1))/(sw*sqrt(2.0)))));
    right(0.0);
    if(p1->id()!=-2) {Complex ltemp=left(), rtemp=right(); left(-rtemp); right(-ltemp);}
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
    FFVVertex::doinit();
  }
  //    void getParams(Energy2);
 private:
  FRModelV_V_207 & operator=(const FRModelV_V_207 &);
  //    Complex leftval, rightval, normval;
  tcHwFRModelPtr model_;
};
DescribeClass<FRModelV_V_207,Helicity::FFVVertex>
describeHerwigFRModelV_V_207("Herwig::FRModelV_V_207",
				       "FRModel.so");
// void FRModelV_V_207::getParams(Energy2 ) {
// }

class FRModelV_V_208: public FFVVertex {
 public:
  FRModelV_V_208() {
    kinematics(false);
    addToList(-4,1,24);
  }
  void setCoupling(Energy2 ,tcPDPtr p1,tcPDPtr,tcPDPtr) {
    double ee = model_->ee();
    Complex CKM2x1 = model_->CKM2x1();
    double sw = model_->sw();
    //    getParams(q2);
    norm(1.0);
    left(((((1.0*(-ii))*1.0)*1.0)*(((ee*ii)*conj(CKM2x1))/(sw*sqrt(2.0)))));
    right(0.0);
    if(p1->id()!=-4) {Complex ltemp=left(), rtemp=right(); left(-rtemp); right(-ltemp);}
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
    FFVVertex::doinit();
  }
  //    void getParams(Energy2);
 private:
  FRModelV_V_208 & operator=(const FRModelV_V_208 &);
  //    Complex leftval, rightval, normval;
  tcHwFRModelPtr model_;
};
DescribeClass<FRModelV_V_208,Helicity::FFVVertex>
describeHerwigFRModelV_V_208("Herwig::FRModelV_V_208",
				       "FRModel.so");
// void FRModelV_V_208::getParams(Energy2 ) {
// }

class FRModelV_V_209: public FFVVertex {
 public:
  FRModelV_V_209() {
    kinematics(false);
    addToList(-6,1,24);
  }
  void setCoupling(Energy2 ,tcPDPtr p1,tcPDPtr,tcPDPtr) {
    double ee = model_->ee();
    double sw = model_->sw();
    Complex CKM3x1 = model_->CKM3x1();
    //    getParams(q2);
    norm(1.0);
    left(((((1.0*(-ii))*1.0)*1.0)*(((ee*ii)*conj(CKM3x1))/(sw*sqrt(2.0)))));
    right(0.0);
    if(p1->id()!=-6) {Complex ltemp=left(), rtemp=right(); left(-rtemp); right(-ltemp);}
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
    FFVVertex::doinit();
  }
  //    void getParams(Energy2);
 private:
  FRModelV_V_209 & operator=(const FRModelV_V_209 &);
  //    Complex leftval, rightval, normval;
  tcHwFRModelPtr model_;
};
DescribeClass<FRModelV_V_209,Helicity::FFVVertex>
describeHerwigFRModelV_V_209("Herwig::FRModelV_V_209",
				       "FRModel.so");
// void FRModelV_V_209::getParams(Energy2 ) {
// }

class FRModelV_V_210: public FFVVertex {
 public:
  FRModelV_V_210() {
    kinematics(false);
    addToList(-2,3,24);
  }
  void setCoupling(Energy2 ,tcPDPtr p1,tcPDPtr,tcPDPtr) {
    double ee = model_->ee();
    Complex CKM1x2 = model_->CKM1x2();
    double sw = model_->sw();
    //    getParams(q2);
    norm(1.0);
    left(((((1.0*(-ii))*1.0)*1.0)*(((ee*ii)*conj(CKM1x2))/(sw*sqrt(2.0)))));
    right(0.0);
    if(p1->id()!=-2) {Complex ltemp=left(), rtemp=right(); left(-rtemp); right(-ltemp);}
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
    FFVVertex::doinit();
  }
  //    void getParams(Energy2);
 private:
  FRModelV_V_210 & operator=(const FRModelV_V_210 &);
  //    Complex leftval, rightval, normval;
  tcHwFRModelPtr model_;
};
DescribeClass<FRModelV_V_210,Helicity::FFVVertex>
describeHerwigFRModelV_V_210("Herwig::FRModelV_V_210",
				       "FRModel.so");
// void FRModelV_V_210::getParams(Energy2 ) {
// }

class FRModelV_V_211: public FFVVertex {
 public:
  FRModelV_V_211() {
    kinematics(false);
    addToList(-4,3,24);
  }
  void setCoupling(Energy2 ,tcPDPtr p1,tcPDPtr,tcPDPtr) {
    double ee = model_->ee();
    double sw = model_->sw();
    Complex CKM2x2 = model_->CKM2x2();
    //    getParams(q2);
    norm(1.0);
    left(((((1.0*(-ii))*1.0)*1.0)*(((ee*ii)*conj(CKM2x2))/(sw*sqrt(2.0)))));
    right(0.0);
    if(p1->id()!=-4) {Complex ltemp=left(), rtemp=right(); left(-rtemp); right(-ltemp);}
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
    FFVVertex::doinit();
  }
  //    void getParams(Energy2);
 private:
  FRModelV_V_211 & operator=(const FRModelV_V_211 &);
  //    Complex leftval, rightval, normval;
  tcHwFRModelPtr model_;
};
DescribeClass<FRModelV_V_211,Helicity::FFVVertex>
describeHerwigFRModelV_V_211("Herwig::FRModelV_V_211",
				       "FRModel.so");
// void FRModelV_V_211::getParams(Energy2 ) {
// }

class FRModelV_V_212: public FFVVertex {
 public:
  FRModelV_V_212() {
    kinematics(false);
    addToList(-6,3,24);
  }
  void setCoupling(Energy2 ,tcPDPtr p1,tcPDPtr,tcPDPtr) {
    double ee = model_->ee();
    double sw = model_->sw();
    Complex CKM3x2 = model_->CKM3x2();
    //    getParams(q2);
    norm(1.0);
    left(((((1.0*(-ii))*1.0)*1.0)*(((ee*ii)*conj(CKM3x2))/(sw*sqrt(2.0)))));
    right(0.0);
    if(p1->id()!=-6) {Complex ltemp=left(), rtemp=right(); left(-rtemp); right(-ltemp);}
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
    FFVVertex::doinit();
  }
  //    void getParams(Energy2);
 private:
  FRModelV_V_212 & operator=(const FRModelV_V_212 &);
  //    Complex leftval, rightval, normval;
  tcHwFRModelPtr model_;
};
DescribeClass<FRModelV_V_212,Helicity::FFVVertex>
describeHerwigFRModelV_V_212("Herwig::FRModelV_V_212",
				       "FRModel.so");
// void FRModelV_V_212::getParams(Energy2 ) {
// }

class FRModelV_V_213: public FFVVertex {
 public:
  FRModelV_V_213() {
    kinematics(false);
    addToList(-2,5,24);
  }
  void setCoupling(Energy2 ,tcPDPtr p1,tcPDPtr,tcPDPtr) {
    double ee = model_->ee();
    double sw = model_->sw();
    Complex CKM1x3 = model_->CKM1x3();
    //    getParams(q2);
    norm(1.0);
    left(((((1.0*(-ii))*1.0)*1.0)*(((ee*ii)*conj(CKM1x3))/(sw*sqrt(2.0)))));
    right(0.0);
    if(p1->id()!=-2) {Complex ltemp=left(), rtemp=right(); left(-rtemp); right(-ltemp);}
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
    FFVVertex::doinit();
  }
  //    void getParams(Energy2);
 private:
  FRModelV_V_213 & operator=(const FRModelV_V_213 &);
  //    Complex leftval, rightval, normval;
  tcHwFRModelPtr model_;
};
DescribeClass<FRModelV_V_213,Helicity::FFVVertex>
describeHerwigFRModelV_V_213("Herwig::FRModelV_V_213",
				       "FRModel.so");
// void FRModelV_V_213::getParams(Energy2 ) {
// }

class FRModelV_V_214: public FFVVertex {
 public:
  FRModelV_V_214() {
    kinematics(false);
    addToList(-4,5,24);
  }
  void setCoupling(Energy2 ,tcPDPtr p1,tcPDPtr,tcPDPtr) {
    double ee = model_->ee();
    double sw = model_->sw();
    Complex CKM2x3 = model_->CKM2x3();
    //    getParams(q2);
    norm(1.0);
    left(((((1.0*(-ii))*1.0)*1.0)*(((ee*ii)*conj(CKM2x3))/(sw*sqrt(2.0)))));
    right(0.0);
    if(p1->id()!=-4) {Complex ltemp=left(), rtemp=right(); left(-rtemp); right(-ltemp);}
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
    FFVVertex::doinit();
  }
  //    void getParams(Energy2);
 private:
  FRModelV_V_214 & operator=(const FRModelV_V_214 &);
  //    Complex leftval, rightval, normval;
  tcHwFRModelPtr model_;
};
DescribeClass<FRModelV_V_214,Helicity::FFVVertex>
describeHerwigFRModelV_V_214("Herwig::FRModelV_V_214",
				       "FRModel.so");
// void FRModelV_V_214::getParams(Energy2 ) {
// }

class FRModelV_V_215: public FFVVertex {
 public:
  FRModelV_V_215() {
    kinematics(false);
    addToList(-6,5,24);
  }
  void setCoupling(Energy2 ,tcPDPtr p1,tcPDPtr,tcPDPtr) {
    double ee = model_->ee();
    double sw = model_->sw();
    Complex CKM3x3 = model_->CKM3x3();
    //    getParams(q2);
    norm(1.0);
    left(((((1.0*(-ii))*1.0)*1.0)*(((ee*ii)*conj(CKM3x3))/(sw*sqrt(2.0)))));
    right(0.0);
    if(p1->id()!=-6) {Complex ltemp=left(), rtemp=right(); left(-rtemp); right(-ltemp);}
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
    FFVVertex::doinit();
  }
  //    void getParams(Energy2);
 private:
  FRModelV_V_215 & operator=(const FRModelV_V_215 &);
  //    Complex leftval, rightval, normval;
  tcHwFRModelPtr model_;
};
DescribeClass<FRModelV_V_215,Helicity::FFVVertex>
describeHerwigFRModelV_V_215("Herwig::FRModelV_V_215",
				       "FRModel.so");
// void FRModelV_V_215::getParams(Energy2 ) {
// }

class FRModelV_V_216: public FFVVertex {
 public:
  FRModelV_V_216() {
    kinematics(false);
    addToList(-11,12,-24);
  }
  void setCoupling(Energy2 ,tcPDPtr p1,tcPDPtr,tcPDPtr) {
    double ee = model_->ee();
    double sw = model_->sw();
    //    getParams(q2);
    norm(1.0);
    left(((((1.0*(-ii))*1.0)*1.0)*((ee*ii)/(sw*sqrt(2.0)))));
    right(0.0);
    if(p1->id()!=-11) {Complex ltemp=left(), rtemp=right(); left(-rtemp); right(-ltemp);}
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
    FFVVertex::doinit();
  }
  //    void getParams(Energy2);
 private:
  FRModelV_V_216 & operator=(const FRModelV_V_216 &);
  //    Complex leftval, rightval, normval;
  tcHwFRModelPtr model_;
};
DescribeClass<FRModelV_V_216,Helicity::FFVVertex>
describeHerwigFRModelV_V_216("Herwig::FRModelV_V_216",
				       "FRModel.so");
// void FRModelV_V_216::getParams(Energy2 ) {
// }

class FRModelV_V_217: public FFVVertex {
 public:
  FRModelV_V_217() {
    kinematics(false);
    addToList(-13,14,-24);
  }
  void setCoupling(Energy2 ,tcPDPtr p1,tcPDPtr,tcPDPtr) {
    double ee = model_->ee();
    double sw = model_->sw();
    //    getParams(q2);
    norm(1.0);
    left(((((1.0*(-ii))*1.0)*1.0)*((ee*ii)/(sw*sqrt(2.0)))));
    right(0.0);
    if(p1->id()!=-13) {Complex ltemp=left(), rtemp=right(); left(-rtemp); right(-ltemp);}
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
    FFVVertex::doinit();
  }
  //    void getParams(Energy2);
 private:
  FRModelV_V_217 & operator=(const FRModelV_V_217 &);
  //    Complex leftval, rightval, normval;
  tcHwFRModelPtr model_;
};
DescribeClass<FRModelV_V_217,Helicity::FFVVertex>
describeHerwigFRModelV_V_217("Herwig::FRModelV_V_217",
				       "FRModel.so");
// void FRModelV_V_217::getParams(Energy2 ) {
// }

class FRModelV_V_218: public FFVVertex {
 public:
  FRModelV_V_218() {
    kinematics(false);
    addToList(-15,16,-24);
  }
  void setCoupling(Energy2 ,tcPDPtr p1,tcPDPtr,tcPDPtr) {
    double ee = model_->ee();
    double sw = model_->sw();
    //    getParams(q2);
    norm(1.0);
    left(((((1.0*(-ii))*1.0)*1.0)*((ee*ii)/(sw*sqrt(2.0)))));
    right(0.0);
    if(p1->id()!=-15) {Complex ltemp=left(), rtemp=right(); left(-rtemp); right(-ltemp);}
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
    FFVVertex::doinit();
  }
  //    void getParams(Energy2);
 private:
  FRModelV_V_218 & operator=(const FRModelV_V_218 &);
  //    Complex leftval, rightval, normval;
  tcHwFRModelPtr model_;
};
DescribeClass<FRModelV_V_218,Helicity::FFVVertex>
describeHerwigFRModelV_V_218("Herwig::FRModelV_V_218",
				       "FRModel.so");
// void FRModelV_V_218::getParams(Energy2 ) {
// }

class FRModelV_V_219: public FFVVertex {
 public:
  FRModelV_V_219() {
    kinematics(false);
    addToList(-12,11,24);
  }
  void setCoupling(Energy2 ,tcPDPtr p1,tcPDPtr,tcPDPtr) {
    double ee = model_->ee();
    double sw = model_->sw();
    //    getParams(q2);
    norm(1.0);
    left(((((1.0*(-ii))*1.0)*1.0)*((ee*ii)/(sw*sqrt(2.0)))));
    right(0.0);
    if(p1->id()!=-12) {Complex ltemp=left(), rtemp=right(); left(-rtemp); right(-ltemp);}
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
    FFVVertex::doinit();
  }
  //    void getParams(Energy2);
 private:
  FRModelV_V_219 & operator=(const FRModelV_V_219 &);
  //    Complex leftval, rightval, normval;
  tcHwFRModelPtr model_;
};
DescribeClass<FRModelV_V_219,Helicity::FFVVertex>
describeHerwigFRModelV_V_219("Herwig::FRModelV_V_219",
				       "FRModel.so");
// void FRModelV_V_219::getParams(Energy2 ) {
// }

class FRModelV_V_220: public FFVVertex {
 public:
  FRModelV_V_220() {
    kinematics(false);
    addToList(-14,13,24);
  }
  void setCoupling(Energy2 ,tcPDPtr p1,tcPDPtr,tcPDPtr) {
    double ee = model_->ee();
    double sw = model_->sw();
    //    getParams(q2);
    norm(1.0);
    left(((((1.0*(-ii))*1.0)*1.0)*((ee*ii)/(sw*sqrt(2.0)))));
    right(0.0);
    if(p1->id()!=-14) {Complex ltemp=left(), rtemp=right(); left(-rtemp); right(-ltemp);}
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
    FFVVertex::doinit();
  }
  //    void getParams(Energy2);
 private:
  FRModelV_V_220 & operator=(const FRModelV_V_220 &);
  //    Complex leftval, rightval, normval;
  tcHwFRModelPtr model_;
};
DescribeClass<FRModelV_V_220,Helicity::FFVVertex>
describeHerwigFRModelV_V_220("Herwig::FRModelV_V_220",
				       "FRModel.so");
// void FRModelV_V_220::getParams(Energy2 ) {
// }

class FRModelV_V_221: public FFVVertex {
 public:
  FRModelV_V_221() {
    kinematics(false);
    addToList(-16,15,24);
  }
  void setCoupling(Energy2 ,tcPDPtr p1,tcPDPtr,tcPDPtr) {
    double ee = model_->ee();
    double sw = model_->sw();
    //    getParams(q2);
    norm(1.0);
    left(((((1.0*(-ii))*1.0)*1.0)*((ee*ii)/(sw*sqrt(2.0)))));
    right(0.0);
    if(p1->id()!=-16) {Complex ltemp=left(), rtemp=right(); left(-rtemp); right(-ltemp);}
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
    FFVVertex::doinit();
  }
  //    void getParams(Energy2);
 private:
  FRModelV_V_221 & operator=(const FRModelV_V_221 &);
  //    Complex leftval, rightval, normval;
  tcHwFRModelPtr model_;
};
DescribeClass<FRModelV_V_221,Helicity::FFVVertex>
describeHerwigFRModelV_V_221("Herwig::FRModelV_V_221",
				       "FRModel.so");
// void FRModelV_V_221::getParams(Energy2 ) {
// }

class FRModelV_V_222: public FFVVertex {
 public:
  FRModelV_V_222() {
    kinematics(false);
    addToList(-2,2,23);
  }
  void setCoupling(Energy2 ,tcPDPtr p1,tcPDPtr,tcPDPtr) {
    double ee = model_->ee();
    double cw = model_->cw();
    double sw = model_->sw();
    //    getParams(q2);
    norm(1.0);
    left((((((1.0*(-ii))*1.0)*1.0)*((-((ee*ii)*sw))/(6.0*cw)))+((((1.0*(-ii))*1.0)*1.0)*(((cw*ee)*ii)/(2.0*sw)))));
    right(((((1.0*(-ii))*1.0)*4.0)*((-((ee*ii)*sw))/(6.0*cw))));
    if(p1->id()!=-2) {Complex ltemp=left(), rtemp=right(); left(-rtemp); right(-ltemp);}
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
    FFVVertex::doinit();
  }
  //    void getParams(Energy2);
 private:
  FRModelV_V_222 & operator=(const FRModelV_V_222 &);
  //    Complex leftval, rightval, normval;
  tcHwFRModelPtr model_;
};
DescribeClass<FRModelV_V_222,Helicity::FFVVertex>
describeHerwigFRModelV_V_222("Herwig::FRModelV_V_222",
				       "FRModel.so");
// void FRModelV_V_222::getParams(Energy2 ) {
// }

class FRModelV_V_223: public FFVVertex {
 public:
  FRModelV_V_223() {
    kinematics(false);
    addToList(-4,4,23);
  }
  void setCoupling(Energy2 ,tcPDPtr p1,tcPDPtr,tcPDPtr) {
    double ee = model_->ee();
    double cw = model_->cw();
    double sw = model_->sw();
    //    getParams(q2);
    norm(1.0);
    left((((((1.0*(-ii))*1.0)*1.0)*((-((ee*ii)*sw))/(6.0*cw)))+((((1.0*(-ii))*1.0)*1.0)*(((cw*ee)*ii)/(2.0*sw)))));
    right(((((1.0*(-ii))*1.0)*4.0)*((-((ee*ii)*sw))/(6.0*cw))));
    if(p1->id()!=-4) {Complex ltemp=left(), rtemp=right(); left(-rtemp); right(-ltemp);}
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
    FFVVertex::doinit();
  }
  //    void getParams(Energy2);
 private:
  FRModelV_V_223 & operator=(const FRModelV_V_223 &);
  //    Complex leftval, rightval, normval;
  tcHwFRModelPtr model_;
};
DescribeClass<FRModelV_V_223,Helicity::FFVVertex>
describeHerwigFRModelV_V_223("Herwig::FRModelV_V_223",
				       "FRModel.so");
// void FRModelV_V_223::getParams(Energy2 ) {
// }

class FRModelV_V_224: public FFVVertex {
 public:
  FRModelV_V_224() {
    kinematics(false);
    addToList(-6,6,23);
  }
  void setCoupling(Energy2 ,tcPDPtr p1,tcPDPtr,tcPDPtr) {
    double ee = model_->ee();
    double cw = model_->cw();
    double sw = model_->sw();
    //    getParams(q2);
    norm(1.0);
    left((((((1.0*(-ii))*1.0)*1.0)*((-((ee*ii)*sw))/(6.0*cw)))+((((1.0*(-ii))*1.0)*1.0)*(((cw*ee)*ii)/(2.0*sw)))));
    right(((((1.0*(-ii))*1.0)*4.0)*((-((ee*ii)*sw))/(6.0*cw))));
    if(p1->id()!=-6) {Complex ltemp=left(), rtemp=right(); left(-rtemp); right(-ltemp);}
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
    FFVVertex::doinit();
  }
  //    void getParams(Energy2);
 private:
  FRModelV_V_224 & operator=(const FRModelV_V_224 &);
  //    Complex leftval, rightval, normval;
  tcHwFRModelPtr model_;
};
DescribeClass<FRModelV_V_224,Helicity::FFVVertex>
describeHerwigFRModelV_V_224("Herwig::FRModelV_V_224",
				       "FRModel.so");
// void FRModelV_V_224::getParams(Energy2 ) {
// }

class FRModelV_V_225: public FFVVertex {
 public:
  FRModelV_V_225() {
    kinematics(false);
    addToList(-1,1,23);
  }
  void setCoupling(Energy2 ,tcPDPtr p1,tcPDPtr,tcPDPtr) {
    double ee = model_->ee();
    double cw = model_->cw();
    double sw = model_->sw();
    //    getParams(q2);
    norm(1.0);
    left((((((1.0*(-ii))*1.0)*1.0)*((-((ee*ii)*sw))/(6.0*cw)))+((((1.0*(-ii))*1.0)*1.0)*((-((cw*ee)*ii))/(2.0*sw)))));
    right(((((1.0*(-ii))*1.0)*-2.0)*((-((ee*ii)*sw))/(6.0*cw))));
    if(p1->id()!=-1) {Complex ltemp=left(), rtemp=right(); left(-rtemp); right(-ltemp);}
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
    FFVVertex::doinit();
  }
  //    void getParams(Energy2);
 private:
  FRModelV_V_225 & operator=(const FRModelV_V_225 &);
  //    Complex leftval, rightval, normval;
  tcHwFRModelPtr model_;
};
DescribeClass<FRModelV_V_225,Helicity::FFVVertex>
describeHerwigFRModelV_V_225("Herwig::FRModelV_V_225",
				       "FRModel.so");
// void FRModelV_V_225::getParams(Energy2 ) {
// }

}

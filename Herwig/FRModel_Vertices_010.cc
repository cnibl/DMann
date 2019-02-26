// -*- C++ -*-
//
// FRModelV_V_233.cc is a part of Herwig - A multi-purpose Monte Carlo event generator
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

  class FRModelV_V_226: public FFVVertex {
 public:
  FRModelV_V_226() {
    kinematics(false);
    addToList(-3,3,23);
  }
  void setCoupling(Energy2 ,tcPDPtr p1,tcPDPtr,tcPDPtr) {
    double ee = model_->ee();
    double cw = model_->cw();
    double sw = model_->sw();
    //    getParams(q2);
    norm(1.0);
    left((((((1.0*(-ii))*1.0)*1.0)*((-((ee*ii)*sw))/(6.0*cw)))+((((1.0*(-ii))*1.0)*1.0)*((-((cw*ee)*ii))/(2.0*sw)))));
    right(((((1.0*(-ii))*1.0)*-2.0)*((-((ee*ii)*sw))/(6.0*cw))));
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
  FRModelV_V_226 & operator=(const FRModelV_V_226 &);
  //    Complex leftval, rightval, normval;
  tcHwFRModelPtr model_;
};
DescribeClass<FRModelV_V_226,Helicity::FFVVertex>
describeHerwigFRModelV_V_226("Herwig::FRModelV_V_226",
				       "FRModel.so");
// void FRModelV_V_226::getParams(Energy2 ) {
// }

class FRModelV_V_227: public FFVVertex {
 public:
  FRModelV_V_227() {
    kinematics(false);
    addToList(-5,5,23);
  }
  void setCoupling(Energy2 ,tcPDPtr p1,tcPDPtr,tcPDPtr) {
    double ee = model_->ee();
    double cw = model_->cw();
    double sw = model_->sw();
    //    getParams(q2);
    norm(1.0);
    left((((((1.0*(-ii))*1.0)*1.0)*((-((ee*ii)*sw))/(6.0*cw)))+((((1.0*(-ii))*1.0)*1.0)*((-((cw*ee)*ii))/(2.0*sw)))));
    right(((((1.0*(-ii))*1.0)*-2.0)*((-((ee*ii)*sw))/(6.0*cw))));
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
  FRModelV_V_227 & operator=(const FRModelV_V_227 &);
  //    Complex leftval, rightval, normval;
  tcHwFRModelPtr model_;
};
DescribeClass<FRModelV_V_227,Helicity::FFVVertex>
describeHerwigFRModelV_V_227("Herwig::FRModelV_V_227",
				       "FRModel.so");
// void FRModelV_V_227::getParams(Energy2 ) {
// }

class FRModelV_V_228: public FFVVertex {
 public:
  FRModelV_V_228() {
    kinematics(false);
    addToList(-12,12,23);
  }
  void setCoupling(Energy2 ,tcPDPtr p1,tcPDPtr,tcPDPtr) {
    double ee = model_->ee();
    double cw = model_->cw();
    double sw = model_->sw();
    //    getParams(q2);
    norm(1.0);
    left(((((1.0*(-ii))*1.0)*1.0)*((((cw*ee)*ii)/(2.0*sw))+(((ee*ii)*sw)/(2.0*cw)))));
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
  FRModelV_V_228 & operator=(const FRModelV_V_228 &);
  //    Complex leftval, rightval, normval;
  tcHwFRModelPtr model_;
};
DescribeClass<FRModelV_V_228,Helicity::FFVVertex>
describeHerwigFRModelV_V_228("Herwig::FRModelV_V_228",
				       "FRModel.so");
// void FRModelV_V_228::getParams(Energy2 ) {
// }

class FRModelV_V_229: public FFVVertex {
 public:
  FRModelV_V_229() {
    kinematics(false);
    addToList(-14,14,23);
  }
  void setCoupling(Energy2 ,tcPDPtr p1,tcPDPtr,tcPDPtr) {
    double ee = model_->ee();
    double cw = model_->cw();
    double sw = model_->sw();
    //    getParams(q2);
    norm(1.0);
    left(((((1.0*(-ii))*1.0)*1.0)*((((cw*ee)*ii)/(2.0*sw))+(((ee*ii)*sw)/(2.0*cw)))));
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
  FRModelV_V_229 & operator=(const FRModelV_V_229 &);
  //    Complex leftval, rightval, normval;
  tcHwFRModelPtr model_;
};
DescribeClass<FRModelV_V_229,Helicity::FFVVertex>
describeHerwigFRModelV_V_229("Herwig::FRModelV_V_229",
				       "FRModel.so");
// void FRModelV_V_229::getParams(Energy2 ) {
// }

class FRModelV_V_230: public FFVVertex {
 public:
  FRModelV_V_230() {
    kinematics(false);
    addToList(-16,16,23);
  }
  void setCoupling(Energy2 ,tcPDPtr p1,tcPDPtr,tcPDPtr) {
    double ee = model_->ee();
    double cw = model_->cw();
    double sw = model_->sw();
    //    getParams(q2);
    norm(1.0);
    left(((((1.0*(-ii))*1.0)*1.0)*((((cw*ee)*ii)/(2.0*sw))+(((ee*ii)*sw)/(2.0*cw)))));
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
  FRModelV_V_230 & operator=(const FRModelV_V_230 &);
  //    Complex leftval, rightval, normval;
  tcHwFRModelPtr model_;
};
DescribeClass<FRModelV_V_230,Helicity::FFVVertex>
describeHerwigFRModelV_V_230("Herwig::FRModelV_V_230",
				       "FRModel.so");
// void FRModelV_V_230::getParams(Energy2 ) {
// }

class FRModelV_V_231: public FFVVertex {
 public:
  FRModelV_V_231() {
    kinematics(false);
    addToList(-11,11,23);
  }
  void setCoupling(Energy2 ,tcPDPtr p1,tcPDPtr,tcPDPtr) {
    double ee = model_->ee();
    double cw = model_->cw();
    double sw = model_->sw();
    //    getParams(q2);
    norm(1.0);
    left((((((1.0*(-ii))*1.0)*1.0)*(((ee*ii)*sw)/(2.0*cw)))+((((1.0*(-ii))*1.0)*1.0)*((-((cw*ee)*ii))/(2.0*sw)))));
    right(((((1.0*(-ii))*1.0)*2.0)*(((ee*ii)*sw)/(2.0*cw))));
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
  FRModelV_V_231 & operator=(const FRModelV_V_231 &);
  //    Complex leftval, rightval, normval;
  tcHwFRModelPtr model_;
};
DescribeClass<FRModelV_V_231,Helicity::FFVVertex>
describeHerwigFRModelV_V_231("Herwig::FRModelV_V_231",
				       "FRModel.so");
// void FRModelV_V_231::getParams(Energy2 ) {
// }

class FRModelV_V_232: public FFVVertex {
 public:
  FRModelV_V_232() {
    kinematics(false);
    addToList(-13,13,23);
  }
  void setCoupling(Energy2 ,tcPDPtr p1,tcPDPtr,tcPDPtr) {
    double ee = model_->ee();
    double cw = model_->cw();
    double sw = model_->sw();
    //    getParams(q2);
    norm(1.0);
    left((((((1.0*(-ii))*1.0)*1.0)*(((ee*ii)*sw)/(2.0*cw)))+((((1.0*(-ii))*1.0)*1.0)*((-((cw*ee)*ii))/(2.0*sw)))));
    right(((((1.0*(-ii))*1.0)*2.0)*(((ee*ii)*sw)/(2.0*cw))));
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
  FRModelV_V_232 & operator=(const FRModelV_V_232 &);
  //    Complex leftval, rightval, normval;
  tcHwFRModelPtr model_;
};
DescribeClass<FRModelV_V_232,Helicity::FFVVertex>
describeHerwigFRModelV_V_232("Herwig::FRModelV_V_232",
				       "FRModel.so");
// void FRModelV_V_232::getParams(Energy2 ) {
// }

class FRModelV_V_233: public FFVVertex {
 public:
  FRModelV_V_233() {
    kinematics(false);
    addToList(-15,15,23);
  }
  void setCoupling(Energy2 ,tcPDPtr p1,tcPDPtr,tcPDPtr) {
    double ee = model_->ee();
    double cw = model_->cw();
    double sw = model_->sw();
    //    getParams(q2);
    norm(1.0);
    left((((((1.0*(-ii))*1.0)*1.0)*(((ee*ii)*sw)/(2.0*cw)))+((((1.0*(-ii))*1.0)*1.0)*((-((cw*ee)*ii))/(2.0*sw)))));
    right(((((1.0*(-ii))*1.0)*2.0)*(((ee*ii)*sw)/(2.0*cw))));
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
  FRModelV_V_233 & operator=(const FRModelV_V_233 &);
  //    Complex leftval, rightval, normval;
  tcHwFRModelPtr model_;
};
DescribeClass<FRModelV_V_233,Helicity::FFVVertex>
describeHerwigFRModelV_V_233("Herwig::FRModelV_V_233",
				       "FRModel.so");
// void FRModelV_V_233::getParams(Energy2 ) {
// }

}

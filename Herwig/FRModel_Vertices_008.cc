// -*- C++ -*-
//
// FRModelV_V_200.cc is a part of Herwig - A multi-purpose Monte Carlo event generator
// Copyright (C) 2002-2007 The Herwig Collaboration
//
// Herwig is licenced under version 2 of the GPL, see COPYING for details.
// Please respect the MCnet academic guidelines, see GUIDELINES for details.

#include "FRModel.h"
#include "ThePEG/Helicity/Vertex/Vector/VVVVVertex.h"
#include "ThePEG/Helicity/Vertex/Vector/FFVVertex.h"
#include "ThePEG/Helicity/Vertex/Scalar/VVSVertex.h"
#include "ThePEG/Helicity/Vertex/Scalar/VVSSVertex.h"

#include "ThePEG/Utilities/DescribeClass.h"
#include "ThePEG/Persistency/PersistentOStream.h"
#include "ThePEG/Persistency/PersistentIStream.h"

namespace Herwig 
{
  using namespace ThePEG;
  using namespace ThePEG::Helicity;
  using ThePEG::Constants::pi;

  class FRModelV_V_176: public VVSVertex {
 public:
  FRModelV_V_176() {
    kinematics(false);
    addToList(23,23,25);
  }
  void setCoupling(Energy2 ,tcPDPtr,tcPDPtr,tcPDPtr) {
    double ee = model_->ee();
    double vev = model_->vev();
    double cw = model_->cw();
    double sw = model_->sw();
    //    getParams(q2);
    norm(Complex((((((1.0*(-ii))*1.0)*((((sqr(ee)*ii)*vev)+((((sqr(cw)*sqr(ee))*ii)*vev)/(2.0*sqr(sw))))+((((sqr(ee)*ii)*sqr(sw))*vev)/(2.0*sqr(cw)))))*1.0)) * GeV / UnitRemoval::E));
    
    
    
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
  FRModelV_V_176 & operator=(const FRModelV_V_176 &);
  //    Complex leftval, rightval, normval;
  tcHwFRModelPtr model_;
};
DescribeClass<FRModelV_V_176,Helicity::VVSVertex>
describeHerwigFRModelV_V_176("Herwig::FRModelV_V_176",
				       "FRModel.so");
// void FRModelV_V_176::getParams(Energy2 ) {
// }

class FRModelV_V_180: public VVSSVertex {
 public:
  FRModelV_V_180() {
    kinematics(false);
    addToList(23,23,25,9000006);
  }
  void setCoupling(Energy2 ,tcPDPtr,tcPDPtr,tcPDPtr,tcPDPtr) {
    double vev = model_->vev();
    double ee = model_->ee();
    double cw = model_->cw();
    double gSh1 = model_->gSh1();
    double sw = model_->sw();
    double Lambda = model_->Lambda();
    //    getParams(q2);
    norm((((1.0*(-ii))*1.0)*((((((sqr(ee)*ii)*gSh1)*vev)/Lambda)+(((((sqr(cw)*sqr(ee))*ii)*gSh1)*vev)/((2.0*Lambda)*sqr(sw))))+(((((sqr(ee)*ii)*gSh1)*sqr(sw))*vev)/((2.0*sqr(cw))*Lambda)))));
    
    
    
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
  FRModelV_V_180 & operator=(const FRModelV_V_180 &);
  //    Complex leftval, rightval, normval;
  tcHwFRModelPtr model_;
};
DescribeClass<FRModelV_V_180,Helicity::VVSSVertex>
describeHerwigFRModelV_V_180("Herwig::FRModelV_V_180",
				       "FRModel.so");
// void FRModelV_V_180::getParams(Energy2 ) {
// }

class FRModelV_V_181: public VVVVVertex {
 public:
  FRModelV_V_181() {
    kinematics(false);
    addToList(-24,24,23,23);
  }
  void setCoupling(Energy2 ,tcPDPtr p1,tcPDPtr p2,tcPDPtr p3,tcPDPtr p4) {
    double ee = model_->ee();
    double cw = model_->cw();
    double sw = model_->sw();
    //    getParams(q2);
    norm(((((1.0*ii)*1.0)*-1.0)*(((sqr(cw)*sqr(ee))*ii)/sqr(sw))));
    
    
    bool done[4]={false,false,false,false};
    tcPDPtr part[4]={p1,p2,p3,p4};
    unsigned int iorder[4]={0,0,0,0};
    for(unsigned int ix=0;ix<4;++ix) {
       if(!done[0] && part[ix]->id()==-24) {done[0]=true; iorder[0] = ix; continue;}
       if(!done[1] && part[ix]->id()==24) {done[1]=true; iorder[1] = ix; continue;}
       if(!done[2] && part[ix]->id()==23) {done[2]=true; iorder[2] = ix; continue;}
       if(!done[3] && part[ix]->id()==23) {done[3]=true; iorder[3] = ix; continue;}
    }
    setType(2);
    setOrder(iorder[0],iorder[1],iorder[2],iorder[3]);
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
    VVVVVertex::doinit();
  }
  //    void getParams(Energy2);
 private:
  FRModelV_V_181 & operator=(const FRModelV_V_181 &);
  //    Complex leftval, rightval, normval;
  tcHwFRModelPtr model_;
};
DescribeClass<FRModelV_V_181,Helicity::VVVVVertex>
describeHerwigFRModelV_V_181("Herwig::FRModelV_V_181",
				       "FRModel.so");
// void FRModelV_V_181::getParams(Energy2 ) {
// }

class FRModelV_V_183: public FFVVertex {
 public:
  FRModelV_V_183() {
    kinematics(false);
    addToList(-11,11,22);
  }
  void setCoupling(Energy2 ,tcPDPtr p1,tcPDPtr,tcPDPtr) {
    double ee = model_->ee();
    //    getParams(q2);
    norm(1.0);
    left(((((1.0*(-ii))*1.0)*1.0)*(-(ee*ii))));
    right(((((1.0*(-ii))*1.0)*1.0)*(-(ee*ii))));
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
  FRModelV_V_183 & operator=(const FRModelV_V_183 &);
  //    Complex leftval, rightval, normval;
  tcHwFRModelPtr model_;
};
DescribeClass<FRModelV_V_183,Helicity::FFVVertex>
describeHerwigFRModelV_V_183("Herwig::FRModelV_V_183",
				       "FRModel.so");
// void FRModelV_V_183::getParams(Energy2 ) {
// }

class FRModelV_V_184: public FFVVertex {
 public:
  FRModelV_V_184() {
    kinematics(false);
    addToList(-13,13,22);
  }
  void setCoupling(Energy2 ,tcPDPtr p1,tcPDPtr,tcPDPtr) {
    double ee = model_->ee();
    //    getParams(q2);
    norm(1.0);
    left(((((1.0*(-ii))*1.0)*1.0)*(-(ee*ii))));
    right(((((1.0*(-ii))*1.0)*1.0)*(-(ee*ii))));
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
  FRModelV_V_184 & operator=(const FRModelV_V_184 &);
  //    Complex leftval, rightval, normval;
  tcHwFRModelPtr model_;
};
DescribeClass<FRModelV_V_184,Helicity::FFVVertex>
describeHerwigFRModelV_V_184("Herwig::FRModelV_V_184",
				       "FRModel.so");
// void FRModelV_V_184::getParams(Energy2 ) {
// }

class FRModelV_V_185: public FFVVertex {
 public:
  FRModelV_V_185() {
    kinematics(false);
    addToList(-15,15,22);
  }
  void setCoupling(Energy2 ,tcPDPtr p1,tcPDPtr,tcPDPtr) {
    double ee = model_->ee();
    //    getParams(q2);
    norm(1.0);
    left(((((1.0*(-ii))*1.0)*1.0)*(-(ee*ii))));
    right(((((1.0*(-ii))*1.0)*1.0)*(-(ee*ii))));
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
  FRModelV_V_185 & operator=(const FRModelV_V_185 &);
  //    Complex leftval, rightval, normval;
  tcHwFRModelPtr model_;
};
DescribeClass<FRModelV_V_185,Helicity::FFVVertex>
describeHerwigFRModelV_V_185("Herwig::FRModelV_V_185",
				       "FRModel.so");
// void FRModelV_V_185::getParams(Energy2 ) {
// }

class FRModelV_V_186: public FFVVertex {
 public:
  FRModelV_V_186() {
    kinematics(false);
    addToList(-2,2,22);
  }
  void setCoupling(Energy2 ,tcPDPtr p1,tcPDPtr,tcPDPtr) {
    double ee = model_->ee();
    //    getParams(q2);
    norm(1.0);
    left(((((1.0*(-ii))*1.0)*1.0)*(((2.0*ee)*ii)/3.0)));
    right(((((1.0*(-ii))*1.0)*1.0)*(((2.0*ee)*ii)/3.0)));
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
  FRModelV_V_186 & operator=(const FRModelV_V_186 &);
  //    Complex leftval, rightval, normval;
  tcHwFRModelPtr model_;
};
DescribeClass<FRModelV_V_186,Helicity::FFVVertex>
describeHerwigFRModelV_V_186("Herwig::FRModelV_V_186",
				       "FRModel.so");
// void FRModelV_V_186::getParams(Energy2 ) {
// }

class FRModelV_V_187: public FFVVertex {
 public:
  FRModelV_V_187() {
    kinematics(false);
    addToList(-4,4,22);
  }
  void setCoupling(Energy2 ,tcPDPtr p1,tcPDPtr,tcPDPtr) {
    double ee = model_->ee();
    //    getParams(q2);
    norm(1.0);
    left(((((1.0*(-ii))*1.0)*1.0)*(((2.0*ee)*ii)/3.0)));
    right(((((1.0*(-ii))*1.0)*1.0)*(((2.0*ee)*ii)/3.0)));
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
  FRModelV_V_187 & operator=(const FRModelV_V_187 &);
  //    Complex leftval, rightval, normval;
  tcHwFRModelPtr model_;
};
DescribeClass<FRModelV_V_187,Helicity::FFVVertex>
describeHerwigFRModelV_V_187("Herwig::FRModelV_V_187",
				       "FRModel.so");
// void FRModelV_V_187::getParams(Energy2 ) {
// }

class FRModelV_V_188: public FFVVertex {
 public:
  FRModelV_V_188() {
    kinematics(false);
    addToList(-6,6,22);
  }
  void setCoupling(Energy2 ,tcPDPtr p1,tcPDPtr,tcPDPtr) {
    double ee = model_->ee();
    //    getParams(q2);
    norm(1.0);
    left(((((1.0*(-ii))*1.0)*1.0)*(((2.0*ee)*ii)/3.0)));
    right(((((1.0*(-ii))*1.0)*1.0)*(((2.0*ee)*ii)/3.0)));
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
  FRModelV_V_188 & operator=(const FRModelV_V_188 &);
  //    Complex leftval, rightval, normval;
  tcHwFRModelPtr model_;
};
DescribeClass<FRModelV_V_188,Helicity::FFVVertex>
describeHerwigFRModelV_V_188("Herwig::FRModelV_V_188",
				       "FRModel.so");
// void FRModelV_V_188::getParams(Energy2 ) {
// }

class FRModelV_V_189: public FFVVertex {
 public:
  FRModelV_V_189() {
    kinematics(false);
    addToList(-1,1,22);
  }
  void setCoupling(Energy2 ,tcPDPtr p1,tcPDPtr,tcPDPtr) {
    double ee = model_->ee();
    //    getParams(q2);
    norm(1.0);
    left(((((1.0*(-ii))*1.0)*1.0)*((-(ee*ii))/3.0)));
    right(((((1.0*(-ii))*1.0)*1.0)*((-(ee*ii))/3.0)));
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
  FRModelV_V_189 & operator=(const FRModelV_V_189 &);
  //    Complex leftval, rightval, normval;
  tcHwFRModelPtr model_;
};
DescribeClass<FRModelV_V_189,Helicity::FFVVertex>
describeHerwigFRModelV_V_189("Herwig::FRModelV_V_189",
				       "FRModel.so");
// void FRModelV_V_189::getParams(Energy2 ) {
// }

class FRModelV_V_190: public FFVVertex {
 public:
  FRModelV_V_190() {
    kinematics(false);
    addToList(-3,3,22);
  }
  void setCoupling(Energy2 ,tcPDPtr p1,tcPDPtr,tcPDPtr) {
    double ee = model_->ee();
    //    getParams(q2);
    norm(1.0);
    left(((((1.0*(-ii))*1.0)*1.0)*((-(ee*ii))/3.0)));
    right(((((1.0*(-ii))*1.0)*1.0)*((-(ee*ii))/3.0)));
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
  FRModelV_V_190 & operator=(const FRModelV_V_190 &);
  //    Complex leftval, rightval, normval;
  tcHwFRModelPtr model_;
};
DescribeClass<FRModelV_V_190,Helicity::FFVVertex>
describeHerwigFRModelV_V_190("Herwig::FRModelV_V_190",
				       "FRModel.so");
// void FRModelV_V_190::getParams(Energy2 ) {
// }

class FRModelV_V_191: public FFVVertex {
 public:
  FRModelV_V_191() {
    kinematics(false);
    addToList(-5,5,22);
  }
  void setCoupling(Energy2 ,tcPDPtr p1,tcPDPtr,tcPDPtr) {
    double ee = model_->ee();
    //    getParams(q2);
    norm(1.0);
    left(((((1.0*(-ii))*1.0)*1.0)*((-(ee*ii))/3.0)));
    right(((((1.0*(-ii))*1.0)*1.0)*((-(ee*ii))/3.0)));
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
  FRModelV_V_191 & operator=(const FRModelV_V_191 &);
  //    Complex leftval, rightval, normval;
  tcHwFRModelPtr model_;
};
DescribeClass<FRModelV_V_191,Helicity::FFVVertex>
describeHerwigFRModelV_V_191("Herwig::FRModelV_V_191",
				       "FRModel.so");
// void FRModelV_V_191::getParams(Energy2 ) {
// }

class FRModelV_V_192: public FFVVertex {
 public:
  FRModelV_V_192() {
    kinematics(false);
    addToList(-2,2,21);
  }
  void setCoupling(Energy2 ,tcPDPtr p1,tcPDPtr,tcPDPtr) {
    double G = model_->G();
    //    getParams(q2);
    norm(1.0);
    left(((((1.0*(-ii))*1.0)*1.0)*(ii*G)));
    right(((((1.0*(-ii))*1.0)*1.0)*(ii*G)));
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
    
    
    orderInGem(0);
    orderInGs(1);
    FFVVertex::doinit();
  }
  //    void getParams(Energy2);
 private:
  FRModelV_V_192 & operator=(const FRModelV_V_192 &);
  //    Complex leftval, rightval, normval;
  tcHwFRModelPtr model_;
};
DescribeClass<FRModelV_V_192,Helicity::FFVVertex>
describeHerwigFRModelV_V_192("Herwig::FRModelV_V_192",
				       "FRModel.so");
// void FRModelV_V_192::getParams(Energy2 ) {
// }

class FRModelV_V_193: public FFVVertex {
 public:
  FRModelV_V_193() {
    kinematics(false);
    addToList(-4,4,21);
  }
  void setCoupling(Energy2 ,tcPDPtr p1,tcPDPtr,tcPDPtr) {
    double G = model_->G();
    //    getParams(q2);
    norm(1.0);
    left(((((1.0*(-ii))*1.0)*1.0)*(ii*G)));
    right(((((1.0*(-ii))*1.0)*1.0)*(ii*G)));
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
    
    
    orderInGem(0);
    orderInGs(1);
    FFVVertex::doinit();
  }
  //    void getParams(Energy2);
 private:
  FRModelV_V_193 & operator=(const FRModelV_V_193 &);
  //    Complex leftval, rightval, normval;
  tcHwFRModelPtr model_;
};
DescribeClass<FRModelV_V_193,Helicity::FFVVertex>
describeHerwigFRModelV_V_193("Herwig::FRModelV_V_193",
				       "FRModel.so");
// void FRModelV_V_193::getParams(Energy2 ) {
// }

class FRModelV_V_194: public FFVVertex {
 public:
  FRModelV_V_194() {
    kinematics(false);
    addToList(-6,6,21);
  }
  void setCoupling(Energy2 ,tcPDPtr p1,tcPDPtr,tcPDPtr) {
    double G = model_->G();
    //    getParams(q2);
    norm(1.0);
    left(((((1.0*(-ii))*1.0)*1.0)*(ii*G)));
    right(((((1.0*(-ii))*1.0)*1.0)*(ii*G)));
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
    
    
    orderInGem(0);
    orderInGs(1);
    FFVVertex::doinit();
  }
  //    void getParams(Energy2);
 private:
  FRModelV_V_194 & operator=(const FRModelV_V_194 &);
  //    Complex leftval, rightval, normval;
  tcHwFRModelPtr model_;
};
DescribeClass<FRModelV_V_194,Helicity::FFVVertex>
describeHerwigFRModelV_V_194("Herwig::FRModelV_V_194",
				       "FRModel.so");
// void FRModelV_V_194::getParams(Energy2 ) {
// }

class FRModelV_V_195: public FFVVertex {
 public:
  FRModelV_V_195() {
    kinematics(false);
    addToList(-1,1,21);
  }
  void setCoupling(Energy2 ,tcPDPtr p1,tcPDPtr,tcPDPtr) {
    double G = model_->G();
    //    getParams(q2);
    norm(1.0);
    left(((((1.0*(-ii))*1.0)*1.0)*(ii*G)));
    right(((((1.0*(-ii))*1.0)*1.0)*(ii*G)));
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
    
    
    orderInGem(0);
    orderInGs(1);
    FFVVertex::doinit();
  }
  //    void getParams(Energy2);
 private:
  FRModelV_V_195 & operator=(const FRModelV_V_195 &);
  //    Complex leftval, rightval, normval;
  tcHwFRModelPtr model_;
};
DescribeClass<FRModelV_V_195,Helicity::FFVVertex>
describeHerwigFRModelV_V_195("Herwig::FRModelV_V_195",
				       "FRModel.so");
// void FRModelV_V_195::getParams(Energy2 ) {
// }

class FRModelV_V_196: public FFVVertex {
 public:
  FRModelV_V_196() {
    kinematics(false);
    addToList(-3,3,21);
  }
  void setCoupling(Energy2 ,tcPDPtr p1,tcPDPtr,tcPDPtr) {
    double G = model_->G();
    //    getParams(q2);
    norm(1.0);
    left(((((1.0*(-ii))*1.0)*1.0)*(ii*G)));
    right(((((1.0*(-ii))*1.0)*1.0)*(ii*G)));
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
    
    
    orderInGem(0);
    orderInGs(1);
    FFVVertex::doinit();
  }
  //    void getParams(Energy2);
 private:
  FRModelV_V_196 & operator=(const FRModelV_V_196 &);
  //    Complex leftval, rightval, normval;
  tcHwFRModelPtr model_;
};
DescribeClass<FRModelV_V_196,Helicity::FFVVertex>
describeHerwigFRModelV_V_196("Herwig::FRModelV_V_196",
				       "FRModel.so");
// void FRModelV_V_196::getParams(Energy2 ) {
// }

class FRModelV_V_197: public FFVVertex {
 public:
  FRModelV_V_197() {
    kinematics(false);
    addToList(-5,5,21);
  }
  void setCoupling(Energy2 ,tcPDPtr p1,tcPDPtr,tcPDPtr) {
    double G = model_->G();
    //    getParams(q2);
    norm(1.0);
    left(((((1.0*(-ii))*1.0)*1.0)*(ii*G)));
    right(((((1.0*(-ii))*1.0)*1.0)*(ii*G)));
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
    
    
    orderInGem(0);
    orderInGs(1);
    FFVVertex::doinit();
  }
  //    void getParams(Energy2);
 private:
  FRModelV_V_197 & operator=(const FRModelV_V_197 &);
  //    Complex leftval, rightval, normval;
  tcHwFRModelPtr model_;
};
DescribeClass<FRModelV_V_197,Helicity::FFVVertex>
describeHerwigFRModelV_V_197("Herwig::FRModelV_V_197",
				       "FRModel.so");
// void FRModelV_V_197::getParams(Energy2 ) {
// }

class FRModelV_V_198: public FFVVertex {
 public:
  FRModelV_V_198() {
    kinematics(false);
    addToList(-1,2,-24);
  }
  void setCoupling(Energy2 ,tcPDPtr p1,tcPDPtr,tcPDPtr) {
    double ee = model_->ee();
    double sw = model_->sw();
    Complex CKM1x1 = model_->CKM1x1();
    //    getParams(q2);
    norm(1.0);
    left(((((1.0*(-ii))*1.0)*1.0)*(((CKM1x1*ee)*ii)/(sw*sqrt(2.0)))));
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
  FRModelV_V_198 & operator=(const FRModelV_V_198 &);
  //    Complex leftval, rightval, normval;
  tcHwFRModelPtr model_;
};
DescribeClass<FRModelV_V_198,Helicity::FFVVertex>
describeHerwigFRModelV_V_198("Herwig::FRModelV_V_198",
				       "FRModel.so");
// void FRModelV_V_198::getParams(Energy2 ) {
// }

class FRModelV_V_199: public FFVVertex {
 public:
  FRModelV_V_199() {
    kinematics(false);
    addToList(-3,2,-24);
  }
  void setCoupling(Energy2 ,tcPDPtr p1,tcPDPtr,tcPDPtr) {
    double ee = model_->ee();
    Complex CKM1x2 = model_->CKM1x2();
    double sw = model_->sw();
    //    getParams(q2);
    norm(1.0);
    left(((((1.0*(-ii))*1.0)*1.0)*(((CKM1x2*ee)*ii)/(sw*sqrt(2.0)))));
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
  FRModelV_V_199 & operator=(const FRModelV_V_199 &);
  //    Complex leftval, rightval, normval;
  tcHwFRModelPtr model_;
};
DescribeClass<FRModelV_V_199,Helicity::FFVVertex>
describeHerwigFRModelV_V_199("Herwig::FRModelV_V_199",
				       "FRModel.so");
// void FRModelV_V_199::getParams(Energy2 ) {
// }

class FRModelV_V_200: public FFVVertex {
 public:
  FRModelV_V_200() {
    kinematics(false);
    addToList(-5,2,-24);
  }
  void setCoupling(Energy2 ,tcPDPtr p1,tcPDPtr,tcPDPtr) {
    double ee = model_->ee();
    double sw = model_->sw();
    Complex CKM1x3 = model_->CKM1x3();
    //    getParams(q2);
    norm(1.0);
    left(((((1.0*(-ii))*1.0)*1.0)*(((CKM1x3*ee)*ii)/(sw*sqrt(2.0)))));
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
  FRModelV_V_200 & operator=(const FRModelV_V_200 &);
  //    Complex leftval, rightval, normval;
  tcHwFRModelPtr model_;
};
DescribeClass<FRModelV_V_200,Helicity::FFVVertex>
describeHerwigFRModelV_V_200("Herwig::FRModelV_V_200",
				       "FRModel.so");
// void FRModelV_V_200::getParams(Energy2 ) {
// }

}

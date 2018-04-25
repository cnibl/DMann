// -*- C++ -*-
//
// FRModelV_V_125.cc is a part of Herwig - A multi-purpose Monte Carlo event generator
// Copyright (C) 2002-2007 The Herwig Collaboration
//
// Herwig is licenced under version 2 of the GPL, see COPYING for details.
// Please respect the MCnet academic guidelines, see GUIDELINES for details.

#include "FRModel.h"
#include "ThePEG/Helicity/Vertex/Vector/VVVVVertex.h"
#include "ThePEG/Helicity/Vertex/Vector/VVVVertex.h"
#include "ThePEG/Helicity/Vertex/Scalar/VVSVertex.h"
#include "ThePEG/Helicity/Vertex/Vector/FFVVertex.h"
#include "ThePEG/Helicity/Vertex/Scalar/VVSSVertex.h"

#include "ThePEG/Utilities/DescribeClass.h"
#include "ThePEG/Persistency/PersistentOStream.h"
#include "ThePEG/Persistency/PersistentIStream.h"

namespace Herwig 
{
  using namespace ThePEG;
  using namespace ThePEG::Helicity;
  using ThePEG::Constants::pi;

  class FRModelV_V_101: public VVSVertex {
 public:
  FRModelV_V_101() {
    kinematics(false);
    addToList(-24,24,25);
  }
  void setCoupling(Energy2 ,tcPDPtr,tcPDPtr,tcPDPtr) {
    double ee = model_->ee();
    double vev = model_->vev();
    double sw = model_->sw();
    //    getParams(q2);
    norm(Complex((((((1.0*(-ii))*1.0)*(((sqr(ee)*ii)*vev)/(2.0*sqr(sw))))*1.0)) * GeV / UnitRemoval::E));
    
    
    
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
  FRModelV_V_101 & operator=(const FRModelV_V_101 &);
  //    Complex leftval, rightval, normval;
  tcHwFRModelPtr model_;
};
DescribeClass<FRModelV_V_101,Helicity::VVSVertex>
describeHerwigFRModelV_V_101("Herwig::FRModelV_V_101",
				       "FRModel.so");
// void FRModelV_V_101::getParams(Energy2 ) {
// }

class FRModelV_V_102: public VVVVVertex {
 public:
  FRModelV_V_102() {
    kinematics(false);
    addToList(22,22,-24,24);
  }
  void setCoupling(Energy2 ,tcPDPtr p1,tcPDPtr p2,tcPDPtr p3,tcPDPtr p4) {
    double ee = model_->ee();
    //    getParams(q2);
    norm(((((1.0*ii)*1.0)*-1.0)*(sqr(ee)*ii)));
    
    
    bool done[4]={false,false,false,false};
    tcPDPtr part[4]={p1,p2,p3,p4};
    unsigned int iorder[4]={0,0,0,0};
    for(unsigned int ix=0;ix<4;++ix) {
       if(!done[0] && part[ix]->id()==22) {done[0]=true; iorder[0] = ix; continue;}
       if(!done[1] && part[ix]->id()==22) {done[1]=true; iorder[1] = ix; continue;}
       if(!done[2] && part[ix]->id()==-24) {done[2]=true; iorder[2] = ix; continue;}
       if(!done[3] && part[ix]->id()==24) {done[3]=true; iorder[3] = ix; continue;}
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
  FRModelV_V_102 & operator=(const FRModelV_V_102 &);
  //    Complex leftval, rightval, normval;
  tcHwFRModelPtr model_;
};
DescribeClass<FRModelV_V_102,Helicity::VVVVVertex>
describeHerwigFRModelV_V_102("Herwig::FRModelV_V_102",
				       "FRModel.so");
// void FRModelV_V_102::getParams(Energy2 ) {
// }

class FRModelV_V_103: public VVVVertex {
 public:
  FRModelV_V_103() {
    kinematics(false);
    addToList(-24,24,23);
  }
  void setCoupling(Energy2 ,tcPDPtr p1,tcPDPtr p2,tcPDPtr p3) {
    double ee = model_->ee();
    double cw = model_->cw();
    double sw = model_->sw();
    //    getParams(q2);
    norm((((1.0*ii)*1.0)*(((cw*ee)*ii)/sw)));
    
    
    if((p1->id()==24&&p2->id()==-24&&p3->id()==23)||(p1->id()==-24&&p2->id()==23&&p3->id()==24)||(p1->id()==23&&p2->id()==24&&p3->id()==-24)) {norm(-norm());}
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
  FRModelV_V_103 & operator=(const FRModelV_V_103 &);
  //    Complex leftval, rightval, normval;
  tcHwFRModelPtr model_;
};
DescribeClass<FRModelV_V_103,Helicity::VVVVertex>
describeHerwigFRModelV_V_103("Herwig::FRModelV_V_103",
				       "FRModel.so");
// void FRModelV_V_103::getParams(Energy2 ) {
// }

class FRModelV_V_104: public VVVVVertex {
 public:
  FRModelV_V_104() {
    kinematics(false);
    addToList(-24,-24,24,24);
  }
  void setCoupling(Energy2 ,tcPDPtr p1,tcPDPtr p2,tcPDPtr p3,tcPDPtr p4) {
    double ee = model_->ee();
    double sw = model_->sw();
    //    getParams(q2);
    norm(((((1.0*ii)*1.0)*-1.0)*(-((sqr(ee)*ii)/sqr(sw)))));
    
    
    bool done[4]={false,false,false,false};
    tcPDPtr part[4]={p1,p2,p3,p4};
    unsigned int iorder[4]={0,0,0,0};
    for(unsigned int ix=0;ix<4;++ix) {
       if(!done[0] && part[ix]->id()==-24) {done[0]=true; iorder[0] = ix; continue;}
       if(!done[1] && part[ix]->id()==-24) {done[1]=true; iorder[1] = ix; continue;}
       if(!done[2] && part[ix]->id()==24) {done[2]=true; iorder[2] = ix; continue;}
       if(!done[3] && part[ix]->id()==24) {done[3]=true; iorder[3] = ix; continue;}
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
  FRModelV_V_104 & operator=(const FRModelV_V_104 &);
  //    Complex leftval, rightval, normval;
  tcHwFRModelPtr model_;
};
DescribeClass<FRModelV_V_104,Helicity::VVVVVertex>
describeHerwigFRModelV_V_104("Herwig::FRModelV_V_104",
				       "FRModel.so");
// void FRModelV_V_104::getParams(Energy2 ) {
// }

class FRModelV_V_117: public VVVVVertex {
 public:
  FRModelV_V_117() {
    kinematics(false);
    addToList(22,-24,24,23);
  }
  void setCoupling(Energy2 ,tcPDPtr p1,tcPDPtr p2,tcPDPtr p3,tcPDPtr p4) {
    double ee = model_->ee();
    double cw = model_->cw();
    double sw = model_->sw();
    //    getParams(q2);
    norm(((((1.0*ii)*1.0)*0.5)*((((-2.0*cw)*sqr(ee))*ii)/sw)));
    
    
    bool done[4]={false,false,false,false};
    tcPDPtr part[4]={p1,p2,p3,p4};
    unsigned int iorder[4]={0,0,0,0};
    for(unsigned int ix=0;ix<4;++ix) {
       if(!done[0] && part[ix]->id()==22) {done[0]=true; iorder[0] = ix; continue;}
       if(!done[1] && part[ix]->id()==-24) {done[1]=true; iorder[3] = ix; continue;}
       if(!done[2] && part[ix]->id()==24) {done[2]=true; iorder[1] = ix; continue;}
       if(!done[3] && part[ix]->id()==23) {done[3]=true; iorder[2] = ix; continue;}
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
  FRModelV_V_117 & operator=(const FRModelV_V_117 &);
  //    Complex leftval, rightval, normval;
  tcHwFRModelPtr model_;
};
DescribeClass<FRModelV_V_117,Helicity::VVVVVertex>
describeHerwigFRModelV_V_117("Herwig::FRModelV_V_117",
				       "FRModel.so");
// void FRModelV_V_117::getParams(Energy2 ) {
// }

class FRModelV_V_120: public VVSSVertex {
 public:
  FRModelV_V_120() {
    kinematics(false);
    addToList(23,23,25,25);
  }
  void setCoupling(Energy2 ,tcPDPtr,tcPDPtr,tcPDPtr,tcPDPtr) {
    double ee = model_->ee();
    double cw = model_->cw();
    double sw = model_->sw();
    //    getParams(q2);
    norm((((1.0*(-ii))*1.0)*(((sqr(ee)*ii)+(((sqr(cw)*sqr(ee))*ii)/(2.0*sqr(sw))))+(((sqr(ee)*ii)*sqr(sw))/(2.0*sqr(cw))))));
    
    
    
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
  FRModelV_V_120 & operator=(const FRModelV_V_120 &);
  //    Complex leftval, rightval, normval;
  tcHwFRModelPtr model_;
};
DescribeClass<FRModelV_V_120,Helicity::VVSSVertex>
describeHerwigFRModelV_V_120("Herwig::FRModelV_V_120",
				       "FRModel.so");
// void FRModelV_V_120::getParams(Energy2 ) {
// }

class FRModelV_V_121: public VVSVertex {
 public:
  FRModelV_V_121() {
    kinematics(false);
    addToList(23,23,999);
  }
  void setCoupling(Energy2 ,tcPDPtr,tcPDPtr,tcPDPtr) {
    double gSEW = model_->gSEW();
    double Lambda = model_->Lambda();
    //    getParams(q2);
    norm(Complex((((((1.0*(-ii))*1.0)*(((2.0*ii)*gSEW)/Lambda))*1.0)) * GeV / UnitRemoval::E));
    
    
    
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
  FRModelV_V_121 & operator=(const FRModelV_V_121 &);
  //    Complex leftval, rightval, normval;
  tcHwFRModelPtr model_;
};
DescribeClass<FRModelV_V_121,Helicity::VVSVertex>
describeHerwigFRModelV_V_121("Herwig::FRModelV_V_121",
				       "FRModel.so");
// void FRModelV_V_121::getParams(Energy2 ) {
// }

class FRModelV_V_122: public VVSVertex {
 public:
  FRModelV_V_122() {
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
  FRModelV_V_122 & operator=(const FRModelV_V_122 &);
  //    Complex leftval, rightval, normval;
  tcHwFRModelPtr model_;
};
DescribeClass<FRModelV_V_122,Helicity::VVSVertex>
describeHerwigFRModelV_V_122("Herwig::FRModelV_V_122",
				       "FRModel.so");
// void FRModelV_V_122::getParams(Energy2 ) {
// }

class FRModelV_V_123: public VVVVVertex {
 public:
  FRModelV_V_123() {
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
  FRModelV_V_123 & operator=(const FRModelV_V_123 &);
  //    Complex leftval, rightval, normval;
  tcHwFRModelPtr model_;
};
DescribeClass<FRModelV_V_123,Helicity::VVVVVertex>
describeHerwigFRModelV_V_123("Herwig::FRModelV_V_123",
				       "FRModel.so");
// void FRModelV_V_123::getParams(Energy2 ) {
// }

class FRModelV_V_124: public FFVVertex {
 public:
  FRModelV_V_124() {
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
  FRModelV_V_124 & operator=(const FRModelV_V_124 &);
  //    Complex leftval, rightval, normval;
  tcHwFRModelPtr model_;
};
DescribeClass<FRModelV_V_124,Helicity::FFVVertex>
describeHerwigFRModelV_V_124("Herwig::FRModelV_V_124",
				       "FRModel.so");
// void FRModelV_V_124::getParams(Energy2 ) {
// }

class FRModelV_V_125: public FFVVertex {
 public:
  FRModelV_V_125() {
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
  FRModelV_V_125 & operator=(const FRModelV_V_125 &);
  //    Complex leftval, rightval, normval;
  tcHwFRModelPtr model_;
};
DescribeClass<FRModelV_V_125,Helicity::FFVVertex>
describeHerwigFRModelV_V_125("Herwig::FRModelV_V_125",
				       "FRModel.so");
// void FRModelV_V_125::getParams(Energy2 ) {
// }

}

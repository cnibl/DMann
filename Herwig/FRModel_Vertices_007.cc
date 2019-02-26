// -*- C++ -*-
//
// FRModelV_V_175.cc is a part of Herwig - A multi-purpose Monte Carlo event generator
// Copyright (C) 2002-2007 The Herwig Collaboration
//
// Herwig is licenced under version 2 of the GPL, see COPYING for details.
// Please respect the MCnet academic guidelines, see GUIDELINES for details.

#include "FRModel.h"
#include "ThePEG/Helicity/Vertex/Vector/VVVVVertex.h"
#include "ThePEG/Helicity/Vertex/Vector/VVVVertex.h"
#include "ThePEG/Helicity/Vertex/Scalar/VVSSVertex.h"
#include "ThePEG/Helicity/Vertex/Vector/FFVVertex.h"
#include "ThePEG/Helicity/Vertex/Scalar/VVSVertex.h"

#include "ThePEG/Utilities/DescribeClass.h"
#include "ThePEG/Persistency/PersistentOStream.h"
#include "ThePEG/Persistency/PersistentIStream.h"

namespace Herwig 
{
  using namespace ThePEG;
  using namespace ThePEG::Helicity;
  using ThePEG::Constants::pi;

  class FRModelV_V_112: public VVVVertex {
 public:
  FRModelV_V_112() {
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
  FRModelV_V_112 & operator=(const FRModelV_V_112 &);
  //    Complex leftval, rightval, normval;
  tcHwFRModelPtr model_;
};
DescribeClass<FRModelV_V_112,Helicity::VVVVertex>
describeHerwigFRModelV_V_112("Herwig::FRModelV_V_112",
				       "FRModel.so");
// void FRModelV_V_112::getParams(Energy2 ) {
// }

class FRModelV_V_127: public VVSSVertex {
 public:
  FRModelV_V_127() {
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
  FRModelV_V_127 & operator=(const FRModelV_V_127 &);
  //    Complex leftval, rightval, normval;
  tcHwFRModelPtr model_;
};
DescribeClass<FRModelV_V_127,Helicity::VVSSVertex>
describeHerwigFRModelV_V_127("Herwig::FRModelV_V_127",
				       "FRModel.so");
// void FRModelV_V_127::getParams(Energy2 ) {
// }

class FRModelV_V_128: public VVSVertex {
 public:
  FRModelV_V_128() {
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
  FRModelV_V_128 & operator=(const FRModelV_V_128 &);
  //    Complex leftval, rightval, normval;
  tcHwFRModelPtr model_;
};
DescribeClass<FRModelV_V_128,Helicity::VVSVertex>
describeHerwigFRModelV_V_128("Herwig::FRModelV_V_128",
				       "FRModel.so");
// void FRModelV_V_128::getParams(Energy2 ) {
// }

class FRModelV_V_132: public VVSSVertex {
 public:
  FRModelV_V_132() {
    kinematics(false);
    addToList(-24,24,25,9000006);
  }
  void setCoupling(Energy2 ,tcPDPtr,tcPDPtr,tcPDPtr,tcPDPtr) {
    double ee = model_->ee();
    double vev = model_->vev();
    double gSh1 = model_->gSh1();
    double sw = model_->sw();
    double Lambda = model_->Lambda();
    //    getParams(q2);
    norm((((1.0*(-ii))*1.0)*((((sqr(ee)*ii)*gSh1)*vev)/((2.0*Lambda)*sqr(sw)))));
    
    
    
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
  FRModelV_V_132 & operator=(const FRModelV_V_132 &);
  //    Complex leftval, rightval, normval;
  tcHwFRModelPtr model_;
};
DescribeClass<FRModelV_V_132,Helicity::VVSSVertex>
describeHerwigFRModelV_V_132("Herwig::FRModelV_V_132",
				       "FRModel.so");
// void FRModelV_V_132::getParams(Energy2 ) {
// }

class FRModelV_V_133: public VVVVVertex {
 public:
  FRModelV_V_133() {
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
  FRModelV_V_133 & operator=(const FRModelV_V_133 &);
  //    Complex leftval, rightval, normval;
  tcHwFRModelPtr model_;
};
DescribeClass<FRModelV_V_133,Helicity::VVVVVertex>
describeHerwigFRModelV_V_133("Herwig::FRModelV_V_133",
				       "FRModel.so");
// void FRModelV_V_133::getParams(Energy2 ) {
// }

class FRModelV_V_135: public VVVVertex {
 public:
  FRModelV_V_135() {
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
  FRModelV_V_135 & operator=(const FRModelV_V_135 &);
  //    Complex leftval, rightval, normval;
  tcHwFRModelPtr model_;
};
DescribeClass<FRModelV_V_135,Helicity::VVVVertex>
describeHerwigFRModelV_V_135("Herwig::FRModelV_V_135",
				       "FRModel.so");
// void FRModelV_V_135::getParams(Energy2 ) {
// }

class FRModelV_V_137: public VVVVVertex {
 public:
  FRModelV_V_137() {
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
  FRModelV_V_137 & operator=(const FRModelV_V_137 &);
  //    Complex leftval, rightval, normval;
  tcHwFRModelPtr model_;
};
DescribeClass<FRModelV_V_137,Helicity::VVVVVertex>
describeHerwigFRModelV_V_137("Herwig::FRModelV_V_137",
				       "FRModel.so");
// void FRModelV_V_137::getParams(Energy2 ) {
// }

class FRModelV_V_139: public FFVVertex {
 public:
  FRModelV_V_139() {
    kinematics(false);
    addToList(-5,5,9000007);
  }
  void setCoupling(Energy2 ,tcPDPtr p1,tcPDPtr,tcPDPtr) {
    double gVd33 = model_->gVd33();
    double gAd33 = model_->gAd33();
    //    getParams(q2);
    norm(1.0);
    left((((((1.0*(-ii))*1.0)*-1.0)*((ii*gAd33)/sqrt(2.0)))+((((1.0*(-ii))*1.0)*1.0)*((ii*gVd33)/sqrt(2.0)))));
    right((((((1.0*(-ii))*1.0)*1.0)*((ii*gAd33)/sqrt(2.0)))+((((1.0*(-ii))*1.0)*1.0)*((ii*gVd33)/sqrt(2.0)))));
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
  FRModelV_V_139 & operator=(const FRModelV_V_139 &);
  //    Complex leftval, rightval, normval;
  tcHwFRModelPtr model_;
};
DescribeClass<FRModelV_V_139,Helicity::FFVVertex>
describeHerwigFRModelV_V_139("Herwig::FRModelV_V_139",
				       "FRModel.so");
// void FRModelV_V_139::getParams(Energy2 ) {
// }

class FRModelV_V_140: public FFVVertex {
 public:
  FRModelV_V_140() {
    kinematics(false);
    addToList(-4,4,9000007);
  }
  void setCoupling(Energy2 ,tcPDPtr p1,tcPDPtr,tcPDPtr) {
    double gAu22 = model_->gAu22();
    double gVu22 = model_->gVu22();
    //    getParams(q2);
    norm(1.0);
    left((((((1.0*(-ii))*1.0)*-1.0)*((ii*gAu22)/sqrt(2.0)))+((((1.0*(-ii))*1.0)*1.0)*((ii*gVu22)/sqrt(2.0)))));
    right((((((1.0*(-ii))*1.0)*1.0)*((ii*gAu22)/sqrt(2.0)))+((((1.0*(-ii))*1.0)*1.0)*((ii*gVu22)/sqrt(2.0)))));
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
  FRModelV_V_140 & operator=(const FRModelV_V_140 &);
  //    Complex leftval, rightval, normval;
  tcHwFRModelPtr model_;
};
DescribeClass<FRModelV_V_140,Helicity::FFVVertex>
describeHerwigFRModelV_V_140("Herwig::FRModelV_V_140",
				       "FRModel.so");
// void FRModelV_V_140::getParams(Energy2 ) {
// }

class FRModelV_V_141: public FFVVertex {
 public:
  FRModelV_V_141() {
    kinematics(false);
    addToList(-1,1,9000007);
  }
  void setCoupling(Energy2 ,tcPDPtr p1,tcPDPtr,tcPDPtr) {
    double gVd11 = model_->gVd11();
    double gAd11 = model_->gAd11();
    //    getParams(q2);
    norm(1.0);
    left((((((1.0*(-ii))*1.0)*-1.0)*((ii*gAd11)/sqrt(2.0)))+((((1.0*(-ii))*1.0)*1.0)*((ii*gVd11)/sqrt(2.0)))));
    right((((((1.0*(-ii))*1.0)*1.0)*((ii*gAd11)/sqrt(2.0)))+((((1.0*(-ii))*1.0)*1.0)*((ii*gVd11)/sqrt(2.0)))));
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
  FRModelV_V_141 & operator=(const FRModelV_V_141 &);
  //    Complex leftval, rightval, normval;
  tcHwFRModelPtr model_;
};
DescribeClass<FRModelV_V_141,Helicity::FFVVertex>
describeHerwigFRModelV_V_141("Herwig::FRModelV_V_141",
				       "FRModel.so");
// void FRModelV_V_141::getParams(Energy2 ) {
// }

class FRModelV_V_142: public FFVVertex {
 public:
  FRModelV_V_142() {
    kinematics(false);
    addToList(-11,11,9000007);
  }
  void setCoupling(Energy2 ,tcPDPtr p1,tcPDPtr,tcPDPtr) {
    double gAe = model_->gAe();
    double gVe = model_->gVe();
    //    getParams(q2);
    norm(1.0);
    left((((((1.0*(-ii))*1.0)*-1.0)*((ii*gAe)/sqrt(2.0)))+((((1.0*(-ii))*1.0)*1.0)*((ii*gVe)/sqrt(2.0)))));
    right((((((1.0*(-ii))*1.0)*1.0)*((ii*gAe)/sqrt(2.0)))+((((1.0*(-ii))*1.0)*1.0)*((ii*gVe)/sqrt(2.0)))));
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
  FRModelV_V_142 & operator=(const FRModelV_V_142 &);
  //    Complex leftval, rightval, normval;
  tcHwFRModelPtr model_;
};
DescribeClass<FRModelV_V_142,Helicity::FFVVertex>
describeHerwigFRModelV_V_142("Herwig::FRModelV_V_142",
				       "FRModel.so");
// void FRModelV_V_142::getParams(Energy2 ) {
// }

class FRModelV_V_143: public FFVVertex {
 public:
  FRModelV_V_143() {
    kinematics(false);
    addToList(-13,13,9000007);
  }
  void setCoupling(Energy2 ,tcPDPtr p1,tcPDPtr,tcPDPtr) {
    double gAmm = model_->gAmm();
    double gVmm = model_->gVmm();
    //    getParams(q2);
    norm(1.0);
    left((((((1.0*(-ii))*1.0)*-1.0)*((ii*gAmm)/sqrt(2.0)))+((((1.0*(-ii))*1.0)*1.0)*((ii*gVmm)/sqrt(2.0)))));
    right((((((1.0*(-ii))*1.0)*1.0)*((ii*gAmm)/sqrt(2.0)))+((((1.0*(-ii))*1.0)*1.0)*((ii*gVmm)/sqrt(2.0)))));
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
  FRModelV_V_143 & operator=(const FRModelV_V_143 &);
  //    Complex leftval, rightval, normval;
  tcHwFRModelPtr model_;
};
DescribeClass<FRModelV_V_143,Helicity::FFVVertex>
describeHerwigFRModelV_V_143("Herwig::FRModelV_V_143",
				       "FRModel.so");
// void FRModelV_V_143::getParams(Energy2 ) {
// }

class FRModelV_V_144: public FFVVertex {
 public:
  FRModelV_V_144() {
    kinematics(false);
    addToList(-3,3,9000007);
  }
  void setCoupling(Energy2 ,tcPDPtr p1,tcPDPtr,tcPDPtr) {
    double gVd22 = model_->gVd22();
    double gAd22 = model_->gAd22();
    //    getParams(q2);
    norm(1.0);
    left((((((1.0*(-ii))*1.0)*-1.0)*((ii*gAd22)/sqrt(2.0)))+((((1.0*(-ii))*1.0)*1.0)*((ii*gVd22)/sqrt(2.0)))));
    right((((((1.0*(-ii))*1.0)*1.0)*((ii*gAd22)/sqrt(2.0)))+((((1.0*(-ii))*1.0)*1.0)*((ii*gVd22)/sqrt(2.0)))));
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
  FRModelV_V_144 & operator=(const FRModelV_V_144 &);
  //    Complex leftval, rightval, normval;
  tcHwFRModelPtr model_;
};
DescribeClass<FRModelV_V_144,Helicity::FFVVertex>
describeHerwigFRModelV_V_144("Herwig::FRModelV_V_144",
				       "FRModel.so");
// void FRModelV_V_144::getParams(Energy2 ) {
// }

class FRModelV_V_145: public FFVVertex {
 public:
  FRModelV_V_145() {
    kinematics(false);
    addToList(-15,15,9000007);
  }
  void setCoupling(Energy2 ,tcPDPtr p1,tcPDPtr,tcPDPtr) {
    double gVta = model_->gVta();
    double gAta = model_->gAta();
    //    getParams(q2);
    norm(1.0);
    left((((((1.0*(-ii))*1.0)*-1.0)*((ii*gAta)/sqrt(2.0)))+((((1.0*(-ii))*1.0)*1.0)*((ii*gVta)/sqrt(2.0)))));
    right((((((1.0*(-ii))*1.0)*1.0)*((ii*gAta)/sqrt(2.0)))+((((1.0*(-ii))*1.0)*1.0)*((ii*gVta)/sqrt(2.0)))));
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
  FRModelV_V_145 & operator=(const FRModelV_V_145 &);
  //    Complex leftval, rightval, normval;
  tcHwFRModelPtr model_;
};
DescribeClass<FRModelV_V_145,Helicity::FFVVertex>
describeHerwigFRModelV_V_145("Herwig::FRModelV_V_145",
				       "FRModel.so");
// void FRModelV_V_145::getParams(Energy2 ) {
// }

class FRModelV_V_146: public FFVVertex {
 public:
  FRModelV_V_146() {
    kinematics(false);
    addToList(-6,6,9000007);
  }
  void setCoupling(Energy2 ,tcPDPtr p1,tcPDPtr,tcPDPtr) {
    double gVu33 = model_->gVu33();
    double gAu33 = model_->gAu33();
    //    getParams(q2);
    norm(1.0);
    left((((((1.0*(-ii))*1.0)*-1.0)*((ii*gAu33)/sqrt(2.0)))+((((1.0*(-ii))*1.0)*1.0)*((ii*gVu33)/sqrt(2.0)))));
    right((((((1.0*(-ii))*1.0)*1.0)*((ii*gAu33)/sqrt(2.0)))+((((1.0*(-ii))*1.0)*1.0)*((ii*gVu33)/sqrt(2.0)))));
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
  FRModelV_V_146 & operator=(const FRModelV_V_146 &);
  //    Complex leftval, rightval, normval;
  tcHwFRModelPtr model_;
};
DescribeClass<FRModelV_V_146,Helicity::FFVVertex>
describeHerwigFRModelV_V_146("Herwig::FRModelV_V_146",
				       "FRModel.so");
// void FRModelV_V_146::getParams(Energy2 ) {
// }

class FRModelV_V_147: public FFVVertex {
 public:
  FRModelV_V_147() {
    kinematics(false);
    addToList(-2,2,9000007);
  }
  void setCoupling(Energy2 ,tcPDPtr p1,tcPDPtr,tcPDPtr) {
    double gAu11 = model_->gAu11();
    double gVu11 = model_->gVu11();
    //    getParams(q2);
    norm(1.0);
    left((((((1.0*(-ii))*1.0)*-1.0)*((ii*gAu11)/sqrt(2.0)))+((((1.0*(-ii))*1.0)*1.0)*((ii*gVu11)/sqrt(2.0)))));
    right((((((1.0*(-ii))*1.0)*1.0)*((ii*gAu11)/sqrt(2.0)))+((((1.0*(-ii))*1.0)*1.0)*((ii*gVu11)/sqrt(2.0)))));
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
  FRModelV_V_147 & operator=(const FRModelV_V_147 &);
  //    Complex leftval, rightval, normval;
  tcHwFRModelPtr model_;
};
DescribeClass<FRModelV_V_147,Helicity::FFVVertex>
describeHerwigFRModelV_V_147("Herwig::FRModelV_V_147",
				       "FRModel.so");
// void FRModelV_V_147::getParams(Energy2 ) {
// }

class FRModelV_V_148: public FFVVertex {
 public:
  FRModelV_V_148() {
    kinematics(false);
    addToList(-9000010,9000010,9000007);
  }
  void setCoupling(Energy2 ,tcPDPtr p1,tcPDPtr,tcPDPtr) {
    double gVXd = model_->gVXd();
    double gAXd = model_->gAXd();
    //    getParams(q2);
    norm(1.0);
    left((((((1.0*(-ii))*1.0)*-1.0)*(ii*gAXd))+((((1.0*(-ii))*1.0)*1.0)*(ii*gVXd))));
    right((((((1.0*(-ii))*1.0)*1.0)*(ii*gAXd))+((((1.0*(-ii))*1.0)*1.0)*(ii*gVXd))));
    if(p1->id()!=-9000010) {Complex ltemp=left(), rtemp=right(); left(-rtemp); right(-ltemp);}
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
  FRModelV_V_148 & operator=(const FRModelV_V_148 &);
  //    Complex leftval, rightval, normval;
  tcHwFRModelPtr model_;
};
DescribeClass<FRModelV_V_148,Helicity::FFVVertex>
describeHerwigFRModelV_V_148("Herwig::FRModelV_V_148",
				       "FRModel.so");
// void FRModelV_V_148::getParams(Energy2 ) {
// }

class FRModelV_V_171: public VVVVVertex {
 public:
  FRModelV_V_171() {
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
  FRModelV_V_171 & operator=(const FRModelV_V_171 &);
  //    Complex leftval, rightval, normval;
  tcHwFRModelPtr model_;
};
DescribeClass<FRModelV_V_171,Helicity::VVVVVertex>
describeHerwigFRModelV_V_171("Herwig::FRModelV_V_171",
				       "FRModel.so");
// void FRModelV_V_171::getParams(Energy2 ) {
// }

class FRModelV_V_175: public VVSSVertex {
 public:
  FRModelV_V_175() {
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
  FRModelV_V_175 & operator=(const FRModelV_V_175 &);
  //    Complex leftval, rightval, normval;
  tcHwFRModelPtr model_;
};
DescribeClass<FRModelV_V_175,Helicity::VVSSVertex>
describeHerwigFRModelV_V_175("Herwig::FRModelV_V_175",
				       "FRModel.so");
// void FRModelV_V_175::getParams(Energy2 ) {
// }

}

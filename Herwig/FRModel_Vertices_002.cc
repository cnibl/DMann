// -*- C++ -*-
//
// FRModelV_V_50.cc is a part of Herwig - A multi-purpose Monte Carlo event generator
// Copyright (C) 2002-2007 The Herwig Collaboration
//
// Herwig is licenced under version 2 of the GPL, see COPYING for details.
// Please respect the MCnet academic guidelines, see GUIDELINES for details.

#include "FRModel.h"
#include "ThePEG/Helicity/Vertex/Scalar/GeneralVVSVertex.h"
#include "ThePEG/Helicity/Vertex/Scalar/SSSVertex.h"
#include "ThePEG/Helicity/Vertex/Scalar/FFSVertex.h"
#include "ThePEG/Helicity/Vertex/Scalar/SSSSVertex.h"

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

class FRModelV_V_12: public SSSVertex {
 public:
  FRModelV_V_12() {
    kinematics(false);
    addToList(25,25,9000006);
  }
  void setCoupling(Energy2 ,tcPDPtr,tcPDPtr,tcPDPtr) {
    double gSh2 = model_->gSh2();
    double gSh1 = model_->gSh1();
    double MH = model_->MH();
    double Lambda = model_->Lambda();
    //    getParams(q2);
    norm(Complex((((((1.0*(-ii))*1.0)*(-((ii*gSh1)/Lambda)))+(((1.0*(-ii))*1.0)*(((ii*gSh2)*sqr(MH))/Lambda)))) * GeV / UnitRemoval::E));
    
    
    
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
  FRModelV_V_12 & operator=(const FRModelV_V_12 &);
  //    Complex leftval, rightval, normval;
  tcHwFRModelPtr model_;
};
DescribeClass<FRModelV_V_12,Helicity::SSSVertex>
describeHerwigFRModelV_V_12("Herwig::FRModelV_V_12",
				       "FRModel.so");
// void FRModelV_V_12::getParams(Energy2 ) {
// }

class FRModelV_V_13: public SSSVertex {
 public:
  FRModelV_V_13() {
    kinematics(false);
    addToList(-9000009,9000009,9000006);
  }
  void setCoupling(Energy2 ,tcPDPtr,tcPDPtr,tcPDPtr) {
    double gSXc = model_->gSXc();
    double MXc = model_->MXc();
    //    getParams(q2);
    norm(Complex(((((1.0*(-ii))*1.0)*((ii*gSXc)*MXc))) * GeV / UnitRemoval::E));
    
    
    
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
  FRModelV_V_13 & operator=(const FRModelV_V_13 &);
  //    Complex leftval, rightval, normval;
  tcHwFRModelPtr model_;
};
DescribeClass<FRModelV_V_13,Helicity::SSSVertex>
describeHerwigFRModelV_V_13("Herwig::FRModelV_V_13",
				       "FRModel.so");
// void FRModelV_V_13::getParams(Energy2 ) {
// }

class FRModelV_V_14: public SSSVertex {
 public:
  FRModelV_V_14() {
    kinematics(false);
    addToList(9000008,9000008,9000006);
  }
  void setCoupling(Energy2 ,tcPDPtr,tcPDPtr,tcPDPtr) {
    double gSXr = model_->gSXr();
    double Lambda = model_->Lambda();
    //    getParams(q2);
    norm(Complex(((((1.0*(-ii))*1.0)*((ii*gSXr)*Lambda))) * GeV / UnitRemoval::E));
    
    
    
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
  FRModelV_V_14 & operator=(const FRModelV_V_14 &);
  //    Complex leftval, rightval, normval;
  tcHwFRModelPtr model_;
};
DescribeClass<FRModelV_V_14,Helicity::SSSVertex>
describeHerwigFRModelV_V_14("Herwig::FRModelV_V_14",
				       "FRModel.so");
// void FRModelV_V_14::getParams(Energy2 ) {
// }

class FRModelV_V_17: public GeneralVVSVertex {
 public:
  FRModelV_V_17() {
    kinematics(true);
    addToList(22,22,9000006);
  }
  void setCoupling(Energy2 ,tcPDPtr,tcPDPtr,tcPDPtr) {
    double gSBT = model_->gSBT();
    double gSWL = model_->gSWL();
    double sw = model_->sw();
    double gPWT = model_->gPWT();
    double gPBT = model_->gPBT();
    double gSBL = model_->gSBL();
    double gSWT = model_->gSWT();
    double cw = model_->cw();
    double Lambda = model_->Lambda();
    //    getParams(q2);
    norm(Complex(-(1.0) * UnitRemoval::E / GeV ));
    a00( ((((1.0*(-ii))*1.0)*(((((4.0*sqr(cw))*ii)*gSBT)/Lambda)+((((4.0*ii)*gSWT)*sqr(sw))/Lambda)))*-1.0) + Complex(( ((((1.0*(-ii))*1.0)*(((((2.0*sqr(cw))*ii)*gSBL)*Lambda)+((((2.0*ii)*gSWL)*Lambda)*sqr(sw))))*1.0) )* GeV2/invariant(1,2)));
    a11( 0.0 );
    a12( 0.0 );
    a21( ((((1.0*(-ii))*1.0)*(((((4.0*sqr(cw))*ii)*gSBT)/Lambda)+((((4.0*ii)*gSWT)*sqr(sw))/Lambda)))*1.0) );
    a22( 0.0 ); aEp( ((((1.0*(-ii))*1.0)*(((((-2.0*sqr(cw))*ii)*gPBT)/Lambda)-((((2.0*ii)*gPWT)*sqr(sw))/Lambda)))*(-1.0+-1.0)) ); 
    
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
    GeneralVVSVertex::doinit();
  }
  //    void getParams(Energy2);
 private:
  FRModelV_V_17 & operator=(const FRModelV_V_17 &);
  //    Complex leftval, rightval, normval;
  tcHwFRModelPtr model_;
};
DescribeClass<FRModelV_V_17,Helicity::GeneralVVSVertex>
describeHerwigFRModelV_V_17("Herwig::FRModelV_V_17",
				       "FRModel.so");
// void FRModelV_V_17::getParams(Energy2 ) {
// }

class FRModelV_V_20: public GeneralVVSVertex {
 public:
  FRModelV_V_20() {
    kinematics(true);
    addToList(21,21,9000006);
  }
  void setCoupling(Energy2 ,tcPDPtr,tcPDPtr,tcPDPtr) {
    double gPg = model_->gPg();
    double gSg = model_->gSg();
    double Lambda = model_->Lambda();
    //    getParams(q2);
    norm(Complex(-(1.0) * UnitRemoval::E / GeV ));
    a00( ((((1.0*(-ii))*1.0)*(((8.0*ii)*gSg)/Lambda))*-1.0) );
    a11( 0.0 );
    a12( 0.0 );
    a21( ((((1.0*(-ii))*1.0)*(((8.0*ii)*gSg)/Lambda))*1.0) );
    a22( 0.0 ); aEp( ((((1.0*(-ii))*1.0)*((-(ii*gPg))/(2.0*Lambda)))*(-8.0+-8.0)) ); 
    
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
    GeneralVVSVertex::doinit();
  }
  //    void getParams(Energy2);
 private:
  FRModelV_V_20 & operator=(const FRModelV_V_20 &);
  //    Complex leftval, rightval, normval;
  tcHwFRModelPtr model_;
};
DescribeClass<FRModelV_V_20,Helicity::GeneralVVSVertex>
describeHerwigFRModelV_V_20("Herwig::FRModelV_V_20",
				       "FRModel.so");
// void FRModelV_V_20::getParams(Energy2 ) {
// }

class FRModelV_V_21: public GeneralVVSVertex {
 public:
  FRModelV_V_21() {
    kinematics(true);
    addToList(-24,24,9000006);
  }
  void setCoupling(Energy2 ,tcPDPtr,tcPDPtr,tcPDPtr) {
    double vev = model_->vev();
    double gSh1 = model_->gSh1();
    double gSWL = model_->gSWL();
    double ee = model_->ee();
    double sw = model_->sw();
    double gPWT = model_->gPWT();
    double Lambda = model_->Lambda();
    double gSWT = model_->gSWT();
    //    getParams(q2);
    norm(Complex(-(1.0) * UnitRemoval::E / GeV ));
    a00( ((((1.0*(-ii))*1.0)*(((4.0*ii)*gSWT)/Lambda))*-1.0) + Complex(( ((((1.0*(-ii))*1.0)*((((2.0*ii)*gSWL)*Lambda)+((((sqr(ee)*ii)*gSh1)*sqr(vev))/((4.0*Lambda)*sqr(sw)))))*1.0) )* GeV2/invariant(1,2)));
    a11( 0.0 );
    a12( 0.0 );
    a21( ((((1.0*(-ii))*1.0)*(((4.0*ii)*gSWT)/Lambda))*1.0) );
    a22( 0.0 ); aEp( ((((1.0*(-ii))*1.0)*(((-2.0*ii)*gPWT)/Lambda))*(-1.0+-1.0)) ); 
    
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
    GeneralVVSVertex::doinit();
  }
  //    void getParams(Energy2);
 private:
  FRModelV_V_21 & operator=(const FRModelV_V_21 &);
  //    Complex leftval, rightval, normval;
  tcHwFRModelPtr model_;
};
DescribeClass<FRModelV_V_21,Helicity::GeneralVVSVertex>
describeHerwigFRModelV_V_21("Herwig::FRModelV_V_21",
				       "FRModel.so");
// void FRModelV_V_21::getParams(Energy2 ) {
// }

class FRModelV_V_22: public GeneralVVSVertex {
 public:
  FRModelV_V_22() {
    kinematics(true);
    addToList(22,23,9000006);
  }
  void setCoupling(Energy2 ,tcPDPtr,tcPDPtr,tcPDPtr) {
    double gSBT = model_->gSBT();
    double gSWL = model_->gSWL();
    double sw = model_->sw();
    double gPWT = model_->gPWT();
    double gPBT = model_->gPBT();
    double gSBL = model_->gSBL();
    double gSWT = model_->gSWT();
    double cw = model_->cw();
    double Lambda = model_->Lambda();
    //    getParams(q2);
    norm(Complex(-(1.0) * UnitRemoval::E / GeV ));
    a00( ((((1.0*(-ii))*1.0)*((((((-4.0*cw)*ii)*gSBT)*sw)/Lambda)+(((((4.0*cw)*ii)*gSWT)*sw)/Lambda)))*-1.0) + Complex(( ((((1.0*(-ii))*1.0)*((((((-2.0*cw)*ii)*gSBL)*Lambda)*sw)+(((((2.0*cw)*ii)*gSWL)*Lambda)*sw)))*1.0) )* GeV2/invariant(1,2)));
    a11( 0.0 );
    a12( 0.0 );
    a21( ((((1.0*(-ii))*1.0)*((((((-4.0*cw)*ii)*gSBT)*sw)/Lambda)+(((((4.0*cw)*ii)*gSWT)*sw)/Lambda)))*1.0) );
    a22( 0.0 ); aEp( ((((1.0*(-ii))*1.0)*((((((2.0*cw)*ii)*gPBT)*sw)/Lambda)-(((((2.0*cw)*ii)*gPWT)*sw)/Lambda)))*(-1.0+-1.0)) ); 
    
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
    GeneralVVSVertex::doinit();
  }
  //    void getParams(Energy2);
 private:
  FRModelV_V_22 & operator=(const FRModelV_V_22 &);
  //    Complex leftval, rightval, normval;
  tcHwFRModelPtr model_;
};
DescribeClass<FRModelV_V_22,Helicity::GeneralVVSVertex>
describeHerwigFRModelV_V_22("Herwig::FRModelV_V_22",
				       "FRModel.so");
// void FRModelV_V_22::getParams(Energy2 ) {
// }

class FRModelV_V_23: public GeneralVVSVertex {
 public:
  FRModelV_V_23() {
    kinematics(true);
    addToList(23,23,9000006);
  }
  void setCoupling(Energy2 ,tcPDPtr,tcPDPtr,tcPDPtr) {
    double gSBT = model_->gSBT();
    double vev = model_->vev();
    double gSh1 = model_->gSh1();
    double gSWL = model_->gSWL();
    double ee = model_->ee();
    double sw = model_->sw();
    double gPWT = model_->gPWT();
    double gPBT = model_->gPBT();
    double gSBL = model_->gSBL();
    double Lambda = model_->Lambda();
    double cw = model_->cw();
    double gSWT = model_->gSWT();
    //    getParams(q2);
    norm(Complex(-(1.0) * UnitRemoval::E / GeV ));
    a00( ((((1.0*(-ii))*1.0)*(((((4.0*sqr(cw))*ii)*gSWT)/Lambda)+((((4.0*ii)*gSBT)*sqr(sw))/Lambda)))*-1.0) + Complex(( ((((1.0*(-ii))*1.0)*((((((((2.0*sqr(cw))*ii)*gSWL)*Lambda)+((((2.0*ii)*gSBL)*Lambda)*sqr(sw)))+((((sqr(ee)*ii)*gSh1)*sqr(vev))/(2.0*Lambda)))+(((((sqr(cw)*sqr(ee))*ii)*gSh1)*sqr(vev))/((4.0*Lambda)*sqr(sw))))+(((((sqr(ee)*ii)*gSh1)*sqr(sw))*sqr(vev))/((4.0*sqr(cw))*Lambda))))*1.0) )* GeV2/invariant(1,2)));
    a11( 0.0 );
    a12( 0.0 );
    a21( ((((1.0*(-ii))*1.0)*(((((4.0*sqr(cw))*ii)*gSWT)/Lambda)+((((4.0*ii)*gSBT)*sqr(sw))/Lambda)))*1.0) );
    a22( 0.0 ); aEp( ((((1.0*(-ii))*1.0)*(((((-2.0*sqr(cw))*ii)*gPWT)/Lambda)-((((2.0*ii)*gPBT)*sqr(sw))/Lambda)))*(-1.0+-1.0)) ); 
    
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
    GeneralVVSVertex::doinit();
  }
  //    void getParams(Energy2);
 private:
  FRModelV_V_23 & operator=(const FRModelV_V_23 &);
  //    Complex leftval, rightval, normval;
  tcHwFRModelPtr model_;
};
DescribeClass<FRModelV_V_23,Helicity::GeneralVVSVertex>
describeHerwigFRModelV_V_23("Herwig::FRModelV_V_23",
				       "FRModel.so");
// void FRModelV_V_23::getParams(Energy2 ) {
// }

class FRModelV_V_47: public FFSVertex {
 public:
  FRModelV_V_47() {
    kinematics(false);
    addToList(-5,5,9000006);
  }
  void setCoupling(Energy2 ,tcPDPtr,tcPDPtr,tcPDPtr) {
    double gPd33 = model_->gPd33();
    double gSd33 = model_->gSd33();
    //    getParams(q2);
    norm(1.0);
    left((((((1.0*(-ii))*1.0)*1.0)*((ii*gSd33)/sqrt(2.0)))+((((1.0*(-ii))*1.0)*-1.0)*((ii*gPd33)/sqrt(2.0)))));
    right((((((1.0*(-ii))*1.0)*1.0)*((ii*gSd33)/sqrt(2.0)))+((((1.0*(-ii))*1.0)*1.0)*((ii*gPd33)/sqrt(2.0)))));
    
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
  FRModelV_V_47 & operator=(const FRModelV_V_47 &);
  //    Complex leftval, rightval, normval;
  tcHwFRModelPtr model_;
};
DescribeClass<FRModelV_V_47,Helicity::FFSVertex>
describeHerwigFRModelV_V_47("Herwig::FRModelV_V_47",
				       "FRModel.so");
// void FRModelV_V_47::getParams(Energy2 ) {
// }

class FRModelV_V_48: public FFSVertex {
 public:
  FRModelV_V_48() {
    kinematics(false);
    addToList(-4,4,9000006);
  }
  void setCoupling(Energy2 ,tcPDPtr,tcPDPtr,tcPDPtr) {
    double gSu22 = model_->gSu22();
    double gPu22 = model_->gPu22();
    //    getParams(q2);
    norm(1.0);
    left((((((1.0*(-ii))*1.0)*1.0)*((ii*gSu22)/sqrt(2.0)))+((((1.0*(-ii))*1.0)*-1.0)*((ii*gPu22)/sqrt(2.0)))));
    right((((((1.0*(-ii))*1.0)*1.0)*((ii*gSu22)/sqrt(2.0)))+((((1.0*(-ii))*1.0)*1.0)*((ii*gPu22)/sqrt(2.0)))));
    
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
  FRModelV_V_48 & operator=(const FRModelV_V_48 &);
  //    Complex leftval, rightval, normval;
  tcHwFRModelPtr model_;
};
DescribeClass<FRModelV_V_48,Helicity::FFSVertex>
describeHerwigFRModelV_V_48("Herwig::FRModelV_V_48",
				       "FRModel.so");
// void FRModelV_V_48::getParams(Energy2 ) {
// }

class FRModelV_V_49: public FFSVertex {
 public:
  FRModelV_V_49() {
    kinematics(false);
    addToList(-1,1,9000006);
  }
  void setCoupling(Energy2 ,tcPDPtr,tcPDPtr,tcPDPtr) {
    double gPd11 = model_->gPd11();
    double gSd11 = model_->gSd11();
    //    getParams(q2);
    norm(1.0);
    left((((((1.0*(-ii))*1.0)*1.0)*((ii*gSd11)/sqrt(2.0)))+((((1.0*(-ii))*1.0)*-1.0)*((ii*gPd11)/sqrt(2.0)))));
    right((((((1.0*(-ii))*1.0)*1.0)*((ii*gSd11)/sqrt(2.0)))+((((1.0*(-ii))*1.0)*1.0)*((ii*gPd11)/sqrt(2.0)))));
    
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
  FRModelV_V_49 & operator=(const FRModelV_V_49 &);
  //    Complex leftval, rightval, normval;
  tcHwFRModelPtr model_;
};
DescribeClass<FRModelV_V_49,Helicity::FFSVertex>
describeHerwigFRModelV_V_49("Herwig::FRModelV_V_49",
				       "FRModel.so");
// void FRModelV_V_49::getParams(Energy2 ) {
// }

class FRModelV_V_50: public FFSVertex {
 public:
  FRModelV_V_50() {
    kinematics(false);
    addToList(-11,11,9000006);
  }
  void setCoupling(Energy2 ,tcPDPtr,tcPDPtr,tcPDPtr) {
    double gPe = model_->gPe();
    double gSe = model_->gSe();
    //    getParams(q2);
    norm(1.0);
    left((((((1.0*(-ii))*1.0)*1.0)*((ii*gSe)/sqrt(2.0)))+((((1.0*(-ii))*1.0)*-1.0)*((ii*gPe)/sqrt(2.0)))));
    right((((((1.0*(-ii))*1.0)*1.0)*((ii*gSe)/sqrt(2.0)))+((((1.0*(-ii))*1.0)*1.0)*((ii*gPe)/sqrt(2.0)))));
    
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
  FRModelV_V_50 & operator=(const FRModelV_V_50 &);
  //    Complex leftval, rightval, normval;
  tcHwFRModelPtr model_;
};
DescribeClass<FRModelV_V_50,Helicity::FFSVertex>
describeHerwigFRModelV_V_50("Herwig::FRModelV_V_50",
				       "FRModel.so");
// void FRModelV_V_50::getParams(Energy2 ) {
// }

}

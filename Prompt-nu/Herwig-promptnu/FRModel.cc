// -*- C++ -*-
//
// FRModel.cc is a part of Herwig - A multi-purpose Monte Carlo event generator
// Copyright (C) 2002-2007 The Herwig Collaboration
//
// Herwig is licenced under version 2 of the GPL, see COPYING for details.
// Please respect the MCnet academic guidelines, see GUIDELINES for details.
//
//
// This is the implementation of the non-inlined, non-templated member
// functions of the FRModel class.
//

#include "FRModel.h"
#include "ThePEG/Interface/ClassDocumentation.h"
#include "ThePEG/Interface/Reference.h"
#include "ThePEG/Interface/Parameter.h"
#include "ThePEG/Persistency/PersistentOStream.h"
#include "ThePEG/Persistency/PersistentIStream.h"
#include "ThePEG/Helicity/Vertex/VertexBase.h"
#include "ThePEG/Utilities/DescribeClass.h"
#include <fstream>

//#include "Herwig/Models/General/ModelGenerator.h"

using namespace ThePEG;
using namespace Herwig;

FRModel::FRModel()
: ZERO_(),
cabi_(0.227736),gSf_(1.0),Lambda_(1.0),gSEW_(1.0),gPg_(0.0),
aEWM1_(127.9),Gf_(1.16637e-05),aS_(0.1184),ymdo_(0.00504),ymup_(0.00255),
yms_(0.101),ymc_(1.27),ymb_(4.7),ymt_(172),yme_(0.000511),
ymm_(0.10566),ymtau_(1.777),MZ_(91.1876),Me_(0.000511),MMU_(0.10566),
MTA_(1.777),MU_(0.00255),MC_(1.27),MT_(172),MD_(0.00504),
MS_(0.101),MB_(4.7),MH_(125),MGR_(100.0),WZ_(2.4952),
WW_(2.085),WT_(1.50833649),WH_(0.00407),WGR_(10.0),aEW_(),
G_(),CKM1x1_(0.0,0.0),CKM1x2_(0.0,0.0),CKM1x3_(0.0,0.0),CKM2x1_(0.0,0.0),
CKM2x2_(0.0,0.0),CKM2x3_(0.0,0.0),CKM3x1_(0.0,0.0),CKM3x2_(0.0,0.0),CKM3x3_(0.0,0.0),
MW_(),ee_(),sw2_(),cw_(),sw_(),
g1_(),gw_(),vev_(),lam_(),yb_(),
yc_(),ydo_(),ye_(),ym_(),ys_(),
yt_(),ytau_(),yup_(),muH_(),I1b11_(0.0,0.0),
I1b12_(0.0,0.0),I1b13_(0.0,0.0),I1b21_(0.0,0.0),I1b22_(0.0,0.0),I1b23_(0.0,0.0),
I1b31_(0.0,0.0),I1b32_(0.0,0.0),I1b33_(0.0,0.0),I2b11_(0.0,0.0),I2b12_(0.0,0.0),
I2b13_(0.0,0.0),I2b21_(0.0,0.0),I2b22_(0.0,0.0),I2b23_(0.0,0.0),I2b31_(0.0,0.0),
I2b32_(0.0,0.0),I2b33_(0.0,0.0),I3b11_(0.0,0.0),I3b12_(0.0,0.0),I3b13_(0.0,0.0),
I3b21_(0.0,0.0),I3b22_(0.0,0.0),I3b23_(0.0,0.0),I3b31_(0.0,0.0),I3b32_(0.0,0.0),
I3b33_(0.0,0.0),I4b11_(0.0,0.0),I4b12_(0.0,0.0),I4b13_(0.0,0.0),I4b21_(0.0,0.0),
I4b22_(0.0,0.0),I4b23_(0.0,0.0),I4b31_(0.0,0.0),I4b32_(0.0,0.0),I4b33_(0.0,0.0)

{}

IBPtr FRModel::clone() const {
  return new_ptr(*this);
}

IBPtr FRModel::fullclone() const {
  return new_ptr(*this);
}

void FRModel::doinit() {
     ZERO_ = 0.0;
   aEW_ = (1.0/aEWM1());
   G_ = ((2.0*sqrt(aS()))*sqrt(pi));
   CKM1x1_ = cos(cabi());
   CKM1x2_ = sin(cabi());
   CKM1x3_ = 0.0;
   CKM2x1_ = (-sin(cabi()));
   CKM2x2_ = cos(cabi());
   CKM2x3_ = 0.0;
   CKM3x1_ = 0.0;
   CKM3x2_ = 0.0;
   CKM3x3_ = 1.0;
   MW_ = sqrt(((sqr(MZ())/2.0)+sqrt(((pow(MZ(),4.0)/4.0)-(((aEW()*pi)*sqr(MZ()))/(Gf()*sqrt(2.0)))))));
   ee_ = ((2.0*sqrt(aEW()))*sqrt(pi));
   sw2_ = (1.0-(sqr(MW())/sqr(MZ())));
   cw_ = sqrt((1.0-sw2()));
   sw_ = sqrt(sw2());
   g1_ = (ee()/cw());
   gw_ = (ee()/sw());
   vev_ = (((2.0*MW())*sw())/ee());
   lam_ = (sqr(MH())/(2.0*sqr(vev())));
   yb_ = ((ymb()*sqrt(2.0))/vev());
   yc_ = ((ymc()*sqrt(2.0))/vev());
   ydo_ = ((ymdo()*sqrt(2.0))/vev());
   ye_ = ((yme()*sqrt(2.0))/vev());
   ym_ = ((ymm()*sqrt(2.0))/vev());
   ys_ = ((yms()*sqrt(2.0))/vev());
   yt_ = ((ymt()*sqrt(2.0))/vev());
   ytau_ = ((ymtau()*sqrt(2.0))/vev());
   yup_ = ((ymup()*sqrt(2.0))/vev());
   muH_ = sqrt((lam()*sqr(vev())));
   I1b11_ = (ydo()*conj(CKM1x1()));
   I1b12_ = (ydo()*conj(CKM2x1()));
   I1b13_ = (ydo()*conj(CKM3x1()));
   I1b21_ = (ys()*conj(CKM1x2()));
   I1b22_ = (ys()*conj(CKM2x2()));
   I1b23_ = (ys()*conj(CKM3x2()));
   I1b31_ = (yb()*conj(CKM1x3()));
   I1b32_ = (yb()*conj(CKM2x3()));
   I1b33_ = (yb()*conj(CKM3x3()));
   I2b11_ = (yup()*conj(CKM1x1()));
   I2b12_ = (yc()*conj(CKM2x1()));
   I2b13_ = (yt()*conj(CKM3x1()));
   I2b21_ = (yup()*conj(CKM1x2()));
   I2b22_ = (yc()*conj(CKM2x2()));
   I2b23_ = (yt()*conj(CKM3x2()));
   I2b31_ = (yup()*conj(CKM1x3()));
   I2b32_ = (yc()*conj(CKM2x3()));
   I2b33_ = (yt()*conj(CKM3x3()));
   I3b11_ = (CKM1x1()*yup());
   I3b12_ = (CKM1x2()*yup());
   I3b13_ = (CKM1x3()*yup());
   I3b21_ = (CKM2x1()*yc());
   I3b22_ = (CKM2x2()*yc());
   I3b23_ = (CKM2x3()*yc());
   I3b31_ = (CKM3x1()*yt());
   I3b32_ = (CKM3x2()*yt());
   I3b33_ = (CKM3x3()*yt());
   I4b11_ = (CKM1x1()*ydo());
   I4b12_ = (CKM1x2()*ys());
   I4b13_ = (CKM1x3()*yb());
   I4b21_ = (CKM2x1()*ydo());
   I4b22_ = (CKM2x2()*ys());
   I4b23_ = (CKM2x3()*yb());
   I4b31_ = (CKM3x1()*ydo());
   I4b32_ = (CKM3x2()*ys());
   I4b33_ = (CKM3x3()*yb());
  BSMModel::doinit();
  
  writeParamCard();
}

void FRModel::doinitrun() {
  BSMModel::doinitrun();
  writeParamCard();
}

void FRModel::persistentOutput(PersistentOStream & os) const {
  os << ZERO_
<< cabi_<< gSf_<< Lambda_<< gSEW_<< gPg_
<< aEWM1_<< Gf_<< aS_<< ymdo_<< ymup_
<< yms_<< ymc_<< ymb_<< ymt_<< yme_
<< ymm_<< ymtau_<< MZ_<< Me_<< MMU_
<< MTA_<< MU_<< MC_<< MT_<< MD_
<< MS_<< MB_<< MH_<< MGR_<< WZ_
<< WW_<< WT_<< WH_<< WGR_<< aEW_
<< G_<< CKM1x1_<< CKM1x2_<< CKM1x3_<< CKM2x1_
<< CKM2x2_<< CKM2x3_<< CKM3x1_<< CKM3x2_<< CKM3x3_
<< MW_<< ee_<< sw2_<< cw_<< sw_
<< g1_<< gw_<< vev_<< lam_<< yb_
<< yc_<< ydo_<< ye_<< ym_<< ys_
<< yt_<< ytau_<< yup_<< muH_<< I1b11_
<< I1b12_<< I1b13_<< I1b21_<< I1b22_<< I1b23_
<< I1b31_<< I1b32_<< I1b33_<< I2b11_<< I2b12_
<< I2b13_<< I2b21_<< I2b22_<< I2b23_<< I2b31_
<< I2b32_<< I2b33_<< I3b11_<< I3b12_<< I3b13_
<< I3b21_<< I3b22_<< I3b23_<< I3b31_<< I3b32_
<< I3b33_<< I4b11_<< I4b12_<< I4b13_<< I4b21_
<< I4b22_<< I4b23_<< I4b31_<< I4b32_<< I4b33_
 ;
}

void FRModel::persistentInput(PersistentIStream & is, int) {
  is >> ZERO_
>> cabi_>> gSf_>> Lambda_>> gSEW_>> gPg_
>> aEWM1_>> Gf_>> aS_>> ymdo_>> ymup_
>> yms_>> ymc_>> ymb_>> ymt_>> yme_
>> ymm_>> ymtau_>> MZ_>> Me_>> MMU_
>> MTA_>> MU_>> MC_>> MT_>> MD_
>> MS_>> MB_>> MH_>> MGR_>> WZ_
>> WW_>> WT_>> WH_>> WGR_>> aEW_
>> G_>> CKM1x1_>> CKM1x2_>> CKM1x3_>> CKM2x1_
>> CKM2x2_>> CKM2x3_>> CKM3x1_>> CKM3x2_>> CKM3x3_
>> MW_>> ee_>> sw2_>> cw_>> sw_
>> g1_>> gw_>> vev_>> lam_>> yb_
>> yc_>> ydo_>> ye_>> ym_>> ys_
>> yt_>> ytau_>> yup_>> muH_>> I1b11_
>> I1b12_>> I1b13_>> I1b21_>> I1b22_>> I1b23_
>> I1b31_>> I1b32_>> I1b33_>> I2b11_>> I2b12_
>> I2b13_>> I2b21_>> I2b22_>> I2b23_>> I2b31_
>> I2b32_>> I2b33_>> I3b11_>> I3b12_>> I3b13_
>> I3b21_>> I3b22_>> I3b23_>> I3b31_>> I3b32_
>> I3b33_>> I4b11_>> I4b12_>> I4b13_>> I4b21_
>> I4b22_>> I4b23_>> I4b31_>> I4b32_>> I4b33_
 ;
}

void FRModel::writeParamCard() const {
  ofstream card("param_card.dat");

  card 
    << "#####################################################\n"
    << "## DO NOT EDIT - GENERATED BY HERWIG UFO CONVERTER ##\n"
    << "#####################################################\n\n";

  card 
    << "Block YUKAWA\n"
<< "    1 " << ymdo() << " # ymdo\n"
<< "    2 " << ymup() << " # ymup\n"
<< "    3 " << yms() << " # yms\n"
<< "    4 " << ymc() << " # ymc\n"
<< "    5 " << ymb() << " # ymb\n"
<< "    6 " << ymt() << " # ymt\n"
<< "   11 " << yme() << " # yme\n"
<< "   13 " << ymm() << " # ymm\n"
<< "   15 " << ymtau() << " # ymtau\n"
<< "DECAY  23 " << WZ() << "\n"
<< "DECAY  24 " << WW() << "\n"
<< "DECAY   6 " << WT() << "\n"
<< "DECAY  25 " << WH() << "\n"
<< "DECAY 999 " << WGR() << "\n"
<< "Block CKMBLOCK\n"
<< "    1 " << cabi() << " # cabi\n"
<< "Block MASS\n"
<< "   23 " << MZ() << " # MZ\n"
<< "   11 " << Me() << " # Me\n"
<< "   13 " << MMU() << " # MMU\n"
<< "   15 " << MTA() << " # MTA\n"
<< "    2 " << MU() << " # MU\n"
<< "    4 " << MC() << " # MC\n"
<< "    6 " << MT() << " # MT\n"
<< "    1 " << MD() << " # MD\n"
<< "    3 " << MS() << " # MS\n"
<< "    5 " << MB() << " # MB\n"
<< "   25 " << MH() << " # MH\n"
<< "  999 " << MGR() << " # MGR\n"
<< "Block DMINPUTS\n"
<< "    1 " << gSf() << " # gSf\n"
<< "    2 " << Lambda() << " # Lambda\n"
<< "    3 " << gSEW() << " # gSEW\n"
<< "    4 " << gPg() << " # gPg\n"
<< "Block SMINPUTS\n"
<< "    1 " << aEWM1() << " # aEWM1\n"
<< "    2 " << Gf() << " # Gf\n"
<< "    3 " << aS() << " # aS\n"
    << '\n';

  card.close();
}

// Static variable needed for the type description system in ThePEG.
DescribeClass<FRModel,BSMModel>
  describeThePEGFRModel("Herwig::FRModel", "FRModel.so");

void FRModel::Init() {
  


static ClassDocumentation<FRModel> documentation
  ("The FRModel class inherits from BSMModel"
   "and supplies additional couplings and access to the FRModel"
   "vertices for helicity amplitude calculations" );

 static Parameter<FRModel, double> interfacecabi
  ("cabi",
   "The interface for parameter cabi",
   &FRModel::cabi_, 0.227736, 0, 0,
   false, false, Interface::nolimits);
static Parameter<FRModel, double> interfacegSf
  ("gSf",
   "The interface for parameter gSf",
   &FRModel::gSf_, 1.0, 0, 0,
   false, false, Interface::nolimits);
static Parameter<FRModel, double> interfaceLambda
  ("Lambda",
   "The interface for parameter Lambda",
   &FRModel::Lambda_, 1.0, 0, 0,
   false, false, Interface::nolimits);
static Parameter<FRModel, double> interfacegSEW
  ("gSEW",
   "The interface for parameter gSEW",
   &FRModel::gSEW_, 1.0, 0, 0,
   false, false, Interface::nolimits);
static Parameter<FRModel, double> interfacegPg
  ("gPg",
   "The interface for parameter gPg",
   &FRModel::gPg_, 0.0, 0, 0,
   false, false, Interface::nolimits);
static Parameter<FRModel, double> interfaceaEWM1
  ("aEWM1",
   "The interface for parameter aEWM1",
   &FRModel::aEWM1_, 127.9, 0, 0,
   false, false, Interface::nolimits);
static Parameter<FRModel, double> interfaceGf
  ("Gf",
   "The interface for parameter Gf",
   &FRModel::Gf_, 1.16637e-05, 0, 0,
   false, false, Interface::nolimits);
static Parameter<FRModel, double> interfaceaS
  ("aS",
   "The interface for parameter aS",
   &FRModel::aS_, 0.1184, 0, 0,
   false, false, Interface::nolimits);
static Parameter<FRModel, double> interfaceymdo
  ("ymdo",
   "The interface for parameter ymdo",
   &FRModel::ymdo_, 0.00504, 0, 0,
   false, false, Interface::nolimits);
static Parameter<FRModel, double> interfaceymup
  ("ymup",
   "The interface for parameter ymup",
   &FRModel::ymup_, 0.00255, 0, 0,
   false, false, Interface::nolimits);
static Parameter<FRModel, double> interfaceyms
  ("yms",
   "The interface for parameter yms",
   &FRModel::yms_, 0.101, 0, 0,
   false, false, Interface::nolimits);
static Parameter<FRModel, double> interfaceymc
  ("ymc",
   "The interface for parameter ymc",
   &FRModel::ymc_, 1.27, 0, 0,
   false, false, Interface::nolimits);
static Parameter<FRModel, double> interfaceymb
  ("ymb",
   "The interface for parameter ymb",
   &FRModel::ymb_, 4.7, 0, 0,
   false, false, Interface::nolimits);
static Parameter<FRModel, double> interfaceymt
  ("ymt",
   "The interface for parameter ymt",
   &FRModel::ymt_, 172, 0, 0,
   false, false, Interface::nolimits);
static Parameter<FRModel, double> interfaceyme
  ("yme",
   "The interface for parameter yme",
   &FRModel::yme_, 0.000511, 0, 0,
   false, false, Interface::nolimits);
static Parameter<FRModel, double> interfaceymm
  ("ymm",
   "The interface for parameter ymm",
   &FRModel::ymm_, 0.10566, 0, 0,
   false, false, Interface::nolimits);
static Parameter<FRModel, double> interfaceymtau
  ("ymtau",
   "The interface for parameter ymtau",
   &FRModel::ymtau_, 1.777, 0, 0,
   false, false, Interface::nolimits);
static Parameter<FRModel, double> interfaceMZ
  ("MZ",
   "The interface for parameter MZ",
   &FRModel::MZ_, 91.1876, 0, 0,
   false, false, Interface::nolimits);
static Parameter<FRModel, double> interfaceMe
  ("Me",
   "The interface for parameter Me",
   &FRModel::Me_, 0.000511, 0, 0,
   false, false, Interface::nolimits);
static Parameter<FRModel, double> interfaceMMU
  ("MMU",
   "The interface for parameter MMU",
   &FRModel::MMU_, 0.10566, 0, 0,
   false, false, Interface::nolimits);
static Parameter<FRModel, double> interfaceMTA
  ("MTA",
   "The interface for parameter MTA",
   &FRModel::MTA_, 1.777, 0, 0,
   false, false, Interface::nolimits);
static Parameter<FRModel, double> interfaceMU
  ("MU",
   "The interface for parameter MU",
   &FRModel::MU_, 0.00255, 0, 0,
   false, false, Interface::nolimits);
static Parameter<FRModel, double> interfaceMC
  ("MC",
   "The interface for parameter MC",
   &FRModel::MC_, 1.27, 0, 0,
   false, false, Interface::nolimits);
static Parameter<FRModel, double> interfaceMT
  ("MT",
   "The interface for parameter MT",
   &FRModel::MT_, 172, 0, 0,
   false, false, Interface::nolimits);
static Parameter<FRModel, double> interfaceMD
  ("MD",
   "The interface for parameter MD",
   &FRModel::MD_, 0.00504, 0, 0,
   false, false, Interface::nolimits);
static Parameter<FRModel, double> interfaceMS
  ("MS",
   "The interface for parameter MS",
   &FRModel::MS_, 0.101, 0, 0,
   false, false, Interface::nolimits);
static Parameter<FRModel, double> interfaceMB
  ("MB",
   "The interface for parameter MB",
   &FRModel::MB_, 4.7, 0, 0,
   false, false, Interface::nolimits);
static Parameter<FRModel, double> interfaceMH
  ("MH",
   "The interface for parameter MH",
   &FRModel::MH_, 125, 0, 0,
   false, false, Interface::nolimits);
static Parameter<FRModel, double> interfaceMGR
  ("MGR",
   "The interface for parameter MGR",
   &FRModel::MGR_, 100.0, 0, 0,
   false, false, Interface::nolimits);
static Parameter<FRModel, double> interfaceWZ
  ("WZ",
   "The interface for parameter WZ",
   &FRModel::WZ_, 2.4952, 0, 0,
   false, false, Interface::nolimits);
static Parameter<FRModel, double> interfaceWW
  ("WW",
   "The interface for parameter WW",
   &FRModel::WW_, 2.085, 0, 0,
   false, false, Interface::nolimits);
static Parameter<FRModel, double> interfaceWT
  ("WT",
   "The interface for parameter WT",
   &FRModel::WT_, 1.50833649, 0, 0,
   false, false, Interface::nolimits);
static Parameter<FRModel, double> interfaceWH
  ("WH",
   "The interface for parameter WH",
   &FRModel::WH_, 0.00407, 0, 0,
   false, false, Interface::nolimits);
static Parameter<FRModel, double> interfaceWGR
  ("WGR",
   "The interface for parameter WGR",
   &FRModel::WGR_, 10.0, 0, 0,
   false, false, Interface::nolimits);


}



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
cabi_(0.227736),gSh1_(1.0),gSh2_(1.0),gSWT_(1.0),gPWT_(1.0),
gPBT_(1.0),gSBT_(1.0),gSWL_(1.0),gSBL_(1.0),gSg_(1.0),
gPg_(1.0),gSd11_(1.0),gSu11_(1.0),gSd22_(1.0),gSu22_(1.0),
gSd33_(1.0),gSu33_(1.0),gPd11_(1.0),gPu11_(1.0),gPd22_(1.0),
gPu22_(1.0),gPd33_(1.0),gPu33_(1.0),gSe_(1.0),gPe_(1.0),
gSmm_(1.0),gPmm_(1.0),gSta_(1.0),gPta_(1.0),gVd11_(1.0),
gVu11_(1.0),gVd22_(1.0),gVu22_(1.0),gVd33_(1.0),gVu33_(1.0),
gAd11_(1.0),gAu11_(1.0),gAd22_(1.0),gAu22_(1.0),gAd33_(1.0),
gAu33_(1.0),gVe_(1.0),gAe_(1.0),gVmm_(1.0),gAmm_(1.0),
gVta_(1.0),gAta_(1.0),gSXr_(1.0),gSXc_(1.0),gSXd_(1.0),
gPXd_(1.0),gVXd_(1.0),gAXd_(1.0),Lambda_(1.0),aEWM1_(127.9),
Gf_(1.16637e-05),aS_(0.1181),ymdo_(0.00504),ymup_(0.00255),yms_(0.095),
ymc_(1.27),ymb_(4.78),ymt_(173),yme_(0.000511),ymm_(0.10566),
ymtau_(1.777),MZ_(91.1876),Me_(0.000511),MMU_(0.10566),MTA_(1.777),
MU_(0.00255),MC_(1.27),MT_(173),MD_(0.00504),MS_(0.095),
MB_(4.78),MH_(125.18),MD0_(1000.0),MD1_(1000.0),MXr_(1.0),
MXc_(499.0),MXd_(499.0),WZ_(2.4952),WW_(2.085),WE_(0.0),
WMU_(3e-19),WTA_(2.27e-12),WT_(1.41),WH_(0.00407),WD0_(10.0),
WD1_(10.0),aEW_(),G_(),CKM1x1_(0.0,0.0),CKM1x2_(0.0,0.0),
CKM1x3_(0.0,0.0),CKM2x1_(0.0,0.0),CKM2x2_(0.0,0.0),CKM2x3_(0.0,0.0),CKM3x1_(0.0,0.0),
CKM3x2_(0.0,0.0),CKM3x3_(0.0,0.0),MW_(),ee_(),sw2_(),
cw_(),sw_(),g1_(),gw_(),vev_(),
lam_(),yb_(),yc_(),ydo_(),ye_(),
ym_(),ys_(),yt_(),ytau_(),yup_(),
muH_(),I1a11_(0.0,0.0),I1a12_(0.0,0.0),I1a13_(0.0,0.0),I1a21_(0.0,0.0),
I1a22_(0.0,0.0),I1a23_(0.0,0.0),I1a31_(0.0,0.0),I1a32_(0.0,0.0),I1a33_(0.0,0.0),
I2a11_(0.0,0.0),I2a12_(0.0,0.0),I2a13_(0.0,0.0),I2a21_(0.0,0.0),I2a22_(0.0,0.0),
I2a23_(0.0,0.0),I2a31_(0.0,0.0),I2a32_(0.0,0.0),I2a33_(0.0,0.0),I3a11_(0.0,0.0),
I3a12_(0.0,0.0),I3a13_(0.0,0.0),I3a21_(0.0,0.0),I3a22_(0.0,0.0),I3a23_(0.0,0.0),
I3a31_(0.0,0.0),I3a32_(0.0,0.0),I3a33_(0.0,0.0),I4a11_(0.0,0.0),I4a12_(0.0,0.0),
I4a13_(0.0,0.0),I4a21_(0.0,0.0),I4a22_(0.0,0.0),I4a23_(0.0,0.0),I4a31_(0.0,0.0),
I4a32_(0.0,0.0),I4a33_(0.0,0.0)
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
   I1a11_ = (ydo()*conj(CKM1x1()));
   I1a12_ = (ydo()*conj(CKM2x1()));
   I1a13_ = (ydo()*conj(CKM3x1()));
   I1a21_ = (ys()*conj(CKM1x2()));
   I1a22_ = (ys()*conj(CKM2x2()));
   I1a23_ = (ys()*conj(CKM3x2()));
   I1a31_ = (yb()*conj(CKM1x3()));
   I1a32_ = (yb()*conj(CKM2x3()));
   I1a33_ = (yb()*conj(CKM3x3()));
   I2a11_ = (yup()*conj(CKM1x1()));
   I2a12_ = (yc()*conj(CKM2x1()));
   I2a13_ = (yt()*conj(CKM3x1()));
   I2a21_ = (yup()*conj(CKM1x2()));
   I2a22_ = (yc()*conj(CKM2x2()));
   I2a23_ = (yt()*conj(CKM3x2()));
   I2a31_ = (yup()*conj(CKM1x3()));
   I2a32_ = (yc()*conj(CKM2x3()));
   I2a33_ = (yt()*conj(CKM3x3()));
   I3a11_ = (CKM1x1()*yup());
   I3a12_ = (CKM1x2()*yup());
   I3a13_ = (CKM1x3()*yup());
   I3a21_ = (CKM2x1()*yc());
   I3a22_ = (CKM2x2()*yc());
   I3a23_ = (CKM2x3()*yc());
   I3a31_ = (CKM3x1()*yt());
   I3a32_ = (CKM3x2()*yt());
   I3a33_ = (CKM3x3()*yt());
   I4a11_ = (CKM1x1()*ydo());
   I4a12_ = (CKM1x2()*ys());
   I4a13_ = (CKM1x3()*yb());
   I4a21_ = (CKM2x1()*ydo());
   I4a22_ = (CKM2x2()*ys());
   I4a23_ = (CKM2x3()*yb());
   I4a31_ = (CKM3x1()*ydo());
   I4a32_ = (CKM3x2()*ys());
   I4a33_ = (CKM3x3()*yb());
  BSMModel::doinit();
  
  writeParamCard();
}

void FRModel::doinitrun() {
  BSMModel::doinitrun();
  writeParamCard();
}

void FRModel::persistentOutput(PersistentOStream & os) const {
  os << ZERO_
<< cabi_<< gSh1_<< gSh2_<< gSWT_<< gPWT_
<< gPBT_<< gSBT_<< gSWL_<< gSBL_<< gSg_
<< gPg_<< gSd11_<< gSu11_<< gSd22_<< gSu22_
<< gSd33_<< gSu33_<< gPd11_<< gPu11_<< gPd22_
<< gPu22_<< gPd33_<< gPu33_<< gSe_<< gPe_
<< gSmm_<< gPmm_<< gSta_<< gPta_<< gVd11_
<< gVu11_<< gVd22_<< gVu22_<< gVd33_<< gVu33_
<< gAd11_<< gAu11_<< gAd22_<< gAu22_<< gAd33_
<< gAu33_<< gVe_<< gAe_<< gVmm_<< gAmm_
<< gVta_<< gAta_<< gSXr_<< gSXc_<< gSXd_
<< gPXd_<< gVXd_<< gAXd_<< Lambda_<< aEWM1_
<< Gf_<< aS_<< ymdo_<< ymup_<< yms_
<< ymc_<< ymb_<< ymt_<< yme_<< ymm_
<< ymtau_<< MZ_<< Me_<< MMU_<< MTA_
<< MU_<< MC_<< MT_<< MD_<< MS_
<< MB_<< MH_<< MD0_<< MD1_<< MXr_
<< MXc_<< MXd_<< WZ_<< WW_<< WE_
<< WMU_<< WTA_<< WT_<< WH_<< WD0_
<< WD1_<< aEW_<< G_<< CKM1x1_<< CKM1x2_
<< CKM1x3_<< CKM2x1_<< CKM2x2_<< CKM2x3_<< CKM3x1_
<< CKM3x2_<< CKM3x3_<< MW_<< ee_<< sw2_
<< cw_<< sw_<< g1_<< gw_<< vev_
<< lam_<< yb_<< yc_<< ydo_<< ye_
<< ym_<< ys_<< yt_<< ytau_<< yup_
<< muH_<< I1a11_<< I1a12_<< I1a13_<< I1a21_
<< I1a22_<< I1a23_<< I1a31_<< I1a32_<< I1a33_
<< I2a11_<< I2a12_<< I2a13_<< I2a21_<< I2a22_
<< I2a23_<< I2a31_<< I2a32_<< I2a33_<< I3a11_
<< I3a12_<< I3a13_<< I3a21_<< I3a22_<< I3a23_
<< I3a31_<< I3a32_<< I3a33_<< I4a11_<< I4a12_
<< I4a13_<< I4a21_<< I4a22_<< I4a23_<< I4a31_
<< I4a32_<< I4a33_ ;
}

void FRModel::persistentInput(PersistentIStream & is, int) {
  is >> ZERO_
>> cabi_>> gSh1_>> gSh2_>> gSWT_>> gPWT_
>> gPBT_>> gSBT_>> gSWL_>> gSBL_>> gSg_
>> gPg_>> gSd11_>> gSu11_>> gSd22_>> gSu22_
>> gSd33_>> gSu33_>> gPd11_>> gPu11_>> gPd22_
>> gPu22_>> gPd33_>> gPu33_>> gSe_>> gPe_
>> gSmm_>> gPmm_>> gSta_>> gPta_>> gVd11_
>> gVu11_>> gVd22_>> gVu22_>> gVd33_>> gVu33_
>> gAd11_>> gAu11_>> gAd22_>> gAu22_>> gAd33_
>> gAu33_>> gVe_>> gAe_>> gVmm_>> gAmm_
>> gVta_>> gAta_>> gSXr_>> gSXc_>> gSXd_
>> gPXd_>> gVXd_>> gAXd_>> Lambda_>> aEWM1_
>> Gf_>> aS_>> ymdo_>> ymup_>> yms_
>> ymc_>> ymb_>> ymt_>> yme_>> ymm_
>> ymtau_>> MZ_>> Me_>> MMU_>> MTA_
>> MU_>> MC_>> MT_>> MD_>> MS_
>> MB_>> MH_>> MD0_>> MD1_>> MXr_
>> MXc_>> MXd_>> WZ_>> WW_>> WE_
>> WMU_>> WTA_>> WT_>> WH_>> WD0_
>> WD1_>> aEW_>> G_>> CKM1x1_>> CKM1x2_
>> CKM1x3_>> CKM2x1_>> CKM2x2_>> CKM2x3_>> CKM3x1_
>> CKM3x2_>> CKM3x3_>> MW_>> ee_>> sw2_
>> cw_>> sw_>> g1_>> gw_>> vev_
>> lam_>> yb_>> yc_>> ydo_>> ye_
>> ym_>> ys_>> yt_>> ytau_>> yup_
>> muH_>> I1a11_>> I1a12_>> I1a13_>> I1a21_
>> I1a22_>> I1a23_>> I1a31_>> I1a32_>> I1a33_
>> I2a11_>> I2a12_>> I2a13_>> I2a21_>> I2a22_
>> I2a23_>> I2a31_>> I2a32_>> I2a33_>> I3a11_
>> I3a12_>> I3a13_>> I3a21_>> I3a22_>> I3a23_
>> I3a31_>> I3a32_>> I3a33_>> I4a11_>> I4a12_
>> I4a13_>> I4a21_>> I4a22_>> I4a23_>> I4a31_
>> I4a32_>> I4a33_ ;
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
<< "DECAY  11 " << WE() << "\n"
<< "DECAY  13 " << WMU() << "\n"
<< "DECAY  15 " << WTA() << "\n"
<< "DECAY   6 " << WT() << "\n"
<< "DECAY  25 " << WH() << "\n"
<< "DECAY 9000006 " << WD0() << "\n"
<< "DECAY 9000007 " << WD1() << "\n"
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
<< "  9000006 " << MD0() << " # MD0\n"
<< "  9000007 " << MD1() << " # MD1\n"
<< "  9000008 " << MXr() << " # MXr\n"
<< "  9000009 " << MXc() << " # MXc\n"
<< "  9000010 " << MXd() << " # MXd\n"
<< "Block DMINPUTS\n"
<< "    1 " << gSh1() << " # gSh1\n"
<< "    2 " << gSh2() << " # gSh2\n"
<< "    3 " << gSWT() << " # gSWT\n"
<< "    4 " << gPWT() << " # gPWT\n"
<< "    5 " << gPBT() << " # gPBT\n"
<< "    6 " << gSBT() << " # gSBT\n"
<< "    7 " << gSWL() << " # gSWL\n"
<< "    8 " << gSBL() << " # gSBL\n"
<< "    9 " << gSg() << " # gSg\n"
<< "   10 " << gPg() << " # gPg\n"
<< "   11 " << gSd11() << " # gSd11\n"
<< "   12 " << gSu11() << " # gSu11\n"
<< "   13 " << gSd22() << " # gSd22\n"
<< "   14 " << gSu22() << " # gSu22\n"
<< "   15 " << gSd33() << " # gSd33\n"
<< "   16 " << gSu33() << " # gSu33\n"
<< "   17 " << gPd11() << " # gPd11\n"
<< "   18 " << gPu11() << " # gPu11\n"
<< "   19 " << gPd22() << " # gPd22\n"
<< "   20 " << gPu22() << " # gPu22\n"
<< "   21 " << gPd33() << " # gPd33\n"
<< "   22 " << gPu33() << " # gPu33\n"
<< "   23 " << gSe() << " # gSe\n"
<< "   24 " << gPe() << " # gPe\n"
<< "   25 " << gSmm() << " # gSmm\n"
<< "   26 " << gPmm() << " # gPmm\n"
<< "   27 " << gSta() << " # gSta\n"
<< "   28 " << gPta() << " # gPta\n"
<< "   29 " << gVd11() << " # gVd11\n"
<< "   30 " << gVu11() << " # gVu11\n"
<< "   31 " << gVd22() << " # gVd22\n"
<< "   32 " << gVu22() << " # gVu22\n"
<< "   33 " << gVd33() << " # gVd33\n"
<< "   34 " << gVu33() << " # gVu33\n"
<< "   35 " << gAd11() << " # gAd11\n"
<< "   36 " << gAu11() << " # gAu11\n"
<< "   37 " << gAd22() << " # gAd22\n"
<< "   38 " << gAu22() << " # gAu22\n"
<< "   39 " << gAd33() << " # gAd33\n"
<< "   40 " << gAu33() << " # gAu33\n"
<< "   41 " << gVe() << " # gVe\n"
<< "   42 " << gAe() << " # gAe\n"
<< "   43 " << gVmm() << " # gVmm\n"
<< "   44 " << gAmm() << " # gAmm\n"
<< "   45 " << gVta() << " # gVta\n"
<< "   46 " << gAta() << " # gAta\n"
<< "   47 " << gSXr() << " # gSXr\n"
<< "   48 " << gSXc() << " # gSXc\n"
<< "   49 " << gSXd() << " # gSXd\n"
<< "   50 " << gPXd() << " # gPXd\n"
<< "   51 " << gVXd() << " # gVXd\n"
<< "   52 " << gAXd() << " # gAXd\n"
<< "   53 " << Lambda() << " # Lambda\n"
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
static Parameter<FRModel, double> interfacegSh1
  ("gSh1",
   "The interface for parameter gSh1",
   &FRModel::gSh1_, 1.0, 0, 0,
   false, false, Interface::nolimits);
static Parameter<FRModel, double> interfacegSh2
  ("gSh2",
   "The interface for parameter gSh2",
   &FRModel::gSh2_, 1.0, 0, 0,
   false, false, Interface::nolimits);
static Parameter<FRModel, double> interfacegSWT
  ("gSWT",
   "The interface for parameter gSWT",
   &FRModel::gSWT_, 1.0, 0, 0,
   false, false, Interface::nolimits);
static Parameter<FRModel, double> interfacegPWT
  ("gPWT",
   "The interface for parameter gPWT",
   &FRModel::gPWT_, 1.0, 0, 0,
   false, false, Interface::nolimits);
static Parameter<FRModel, double> interfacegPBT
  ("gPBT",
   "The interface for parameter gPBT",
   &FRModel::gPBT_, 1.0, 0, 0,
   false, false, Interface::nolimits);
static Parameter<FRModel, double> interfacegSBT
  ("gSBT",
   "The interface for parameter gSBT",
   &FRModel::gSBT_, 1.0, 0, 0,
   false, false, Interface::nolimits);
static Parameter<FRModel, double> interfacegSWL
  ("gSWL",
   "The interface for parameter gSWL",
   &FRModel::gSWL_, 1.0, 0, 0,
   false, false, Interface::nolimits);
static Parameter<FRModel, double> interfacegSBL
  ("gSBL",
   "The interface for parameter gSBL",
   &FRModel::gSBL_, 1.0, 0, 0,
   false, false, Interface::nolimits);
static Parameter<FRModel, double> interfacegSg
  ("gSg",
   "The interface for parameter gSg",
   &FRModel::gSg_, 1.0, 0, 0,
   false, false, Interface::nolimits);
static Parameter<FRModel, double> interfacegPg
  ("gPg",
   "The interface for parameter gPg",
   &FRModel::gPg_, 1.0, 0, 0,
   false, false, Interface::nolimits);
static Parameter<FRModel, double> interfacegSd11
  ("gSd11",
   "The interface for parameter gSd11",
   &FRModel::gSd11_, 1.0, 0, 0,
   false, false, Interface::nolimits);
static Parameter<FRModel, double> interfacegSu11
  ("gSu11",
   "The interface for parameter gSu11",
   &FRModel::gSu11_, 1.0, 0, 0,
   false, false, Interface::nolimits);
static Parameter<FRModel, double> interfacegSd22
  ("gSd22",
   "The interface for parameter gSd22",
   &FRModel::gSd22_, 1.0, 0, 0,
   false, false, Interface::nolimits);
static Parameter<FRModel, double> interfacegSu22
  ("gSu22",
   "The interface for parameter gSu22",
   &FRModel::gSu22_, 1.0, 0, 0,
   false, false, Interface::nolimits);
static Parameter<FRModel, double> interfacegSd33
  ("gSd33",
   "The interface for parameter gSd33",
   &FRModel::gSd33_, 1.0, 0, 0,
   false, false, Interface::nolimits);
static Parameter<FRModel, double> interfacegSu33
  ("gSu33",
   "The interface for parameter gSu33",
   &FRModel::gSu33_, 1.0, 0, 0,
   false, false, Interface::nolimits);
static Parameter<FRModel, double> interfacegPd11
  ("gPd11",
   "The interface for parameter gPd11",
   &FRModel::gPd11_, 1.0, 0, 0,
   false, false, Interface::nolimits);
static Parameter<FRModel, double> interfacegPu11
  ("gPu11",
   "The interface for parameter gPu11",
   &FRModel::gPu11_, 1.0, 0, 0,
   false, false, Interface::nolimits);
static Parameter<FRModel, double> interfacegPd22
  ("gPd22",
   "The interface for parameter gPd22",
   &FRModel::gPd22_, 1.0, 0, 0,
   false, false, Interface::nolimits);
static Parameter<FRModel, double> interfacegPu22
  ("gPu22",
   "The interface for parameter gPu22",
   &FRModel::gPu22_, 1.0, 0, 0,
   false, false, Interface::nolimits);
static Parameter<FRModel, double> interfacegPd33
  ("gPd33",
   "The interface for parameter gPd33",
   &FRModel::gPd33_, 1.0, 0, 0,
   false, false, Interface::nolimits);
static Parameter<FRModel, double> interfacegPu33
  ("gPu33",
   "The interface for parameter gPu33",
   &FRModel::gPu33_, 1.0, 0, 0,
   false, false, Interface::nolimits);
static Parameter<FRModel, double> interfacegSe
  ("gSe",
   "The interface for parameter gSe",
   &FRModel::gSe_, 1.0, 0, 0,
   false, false, Interface::nolimits);
static Parameter<FRModel, double> interfacegPe
  ("gPe",
   "The interface for parameter gPe",
   &FRModel::gPe_, 1.0, 0, 0,
   false, false, Interface::nolimits);
static Parameter<FRModel, double> interfacegSmm
  ("gSmm",
   "The interface for parameter gSmm",
   &FRModel::gSmm_, 1.0, 0, 0,
   false, false, Interface::nolimits);
static Parameter<FRModel, double> interfacegPmm
  ("gPmm",
   "The interface for parameter gPmm",
   &FRModel::gPmm_, 1.0, 0, 0,
   false, false, Interface::nolimits);
static Parameter<FRModel, double> interfacegSta
  ("gSta",
   "The interface for parameter gSta",
   &FRModel::gSta_, 1.0, 0, 0,
   false, false, Interface::nolimits);
static Parameter<FRModel, double> interfacegPta
  ("gPta",
   "The interface for parameter gPta",
   &FRModel::gPta_, 1.0, 0, 0,
   false, false, Interface::nolimits);
static Parameter<FRModel, double> interfacegVd11
  ("gVd11",
   "The interface for parameter gVd11",
   &FRModel::gVd11_, 1.0, 0, 0,
   false, false, Interface::nolimits);
static Parameter<FRModel, double> interfacegVu11
  ("gVu11",
   "The interface for parameter gVu11",
   &FRModel::gVu11_, 1.0, 0, 0,
   false, false, Interface::nolimits);
static Parameter<FRModel, double> interfacegVd22
  ("gVd22",
   "The interface for parameter gVd22",
   &FRModel::gVd22_, 1.0, 0, 0,
   false, false, Interface::nolimits);
static Parameter<FRModel, double> interfacegVu22
  ("gVu22",
   "The interface for parameter gVu22",
   &FRModel::gVu22_, 1.0, 0, 0,
   false, false, Interface::nolimits);
static Parameter<FRModel, double> interfacegVd33
  ("gVd33",
   "The interface for parameter gVd33",
   &FRModel::gVd33_, 1.0, 0, 0,
   false, false, Interface::nolimits);
static Parameter<FRModel, double> interfacegVu33
  ("gVu33",
   "The interface for parameter gVu33",
   &FRModel::gVu33_, 1.0, 0, 0,
   false, false, Interface::nolimits);
static Parameter<FRModel, double> interfacegAd11
  ("gAd11",
   "The interface for parameter gAd11",
   &FRModel::gAd11_, 1.0, 0, 0,
   false, false, Interface::nolimits);
static Parameter<FRModel, double> interfacegAu11
  ("gAu11",
   "The interface for parameter gAu11",
   &FRModel::gAu11_, 1.0, 0, 0,
   false, false, Interface::nolimits);
static Parameter<FRModel, double> interfacegAd22
  ("gAd22",
   "The interface for parameter gAd22",
   &FRModel::gAd22_, 1.0, 0, 0,
   false, false, Interface::nolimits);
static Parameter<FRModel, double> interfacegAu22
  ("gAu22",
   "The interface for parameter gAu22",
   &FRModel::gAu22_, 1.0, 0, 0,
   false, false, Interface::nolimits);
static Parameter<FRModel, double> interfacegAd33
  ("gAd33",
   "The interface for parameter gAd33",
   &FRModel::gAd33_, 1.0, 0, 0,
   false, false, Interface::nolimits);
static Parameter<FRModel, double> interfacegAu33
  ("gAu33",
   "The interface for parameter gAu33",
   &FRModel::gAu33_, 1.0, 0, 0,
   false, false, Interface::nolimits);
static Parameter<FRModel, double> interfacegVe
  ("gVe",
   "The interface for parameter gVe",
   &FRModel::gVe_, 1.0, 0, 0,
   false, false, Interface::nolimits);
static Parameter<FRModel, double> interfacegAe
  ("gAe",
   "The interface for parameter gAe",
   &FRModel::gAe_, 1.0, 0, 0,
   false, false, Interface::nolimits);
static Parameter<FRModel, double> interfacegVmm
  ("gVmm",
   "The interface for parameter gVmm",
   &FRModel::gVmm_, 1.0, 0, 0,
   false, false, Interface::nolimits);
static Parameter<FRModel, double> interfacegAmm
  ("gAmm",
   "The interface for parameter gAmm",
   &FRModel::gAmm_, 1.0, 0, 0,
   false, false, Interface::nolimits);
static Parameter<FRModel, double> interfacegVta
  ("gVta",
   "The interface for parameter gVta",
   &FRModel::gVta_, 1.0, 0, 0,
   false, false, Interface::nolimits);
static Parameter<FRModel, double> interfacegAta
  ("gAta",
   "The interface for parameter gAta",
   &FRModel::gAta_, 1.0, 0, 0,
   false, false, Interface::nolimits);
static Parameter<FRModel, double> interfacegSXr
  ("gSXr",
   "The interface for parameter gSXr",
   &FRModel::gSXr_, 1.0, 0, 0,
   false, false, Interface::nolimits);
static Parameter<FRModel, double> interfacegSXc
  ("gSXc",
   "The interface for parameter gSXc",
   &FRModel::gSXc_, 1.0, 0, 0,
   false, false, Interface::nolimits);
static Parameter<FRModel, double> interfacegSXd
  ("gSXd",
   "The interface for parameter gSXd",
   &FRModel::gSXd_, 1.0, 0, 0,
   false, false, Interface::nolimits);
static Parameter<FRModel, double> interfacegPXd
  ("gPXd",
   "The interface for parameter gPXd",
   &FRModel::gPXd_, 1.0, 0, 0,
   false, false, Interface::nolimits);
static Parameter<FRModel, double> interfacegVXd
  ("gVXd",
   "The interface for parameter gVXd",
   &FRModel::gVXd_, 1.0, 0, 0,
   false, false, Interface::nolimits);
static Parameter<FRModel, double> interfacegAXd
  ("gAXd",
   "The interface for parameter gAXd",
   &FRModel::gAXd_, 1.0, 0, 0,
   false, false, Interface::nolimits);
static Parameter<FRModel, double> interfaceLambda
  ("Lambda",
   "The interface for parameter Lambda",
   &FRModel::Lambda_, 1.0, 0, 0,
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
   &FRModel::aS_, 0.1181, 0, 0,
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
   &FRModel::yms_, 0.095, 0, 0,
   false, false, Interface::nolimits);
static Parameter<FRModel, double> interfaceymc
  ("ymc",
   "The interface for parameter ymc",
   &FRModel::ymc_, 1.27, 0, 0,
   false, false, Interface::nolimits);
static Parameter<FRModel, double> interfaceymb
  ("ymb",
   "The interface for parameter ymb",
   &FRModel::ymb_, 4.78, 0, 0,
   false, false, Interface::nolimits);
static Parameter<FRModel, double> interfaceymt
  ("ymt",
   "The interface for parameter ymt",
   &FRModel::ymt_, 173, 0, 0,
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
   &FRModel::MT_, 173, 0, 0,
   false, false, Interface::nolimits);
static Parameter<FRModel, double> interfaceMD
  ("MD",
   "The interface for parameter MD",
   &FRModel::MD_, 0.00504, 0, 0,
   false, false, Interface::nolimits);
static Parameter<FRModel, double> interfaceMS
  ("MS",
   "The interface for parameter MS",
   &FRModel::MS_, 0.095, 0, 0,
   false, false, Interface::nolimits);
static Parameter<FRModel, double> interfaceMB
  ("MB",
   "The interface for parameter MB",
   &FRModel::MB_, 4.78, 0, 0,
   false, false, Interface::nolimits);
static Parameter<FRModel, double> interfaceMH
  ("MH",
   "The interface for parameter MH",
   &FRModel::MH_, 125.18, 0, 0,
   false, false, Interface::nolimits);
static Parameter<FRModel, double> interfaceMD0
  ("MD0",
   "The interface for parameter MD0",
   &FRModel::MD0_, 1000.0, 0, 0,
   false, false, Interface::nolimits);
static Parameter<FRModel, double> interfaceMD1
  ("MD1",
   "The interface for parameter MD1",
   &FRModel::MD1_, 1000.0, 0, 0,
   false, false, Interface::nolimits);
static Parameter<FRModel, double> interfaceMXr
  ("MXr",
   "The interface for parameter MXr",
   &FRModel::MXr_, 1.0, 0, 0,
   false, false, Interface::nolimits);
static Parameter<FRModel, double> interfaceMXc
  ("MXc",
   "The interface for parameter MXc",
   &FRModel::MXc_, 499.0, 0, 0,
   false, false, Interface::nolimits);
static Parameter<FRModel, double> interfaceMXd
  ("MXd",
   "The interface for parameter MXd",
   &FRModel::MXd_, 499.0, 0, 0,
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
static Parameter<FRModel, double> interfaceWE
  ("WE",
   "The interface for parameter WE",
   &FRModel::WE_, 0.0, 0, 0,
   false, false, Interface::nolimits);
static Parameter<FRModel, double> interfaceWMU
  ("WMU",
   "The interface for parameter WMU",
   &FRModel::WMU_, 3e-19, 0, 0,
   false, false, Interface::nolimits);
static Parameter<FRModel, double> interfaceWTA
  ("WTA",
   "The interface for parameter WTA",
   &FRModel::WTA_, 2.27e-12, 0, 0,
   false, false, Interface::nolimits);
static Parameter<FRModel, double> interfaceWT
  ("WT",
   "The interface for parameter WT",
   &FRModel::WT_, 1.41, 0, 0,
   false, false, Interface::nolimits);
static Parameter<FRModel, double> interfaceWH
  ("WH",
   "The interface for parameter WH",
   &FRModel::WH_, 0.00407, 0, 0,
   false, false, Interface::nolimits);
static Parameter<FRModel, double> interfaceWD0
  ("WD0",
   "The interface for parameter WD0",
   &FRModel::WD0_, 10.0, 0, 0,
   false, false, Interface::nolimits);
static Parameter<FRModel, double> interfaceWD1
  ("WD1",
   "The interface for parameter WD1",
   &FRModel::WD1_, 10.0, 0, 0,
   false, false, Interface::nolimits);


}



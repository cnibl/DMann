# This file was automatically created by FeynRules 2.3.31
# Mathematica version: 11.0.0 for Mac OS X x86 (64-bit) (July 28, 2016)
# Date: Tue 19 Feb 2019 18:58:33



from object_library import all_parameters, Parameter


from function_library import complexconjugate, re, im, csc, sec, acsc, asec, cot

# This is a default parameter object representing 0.
ZERO = Parameter(name = 'ZERO',
                 nature = 'internal',
                 type = 'real',
                 value = '0.0',
                 texname = '0')

# User-defined parameters.
cabi = Parameter(name = 'cabi',
                 nature = 'external',
                 type = 'real',
                 value = 0.227736,
                 texname = '\\theta _c',
                 lhablock = 'CKMBLOCK',
                 lhacode = [ 1 ])

gSh1 = Parameter(name = 'gSh1',
                 nature = 'external',
                 type = 'real',
                 value = 1.,
                 texname = 'g_{\\text{Sh1}}',
                 lhablock = 'DMINPUTS',
                 lhacode = [ 1 ])

gSh2 = Parameter(name = 'gSh2',
                 nature = 'external',
                 type = 'real',
                 value = 1.,
                 texname = 'g_{\\text{Sh2}}',
                 lhablock = 'DMINPUTS',
                 lhacode = [ 2 ])

gSWT = Parameter(name = 'gSWT',
                 nature = 'external',
                 type = 'real',
                 value = 1.,
                 texname = 'g_{\\text{SWT}}',
                 lhablock = 'DMINPUTS',
                 lhacode = [ 3 ])

gPWT = Parameter(name = 'gPWT',
                 nature = 'external',
                 type = 'real',
                 value = 1.,
                 texname = 'g_{\\text{PWT}}',
                 lhablock = 'DMINPUTS',
                 lhacode = [ 4 ])

gPBT = Parameter(name = 'gPBT',
                 nature = 'external',
                 type = 'real',
                 value = 1.,
                 texname = 'g_{\\text{PBT}}',
                 lhablock = 'DMINPUTS',
                 lhacode = [ 5 ])

gSBT = Parameter(name = 'gSBT',
                 nature = 'external',
                 type = 'real',
                 value = 1.,
                 texname = 'g_{\\text{SBT}}',
                 lhablock = 'DMINPUTS',
                 lhacode = [ 6 ])

gSWL = Parameter(name = 'gSWL',
                 nature = 'external',
                 type = 'real',
                 value = 1.,
                 texname = 'g_{\\text{SWL}}',
                 lhablock = 'DMINPUTS',
                 lhacode = [ 7 ])

gSBL = Parameter(name = 'gSBL',
                 nature = 'external',
                 type = 'real',
                 value = 1.,
                 texname = 'g_{\\text{SBL}}',
                 lhablock = 'DMINPUTS',
                 lhacode = [ 8 ])

gSg = Parameter(name = 'gSg',
                nature = 'external',
                type = 'real',
                value = 1.,
                texname = 'g_{\\text{Sg}}',
                lhablock = 'DMINPUTS',
                lhacode = [ 9 ])

gPg = Parameter(name = 'gPg',
                nature = 'external',
                type = 'real',
                value = 1.,
                texname = 'g_{\\text{Pg}}',
                lhablock = 'DMINPUTS',
                lhacode = [ 10 ])

gSd11 = Parameter(name = 'gSd11',
                  nature = 'external',
                  type = 'real',
                  value = 1.,
                  texname = 'g_{\\text{Sd11}}',
                  lhablock = 'DMINPUTS',
                  lhacode = [ 11 ])

gSu11 = Parameter(name = 'gSu11',
                  nature = 'external',
                  type = 'real',
                  value = 1.,
                  texname = 'g_{\\text{Su11}}',
                  lhablock = 'DMINPUTS',
                  lhacode = [ 12 ])

gSd22 = Parameter(name = 'gSd22',
                  nature = 'external',
                  type = 'real',
                  value = 1.,
                  texname = 'g_{\\text{Sd22}}',
                  lhablock = 'DMINPUTS',
                  lhacode = [ 13 ])

gSu22 = Parameter(name = 'gSu22',
                  nature = 'external',
                  type = 'real',
                  value = 1.,
                  texname = 'g_{\\text{Su22}}',
                  lhablock = 'DMINPUTS',
                  lhacode = [ 14 ])

gSd33 = Parameter(name = 'gSd33',
                  nature = 'external',
                  type = 'real',
                  value = 1.,
                  texname = 'g_{\\text{Sd33}}',
                  lhablock = 'DMINPUTS',
                  lhacode = [ 15 ])

gSu33 = Parameter(name = 'gSu33',
                  nature = 'external',
                  type = 'real',
                  value = 1.,
                  texname = 'g_{\\text{Su33}}',
                  lhablock = 'DMINPUTS',
                  lhacode = [ 16 ])

gPd11 = Parameter(name = 'gPd11',
                  nature = 'external',
                  type = 'real',
                  value = 1.,
                  texname = 'g_{\\text{Pd11}}',
                  lhablock = 'DMINPUTS',
                  lhacode = [ 17 ])

gPu11 = Parameter(name = 'gPu11',
                  nature = 'external',
                  type = 'real',
                  value = 1.,
                  texname = 'g_{\\text{Pu11}}',
                  lhablock = 'DMINPUTS',
                  lhacode = [ 18 ])

gPd22 = Parameter(name = 'gPd22',
                  nature = 'external',
                  type = 'real',
                  value = 1.,
                  texname = 'g_{\\text{Pd22}}',
                  lhablock = 'DMINPUTS',
                  lhacode = [ 19 ])

gPu22 = Parameter(name = 'gPu22',
                  nature = 'external',
                  type = 'real',
                  value = 1.,
                  texname = 'g_{\\text{Pu22}}',
                  lhablock = 'DMINPUTS',
                  lhacode = [ 20 ])

gPd33 = Parameter(name = 'gPd33',
                  nature = 'external',
                  type = 'real',
                  value = 1.,
                  texname = 'g_{\\text{Pd33}}',
                  lhablock = 'DMINPUTS',
                  lhacode = [ 21 ])

gPu33 = Parameter(name = 'gPu33',
                  nature = 'external',
                  type = 'real',
                  value = 1.,
                  texname = 'g_{\\text{Pu33}}',
                  lhablock = 'DMINPUTS',
                  lhacode = [ 22 ])

gSe = Parameter(name = 'gSe',
                nature = 'external',
                type = 'real',
                value = 1.,
                texname = 'g_{\\text{Pu33}}',
                lhablock = 'DMINPUTS',
                lhacode = [ 23 ])

gPe = Parameter(name = 'gPe',
                nature = 'external',
                type = 'real',
                value = 1.,
                texname = 'g_{\\text{Pu33}}',
                lhablock = 'DMINPUTS',
                lhacode = [ 24 ])

gSmm = Parameter(name = 'gSmm',
                 nature = 'external',
                 type = 'real',
                 value = 1.,
                 texname = 'g_{\\text{Pu33}}',
                 lhablock = 'DMINPUTS',
                 lhacode = [ 25 ])

gPmm = Parameter(name = 'gPmm',
                 nature = 'external',
                 type = 'real',
                 value = 1.,
                 texname = 'g_{\\text{Pu33}}',
                 lhablock = 'DMINPUTS',
                 lhacode = [ 26 ])

gSta = Parameter(name = 'gSta',
                 nature = 'external',
                 type = 'real',
                 value = 1.,
                 texname = 'g_{\\text{Pu33}}',
                 lhablock = 'DMINPUTS',
                 lhacode = [ 27 ])

gPta = Parameter(name = 'gPta',
                 nature = 'external',
                 type = 'real',
                 value = 1.,
                 texname = 'g_{\\text{Pu33}}',
                 lhablock = 'DMINPUTS',
                 lhacode = [ 28 ])

gVd11 = Parameter(name = 'gVd11',
                  nature = 'external',
                  type = 'real',
                  value = 1.,
                  texname = 'g_{\\text{Sd11}}',
                  lhablock = 'DMINPUTS',
                  lhacode = [ 29 ])

gVu11 = Parameter(name = 'gVu11',
                  nature = 'external',
                  type = 'real',
                  value = 1.,
                  texname = 'g_{\\text{Su11}}',
                  lhablock = 'DMINPUTS',
                  lhacode = [ 30 ])

gVd22 = Parameter(name = 'gVd22',
                  nature = 'external',
                  type = 'real',
                  value = 1.,
                  texname = 'g_{\\text{Sd22}}',
                  lhablock = 'DMINPUTS',
                  lhacode = [ 31 ])

gVu22 = Parameter(name = 'gVu22',
                  nature = 'external',
                  type = 'real',
                  value = 1.,
                  texname = 'g_{\\text{Su22}}',
                  lhablock = 'DMINPUTS',
                  lhacode = [ 32 ])

gVd33 = Parameter(name = 'gVd33',
                  nature = 'external',
                  type = 'real',
                  value = 1.,
                  texname = 'g_{\\text{Sd33}}',
                  lhablock = 'DMINPUTS',
                  lhacode = [ 33 ])

gVu33 = Parameter(name = 'gVu33',
                  nature = 'external',
                  type = 'real',
                  value = 1.,
                  texname = 'g_{\\text{Su33}}',
                  lhablock = 'DMINPUTS',
                  lhacode = [ 34 ])

gAd11 = Parameter(name = 'gAd11',
                  nature = 'external',
                  type = 'real',
                  value = 1.,
                  texname = 'g_{\\text{Pd11}}',
                  lhablock = 'DMINPUTS',
                  lhacode = [ 35 ])

gAu11 = Parameter(name = 'gAu11',
                  nature = 'external',
                  type = 'real',
                  value = 1.,
                  texname = 'g_{\\text{Pu11}}',
                  lhablock = 'DMINPUTS',
                  lhacode = [ 36 ])

gAd22 = Parameter(name = 'gAd22',
                  nature = 'external',
                  type = 'real',
                  value = 1.,
                  texname = 'g_{\\text{Pd22}}',
                  lhablock = 'DMINPUTS',
                  lhacode = [ 37 ])

gAu22 = Parameter(name = 'gAu22',
                  nature = 'external',
                  type = 'real',
                  value = 1.,
                  texname = 'g_{\\text{Pu22}}',
                  lhablock = 'DMINPUTS',
                  lhacode = [ 38 ])

gAd33 = Parameter(name = 'gAd33',
                  nature = 'external',
                  type = 'real',
                  value = 1.,
                  texname = 'g_{\\text{Pd33}}',
                  lhablock = 'DMINPUTS',
                  lhacode = [ 39 ])

gAu33 = Parameter(name = 'gAu33',
                  nature = 'external',
                  type = 'real',
                  value = 1.,
                  texname = 'g_{\\text{Pu33}}',
                  lhablock = 'DMINPUTS',
                  lhacode = [ 40 ])

gVe = Parameter(name = 'gVe',
                nature = 'external',
                type = 'real',
                value = 1.,
                texname = 'g_{\\text{Pu33}}',
                lhablock = 'DMINPUTS',
                lhacode = [ 41 ])

gAe = Parameter(name = 'gAe',
                nature = 'external',
                type = 'real',
                value = 1.,
                texname = 'g_{\\text{Pu33}}',
                lhablock = 'DMINPUTS',
                lhacode = [ 42 ])

gVmm = Parameter(name = 'gVmm',
                 nature = 'external',
                 type = 'real',
                 value = 1.,
                 texname = 'g_{\\text{Pu33}}',
                 lhablock = 'DMINPUTS',
                 lhacode = [ 43 ])

gAmm = Parameter(name = 'gAmm',
                 nature = 'external',
                 type = 'real',
                 value = 1.,
                 texname = 'g_{\\text{Pu33}}',
                 lhablock = 'DMINPUTS',
                 lhacode = [ 44 ])

gVta = Parameter(name = 'gVta',
                 nature = 'external',
                 type = 'real',
                 value = 1.,
                 texname = 'g_{\\text{Pu33}}',
                 lhablock = 'DMINPUTS',
                 lhacode = [ 45 ])

gAta = Parameter(name = 'gAta',
                 nature = 'external',
                 type = 'real',
                 value = 1.,
                 texname = 'g_{\\text{Pu33}}',
                 lhablock = 'DMINPUTS',
                 lhacode = [ 46 ])

gSXr = Parameter(name = 'gSXr',
                 nature = 'external',
                 type = 'real',
                 value = 1.,
                 texname = 'g_{\\text{SX}_r}',
                 lhablock = 'DMINPUTS',
                 lhacode = [ 47 ])

gSXc = Parameter(name = 'gSXc',
                 nature = 'external',
                 type = 'real',
                 value = 1.,
                 texname = 'g_{\\text{SX}_c}',
                 lhablock = 'DMINPUTS',
                 lhacode = [ 48 ])

gSXd = Parameter(name = 'gSXd',
                 nature = 'external',
                 type = 'real',
                 value = 1.,
                 texname = 'g_{\\text{SX}_d}',
                 lhablock = 'DMINPUTS',
                 lhacode = [ 49 ])

gPXd = Parameter(name = 'gPXd',
                 nature = 'external',
                 type = 'real',
                 value = 1.,
                 texname = 'g_{\\text{PX}_d}',
                 lhablock = 'DMINPUTS',
                 lhacode = [ 50 ])

gVXd = Parameter(name = 'gVXd',
                 nature = 'external',
                 type = 'real',
                 value = 1.,
                 texname = 'g_{\\text{VX}_d}',
                 lhablock = 'DMINPUTS',
                 lhacode = [ 51 ])

gAXd = Parameter(name = 'gAXd',
                 nature = 'external',
                 type = 'real',
                 value = 1.,
                 texname = 'g_{\\text{AX}_d}',
                 lhablock = 'DMINPUTS',
                 lhacode = [ 52 ])

Lambda = Parameter(name = 'Lambda',
                   nature = 'external',
                   type = 'real',
                   value = 1.,
                   texname = '\\Lambda',
                   lhablock = 'DMINPUTS',
                   lhacode = [ 53 ])

aEWM1 = Parameter(name = 'aEWM1',
                  nature = 'external',
                  type = 'real',
                  value = 127.9,
                  texname = '\\text{aEWM1}',
                  lhablock = 'SMINPUTS',
                  lhacode = [ 1 ])

Gf = Parameter(name = 'Gf',
               nature = 'external',
               type = 'real',
               value = 0.0000116637,
               texname = 'G_f',
               lhablock = 'SMINPUTS',
               lhacode = [ 2 ])

aS = Parameter(name = 'aS',
               nature = 'external',
               type = 'real',
               value = 0.1181,
               texname = '\\alpha _s',
               lhablock = 'SMINPUTS',
               lhacode = [ 3 ])

ymdo = Parameter(name = 'ymdo',
                 nature = 'external',
                 type = 'real',
                 value = 0.00504,
                 texname = '\\text{ymdo}',
                 lhablock = 'YUKAWA',
                 lhacode = [ 1 ])

ymup = Parameter(name = 'ymup',
                 nature = 'external',
                 type = 'real',
                 value = 0.00255,
                 texname = '\\text{ymup}',
                 lhablock = 'YUKAWA',
                 lhacode = [ 2 ])

yms = Parameter(name = 'yms',
                nature = 'external',
                type = 'real',
                value = 0.095,
                texname = '\\text{yms}',
                lhablock = 'YUKAWA',
                lhacode = [ 3 ])

ymc = Parameter(name = 'ymc',
                nature = 'external',
                type = 'real',
                value = 1.27,
                texname = '\\text{ymc}',
                lhablock = 'YUKAWA',
                lhacode = [ 4 ])

ymb = Parameter(name = 'ymb',
                nature = 'external',
                type = 'real',
                value = 4.78,
                texname = '\\text{ymb}',
                lhablock = 'YUKAWA',
                lhacode = [ 5 ])

ymt = Parameter(name = 'ymt',
                nature = 'external',
                type = 'real',
                value = 173,
                texname = '\\text{ymt}',
                lhablock = 'YUKAWA',
                lhacode = [ 6 ])

yme = Parameter(name = 'yme',
                nature = 'external',
                type = 'real',
                value = 0.000511,
                texname = '\\text{yme}',
                lhablock = 'YUKAWA',
                lhacode = [ 11 ])

ymm = Parameter(name = 'ymm',
                nature = 'external',
                type = 'real',
                value = 0.10566,
                texname = '\\text{ymm}',
                lhablock = 'YUKAWA',
                lhacode = [ 13 ])

ymtau = Parameter(name = 'ymtau',
                  nature = 'external',
                  type = 'real',
                  value = 1.777,
                  texname = '\\text{ymtau}',
                  lhablock = 'YUKAWA',
                  lhacode = [ 15 ])

MZ = Parameter(name = 'MZ',
               nature = 'external',
               type = 'real',
               value = 91.1876,
               texname = '\\text{MZ}',
               lhablock = 'MASS',
               lhacode = [ 23 ])

Me = Parameter(name = 'Me',
               nature = 'external',
               type = 'real',
               value = 0.000511,
               texname = '\\text{Me}',
               lhablock = 'MASS',
               lhacode = [ 11 ])

MMU = Parameter(name = 'MMU',
                nature = 'external',
                type = 'real',
                value = 0.10566,
                texname = '\\text{MMU}',
                lhablock = 'MASS',
                lhacode = [ 13 ])

MTA = Parameter(name = 'MTA',
                nature = 'external',
                type = 'real',
                value = 1.777,
                texname = '\\text{MTA}',
                lhablock = 'MASS',
                lhacode = [ 15 ])

MU = Parameter(name = 'MU',
               nature = 'external',
               type = 'real',
               value = 0.00255,
               texname = 'M',
               lhablock = 'MASS',
               lhacode = [ 2 ])

MC = Parameter(name = 'MC',
               nature = 'external',
               type = 'real',
               value = 1.27,
               texname = '\\text{MC}',
               lhablock = 'MASS',
               lhacode = [ 4 ])

MT = Parameter(name = 'MT',
               nature = 'external',
               type = 'real',
               value = 173,
               texname = '\\text{MT}',
               lhablock = 'MASS',
               lhacode = [ 6 ])

MD = Parameter(name = 'MD',
               nature = 'external',
               type = 'real',
               value = 0.00504,
               texname = '\\text{MD}',
               lhablock = 'MASS',
               lhacode = [ 1 ])

MS = Parameter(name = 'MS',
               nature = 'external',
               type = 'real',
               value = 0.095,
               texname = '\\text{MS}',
               lhablock = 'MASS',
               lhacode = [ 3 ])

MB = Parameter(name = 'MB',
               nature = 'external',
               type = 'real',
               value = 4.78,
               texname = '\\text{MB}',
               lhablock = 'MASS',
               lhacode = [ 5 ])

MH = Parameter(name = 'MH',
               nature = 'external',
               type = 'real',
               value = 125.18,
               texname = '\\text{MH}',
               lhablock = 'MASS',
               lhacode = [ 25 ])

MD0 = Parameter(name = 'MD0',
                nature = 'external',
                type = 'real',
                value = 1000.,
                texname = '\\text{MD0}',
                lhablock = 'MASS',
                lhacode = [ 9000006 ])

MD1 = Parameter(name = 'MD1',
                nature = 'external',
                type = 'real',
                value = 1000.,
                texname = '\\text{MD1}',
                lhablock = 'MASS',
                lhacode = [ 9000007 ])

MXr = Parameter(name = 'MXr',
                nature = 'external',
                type = 'real',
                value = 1.,
                texname = '\\text{MXr}',
                lhablock = 'MASS',
                lhacode = [ 9000008 ])

MXc = Parameter(name = 'MXc',
                nature = 'external',
                type = 'real',
                value = 499.,
                texname = '\\text{MXc}',
                lhablock = 'MASS',
                lhacode = [ 9000009 ])

MXd = Parameter(name = 'MXd',
                nature = 'external',
                type = 'real',
                value = 499.,
                texname = '\\text{MXd}',
                lhablock = 'MASS',
                lhacode = [ 9000010 ])

WZ = Parameter(name = 'WZ',
               nature = 'external',
               type = 'real',
               value = 2.4952,
               texname = '\\text{WZ}',
               lhablock = 'DECAY',
               lhacode = [ 23 ])

WW = Parameter(name = 'WW',
               nature = 'external',
               type = 'real',
               value = 2.085,
               texname = '\\text{WW}',
               lhablock = 'DECAY',
               lhacode = [ 24 ])

WE = Parameter(name = 'WE',
               nature = 'external',
               type = 'real',
               value = 0.,
               texname = '\\text{WE}',
               lhablock = 'DECAY',
               lhacode = [ 11 ])

WMU = Parameter(name = 'WMU',
                nature = 'external',
                type = 'real',
                value = 3.e-19,
                texname = '\\text{WMU}',
                lhablock = 'DECAY',
                lhacode = [ 13 ])

WTA = Parameter(name = 'WTA',
                nature = 'external',
                type = 'real',
                value = 2.27e-12,
                texname = '\\text{WTA}',
                lhablock = 'DECAY',
                lhacode = [ 15 ])

WT = Parameter(name = 'WT',
               nature = 'external',
               type = 'real',
               value = 1.41,
               texname = '\\text{WT}',
               lhablock = 'DECAY',
               lhacode = [ 6 ])

WH = Parameter(name = 'WH',
               nature = 'external',
               type = 'real',
               value = 0.00407,
               texname = '\\text{WH}',
               lhablock = 'DECAY',
               lhacode = [ 25 ])

WD0 = Parameter(name = 'WD0',
                nature = 'external',
                type = 'real',
                value = 10.,
                texname = '\\text{WD0}',
                lhablock = 'DECAY',
                lhacode = [ 9000006 ])

WD1 = Parameter(name = 'WD1',
                nature = 'external',
                type = 'real',
                value = 10.,
                texname = '\\text{WD1}',
                lhablock = 'DECAY',
                lhacode = [ 9000007 ])

aEW = Parameter(name = 'aEW',
                nature = 'internal',
                type = 'real',
                value = '1/aEWM1',
                texname = '\\alpha _{\\text{EW}}')

G = Parameter(name = 'G',
              nature = 'internal',
              type = 'real',
              value = '2*cmath.sqrt(aS)*cmath.sqrt(cmath.pi)',
              texname = 'G')

CKM1x1 = Parameter(name = 'CKM1x1',
                   nature = 'internal',
                   type = 'complex',
                   value = 'cmath.cos(cabi)',
                   texname = '\\text{CKM1x1}')

CKM1x2 = Parameter(name = 'CKM1x2',
                   nature = 'internal',
                   type = 'complex',
                   value = 'cmath.sin(cabi)',
                   texname = '\\text{CKM1x2}')

CKM1x3 = Parameter(name = 'CKM1x3',
                   nature = 'internal',
                   type = 'complex',
                   value = '0',
                   texname = '\\text{CKM1x3}')

CKM2x1 = Parameter(name = 'CKM2x1',
                   nature = 'internal',
                   type = 'complex',
                   value = '-cmath.sin(cabi)',
                   texname = '\\text{CKM2x1}')

CKM2x2 = Parameter(name = 'CKM2x2',
                   nature = 'internal',
                   type = 'complex',
                   value = 'cmath.cos(cabi)',
                   texname = '\\text{CKM2x2}')

CKM2x3 = Parameter(name = 'CKM2x3',
                   nature = 'internal',
                   type = 'complex',
                   value = '0',
                   texname = '\\text{CKM2x3}')

CKM3x1 = Parameter(name = 'CKM3x1',
                   nature = 'internal',
                   type = 'complex',
                   value = '0',
                   texname = '\\text{CKM3x1}')

CKM3x2 = Parameter(name = 'CKM3x2',
                   nature = 'internal',
                   type = 'complex',
                   value = '0',
                   texname = '\\text{CKM3x2}')

CKM3x3 = Parameter(name = 'CKM3x3',
                   nature = 'internal',
                   type = 'complex',
                   value = '1',
                   texname = '\\text{CKM3x3}')

MW = Parameter(name = 'MW',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(MZ**2/2. + cmath.sqrt(MZ**4/4. - (aEW*cmath.pi*MZ**2)/(Gf*cmath.sqrt(2))))',
               texname = 'M_W')

ee = Parameter(name = 'ee',
               nature = 'internal',
               type = 'real',
               value = '2*cmath.sqrt(aEW)*cmath.sqrt(cmath.pi)',
               texname = 'e')

sw2 = Parameter(name = 'sw2',
                nature = 'internal',
                type = 'real',
                value = '1 - MW**2/MZ**2',
                texname = '\\text{sw2}')

cw = Parameter(name = 'cw',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(1 - sw2)',
               texname = 'c_w')

sw = Parameter(name = 'sw',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(sw2)',
               texname = 's_w')

g1 = Parameter(name = 'g1',
               nature = 'internal',
               type = 'real',
               value = 'ee/cw',
               texname = 'g_1')

gw = Parameter(name = 'gw',
               nature = 'internal',
               type = 'real',
               value = 'ee/sw',
               texname = 'g_w')

vev = Parameter(name = 'vev',
                nature = 'internal',
                type = 'real',
                value = '(2*MW*sw)/ee',
                texname = '\\text{vev}')

lam = Parameter(name = 'lam',
                nature = 'internal',
                type = 'real',
                value = 'MH**2/(2.*vev**2)',
                texname = '\\text{lam}')

yb = Parameter(name = 'yb',
               nature = 'internal',
               type = 'real',
               value = '(ymb*cmath.sqrt(2))/vev',
               texname = '\\text{yb}')

yc = Parameter(name = 'yc',
               nature = 'internal',
               type = 'real',
               value = '(ymc*cmath.sqrt(2))/vev',
               texname = '\\text{yc}')

ydo = Parameter(name = 'ydo',
                nature = 'internal',
                type = 'real',
                value = '(ymdo*cmath.sqrt(2))/vev',
                texname = '\\text{ydo}')

ye = Parameter(name = 'ye',
               nature = 'internal',
               type = 'real',
               value = '(yme*cmath.sqrt(2))/vev',
               texname = '\\text{ye}')

ym = Parameter(name = 'ym',
               nature = 'internal',
               type = 'real',
               value = '(ymm*cmath.sqrt(2))/vev',
               texname = '\\text{ym}')

ys = Parameter(name = 'ys',
               nature = 'internal',
               type = 'real',
               value = '(yms*cmath.sqrt(2))/vev',
               texname = '\\text{ys}')

yt = Parameter(name = 'yt',
               nature = 'internal',
               type = 'real',
               value = '(ymt*cmath.sqrt(2))/vev',
               texname = '\\text{yt}')

ytau = Parameter(name = 'ytau',
                 nature = 'internal',
                 type = 'real',
                 value = '(ymtau*cmath.sqrt(2))/vev',
                 texname = '\\text{ytau}')

yup = Parameter(name = 'yup',
                nature = 'internal',
                type = 'real',
                value = '(ymup*cmath.sqrt(2))/vev',
                texname = '\\text{yup}')

muH = Parameter(name = 'muH',
                nature = 'internal',
                type = 'real',
                value = 'cmath.sqrt(lam*vev**2)',
                texname = '\\mu')

I1a11 = Parameter(name = 'I1a11',
                  nature = 'internal',
                  type = 'complex',
                  value = 'ydo*complexconjugate(CKM1x1)',
                  texname = '\\text{I1a11}')

I1a12 = Parameter(name = 'I1a12',
                  nature = 'internal',
                  type = 'complex',
                  value = 'ydo*complexconjugate(CKM2x1)',
                  texname = '\\text{I1a12}')

I1a13 = Parameter(name = 'I1a13',
                  nature = 'internal',
                  type = 'complex',
                  value = 'ydo*complexconjugate(CKM3x1)',
                  texname = '\\text{I1a13}')

I1a21 = Parameter(name = 'I1a21',
                  nature = 'internal',
                  type = 'complex',
                  value = 'ys*complexconjugate(CKM1x2)',
                  texname = '\\text{I1a21}')

I1a22 = Parameter(name = 'I1a22',
                  nature = 'internal',
                  type = 'complex',
                  value = 'ys*complexconjugate(CKM2x2)',
                  texname = '\\text{I1a22}')

I1a23 = Parameter(name = 'I1a23',
                  nature = 'internal',
                  type = 'complex',
                  value = 'ys*complexconjugate(CKM3x2)',
                  texname = '\\text{I1a23}')

I1a31 = Parameter(name = 'I1a31',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yb*complexconjugate(CKM1x3)',
                  texname = '\\text{I1a31}')

I1a32 = Parameter(name = 'I1a32',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yb*complexconjugate(CKM2x3)',
                  texname = '\\text{I1a32}')

I1a33 = Parameter(name = 'I1a33',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yb*complexconjugate(CKM3x3)',
                  texname = '\\text{I1a33}')

I2a11 = Parameter(name = 'I2a11',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yup*complexconjugate(CKM1x1)',
                  texname = '\\text{I2a11}')

I2a12 = Parameter(name = 'I2a12',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yc*complexconjugate(CKM2x1)',
                  texname = '\\text{I2a12}')

I2a13 = Parameter(name = 'I2a13',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yt*complexconjugate(CKM3x1)',
                  texname = '\\text{I2a13}')

I2a21 = Parameter(name = 'I2a21',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yup*complexconjugate(CKM1x2)',
                  texname = '\\text{I2a21}')

I2a22 = Parameter(name = 'I2a22',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yc*complexconjugate(CKM2x2)',
                  texname = '\\text{I2a22}')

I2a23 = Parameter(name = 'I2a23',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yt*complexconjugate(CKM3x2)',
                  texname = '\\text{I2a23}')

I2a31 = Parameter(name = 'I2a31',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yup*complexconjugate(CKM1x3)',
                  texname = '\\text{I2a31}')

I2a32 = Parameter(name = 'I2a32',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yc*complexconjugate(CKM2x3)',
                  texname = '\\text{I2a32}')

I2a33 = Parameter(name = 'I2a33',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yt*complexconjugate(CKM3x3)',
                  texname = '\\text{I2a33}')

I3a11 = Parameter(name = 'I3a11',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM1x1*yup',
                  texname = '\\text{I3a11}')

I3a12 = Parameter(name = 'I3a12',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM1x2*yup',
                  texname = '\\text{I3a12}')

I3a13 = Parameter(name = 'I3a13',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM1x3*yup',
                  texname = '\\text{I3a13}')

I3a21 = Parameter(name = 'I3a21',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM2x1*yc',
                  texname = '\\text{I3a21}')

I3a22 = Parameter(name = 'I3a22',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM2x2*yc',
                  texname = '\\text{I3a22}')

I3a23 = Parameter(name = 'I3a23',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM2x3*yc',
                  texname = '\\text{I3a23}')

I3a31 = Parameter(name = 'I3a31',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM3x1*yt',
                  texname = '\\text{I3a31}')

I3a32 = Parameter(name = 'I3a32',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM3x2*yt',
                  texname = '\\text{I3a32}')

I3a33 = Parameter(name = 'I3a33',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM3x3*yt',
                  texname = '\\text{I3a33}')

I4a11 = Parameter(name = 'I4a11',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM1x1*ydo',
                  texname = '\\text{I4a11}')

I4a12 = Parameter(name = 'I4a12',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM1x2*ys',
                  texname = '\\text{I4a12}')

I4a13 = Parameter(name = 'I4a13',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM1x3*yb',
                  texname = '\\text{I4a13}')

I4a21 = Parameter(name = 'I4a21',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM2x1*ydo',
                  texname = '\\text{I4a21}')

I4a22 = Parameter(name = 'I4a22',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM2x2*ys',
                  texname = '\\text{I4a22}')

I4a23 = Parameter(name = 'I4a23',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM2x3*yb',
                  texname = '\\text{I4a23}')

I4a31 = Parameter(name = 'I4a31',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM3x1*ydo',
                  texname = '\\text{I4a31}')

I4a32 = Parameter(name = 'I4a32',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM3x2*ys',
                  texname = '\\text{I4a32}')

I4a33 = Parameter(name = 'I4a33',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM3x3*yb',
                  texname = '\\text{I4a33}')


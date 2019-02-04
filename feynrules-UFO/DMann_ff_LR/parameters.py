# This file was automatically created by FeynRules 2.3.31
# Mathematica version: 11.0.0 for Mac OS X x86 (64-bit) (July 28, 2016)
# Date: Mon 4 Feb 2019 14:07:22



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

gL0d = Parameter(name = 'gL0d',
                 nature = 'external',
                 type = 'real',
                 value = 1.,
                 texname = 'g_{\\text{L0d}}',
                 lhablock = 'DMINPUTS',
                 lhacode = [ 1 ])

gL0u = Parameter(name = 'gL0u',
                 nature = 'external',
                 type = 'real',
                 value = 1.,
                 texname = 'g_{\\text{L0u}}',
                 lhablock = 'DMINPUTS',
                 lhacode = [ 2 ])

gL0s = Parameter(name = 'gL0s',
                 nature = 'external',
                 type = 'real',
                 value = 1.,
                 texname = 'g_{\\text{L0s}}',
                 lhablock = 'DMINPUTS',
                 lhacode = [ 3 ])

gL0c = Parameter(name = 'gL0c',
                 nature = 'external',
                 type = 'real',
                 value = 1.,
                 texname = 'g_{\\text{L0c}}',
                 lhablock = 'DMINPUTS',
                 lhacode = [ 4 ])

gL0b = Parameter(name = 'gL0b',
                 nature = 'external',
                 type = 'real',
                 value = 1.,
                 texname = 'g_{\\text{L0b}}',
                 lhablock = 'DMINPUTS',
                 lhacode = [ 5 ])

gL0t = Parameter(name = 'gL0t',
                 nature = 'external',
                 type = 'real',
                 value = 1.,
                 texname = 'g_{\\text{L0t}}',
                 lhablock = 'DMINPUTS',
                 lhacode = [ 6 ])

gR0d = Parameter(name = 'gR0d',
                 nature = 'external',
                 type = 'real',
                 value = 1.,
                 texname = 'g_{\\text{R0d}}',
                 lhablock = 'DMINPUTS',
                 lhacode = [ 7 ])

gR0u = Parameter(name = 'gR0u',
                 nature = 'external',
                 type = 'real',
                 value = 1.,
                 texname = 'g_{\\text{R0u}}',
                 lhablock = 'DMINPUTS',
                 lhacode = [ 8 ])

gR0s = Parameter(name = 'gR0s',
                 nature = 'external',
                 type = 'real',
                 value = 1.,
                 texname = 'g_{\\text{R0s}}',
                 lhablock = 'DMINPUTS',
                 lhacode = [ 9 ])

gR0c = Parameter(name = 'gR0c',
                 nature = 'external',
                 type = 'real',
                 value = 1.,
                 texname = 'g_{\\text{R0c}}',
                 lhablock = 'DMINPUTS',
                 lhacode = [ 10 ])

gR0b = Parameter(name = 'gR0b',
                 nature = 'external',
                 type = 'real',
                 value = 1.,
                 texname = 'g_{\\text{R0b}}',
                 lhablock = 'DMINPUTS',
                 lhacode = [ 11 ])

gR0t = Parameter(name = 'gR0t',
                 nature = 'external',
                 type = 'real',
                 value = 1.,
                 texname = 'g_{\\text{R0t}}',
                 lhablock = 'DMINPUTS',
                 lhacode = [ 12 ])

gL0e = Parameter(name = 'gL0e',
                 nature = 'external',
                 type = 'real',
                 value = 1.,
                 texname = 'g_{\\text{L0e}}',
                 lhablock = 'DMINPUTS',
                 lhacode = [ 13 ])

gR0e = Parameter(name = 'gR0e',
                 nature = 'external',
                 type = 'real',
                 value = 1.,
                 texname = 'g_{\\text{R0e}}',
                 lhablock = 'DMINPUTS',
                 lhacode = [ 14 ])

gL0mu = Parameter(name = 'gL0mu',
                  nature = 'external',
                  type = 'real',
                  value = 1.,
                  texname = 'g_{\\text{L0mu}}',
                  lhablock = 'DMINPUTS',
                  lhacode = [ 15 ])

gR0mu = Parameter(name = 'gR0mu',
                  nature = 'external',
                  type = 'real',
                  value = 1.,
                  texname = 'g_{\\text{R0mu}}',
                  lhablock = 'DMINPUTS',
                  lhacode = [ 16 ])

gL0ta = Parameter(name = 'gL0ta',
                  nature = 'external',
                  type = 'real',
                  value = 1.,
                  texname = 'g_{\\text{L0ta}}',
                  lhablock = 'DMINPUTS',
                  lhacode = [ 17 ])

gR0ta = Parameter(name = 'gR0ta',
                  nature = 'external',
                  type = 'real',
                  value = 1.,
                  texname = 'g_{\\text{R0ta}}',
                  lhablock = 'DMINPUTS',
                  lhacode = [ 18 ])

gL1d = Parameter(name = 'gL1d',
                 nature = 'external',
                 type = 'real',
                 value = 1.,
                 texname = 'g_{\\text{L1d}}',
                 lhablock = 'DMINPUTS',
                 lhacode = [ 19 ])

gL1u = Parameter(name = 'gL1u',
                 nature = 'external',
                 type = 'real',
                 value = 1.,
                 texname = 'g_{\\text{L1u}}',
                 lhablock = 'DMINPUTS',
                 lhacode = [ 20 ])

gL1s = Parameter(name = 'gL1s',
                 nature = 'external',
                 type = 'real',
                 value = 1.,
                 texname = 'g_{\\text{L1s}}',
                 lhablock = 'DMINPUTS',
                 lhacode = [ 21 ])

gL1c = Parameter(name = 'gL1c',
                 nature = 'external',
                 type = 'real',
                 value = 1.,
                 texname = 'g_{\\text{L1c}}',
                 lhablock = 'DMINPUTS',
                 lhacode = [ 22 ])

gL1b = Parameter(name = 'gL1b',
                 nature = 'external',
                 type = 'real',
                 value = 1.,
                 texname = 'g_{\\text{L1b}}',
                 lhablock = 'DMINPUTS',
                 lhacode = [ 23 ])

gL1t = Parameter(name = 'gL1t',
                 nature = 'external',
                 type = 'real',
                 value = 1.,
                 texname = 'g_{\\text{L1t}}',
                 lhablock = 'DMINPUTS',
                 lhacode = [ 24 ])

gR1d = Parameter(name = 'gR1d',
                 nature = 'external',
                 type = 'real',
                 value = 1.,
                 texname = 'g_{\\text{R1d}}',
                 lhablock = 'DMINPUTS',
                 lhacode = [ 25 ])

gR1u = Parameter(name = 'gR1u',
                 nature = 'external',
                 type = 'real',
                 value = 1.,
                 texname = 'g_{\\text{R1u}}',
                 lhablock = 'DMINPUTS',
                 lhacode = [ 26 ])

gR1s = Parameter(name = 'gR1s',
                 nature = 'external',
                 type = 'real',
                 value = 1.,
                 texname = 'g_{\\text{R1s}}',
                 lhablock = 'DMINPUTS',
                 lhacode = [ 27 ])

gR1c = Parameter(name = 'gR1c',
                 nature = 'external',
                 type = 'real',
                 value = 1.,
                 texname = 'g_{\\text{R1c}}',
                 lhablock = 'DMINPUTS',
                 lhacode = [ 28 ])

gR1b = Parameter(name = 'gR1b',
                 nature = 'external',
                 type = 'real',
                 value = 1.,
                 texname = 'g_{\\text{R1b}}',
                 lhablock = 'DMINPUTS',
                 lhacode = [ 29 ])

gR1t = Parameter(name = 'gR1t',
                 nature = 'external',
                 type = 'real',
                 value = 1.,
                 texname = 'g_{\\text{R1t}}',
                 lhablock = 'DMINPUTS',
                 lhacode = [ 30 ])

gL1e = Parameter(name = 'gL1e',
                 nature = 'external',
                 type = 'real',
                 value = 1.,
                 texname = 'g_{\\text{L1e}}',
                 lhablock = 'DMINPUTS',
                 lhacode = [ 31 ])

gR1e = Parameter(name = 'gR1e',
                 nature = 'external',
                 type = 'real',
                 value = 1.,
                 texname = 'g_{\\text{R1e}}',
                 lhablock = 'DMINPUTS',
                 lhacode = [ 32 ])

gL1mu = Parameter(name = 'gL1mu',
                  nature = 'external',
                  type = 'real',
                  value = 1.,
                  texname = 'g_{\\text{L1mu}}',
                  lhablock = 'DMINPUTS',
                  lhacode = [ 33 ])

gR1mu = Parameter(name = 'gR1mu',
                  nature = 'external',
                  type = 'real',
                  value = 1.,
                  texname = 'g_{\\text{R1mu}}',
                  lhablock = 'DMINPUTS',
                  lhacode = [ 34 ])

gL1ta = Parameter(name = 'gL1ta',
                  nature = 'external',
                  type = 'real',
                  value = 1.,
                  texname = 'g_{\\text{L1ta}}',
                  lhablock = 'DMINPUTS',
                  lhacode = [ 35 ])

gR1ta = Parameter(name = 'gR1ta',
                  nature = 'external',
                  type = 'real',
                  value = 1.,
                  texname = 'g_{\\text{R1ta}}',
                  lhablock = 'DMINPUTS',
                  lhacode = [ 36 ])

Lambda = Parameter(name = 'Lambda',
                   nature = 'external',
                   type = 'real',
                   value = 1000.,
                   texname = '\\Lambda',
                   lhablock = 'DMINPUTS',
                   lhacode = [ 37 ])

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

MY0 = Parameter(name = 'MY0',
                nature = 'external',
                type = 'real',
                value = 1000.,
                texname = '\\text{MY0}',
                lhablock = 'MASS',
                lhacode = [ 9000006 ])

MY1 = Parameter(name = 'MY1',
                nature = 'external',
                type = 'real',
                value = 1000.,
                texname = '\\text{MY1}',
                lhablock = 'MASS',
                lhacode = [ 9000007 ])

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
                value = 0.,
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

WY0 = Parameter(name = 'WY0',
                nature = 'external',
                type = 'real',
                value = 10.,
                texname = '\\text{WY0}',
                lhablock = 'DECAY',
                lhacode = [ 9000006 ])

WY1 = Parameter(name = 'WY1',
                nature = 'external',
                type = 'real',
                value = 10.,
                texname = '\\text{WY1}',
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


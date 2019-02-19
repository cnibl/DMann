# This file was automatically created by FeynRules 2.3.31
# Mathematica version: 11.0.0 for Mac OS X x86 (64-bit) (July 28, 2016)
# Date: Tue 19 Feb 2019 19:52:55


from object_library import all_decays, Decay
import particles as P


Decay_b = Decay(name = 'Decay_b',
                particle = P.b,
                partial_widths = {(P.W__minus__,P.c):'(((3*CKM2x3*ee**2*MB**2*complexconjugate(CKM2x3))/(2.*sw**2) + (3*CKM2x3*ee**2*MC**2*complexconjugate(CKM2x3))/(2.*sw**2) + (3*CKM2x3*ee**2*MB**4*complexconjugate(CKM2x3))/(2.*MW**2*sw**2) - (3*CKM2x3*ee**2*MB**2*MC**2*complexconjugate(CKM2x3))/(MW**2*sw**2) + (3*CKM2x3*ee**2*MC**4*complexconjugate(CKM2x3))/(2.*MW**2*sw**2) - (3*CKM2x3*ee**2*MW**2*complexconjugate(CKM2x3))/sw**2)*cmath.sqrt(MB**4 - 2*MB**2*MC**2 + MC**4 - 2*MB**2*MW**2 - 2*MC**2*MW**2 + MW**4))/(96.*cmath.pi*abs(MB)**3)',
                                  (P.W__minus__,P.t):'(((3*CKM3x3*ee**2*MB**2*complexconjugate(CKM3x3))/(2.*sw**2) + (3*CKM3x3*ee**2*MT**2*complexconjugate(CKM3x3))/(2.*sw**2) + (3*CKM3x3*ee**2*MB**4*complexconjugate(CKM3x3))/(2.*MW**2*sw**2) - (3*CKM3x3*ee**2*MB**2*MT**2*complexconjugate(CKM3x3))/(MW**2*sw**2) + (3*CKM3x3*ee**2*MT**4*complexconjugate(CKM3x3))/(2.*MW**2*sw**2) - (3*CKM3x3*ee**2*MW**2*complexconjugate(CKM3x3))/sw**2)*cmath.sqrt(MB**4 - 2*MB**2*MT**2 + MT**4 - 2*MB**2*MW**2 - 2*MT**2*MW**2 + MW**4))/(96.*cmath.pi*abs(MB)**3)',
                                  (P.W__minus__,P.u):'(((3*CKM1x3*ee**2*MB**2*complexconjugate(CKM1x3))/(2.*sw**2) + (3*CKM1x3*ee**2*MU**2*complexconjugate(CKM1x3))/(2.*sw**2) + (3*CKM1x3*ee**2*MB**4*complexconjugate(CKM1x3))/(2.*MW**2*sw**2) - (3*CKM1x3*ee**2*MB**2*MU**2*complexconjugate(CKM1x3))/(MW**2*sw**2) + (3*CKM1x3*ee**2*MU**4*complexconjugate(CKM1x3))/(2.*MW**2*sw**2) - (3*CKM1x3*ee**2*MW**2*complexconjugate(CKM1x3))/sw**2)*cmath.sqrt(MB**4 - 2*MB**2*MU**2 + MU**4 - 2*MB**2*MW**2 - 2*MU**2*MW**2 + MW**4))/(96.*cmath.pi*abs(MB)**3)'})

Decay_c = Decay(name = 'Decay_c',
                particle = P.c,
                partial_widths = {(P.W__plus__,P.b):'(((3*CKM2x3*ee**2*MB**2*complexconjugate(CKM2x3))/(2.*sw**2) + (3*CKM2x3*ee**2*MC**2*complexconjugate(CKM2x3))/(2.*sw**2) + (3*CKM2x3*ee**2*MB**4*complexconjugate(CKM2x3))/(2.*MW**2*sw**2) - (3*CKM2x3*ee**2*MB**2*MC**2*complexconjugate(CKM2x3))/(MW**2*sw**2) + (3*CKM2x3*ee**2*MC**4*complexconjugate(CKM2x3))/(2.*MW**2*sw**2) - (3*CKM2x3*ee**2*MW**2*complexconjugate(CKM2x3))/sw**2)*cmath.sqrt(MB**4 - 2*MB**2*MC**2 + MC**4 - 2*MB**2*MW**2 - 2*MC**2*MW**2 + MW**4))/(96.*cmath.pi*abs(MC)**3)',
                                  (P.W__plus__,P.d):'(((3*CKM2x1*ee**2*MC**2*complexconjugate(CKM2x1))/(2.*sw**2) + (3*CKM2x1*ee**2*MD**2*complexconjugate(CKM2x1))/(2.*sw**2) + (3*CKM2x1*ee**2*MC**4*complexconjugate(CKM2x1))/(2.*MW**2*sw**2) - (3*CKM2x1*ee**2*MC**2*MD**2*complexconjugate(CKM2x1))/(MW**2*sw**2) + (3*CKM2x1*ee**2*MD**4*complexconjugate(CKM2x1))/(2.*MW**2*sw**2) - (3*CKM2x1*ee**2*MW**2*complexconjugate(CKM2x1))/sw**2)*cmath.sqrt(MC**4 - 2*MC**2*MD**2 + MD**4 - 2*MC**2*MW**2 - 2*MD**2*MW**2 + MW**4))/(96.*cmath.pi*abs(MC)**3)',
                                  (P.W__plus__,P.s):'(((3*CKM2x2*ee**2*MC**2*complexconjugate(CKM2x2))/(2.*sw**2) + (3*CKM2x2*ee**2*MS**2*complexconjugate(CKM2x2))/(2.*sw**2) + (3*CKM2x2*ee**2*MC**4*complexconjugate(CKM2x2))/(2.*MW**2*sw**2) - (3*CKM2x2*ee**2*MC**2*MS**2*complexconjugate(CKM2x2))/(MW**2*sw**2) + (3*CKM2x2*ee**2*MS**4*complexconjugate(CKM2x2))/(2.*MW**2*sw**2) - (3*CKM2x2*ee**2*MW**2*complexconjugate(CKM2x2))/sw**2)*cmath.sqrt(MC**4 - 2*MC**2*MS**2 + MS**4 - 2*MC**2*MW**2 - 2*MS**2*MW**2 + MW**4))/(96.*cmath.pi*abs(MC)**3)'})

Decay_d = Decay(name = 'Decay_d',
                particle = P.d,
                partial_widths = {(P.W__minus__,P.c):'(((3*CKM2x1*ee**2*MC**2*complexconjugate(CKM2x1))/(2.*sw**2) + (3*CKM2x1*ee**2*MD**2*complexconjugate(CKM2x1))/(2.*sw**2) + (3*CKM2x1*ee**2*MC**4*complexconjugate(CKM2x1))/(2.*MW**2*sw**2) - (3*CKM2x1*ee**2*MC**2*MD**2*complexconjugate(CKM2x1))/(MW**2*sw**2) + (3*CKM2x1*ee**2*MD**4*complexconjugate(CKM2x1))/(2.*MW**2*sw**2) - (3*CKM2x1*ee**2*MW**2*complexconjugate(CKM2x1))/sw**2)*cmath.sqrt(MC**4 - 2*MC**2*MD**2 + MD**4 - 2*MC**2*MW**2 - 2*MD**2*MW**2 + MW**4))/(96.*cmath.pi*abs(MD)**3)',
                                  (P.W__minus__,P.t):'(((3*CKM3x1*ee**2*MD**2*complexconjugate(CKM3x1))/(2.*sw**2) + (3*CKM3x1*ee**2*MT**2*complexconjugate(CKM3x1))/(2.*sw**2) + (3*CKM3x1*ee**2*MD**4*complexconjugate(CKM3x1))/(2.*MW**2*sw**2) - (3*CKM3x1*ee**2*MD**2*MT**2*complexconjugate(CKM3x1))/(MW**2*sw**2) + (3*CKM3x1*ee**2*MT**4*complexconjugate(CKM3x1))/(2.*MW**2*sw**2) - (3*CKM3x1*ee**2*MW**2*complexconjugate(CKM3x1))/sw**2)*cmath.sqrt(MD**4 - 2*MD**2*MT**2 + MT**4 - 2*MD**2*MW**2 - 2*MT**2*MW**2 + MW**4))/(96.*cmath.pi*abs(MD)**3)',
                                  (P.W__minus__,P.u):'(((3*CKM1x1*ee**2*MD**2*complexconjugate(CKM1x1))/(2.*sw**2) + (3*CKM1x1*ee**2*MU**2*complexconjugate(CKM1x1))/(2.*sw**2) + (3*CKM1x1*ee**2*MD**4*complexconjugate(CKM1x1))/(2.*MW**2*sw**2) - (3*CKM1x1*ee**2*MD**2*MU**2*complexconjugate(CKM1x1))/(MW**2*sw**2) + (3*CKM1x1*ee**2*MU**4*complexconjugate(CKM1x1))/(2.*MW**2*sw**2) - (3*CKM1x1*ee**2*MW**2*complexconjugate(CKM1x1))/sw**2)*cmath.sqrt(MD**4 - 2*MD**2*MU**2 + MU**4 - 2*MD**2*MW**2 - 2*MU**2*MW**2 + MW**4))/(96.*cmath.pi*abs(MD)**3)'})

Decay_e__minus__ = Decay(name = 'Decay_e__minus__',
                         particle = P.e__minus__,
                         partial_widths = {(P.W__minus__,P.ve):'((Me**2 - MW**2)*((ee**2*Me**2)/(2.*sw**2) + (ee**2*Me**4)/(2.*MW**2*sw**2) - (ee**2*MW**2)/sw**2))/(32.*cmath.pi*abs(Me)**3)'})

Decay_H = Decay(name = 'Decay_H',
                particle = P.H,
                partial_widths = {(P.b,P.b__tilde__):'((-12*MB**2*yb**2 + 3*MH**2*yb**2)*cmath.sqrt(-4*MB**2*MH**2 + MH**4))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.c,P.c__tilde__):'((-12*MC**2*yc**2 + 3*MH**2*yc**2)*cmath.sqrt(-4*MC**2*MH**2 + MH**4))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.d,P.d__tilde__):'((-12*MD**2*ydo**2 + 3*MH**2*ydo**2)*cmath.sqrt(-4*MD**2*MH**2 + MH**4))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.e__minus__,P.e__plus__):'((-4*Me**2*ye**2 + MH**2*ye**2)*cmath.sqrt(-4*Me**2*MH**2 + MH**4))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.mu__minus__,P.mu__plus__):'((MH**2*ym**2 - 4*MMU**2*ym**2)*cmath.sqrt(MH**4 - 4*MH**2*MMU**2))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.s,P.s__tilde__):'((3*MH**2*ys**2 - 12*MS**2*ys**2)*cmath.sqrt(MH**4 - 4*MH**2*MS**2))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.t,P.t__tilde__):'((3*MH**2*yt**2 - 12*MT**2*yt**2)*cmath.sqrt(MH**4 - 4*MH**2*MT**2))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.ta__minus__,P.ta__plus__):'((MH**2*ytau**2 - 4*MTA**2*ytau**2)*cmath.sqrt(MH**4 - 4*MH**2*MTA**2))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.u,P.u__tilde__):'((3*MH**2*yup**2 - 12*MU**2*yup**2)*cmath.sqrt(MH**4 - 4*MH**2*MU**2))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.W__minus__,P.W__plus__):'(((3*ee**4*vev**2)/(4.*sw**4) + (ee**4*MH**4*vev**2)/(16.*MW**4*sw**4) - (ee**4*MH**2*vev**2)/(4.*MW**2*sw**4))*cmath.sqrt(MH**4 - 4*MH**2*MW**2))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.Z,P.Z):'(((9*ee**4*vev**2)/2. + (3*ee**4*MH**4*vev**2)/(8.*MZ**4) - (3*ee**4*MH**2*vev**2)/(2.*MZ**2) + (3*cw**4*ee**4*vev**2)/(4.*sw**4) + (cw**4*ee**4*MH**4*vev**2)/(16.*MZ**4*sw**4) - (cw**4*ee**4*MH**2*vev**2)/(4.*MZ**2*sw**4) + (3*cw**2*ee**4*vev**2)/sw**2 + (cw**2*ee**4*MH**4*vev**2)/(4.*MZ**4*sw**2) - (cw**2*ee**4*MH**2*vev**2)/(MZ**2*sw**2) + (3*ee**4*sw**2*vev**2)/cw**2 + (ee**4*MH**4*sw**2*vev**2)/(4.*cw**2*MZ**4) - (ee**4*MH**2*sw**2*vev**2)/(cw**2*MZ**2) + (3*ee**4*sw**4*vev**2)/(4.*cw**4) + (ee**4*MH**4*sw**4*vev**2)/(16.*cw**4*MZ**4) - (ee**4*MH**2*sw**4*vev**2)/(4.*cw**4*MZ**2))*cmath.sqrt(MH**4 - 4*MH**2*MZ**2))/(32.*cmath.pi*abs(MH)**3)'})

Decay_mu__minus__ = Decay(name = 'Decay_mu__minus__',
                          particle = P.mu__minus__,
                          partial_widths = {(P.W__minus__,P.vm):'((MMU**2 - MW**2)*((ee**2*MMU**2)/(2.*sw**2) + (ee**2*MMU**4)/(2.*MW**2*sw**2) - (ee**2*MW**2)/sw**2))/(32.*cmath.pi*abs(MMU)**3)'})

Decay_s = Decay(name = 'Decay_s',
                particle = P.s,
                partial_widths = {(P.W__minus__,P.c):'(((3*CKM2x2*ee**2*MC**2*complexconjugate(CKM2x2))/(2.*sw**2) + (3*CKM2x2*ee**2*MS**2*complexconjugate(CKM2x2))/(2.*sw**2) + (3*CKM2x2*ee**2*MC**4*complexconjugate(CKM2x2))/(2.*MW**2*sw**2) - (3*CKM2x2*ee**2*MC**2*MS**2*complexconjugate(CKM2x2))/(MW**2*sw**2) + (3*CKM2x2*ee**2*MS**4*complexconjugate(CKM2x2))/(2.*MW**2*sw**2) - (3*CKM2x2*ee**2*MW**2*complexconjugate(CKM2x2))/sw**2)*cmath.sqrt(MC**4 - 2*MC**2*MS**2 + MS**4 - 2*MC**2*MW**2 - 2*MS**2*MW**2 + MW**4))/(96.*cmath.pi*abs(MS)**3)',
                                  (P.W__minus__,P.t):'(((3*CKM3x2*ee**2*MS**2*complexconjugate(CKM3x2))/(2.*sw**2) + (3*CKM3x2*ee**2*MT**2*complexconjugate(CKM3x2))/(2.*sw**2) + (3*CKM3x2*ee**2*MS**4*complexconjugate(CKM3x2))/(2.*MW**2*sw**2) - (3*CKM3x2*ee**2*MS**2*MT**2*complexconjugate(CKM3x2))/(MW**2*sw**2) + (3*CKM3x2*ee**2*MT**4*complexconjugate(CKM3x2))/(2.*MW**2*sw**2) - (3*CKM3x2*ee**2*MW**2*complexconjugate(CKM3x2))/sw**2)*cmath.sqrt(MS**4 - 2*MS**2*MT**2 + MT**4 - 2*MS**2*MW**2 - 2*MT**2*MW**2 + MW**4))/(96.*cmath.pi*abs(MS)**3)',
                                  (P.W__minus__,P.u):'(((3*CKM1x2*ee**2*MS**2*complexconjugate(CKM1x2))/(2.*sw**2) + (3*CKM1x2*ee**2*MU**2*complexconjugate(CKM1x2))/(2.*sw**2) + (3*CKM1x2*ee**2*MS**4*complexconjugate(CKM1x2))/(2.*MW**2*sw**2) - (3*CKM1x2*ee**2*MS**2*MU**2*complexconjugate(CKM1x2))/(MW**2*sw**2) + (3*CKM1x2*ee**2*MU**4*complexconjugate(CKM1x2))/(2.*MW**2*sw**2) - (3*CKM1x2*ee**2*MW**2*complexconjugate(CKM1x2))/sw**2)*cmath.sqrt(MS**4 - 2*MS**2*MU**2 + MU**4 - 2*MS**2*MW**2 - 2*MU**2*MW**2 + MW**4))/(96.*cmath.pi*abs(MS)**3)'})

Decay_t = Decay(name = 'Decay_t',
                particle = P.t,
                partial_widths = {(P.W__plus__,P.b):'(((3*CKM3x3*ee**2*MB**2*complexconjugate(CKM3x3))/(2.*sw**2) + (3*CKM3x3*ee**2*MT**2*complexconjugate(CKM3x3))/(2.*sw**2) + (3*CKM3x3*ee**2*MB**4*complexconjugate(CKM3x3))/(2.*MW**2*sw**2) - (3*CKM3x3*ee**2*MB**2*MT**2*complexconjugate(CKM3x3))/(MW**2*sw**2) + (3*CKM3x3*ee**2*MT**4*complexconjugate(CKM3x3))/(2.*MW**2*sw**2) - (3*CKM3x3*ee**2*MW**2*complexconjugate(CKM3x3))/sw**2)*cmath.sqrt(MB**4 - 2*MB**2*MT**2 + MT**4 - 2*MB**2*MW**2 - 2*MT**2*MW**2 + MW**4))/(96.*cmath.pi*abs(MT)**3)',
                                  (P.W__plus__,P.d):'(((3*CKM3x1*ee**2*MD**2*complexconjugate(CKM3x1))/(2.*sw**2) + (3*CKM3x1*ee**2*MT**2*complexconjugate(CKM3x1))/(2.*sw**2) + (3*CKM3x1*ee**2*MD**4*complexconjugate(CKM3x1))/(2.*MW**2*sw**2) - (3*CKM3x1*ee**2*MD**2*MT**2*complexconjugate(CKM3x1))/(MW**2*sw**2) + (3*CKM3x1*ee**2*MT**4*complexconjugate(CKM3x1))/(2.*MW**2*sw**2) - (3*CKM3x1*ee**2*MW**2*complexconjugate(CKM3x1))/sw**2)*cmath.sqrt(MD**4 - 2*MD**2*MT**2 + MT**4 - 2*MD**2*MW**2 - 2*MT**2*MW**2 + MW**4))/(96.*cmath.pi*abs(MT)**3)',
                                  (P.W__plus__,P.s):'(((3*CKM3x2*ee**2*MS**2*complexconjugate(CKM3x2))/(2.*sw**2) + (3*CKM3x2*ee**2*MT**2*complexconjugate(CKM3x2))/(2.*sw**2) + (3*CKM3x2*ee**2*MS**4*complexconjugate(CKM3x2))/(2.*MW**2*sw**2) - (3*CKM3x2*ee**2*MS**2*MT**2*complexconjugate(CKM3x2))/(MW**2*sw**2) + (3*CKM3x2*ee**2*MT**4*complexconjugate(CKM3x2))/(2.*MW**2*sw**2) - (3*CKM3x2*ee**2*MW**2*complexconjugate(CKM3x2))/sw**2)*cmath.sqrt(MS**4 - 2*MS**2*MT**2 + MT**4 - 2*MS**2*MW**2 - 2*MT**2*MW**2 + MW**4))/(96.*cmath.pi*abs(MT)**3)'})

Decay_ta__minus__ = Decay(name = 'Decay_ta__minus__',
                          particle = P.ta__minus__,
                          partial_widths = {(P.W__minus__,P.vt):'((MTA**2 - MW**2)*((ee**2*MTA**2)/(2.*sw**2) + (ee**2*MTA**4)/(2.*MW**2*sw**2) - (ee**2*MW**2)/sw**2))/(32.*cmath.pi*abs(MTA)**3)'})

Decay_u = Decay(name = 'Decay_u',
                particle = P.u,
                partial_widths = {(P.W__plus__,P.b):'(((3*CKM1x3*ee**2*MB**2*complexconjugate(CKM1x3))/(2.*sw**2) + (3*CKM1x3*ee**2*MU**2*complexconjugate(CKM1x3))/(2.*sw**2) + (3*CKM1x3*ee**2*MB**4*complexconjugate(CKM1x3))/(2.*MW**2*sw**2) - (3*CKM1x3*ee**2*MB**2*MU**2*complexconjugate(CKM1x3))/(MW**2*sw**2) + (3*CKM1x3*ee**2*MU**4*complexconjugate(CKM1x3))/(2.*MW**2*sw**2) - (3*CKM1x3*ee**2*MW**2*complexconjugate(CKM1x3))/sw**2)*cmath.sqrt(MB**4 - 2*MB**2*MU**2 + MU**4 - 2*MB**2*MW**2 - 2*MU**2*MW**2 + MW**4))/(96.*cmath.pi*abs(MU)**3)',
                                  (P.W__plus__,P.d):'(((3*CKM1x1*ee**2*MD**2*complexconjugate(CKM1x1))/(2.*sw**2) + (3*CKM1x1*ee**2*MU**2*complexconjugate(CKM1x1))/(2.*sw**2) + (3*CKM1x1*ee**2*MD**4*complexconjugate(CKM1x1))/(2.*MW**2*sw**2) - (3*CKM1x1*ee**2*MD**2*MU**2*complexconjugate(CKM1x1))/(MW**2*sw**2) + (3*CKM1x1*ee**2*MU**4*complexconjugate(CKM1x1))/(2.*MW**2*sw**2) - (3*CKM1x1*ee**2*MW**2*complexconjugate(CKM1x1))/sw**2)*cmath.sqrt(MD**4 - 2*MD**2*MU**2 + MU**4 - 2*MD**2*MW**2 - 2*MU**2*MW**2 + MW**4))/(96.*cmath.pi*abs(MU)**3)',
                                  (P.W__plus__,P.s):'(((3*CKM1x2*ee**2*MS**2*complexconjugate(CKM1x2))/(2.*sw**2) + (3*CKM1x2*ee**2*MU**2*complexconjugate(CKM1x2))/(2.*sw**2) + (3*CKM1x2*ee**2*MS**4*complexconjugate(CKM1x2))/(2.*MW**2*sw**2) - (3*CKM1x2*ee**2*MS**2*MU**2*complexconjugate(CKM1x2))/(MW**2*sw**2) + (3*CKM1x2*ee**2*MU**4*complexconjugate(CKM1x2))/(2.*MW**2*sw**2) - (3*CKM1x2*ee**2*MW**2*complexconjugate(CKM1x2))/sw**2)*cmath.sqrt(MS**4 - 2*MS**2*MU**2 + MU**4 - 2*MS**2*MW**2 - 2*MU**2*MW**2 + MW**4))/(96.*cmath.pi*abs(MU)**3)'})

Decay_W__plus__ = Decay(name = 'Decay_W__plus__',
                        particle = P.W__plus__,
                        partial_widths = {(P.c,P.b__tilde__):'(((-3*CKM2x3*ee**2*MB**2*complexconjugate(CKM2x3))/(2.*sw**2) - (3*CKM2x3*ee**2*MC**2*complexconjugate(CKM2x3))/(2.*sw**2) - (3*CKM2x3*ee**2*MB**4*complexconjugate(CKM2x3))/(2.*MW**2*sw**2) + (3*CKM2x3*ee**2*MB**2*MC**2*complexconjugate(CKM2x3))/(MW**2*sw**2) - (3*CKM2x3*ee**2*MC**4*complexconjugate(CKM2x3))/(2.*MW**2*sw**2) + (3*CKM2x3*ee**2*MW**2*complexconjugate(CKM2x3))/sw**2)*cmath.sqrt(MB**4 - 2*MB**2*MC**2 + MC**4 - 2*MB**2*MW**2 - 2*MC**2*MW**2 + MW**4))/(48.*cmath.pi*abs(MW)**3)',
                                          (P.c,P.d__tilde__):'(((-3*CKM2x1*ee**2*MC**2*complexconjugate(CKM2x1))/(2.*sw**2) - (3*CKM2x1*ee**2*MD**2*complexconjugate(CKM2x1))/(2.*sw**2) - (3*CKM2x1*ee**2*MC**4*complexconjugate(CKM2x1))/(2.*MW**2*sw**2) + (3*CKM2x1*ee**2*MC**2*MD**2*complexconjugate(CKM2x1))/(MW**2*sw**2) - (3*CKM2x1*ee**2*MD**4*complexconjugate(CKM2x1))/(2.*MW**2*sw**2) + (3*CKM2x1*ee**2*MW**2*complexconjugate(CKM2x1))/sw**2)*cmath.sqrt(MC**4 - 2*MC**2*MD**2 + MD**4 - 2*MC**2*MW**2 - 2*MD**2*MW**2 + MW**4))/(48.*cmath.pi*abs(MW)**3)',
                                          (P.c,P.s__tilde__):'(((-3*CKM2x2*ee**2*MC**2*complexconjugate(CKM2x2))/(2.*sw**2) - (3*CKM2x2*ee**2*MS**2*complexconjugate(CKM2x2))/(2.*sw**2) - (3*CKM2x2*ee**2*MC**4*complexconjugate(CKM2x2))/(2.*MW**2*sw**2) + (3*CKM2x2*ee**2*MC**2*MS**2*complexconjugate(CKM2x2))/(MW**2*sw**2) - (3*CKM2x2*ee**2*MS**4*complexconjugate(CKM2x2))/(2.*MW**2*sw**2) + (3*CKM2x2*ee**2*MW**2*complexconjugate(CKM2x2))/sw**2)*cmath.sqrt(MC**4 - 2*MC**2*MS**2 + MS**4 - 2*MC**2*MW**2 - 2*MS**2*MW**2 + MW**4))/(48.*cmath.pi*abs(MW)**3)',
                                          (P.t,P.b__tilde__):'(((-3*CKM3x3*ee**2*MB**2*complexconjugate(CKM3x3))/(2.*sw**2) - (3*CKM3x3*ee**2*MT**2*complexconjugate(CKM3x3))/(2.*sw**2) - (3*CKM3x3*ee**2*MB**4*complexconjugate(CKM3x3))/(2.*MW**2*sw**2) + (3*CKM3x3*ee**2*MB**2*MT**2*complexconjugate(CKM3x3))/(MW**2*sw**2) - (3*CKM3x3*ee**2*MT**4*complexconjugate(CKM3x3))/(2.*MW**2*sw**2) + (3*CKM3x3*ee**2*MW**2*complexconjugate(CKM3x3))/sw**2)*cmath.sqrt(MB**4 - 2*MB**2*MT**2 + MT**4 - 2*MB**2*MW**2 - 2*MT**2*MW**2 + MW**4))/(48.*cmath.pi*abs(MW)**3)',
                                          (P.t,P.d__tilde__):'(((-3*CKM3x1*ee**2*MD**2*complexconjugate(CKM3x1))/(2.*sw**2) - (3*CKM3x1*ee**2*MT**2*complexconjugate(CKM3x1))/(2.*sw**2) - (3*CKM3x1*ee**2*MD**4*complexconjugate(CKM3x1))/(2.*MW**2*sw**2) + (3*CKM3x1*ee**2*MD**2*MT**2*complexconjugate(CKM3x1))/(MW**2*sw**2) - (3*CKM3x1*ee**2*MT**4*complexconjugate(CKM3x1))/(2.*MW**2*sw**2) + (3*CKM3x1*ee**2*MW**2*complexconjugate(CKM3x1))/sw**2)*cmath.sqrt(MD**4 - 2*MD**2*MT**2 + MT**4 - 2*MD**2*MW**2 - 2*MT**2*MW**2 + MW**4))/(48.*cmath.pi*abs(MW)**3)',
                                          (P.t,P.s__tilde__):'(((-3*CKM3x2*ee**2*MS**2*complexconjugate(CKM3x2))/(2.*sw**2) - (3*CKM3x2*ee**2*MT**2*complexconjugate(CKM3x2))/(2.*sw**2) - (3*CKM3x2*ee**2*MS**4*complexconjugate(CKM3x2))/(2.*MW**2*sw**2) + (3*CKM3x2*ee**2*MS**2*MT**2*complexconjugate(CKM3x2))/(MW**2*sw**2) - (3*CKM3x2*ee**2*MT**4*complexconjugate(CKM3x2))/(2.*MW**2*sw**2) + (3*CKM3x2*ee**2*MW**2*complexconjugate(CKM3x2))/sw**2)*cmath.sqrt(MS**4 - 2*MS**2*MT**2 + MT**4 - 2*MS**2*MW**2 - 2*MT**2*MW**2 + MW**4))/(48.*cmath.pi*abs(MW)**3)',
                                          (P.u,P.b__tilde__):'(((-3*CKM1x3*ee**2*MB**2*complexconjugate(CKM1x3))/(2.*sw**2) - (3*CKM1x3*ee**2*MU**2*complexconjugate(CKM1x3))/(2.*sw**2) - (3*CKM1x3*ee**2*MB**4*complexconjugate(CKM1x3))/(2.*MW**2*sw**2) + (3*CKM1x3*ee**2*MB**2*MU**2*complexconjugate(CKM1x3))/(MW**2*sw**2) - (3*CKM1x3*ee**2*MU**4*complexconjugate(CKM1x3))/(2.*MW**2*sw**2) + (3*CKM1x3*ee**2*MW**2*complexconjugate(CKM1x3))/sw**2)*cmath.sqrt(MB**4 - 2*MB**2*MU**2 + MU**4 - 2*MB**2*MW**2 - 2*MU**2*MW**2 + MW**4))/(48.*cmath.pi*abs(MW)**3)',
                                          (P.u,P.d__tilde__):'(((-3*CKM1x1*ee**2*MD**2*complexconjugate(CKM1x1))/(2.*sw**2) - (3*CKM1x1*ee**2*MU**2*complexconjugate(CKM1x1))/(2.*sw**2) - (3*CKM1x1*ee**2*MD**4*complexconjugate(CKM1x1))/(2.*MW**2*sw**2) + (3*CKM1x1*ee**2*MD**2*MU**2*complexconjugate(CKM1x1))/(MW**2*sw**2) - (3*CKM1x1*ee**2*MU**4*complexconjugate(CKM1x1))/(2.*MW**2*sw**2) + (3*CKM1x1*ee**2*MW**2*complexconjugate(CKM1x1))/sw**2)*cmath.sqrt(MD**4 - 2*MD**2*MU**2 + MU**4 - 2*MD**2*MW**2 - 2*MU**2*MW**2 + MW**4))/(48.*cmath.pi*abs(MW)**3)',
                                          (P.u,P.s__tilde__):'(((-3*CKM1x2*ee**2*MS**2*complexconjugate(CKM1x2))/(2.*sw**2) - (3*CKM1x2*ee**2*MU**2*complexconjugate(CKM1x2))/(2.*sw**2) - (3*CKM1x2*ee**2*MS**4*complexconjugate(CKM1x2))/(2.*MW**2*sw**2) + (3*CKM1x2*ee**2*MS**2*MU**2*complexconjugate(CKM1x2))/(MW**2*sw**2) - (3*CKM1x2*ee**2*MU**4*complexconjugate(CKM1x2))/(2.*MW**2*sw**2) + (3*CKM1x2*ee**2*MW**2*complexconjugate(CKM1x2))/sw**2)*cmath.sqrt(MS**4 - 2*MS**2*MU**2 + MU**4 - 2*MS**2*MW**2 - 2*MU**2*MW**2 + MW**4))/(48.*cmath.pi*abs(MW)**3)',
                                          (P.ve,P.e__plus__):'((-Me**2 + MW**2)*(-(ee**2*Me**2)/(2.*sw**2) - (ee**2*Me**4)/(2.*MW**2*sw**2) + (ee**2*MW**2)/sw**2))/(48.*cmath.pi*abs(MW)**3)',
                                          (P.vm,P.mu__plus__):'((-MMU**2 + MW**2)*(-(ee**2*MMU**2)/(2.*sw**2) - (ee**2*MMU**4)/(2.*MW**2*sw**2) + (ee**2*MW**2)/sw**2))/(48.*cmath.pi*abs(MW)**3)',
                                          (P.vt,P.ta__plus__):'((-MTA**2 + MW**2)*(-(ee**2*MTA**2)/(2.*sw**2) - (ee**2*MTA**4)/(2.*MW**2*sw**2) + (ee**2*MW**2)/sw**2))/(48.*cmath.pi*abs(MW)**3)'})

Decay_Y0 = Decay(name = 'Decay_Y0',
                 particle = P.Y0,
                 partial_widths = {(P.a,P.a):'(MD0**2*(16*cw**4*gSBL**2*Lambda**2 - 24*cw**4*gSBL*gSBT*MD0**2 + (8*cw**4*gPBT**2*MD0**4)/Lambda**2 + (8*cw**4*gSBT**2*MD0**4)/Lambda**2 + 32*cw**2*gSBL*gSWL*Lambda**2*sw**2 - 24*cw**2*gSBT*gSWL*MD0**2*sw**2 - 24*cw**2*gSBL*gSWT*MD0**2*sw**2 + (16*cw**2*gPBT*gPWT*MD0**4*sw**2)/Lambda**2 + (16*cw**2*gSBT*gSWT*MD0**4*sw**2)/Lambda**2 + 16*gSWL**2*Lambda**2*sw**4 - 24*gSWL*gSWT*MD0**2*sw**4 + (8*gPWT**2*MD0**4*sw**4)/Lambda**2 + (8*gSWT**2*MD0**4*sw**4)/Lambda**2))/(32.*cmath.pi*abs(MD0)**3)',
                                   (P.a,P.Z):'((MD0**2 - MZ**2)*(12*cw**2*gSBL**2*Lambda**2*sw**2 - 24*cw**2*gSBL*gSWL*Lambda**2*sw**2 + 12*cw**2*gSWL**2*Lambda**2*sw**2 - 24*cw**2*gSBL*gSBT*MD0**2*sw**2 + 24*cw**2*gSBT*gSWL*MD0**2*sw**2 + 24*cw**2*gSBL*gSWT*MD0**2*sw**2 - 24*cw**2*gSWL*gSWT*MD0**2*sw**2 + (8*cw**2*gPBT**2*MD0**4*sw**2)/Lambda**2 - (16*cw**2*gPBT*gPWT*MD0**4*sw**2)/Lambda**2 + (8*cw**2*gPWT**2*MD0**4*sw**2)/Lambda**2 + (8*cw**2*gSBT**2*MD0**4*sw**2)/Lambda**2 - (16*cw**2*gSBT*gSWT*MD0**4*sw**2)/Lambda**2 + (8*cw**2*gSWT**2*MD0**4*sw**2)/Lambda**2 + 24*cw**2*gSBL*gSBT*MZ**2*sw**2 - 24*cw**2*gSBT*gSWL*MZ**2*sw**2 - 24*cw**2*gSBL*gSWT*MZ**2*sw**2 + 24*cw**2*gSWL*gSWT*MZ**2*sw**2 - (16*cw**2*gPBT**2*MD0**2*MZ**2*sw**2)/Lambda**2 + (32*cw**2*gPBT*gPWT*MD0**2*MZ**2*sw**2)/Lambda**2 - (16*cw**2*gPWT**2*MD0**2*MZ**2*sw**2)/Lambda**2 - (16*cw**2*gSBT**2*MD0**2*MZ**2*sw**2)/Lambda**2 + (32*cw**2*gSBT*gSWT*MD0**2*MZ**2*sw**2)/Lambda**2 - (16*cw**2*gSWT**2*MD0**2*MZ**2*sw**2)/Lambda**2 + (8*cw**2*gPBT**2*MZ**4*sw**2)/Lambda**2 - (16*cw**2*gPBT*gPWT*MZ**4*sw**2)/Lambda**2 + (8*cw**2*gPWT**2*MZ**4*sw**2)/Lambda**2 + (8*cw**2*gSBT**2*MZ**4*sw**2)/Lambda**2 - (16*cw**2*gSBT*gSWT*MZ**4*sw**2)/Lambda**2 + (8*cw**2*gSWT**2*MZ**4*sw**2)/Lambda**2))/(16.*cmath.pi*abs(MD0)**3)',
                                   (P.b,P.b__tilde__):'((-12*gSd33**2*MB**2 + 3*gPd33**2*MD0**2 + 3*gSd33**2*MD0**2)*cmath.sqrt(-4*MB**2*MD0**2 + MD0**4))/(16.*cmath.pi*abs(MD0)**3)',
                                   (P.c,P.c__tilde__):'((-12*gSu22**2*MC**2 + 3*gPu22**2*MD0**2 + 3*gSu22**2*MD0**2)*cmath.sqrt(-4*MC**2*MD0**2 + MD0**4))/(16.*cmath.pi*abs(MD0)**3)',
                                   (P.d,P.d__tilde__):'((-12*gSd11**2*MD**2 + 3*gPd11**2*MD0**2 + 3*gSd11**2*MD0**2)*cmath.sqrt(-4*MD**2*MD0**2 + MD0**4))/(16.*cmath.pi*abs(MD0)**3)',
                                   (P.e__minus__,P.e__plus__):'((gPe**2*MD0**2 + gSe**2*MD0**2 - 4*gSe**2*Me**2)*cmath.sqrt(MD0**4 - 4*MD0**2*Me**2))/(16.*cmath.pi*abs(MD0)**3)',
                                   (P.g,P.g):'(MD0**2*((256*gPg**2*MD0**4)/Lambda**2 + (256*gSg**2*MD0**4)/Lambda**2))/(32.*cmath.pi*abs(MD0)**3)',
                                   (P.H,P.H):'(((gSh1**2*MD0**4)/(4.*Lambda**2) - (gSh1**2*MD0**2*MH**2)/Lambda**2 - (gSh1*gSh2*MD0**2*MH**2)/Lambda**2 + (gSh1**2*MH**4)/Lambda**2 + (2*gSh1*gSh2*MH**4)/Lambda**2 + (gSh2**2*MH**4)/Lambda**2)*cmath.sqrt(MD0**4 - 4*MD0**2*MH**2))/(32.*cmath.pi*abs(MD0)**3)',
                                   (P.mu__minus__,P.mu__plus__):'((gPmm**2*MD0**2 + gSmm**2*MD0**2 - 4*gSmm**2*MMU**2)*cmath.sqrt(MD0**4 - 4*MD0**2*MMU**2))/(16.*cmath.pi*abs(MD0)**3)',
                                   (P.s,P.s__tilde__):'((3*gPd22**2*MD0**2 + 3*gSd22**2*MD0**2 - 12*gSd22**2*MS**2)*cmath.sqrt(MD0**4 - 4*MD0**2*MS**2))/(16.*cmath.pi*abs(MD0)**3)',
                                   (P.t,P.t__tilde__):'((3*gPu33**2*MD0**2 + 3*gSu33**2*MD0**2 - 12*gSu33**2*MT**2)*cmath.sqrt(MD0**4 - 4*MD0**2*MT**2))/(16.*cmath.pi*abs(MD0)**3)',
                                   (P.ta__minus__,P.ta__plus__):'((gPta**2*MD0**2 + gSta**2*MD0**2 - 4*gSta**2*MTA**2)*cmath.sqrt(MD0**4 - 4*MD0**2*MTA**2))/(16.*cmath.pi*abs(MD0)**3)',
                                   (P.u,P.u__tilde__):'((3*gPu11**2*MD0**2 + 3*gSu11**2*MD0**2 - 12*gSu11**2*MU**2)*cmath.sqrt(MD0**4 - 4*MD0**2*MU**2))/(16.*cmath.pi*abs(MD0)**3)',
                                   (P.W__minus__,P.W__plus__):'((12*gSWL**2*Lambda**2 - 24*gSWL*gSWT*MD0**2 + (8*gPWT**2*MD0**4)/Lambda**2 + (8*gSWT**2*MD0**4)/Lambda**2 + (gSWL**2*Lambda**2*MD0**4)/MW**4 - (4*gSWL**2*Lambda**2*MD0**2)/MW**2 + 48*gSWL*gSWT*MW**2 - (32*gPWT**2*MD0**2*MW**2)/Lambda**2 - (32*gSWT**2*MD0**2*MW**2)/Lambda**2 + (48*gSWT**2*MW**4)/Lambda**2 + (3*ee**2*gSh1*gSWL*vev**2)/sw**2 - (3*ee**2*gSh1*gSWT*MD0**2*vev**2)/(Lambda**2*sw**2) + (ee**2*gSh1*gSWL*MD0**4*vev**2)/(4.*MW**4*sw**2) - (ee**2*gSh1*gSWL*MD0**2*vev**2)/(MW**2*sw**2) + (6*ee**2*gSh1*gSWT*MW**2*vev**2)/(Lambda**2*sw**2) + (3*ee**4*gSh1**2*vev**4)/(16.*Lambda**2*sw**4) + (ee**4*gSh1**2*MD0**4*vev**4)/(64.*Lambda**2*MW**4*sw**4) - (ee**4*gSh1**2*MD0**2*vev**4)/(16.*Lambda**2*MW**2*sw**4))*cmath.sqrt(MD0**4 - 4*MD0**2*MW**2))/(16.*cmath.pi*abs(MD0)**3)',
                                   (P.Xc__tilde__,P.Xc):'(gSXc**2*MXc**2*cmath.sqrt(MD0**4 - 4*MD0**2*MXc**2))/(16.*cmath.pi*abs(MD0)**3)',
                                   (P.Xd,P.Xd__tilde__):'((2*gPXd**2*MD0**2 + 2*gSXd**2*MD0**2 - 8*gSXd**2*MXd**2)*cmath.sqrt(MD0**4 - 4*MD0**2*MXd**2))/(16.*cmath.pi*abs(MD0)**3)',
                                   (P.Xr,P.Xr):'(gSXr**2*Lambda**2*cmath.sqrt(MD0**4 - 4*MD0**2*MXr**2))/(32.*cmath.pi*abs(MD0)**3)',
                                   (P.Z,P.Z):'((12*cw**4*gSWL**2*Lambda**2 - 24*cw**4*gSWL*gSWT*MD0**2 + (8*cw**4*gPWT**2*MD0**4)/Lambda**2 + (8*cw**4*gSWT**2*MD0**4)/Lambda**2 + (cw**4*gSWL**2*Lambda**2*MD0**4)/MZ**4 - (4*cw**4*gSWL**2*Lambda**2*MD0**2)/MZ**2 + 48*cw**4*gSWL*gSWT*MZ**2 - (32*cw**4*gPWT**2*MD0**2*MZ**2)/Lambda**2 - (32*cw**4*gSWT**2*MD0**2*MZ**2)/Lambda**2 + (48*cw**4*gSWT**2*MZ**4)/Lambda**2 + 24*cw**2*gSBL*gSWL*Lambda**2*sw**2 - 24*cw**2*gSBT*gSWL*MD0**2*sw**2 - 24*cw**2*gSBL*gSWT*MD0**2*sw**2 + (16*cw**2*gPBT*gPWT*MD0**4*sw**2)/Lambda**2 + (16*cw**2*gSBT*gSWT*MD0**4*sw**2)/Lambda**2 + (2*cw**2*gSBL*gSWL*Lambda**2*MD0**4*sw**2)/MZ**4 - (8*cw**2*gSBL*gSWL*Lambda**2*MD0**2*sw**2)/MZ**2 + 48*cw**2*gSBT*gSWL*MZ**2*sw**2 + 48*cw**2*gSBL*gSWT*MZ**2*sw**2 - (64*cw**2*gPBT*gPWT*MD0**2*MZ**2*sw**2)/Lambda**2 - (64*cw**2*gSBT*gSWT*MD0**2*MZ**2*sw**2)/Lambda**2 + (96*cw**2*gSBT*gSWT*MZ**4*sw**2)/Lambda**2 + 12*gSBL**2*Lambda**2*sw**4 - 24*gSBL*gSBT*MD0**2*sw**4 + (8*gPBT**2*MD0**4*sw**4)/Lambda**2 + (8*gSBT**2*MD0**4*sw**4)/Lambda**2 + (gSBL**2*Lambda**2*MD0**4*sw**4)/MZ**4 - (4*gSBL**2*Lambda**2*MD0**2*sw**4)/MZ**2 + 48*gSBL*gSBT*MZ**2*sw**4 - (32*gPBT**2*MD0**2*MZ**2*sw**4)/Lambda**2 - (32*gSBT**2*MD0**2*MZ**2*sw**4)/Lambda**2 + (48*gSBT**2*MZ**4*sw**4)/Lambda**2 + 3*cw**2*ee**2*gSBL*gSh1*vev**2 + 6*cw**2*ee**2*gSh1*gSWL*vev**2 - (3*cw**2*ee**2*gSBT*gSh1*MD0**2*vev**2)/Lambda**2 - (6*cw**2*ee**2*gSh1*gSWT*MD0**2*vev**2)/Lambda**2 + (cw**2*ee**2*gSBL*gSh1*MD0**4*vev**2)/(4.*MZ**4) + (cw**2*ee**2*gSh1*gSWL*MD0**4*vev**2)/(2.*MZ**4) - (cw**2*ee**2*gSBL*gSh1*MD0**2*vev**2)/MZ**2 - (2*cw**2*ee**2*gSh1*gSWL*MD0**2*vev**2)/MZ**2 + (6*cw**2*ee**2*gSBT*gSh1*MZ**2*vev**2)/Lambda**2 + (12*cw**2*ee**2*gSh1*gSWT*MZ**2*vev**2)/Lambda**2 + (3*cw**4*ee**2*gSh1*gSWL*vev**2)/sw**2 - (3*cw**4*ee**2*gSh1*gSWT*MD0**2*vev**2)/(Lambda**2*sw**2) + (cw**4*ee**2*gSh1*gSWL*MD0**4*vev**2)/(4.*MZ**4*sw**2) - (cw**4*ee**2*gSh1*gSWL*MD0**2*vev**2)/(MZ**2*sw**2) + (6*cw**4*ee**2*gSh1*gSWT*MZ**2*vev**2)/(Lambda**2*sw**2) + 6*ee**2*gSBL*gSh1*sw**2*vev**2 + 3*ee**2*gSh1*gSWL*sw**2*vev**2 - (6*ee**2*gSBT*gSh1*MD0**2*sw**2*vev**2)/Lambda**2 - (3*ee**2*gSh1*gSWT*MD0**2*sw**2*vev**2)/Lambda**2 + (ee**2*gSBL*gSh1*MD0**4*sw**2*vev**2)/(2.*MZ**4) + (ee**2*gSh1*gSWL*MD0**4*sw**2*vev**2)/(4.*MZ**4) - (2*ee**2*gSBL*gSh1*MD0**2*sw**2*vev**2)/MZ**2 - (ee**2*gSh1*gSWL*MD0**2*sw**2*vev**2)/MZ**2 + (12*ee**2*gSBT*gSh1*MZ**2*sw**2*vev**2)/Lambda**2 + (6*ee**2*gSh1*gSWT*MZ**2*sw**2*vev**2)/Lambda**2 + (3*ee**2*gSBL*gSh1*sw**4*vev**2)/cw**2 - (3*ee**2*gSBT*gSh1*MD0**2*sw**4*vev**2)/(cw**2*Lambda**2) + (ee**2*gSBL*gSh1*MD0**4*sw**4*vev**2)/(4.*cw**2*MZ**4) - (ee**2*gSBL*gSh1*MD0**2*sw**4*vev**2)/(cw**2*MZ**2) + (6*ee**2*gSBT*gSh1*MZ**2*sw**4*vev**2)/(cw**2*Lambda**2) + (9*ee**4*gSh1**2*vev**4)/(8.*Lambda**2) + (3*ee**4*gSh1**2*MD0**4*vev**4)/(32.*Lambda**2*MZ**4) - (3*ee**4*gSh1**2*MD0**2*vev**4)/(8.*Lambda**2*MZ**2) + (3*cw**4*ee**4*gSh1**2*vev**4)/(16.*Lambda**2*sw**4) + (cw**4*ee**4*gSh1**2*MD0**4*vev**4)/(64.*Lambda**2*MZ**4*sw**4) - (cw**4*ee**4*gSh1**2*MD0**2*vev**4)/(16.*Lambda**2*MZ**2*sw**4) + (3*cw**2*ee**4*gSh1**2*vev**4)/(4.*Lambda**2*sw**2) + (cw**2*ee**4*gSh1**2*MD0**4*vev**4)/(16.*Lambda**2*MZ**4*sw**2) - (cw**2*ee**4*gSh1**2*MD0**2*vev**4)/(4.*Lambda**2*MZ**2*sw**2) + (3*ee**4*gSh1**2*sw**2*vev**4)/(4.*cw**2*Lambda**2) + (ee**4*gSh1**2*MD0**4*sw**2*vev**4)/(16.*cw**2*Lambda**2*MZ**4) - (ee**4*gSh1**2*MD0**2*sw**2*vev**4)/(4.*cw**2*Lambda**2*MZ**2) + (3*ee**4*gSh1**2*sw**4*vev**4)/(16.*cw**4*Lambda**2) + (ee**4*gSh1**2*MD0**4*sw**4*vev**4)/(64.*cw**4*Lambda**2*MZ**4) - (ee**4*gSh1**2*MD0**2*sw**4*vev**4)/(16.*cw**4*Lambda**2*MZ**2))*cmath.sqrt(MD0**4 - 4*MD0**2*MZ**2))/(32.*cmath.pi*abs(MD0)**3)'})

Decay_Y1 = Decay(name = 'Decay_Y1',
                 particle = P.Y1,
                 partial_widths = {(P.b,P.b__tilde__):'((-24*gAd33**2*MB**2 + 12*gVd33**2*MB**2 + 6*gAd33**2*MD1**2 + 6*gVd33**2*MD1**2)*cmath.sqrt(-4*MB**2*MD1**2 + MD1**4))/(48.*cmath.pi*abs(MD1)**3)',
                                   (P.c,P.c__tilde__):'((-24*gAu22**2*MC**2 + 12*gVu22**2*MC**2 + 6*gAu22**2*MD1**2 + 6*gVu22**2*MD1**2)*cmath.sqrt(-4*MC**2*MD1**2 + MD1**4))/(48.*cmath.pi*abs(MD1)**3)',
                                   (P.d,P.d__tilde__):'((-24*gAd11**2*MD**2 + 12*gVd11**2*MD**2 + 6*gAd11**2*MD1**2 + 6*gVd11**2*MD1**2)*cmath.sqrt(-4*MD**2*MD1**2 + MD1**4))/(48.*cmath.pi*abs(MD1)**3)',
                                   (P.e__minus__,P.e__plus__):'((2*gAe**2*MD1**2 + 2*gVe**2*MD1**2 - 8*gAe**2*Me**2 + 4*gVe**2*Me**2)*cmath.sqrt(MD1**4 - 4*MD1**2*Me**2))/(48.*cmath.pi*abs(MD1)**3)',
                                   (P.mu__minus__,P.mu__plus__):'((2*gAmm**2*MD1**2 + 2*gVmm**2*MD1**2 - 8*gAmm**2*MMU**2 + 4*gVmm**2*MMU**2)*cmath.sqrt(MD1**4 - 4*MD1**2*MMU**2))/(48.*cmath.pi*abs(MD1)**3)',
                                   (P.s,P.s__tilde__):'((6*gAd22**2*MD1**2 + 6*gVd22**2*MD1**2 - 24*gAd22**2*MS**2 + 12*gVd22**2*MS**2)*cmath.sqrt(MD1**4 - 4*MD1**2*MS**2))/(48.*cmath.pi*abs(MD1)**3)',
                                   (P.t,P.t__tilde__):'((6*gAu33**2*MD1**2 + 6*gVu33**2*MD1**2 - 24*gAu33**2*MT**2 + 12*gVu33**2*MT**2)*cmath.sqrt(MD1**4 - 4*MD1**2*MT**2))/(48.*cmath.pi*abs(MD1)**3)',
                                   (P.ta__minus__,P.ta__plus__):'((2*gAta**2*MD1**2 + 2*gVta**2*MD1**2 - 8*gAta**2*MTA**2 + 4*gVta**2*MTA**2)*cmath.sqrt(MD1**4 - 4*MD1**2*MTA**2))/(48.*cmath.pi*abs(MD1)**3)',
                                   (P.u,P.u__tilde__):'((6*gAu11**2*MD1**2 + 6*gVu11**2*MD1**2 - 24*gAu11**2*MU**2 + 12*gVu11**2*MU**2)*cmath.sqrt(MD1**4 - 4*MD1**2*MU**2))/(48.*cmath.pi*abs(MD1)**3)',
                                   (P.Xd,P.Xd__tilde__):'((4*gAXd**2*MD1**2 + 4*gVXd**2*MD1**2 - 16*gAXd**2*MXd**2 + 8*gVXd**2*MXd**2)*cmath.sqrt(MD1**4 - 4*MD1**2*MXd**2))/(48.*cmath.pi*abs(MD1)**3)'})

Decay_Z = Decay(name = 'Decay_Z',
                particle = P.Z,
                partial_widths = {(P.a,P.Y0):'((-MD0**2 + MZ**2)*(12*cw**2*gSBL**2*Lambda**2*sw**2 - 24*cw**2*gSBL*gSWL*Lambda**2*sw**2 + 12*cw**2*gSWL**2*Lambda**2*sw**2 + 24*cw**2*gSBL*gSBT*MD0**2*sw**2 - 24*cw**2*gSBT*gSWL*MD0**2*sw**2 - 24*cw**2*gSBL*gSWT*MD0**2*sw**2 + 24*cw**2*gSWL*gSWT*MD0**2*sw**2 + (8*cw**2*gPBT**2*MD0**4*sw**2)/Lambda**2 - (16*cw**2*gPBT*gPWT*MD0**4*sw**2)/Lambda**2 + (8*cw**2*gPWT**2*MD0**4*sw**2)/Lambda**2 + (8*cw**2*gSBT**2*MD0**4*sw**2)/Lambda**2 - (16*cw**2*gSBT*gSWT*MD0**4*sw**2)/Lambda**2 + (8*cw**2*gSWT**2*MD0**4*sw**2)/Lambda**2 - 24*cw**2*gSBL*gSBT*MZ**2*sw**2 + 24*cw**2*gSBT*gSWL*MZ**2*sw**2 + 24*cw**2*gSBL*gSWT*MZ**2*sw**2 - 24*cw**2*gSWL*gSWT*MZ**2*sw**2 - (16*cw**2*gPBT**2*MD0**2*MZ**2*sw**2)/Lambda**2 + (32*cw**2*gPBT*gPWT*MD0**2*MZ**2*sw**2)/Lambda**2 - (16*cw**2*gPWT**2*MD0**2*MZ**2*sw**2)/Lambda**2 - (16*cw**2*gSBT**2*MD0**2*MZ**2*sw**2)/Lambda**2 + (32*cw**2*gSBT*gSWT*MD0**2*MZ**2*sw**2)/Lambda**2 - (16*cw**2*gSWT**2*MD0**2*MZ**2*sw**2)/Lambda**2 + (8*cw**2*gPBT**2*MZ**4*sw**2)/Lambda**2 - (16*cw**2*gPBT*gPWT*MZ**4*sw**2)/Lambda**2 + (8*cw**2*gPWT**2*MZ**4*sw**2)/Lambda**2 + (8*cw**2*gSBT**2*MZ**4*sw**2)/Lambda**2 - (16*cw**2*gSBT*gSWT*MZ**4*sw**2)/Lambda**2 + (8*cw**2*gSWT**2*MZ**4*sw**2)/Lambda**2))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.b,P.b__tilde__):'((-7*ee**2*MB**2 + ee**2*MZ**2 - (3*cw**2*ee**2*MB**2)/(2.*sw**2) + (3*cw**2*ee**2*MZ**2)/(2.*sw**2) - (17*ee**2*MB**2*sw**2)/(6.*cw**2) + (5*ee**2*MZ**2*sw**2)/(6.*cw**2))*cmath.sqrt(-4*MB**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.c,P.c__tilde__):'((-11*ee**2*MC**2 - ee**2*MZ**2 - (3*cw**2*ee**2*MC**2)/(2.*sw**2) + (3*cw**2*ee**2*MZ**2)/(2.*sw**2) + (7*ee**2*MC**2*sw**2)/(6.*cw**2) + (17*ee**2*MZ**2*sw**2)/(6.*cw**2))*cmath.sqrt(-4*MC**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.d,P.d__tilde__):'((-7*ee**2*MD**2 + ee**2*MZ**2 - (3*cw**2*ee**2*MD**2)/(2.*sw**2) + (3*cw**2*ee**2*MZ**2)/(2.*sw**2) - (17*ee**2*MD**2*sw**2)/(6.*cw**2) + (5*ee**2*MZ**2*sw**2)/(6.*cw**2))*cmath.sqrt(-4*MD**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.e__minus__,P.e__plus__):'((-5*ee**2*Me**2 - ee**2*MZ**2 - (cw**2*ee**2*Me**2)/(2.*sw**2) + (cw**2*ee**2*MZ**2)/(2.*sw**2) + (7*ee**2*Me**2*sw**2)/(2.*cw**2) + (5*ee**2*MZ**2*sw**2)/(2.*cw**2))*cmath.sqrt(-4*Me**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.mu__minus__,P.mu__plus__):'((-5*ee**2*MMU**2 - ee**2*MZ**2 - (cw**2*ee**2*MMU**2)/(2.*sw**2) + (cw**2*ee**2*MZ**2)/(2.*sw**2) + (7*ee**2*MMU**2*sw**2)/(2.*cw**2) + (5*ee**2*MZ**2*sw**2)/(2.*cw**2))*cmath.sqrt(-4*MMU**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.s,P.s__tilde__):'((-7*ee**2*MS**2 + ee**2*MZ**2 - (3*cw**2*ee**2*MS**2)/(2.*sw**2) + (3*cw**2*ee**2*MZ**2)/(2.*sw**2) - (17*ee**2*MS**2*sw**2)/(6.*cw**2) + (5*ee**2*MZ**2*sw**2)/(6.*cw**2))*cmath.sqrt(-4*MS**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.t,P.t__tilde__):'((-11*ee**2*MT**2 - ee**2*MZ**2 - (3*cw**2*ee**2*MT**2)/(2.*sw**2) + (3*cw**2*ee**2*MZ**2)/(2.*sw**2) + (7*ee**2*MT**2*sw**2)/(6.*cw**2) + (17*ee**2*MZ**2*sw**2)/(6.*cw**2))*cmath.sqrt(-4*MT**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.ta__minus__,P.ta__plus__):'((-5*ee**2*MTA**2 - ee**2*MZ**2 - (cw**2*ee**2*MTA**2)/(2.*sw**2) + (cw**2*ee**2*MZ**2)/(2.*sw**2) + (7*ee**2*MTA**2*sw**2)/(2.*cw**2) + (5*ee**2*MZ**2*sw**2)/(2.*cw**2))*cmath.sqrt(-4*MTA**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.u,P.u__tilde__):'((-11*ee**2*MU**2 - ee**2*MZ**2 - (3*cw**2*ee**2*MU**2)/(2.*sw**2) + (3*cw**2*ee**2*MZ**2)/(2.*sw**2) + (7*ee**2*MU**2*sw**2)/(6.*cw**2) + (17*ee**2*MZ**2*sw**2)/(6.*cw**2))*cmath.sqrt(-4*MU**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.ve,P.ve__tilde__):'(MZ**2*(ee**2*MZ**2 + (cw**2*ee**2*MZ**2)/(2.*sw**2) + (ee**2*MZ**2*sw**2)/(2.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.vm,P.vm__tilde__):'(MZ**2*(ee**2*MZ**2 + (cw**2*ee**2*MZ**2)/(2.*sw**2) + (ee**2*MZ**2*sw**2)/(2.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.vt,P.vt__tilde__):'(MZ**2*(ee**2*MZ**2 + (cw**2*ee**2*MZ**2)/(2.*sw**2) + (ee**2*MZ**2*sw**2)/(2.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.W__minus__,P.W__plus__):'(((-12*cw**2*ee**2*MW**2)/sw**2 - (17*cw**2*ee**2*MZ**2)/sw**2 + (4*cw**2*ee**2*MZ**4)/(MW**2*sw**2) + (cw**2*ee**2*MZ**6)/(4.*MW**4*sw**2))*cmath.sqrt(-4*MW**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)'})


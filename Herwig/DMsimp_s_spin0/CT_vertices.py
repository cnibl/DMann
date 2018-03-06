# This file was automatically created by FeynRules 2.3.31
# Mathematica version: 11.0.0 for Mac OS X x86 (64-bit) (July 28, 2016)
# Date: Tue 6 Mar 2018 13:04:49


from object_library import all_vertices, all_CTvertices, Vertex, CTVertex
import particles as P
import CT_couplings as C
import lorentz as L


V_1 = CTVertex(name = 'V_1',
               type = 'R2',
               particles = [ P.t__tilde__, P.t, P.Y0 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS4, L.FFS6 ],
               loop_particles = [ [ [P.g, P.t] ] ],
               couplings = {(0,0,0):C.R2GC_229_69,(0,1,0):C.R2GC_230_70})

V_2 = CTVertex(name = 'V_2',
               type = 'R2',
               particles = [ P.g, P.g, P.g ],
               color = [ 'f(1,2,3)' ],
               lorentz = [ L.VVV1, L.VVV2 ],
               loop_particles = [ [ [P.b], [P.c], [P.d], [P.s], [P.t], [P.u] ], [ [P.g] ] ],
               couplings = {(0,0,0):C.R2GC_208_56,(0,1,1):C.R2GC_131_1})

V_3 = CTVertex(name = 'V_3',
               type = 'R2',
               particles = [ P.g, P.g, P.g, P.g ],
               color = [ 'd(-1,1,3)*d(-1,2,4)', 'd(-1,1,3)*f(-1,2,4)', 'd(-1,1,4)*d(-1,2,3)', 'd(-1,1,4)*f(-1,2,3)', 'd(-1,2,3)*f(-1,1,4)', 'd(-1,2,4)*f(-1,1,3)', 'f(-1,1,2)*f(-1,3,4)', 'f(-1,1,3)*f(-1,2,4)', 'f(-1,1,4)*f(-1,2,3)', 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
               lorentz = [ L.VVVV2, L.VVVV3, L.VVVV5, L.VVVV9 ],
               loop_particles = [ [ [P.b], [P.c], [P.d], [P.s], [P.t], [P.u] ], [ [P.g] ] ],
               couplings = {(2,0,0):C.R2GC_171_34,(2,0,1):C.R2GC_171_35,(0,0,0):C.R2GC_171_34,(0,0,1):C.R2GC_171_35,(4,0,0):C.R2GC_169_30,(4,0,1):C.R2GC_169_31,(3,0,0):C.R2GC_169_30,(3,0,1):C.R2GC_169_31,(8,0,0):C.R2GC_170_32,(8,0,1):C.R2GC_170_33,(7,0,0):C.R2GC_175_40,(7,0,1):C.R2GC_212_61,(5,0,0):C.R2GC_169_30,(5,0,1):C.R2GC_169_31,(1,0,0):C.R2GC_169_30,(1,0,1):C.R2GC_169_31,(6,0,0):C.R2GC_174_39,(6,0,1):C.R2GC_213_62,(11,3,0):C.R2GC_173_37,(11,3,1):C.R2GC_173_38,(10,3,0):C.R2GC_173_37,(10,3,1):C.R2GC_173_38,(9,3,1):C.R2GC_172_36,(2,1,0):C.R2GC_171_34,(2,1,1):C.R2GC_171_35,(0,1,0):C.R2GC_171_34,(0,1,1):C.R2GC_171_35,(6,1,0):C.R2GC_209_57,(6,1,1):C.R2GC_209_58,(4,1,0):C.R2GC_169_30,(4,1,1):C.R2GC_169_31,(3,1,0):C.R2GC_169_30,(3,1,1):C.R2GC_169_31,(8,1,0):C.R2GC_170_32,(8,1,1):C.R2GC_212_61,(7,1,0):C.R2GC_175_40,(7,1,1):C.R2GC_170_33,(5,1,0):C.R2GC_169_30,(5,1,1):C.R2GC_169_31,(1,1,0):C.R2GC_169_30,(1,1,1):C.R2GC_169_31,(2,2,0):C.R2GC_171_34,(2,2,1):C.R2GC_171_35,(0,2,0):C.R2GC_171_34,(0,2,1):C.R2GC_171_35,(4,2,0):C.R2GC_169_30,(4,2,1):C.R2GC_169_31,(3,2,0):C.R2GC_169_30,(3,2,1):C.R2GC_169_31,(8,2,0):C.R2GC_170_32,(8,2,1):C.R2GC_210_60,(6,2,0):C.R2GC_174_39,(7,2,0):C.R2GC_210_59,(7,2,1):C.R2GC_210_60,(5,2,0):C.R2GC_169_30,(5,2,1):C.R2GC_169_31,(1,2,0):C.R2GC_169_30,(1,2,1):C.R2GC_169_31})

V_4 = CTVertex(name = 'V_4',
               type = 'R2',
               particles = [ P.t__tilde__, P.b, P.G__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS5 ],
               loop_particles = [ [ [P.b, P.g, P.t] ] ],
               couplings = {(0,0,0):C.R2GC_225_65})

V_5 = CTVertex(name = 'V_5',
               type = 'R2',
               particles = [ P.b__tilde__, P.t, P.G__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3 ],
               loop_particles = [ [ [P.b, P.g, P.t] ] ],
               couplings = {(0,0,0):C.R2GC_226_66})

V_6 = CTVertex(name = 'V_6',
               type = 'R2',
               particles = [ P.t__tilde__, P.t, P.G0 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               loop_particles = [ [ [P.g, P.t] ] ],
               couplings = {(0,0,0):C.R2GC_227_67})

V_7 = CTVertex(name = 'V_7',
               type = 'R2',
               particles = [ P.t__tilde__, P.t, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               loop_particles = [ [ [P.g, P.t] ] ],
               couplings = {(0,0,0):C.R2GC_228_68})

V_8 = CTVertex(name = 'V_8',
               type = 'R2',
               particles = [ P.u__tilde__, P.u, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               loop_particles = [ [ [P.g, P.u] ] ],
               couplings = {(0,0,0):C.R2GC_181_44})

V_9 = CTVertex(name = 'V_9',
               type = 'R2',
               particles = [ P.c__tilde__, P.c, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               loop_particles = [ [ [P.c, P.g] ] ],
               couplings = {(0,0,0):C.R2GC_181_44})

V_10 = CTVertex(name = 'V_10',
                type = 'R2',
                particles = [ P.t__tilde__, P.t, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_181_44})

V_11 = CTVertex(name = 'V_11',
                type = 'R2',
                particles = [ P.d__tilde__, P.d, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_177_42})

V_12 = CTVertex(name = 'V_12',
                type = 'R2',
                particles = [ P.s__tilde__, P.s, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_177_42})

V_13 = CTVertex(name = 'V_13',
                type = 'R2',
                particles = [ P.b__tilde__, P.b, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_177_42})

V_14 = CTVertex(name = 'V_14',
                type = 'R2',
                particles = [ P.u__tilde__, P.u, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_179_43})

V_15 = CTVertex(name = 'V_15',
                type = 'R2',
                particles = [ P.c__tilde__, P.c, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_179_43})

V_16 = CTVertex(name = 'V_16',
                type = 'R2',
                particles = [ P.t__tilde__, P.t, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_179_43})

V_17 = CTVertex(name = 'V_17',
                type = 'R2',
                particles = [ P.d__tilde__, P.d, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_179_43})

V_18 = CTVertex(name = 'V_18',
                type = 'R2',
                particles = [ P.s__tilde__, P.s, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_179_43})

V_19 = CTVertex(name = 'V_19',
                type = 'R2',
                particles = [ P.b__tilde__, P.b, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_179_43})

V_20 = CTVertex(name = 'V_20',
                type = 'R2',
                particles = [ P.d__tilde__, P.u, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.d, P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_202_49})

V_21 = CTVertex(name = 'V_21',
                type = 'R2',
                particles = [ P.s__tilde__, P.u, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.g, P.s, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_204_51})

V_22 = CTVertex(name = 'V_22',
                type = 'R2',
                particles = [ P.d__tilde__, P.c, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.c, P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_198_45})

V_23 = CTVertex(name = 'V_23',
                type = 'R2',
                particles = [ P.s__tilde__, P.c, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.c, P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_200_47})

V_24 = CTVertex(name = 'V_24',
                type = 'R2',
                particles = [ P.b__tilde__, P.t, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.b, P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_222_63})

V_25 = CTVertex(name = 'V_25',
                type = 'R2',
                particles = [ P.u__tilde__, P.d, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.d, P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_203_50})

V_26 = CTVertex(name = 'V_26',
                type = 'R2',
                particles = [ P.c__tilde__, P.d, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.c, P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_199_46})

V_27 = CTVertex(name = 'V_27',
                type = 'R2',
                particles = [ P.u__tilde__, P.s, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.g, P.s, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_205_52})

V_28 = CTVertex(name = 'V_28',
                type = 'R2',
                particles = [ P.c__tilde__, P.s, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.c, P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_201_48})

V_29 = CTVertex(name = 'V_29',
                type = 'R2',
                particles = [ P.t__tilde__, P.b, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.b, P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_222_63})

V_30 = CTVertex(name = 'V_30',
                type = 'R2',
                particles = [ P.u__tilde__, P.u, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_152_24,(0,1,0):C.R2GC_139_9})

V_31 = CTVertex(name = 'V_31',
                type = 'R2',
                particles = [ P.c__tilde__, P.c, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_152_24,(0,1,0):C.R2GC_139_9})

V_32 = CTVertex(name = 'V_32',
                type = 'R2',
                particles = [ P.t__tilde__, P.t, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_152_24,(0,1,0):C.R2GC_139_9})

V_33 = CTVertex(name = 'V_33',
                type = 'R2',
                particles = [ P.d__tilde__, P.d, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_151_23,(0,1,0):C.R2GC_138_8})

V_34 = CTVertex(name = 'V_34',
                type = 'R2',
                particles = [ P.s__tilde__, P.s, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_151_23,(0,1,0):C.R2GC_138_8})

V_35 = CTVertex(name = 'V_35',
                type = 'R2',
                particles = [ P.b__tilde__, P.b, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_151_23,(0,1,0):C.R2GC_138_8})

V_36 = CTVertex(name = 'V_36',
                type = 'R2',
                particles = [ P.u__tilde__, P.u ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_176_41})

V_37 = CTVertex(name = 'V_37',
                type = 'R2',
                particles = [ P.c__tilde__, P.c ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_176_41})

V_38 = CTVertex(name = 'V_38',
                type = 'R2',
                particles = [ P.t__tilde__, P.t ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF2, L.FF3, L.FF4, L.FF5 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_224_64,(0,2,0):C.R2GC_224_64,(0,1,0):C.R2GC_176_41,(0,3,0):C.R2GC_176_41})

V_39 = CTVertex(name = 'V_39',
                type = 'R2',
                particles = [ P.d__tilde__, P.d ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_176_41})

V_40 = CTVertex(name = 'V_40',
                type = 'R2',
                particles = [ P.s__tilde__, P.s ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_176_41})

V_41 = CTVertex(name = 'V_41',
                type = 'R2',
                particles = [ P.b__tilde__, P.b ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_176_41})

V_42 = CTVertex(name = 'V_42',
                type = 'R2',
                particles = [ P.g, P.g ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VV1, L.VV2, L.VV3 ],
                loop_particles = [ [ [P.b], [P.c], [P.d], [P.s], [P.t], [P.u] ], [ [P.g] ], [ [P.t] ] ],
                couplings = {(0,0,1):C.R2GC_207_55,(0,1,2):C.R2GC_132_2,(0,2,0):C.R2GC_206_53,(0,2,1):C.R2GC_206_54})

V_43 = CTVertex(name = 'V_43',
                type = 'R2',
                particles = [ P.g, P.g, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVS2 ],
                loop_particles = [ [ [P.t] ] ],
                couplings = {(0,0,0):C.R2GC_133_3})

V_44 = CTVertex(name = 'V_44',
                type = 'R2',
                particles = [ P.g, P.g, P.Y0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVS2 ],
                loop_particles = [ [ [P.t] ] ],
                couplings = {(0,0,0):C.R2GC_134_4})

V_45 = CTVertex(name = 'V_45',
                type = 'R2',
                particles = [ P.g, P.g, P.W__minus__, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVVV2, L.VVVV3, L.VVVV5 ],
                loop_particles = [ [ [P.b, P.t] ], [ [P.c, P.d] ], [ [P.c, P.s] ], [ [P.d, P.u] ], [ [P.s, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_156_25,(0,0,1):C.R2GC_156_26,(0,0,2):C.R2GC_156_27,(0,0,3):C.R2GC_156_28,(0,0,4):C.R2GC_156_29,(0,1,0):C.R2GC_156_25,(0,1,1):C.R2GC_156_26,(0,1,2):C.R2GC_156_27,(0,1,3):C.R2GC_156_28,(0,1,4):C.R2GC_156_29,(0,2,0):C.R2GC_156_25,(0,2,1):C.R2GC_156_26,(0,2,2):C.R2GC_156_27,(0,2,3):C.R2GC_156_28,(0,2,4):C.R2GC_156_29})

V_46 = CTVertex(name = 'V_46',
                type = 'R2',
                particles = [ P.a, P.g, P.g, P.Z ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.VVVV2, L.VVVV3, L.VVVV5 ],
                loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_147_15,(0,0,1):C.R2GC_147_16,(0,1,0):C.R2GC_147_15,(0,1,1):C.R2GC_147_16,(0,2,0):C.R2GC_147_15,(0,2,1):C.R2GC_147_16})

V_47 = CTVertex(name = 'V_47',
                type = 'R2',
                particles = [ P.g, P.g, P.Z, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVVV2, L.VVVV3, L.VVVV5 ],
                loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_150_21,(0,0,1):C.R2GC_150_22,(0,1,0):C.R2GC_150_21,(0,1,1):C.R2GC_150_22,(0,2,0):C.R2GC_150_21,(0,2,1):C.R2GC_150_22})

V_48 = CTVertex(name = 'V_48',
                type = 'R2',
                particles = [ P.a, P.a, P.g, P.g ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.VVVV2, L.VVVV3, L.VVVV5 ],
                loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_145_11,(0,0,1):C.R2GC_145_12,(0,1,0):C.R2GC_145_11,(0,1,1):C.R2GC_145_12,(0,2,0):C.R2GC_145_11,(0,2,1):C.R2GC_145_12})

V_49 = CTVertex(name = 'V_49',
                type = 'R2',
                particles = [ P.g, P.g, P.g, P.Z ],
                color = [ 'd(1,2,3)', 'f(1,2,3)' ],
                lorentz = [ L.VVVV1, L.VVVV2, L.VVVV3, L.VVVV5 ],
                loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                couplings = {(1,0,0):C.R2GC_149_19,(1,0,1):C.R2GC_149_20,(0,1,0):C.R2GC_148_17,(0,1,1):C.R2GC_148_18,(0,2,0):C.R2GC_148_17,(0,2,1):C.R2GC_148_18,(0,3,0):C.R2GC_148_17,(0,3,1):C.R2GC_148_18})

V_50 = CTVertex(name = 'V_50',
                type = 'R2',
                particles = [ P.a, P.g, P.g, P.g ],
                color = [ 'd(2,3,4)' ],
                lorentz = [ L.VVVV2, L.VVVV3, L.VVVV5 ],
                loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_146_13,(0,0,1):C.R2GC_146_14,(0,1,0):C.R2GC_146_13,(0,1,1):C.R2GC_146_14,(0,2,0):C.R2GC_146_13,(0,2,1):C.R2GC_146_14})

V_51 = CTVertex(name = 'V_51',
                type = 'R2',
                particles = [ P.g, P.g, P.H, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.t] ] ],
                couplings = {(0,0,0):C.R2GC_135_5})

V_52 = CTVertex(name = 'V_52',
                type = 'R2',
                particles = [ P.g, P.g, P.G0, P.G0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.t] ] ],
                couplings = {(0,0,0):C.R2GC_135_5})

V_53 = CTVertex(name = 'V_53',
                type = 'R2',
                particles = [ P.g, P.g, P.G__minus__, P.G__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.b, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_135_5})

V_54 = CTVertex(name = 'V_54',
                type = 'R2',
                particles = [ P.g, P.g, P.H, P.Y0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.t] ] ],
                couplings = {(0,0,0):C.R2GC_137_7})

V_55 = CTVertex(name = 'V_55',
                type = 'R2',
                particles = [ P.g, P.g, P.G0, P.Y0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.t] ] ],
                couplings = {(0,0,0):C.R2GC_136_6})

V_56 = CTVertex(name = 'V_56',
                type = 'R2',
                particles = [ P.g, P.g, P.Y0, P.Y0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.t] ] ],
                couplings = {(0,0,0):C.R2GC_144_10})

V_57 = CTVertex(name = 'V_57',
                type = 'UV',
                particles = [ P.t__tilde__, P.t, P.Y0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS4, L.FFS6 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_229_84,(0,1,0):C.UVGC_230_85})

V_58 = CTVertex(name = 'V_58',
                type = 'UV',
                particles = [ P.g, P.g, P.g ],
                color = [ 'f(1,2,3)' ],
                lorentz = [ L.VVV1, L.VVV3, L.VVV4 ],
                loop_particles = [ [ [P.b], [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.t] ] ],
                couplings = {(0,0,0):C.UVGC_208_45,(0,0,3):C.UVGC_208_46,(0,1,1):C.UVGC_157_1,(0,2,2):C.UVGC_158_2})

V_59 = CTVertex(name = 'V_59',
                type = 'UV',
                particles = [ P.g, P.g, P.g, P.g ],
                color = [ 'd(-1,1,3)*d(-1,2,4)', 'd(-1,1,3)*f(-1,2,4)', 'd(-1,1,4)*d(-1,2,3)', 'd(-1,1,4)*f(-1,2,3)', 'd(-1,2,3)*f(-1,1,4)', 'd(-1,2,4)*f(-1,1,3)', 'f(-1,1,2)*f(-1,3,4)', 'f(-1,1,3)*f(-1,2,4)', 'f(-1,1,4)*f(-1,2,3)', 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.VVVV2, L.VVVV3, L.VVVV5, L.VVVV9 ],
                loop_particles = [ [ [P.b], [P.c], [P.d], [P.s], [P.t], [P.u] ], [ [P.b], [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.t] ] ],
                couplings = {(2,0,2):C.UVGC_170_9,(2,0,3):C.UVGC_170_8,(0,0,2):C.UVGC_170_9,(0,0,3):C.UVGC_170_8,(4,0,2):C.UVGC_169_6,(4,0,3):C.UVGC_169_7,(3,0,2):C.UVGC_169_6,(3,0,3):C.UVGC_169_7,(8,0,2):C.UVGC_170_8,(8,0,3):C.UVGC_170_9,(7,0,1):C.UVGC_212_55,(7,0,2):C.UVGC_212_56,(7,0,3):C.UVGC_212_57,(7,0,4):C.UVGC_212_58,(5,0,2):C.UVGC_169_6,(5,0,3):C.UVGC_169_7,(1,0,2):C.UVGC_169_6,(1,0,3):C.UVGC_169_7,(6,0,1):C.UVGC_212_55,(6,0,2):C.UVGC_213_59,(6,0,3):C.UVGC_213_60,(6,0,4):C.UVGC_212_58,(11,3,2):C.UVGC_173_12,(11,3,3):C.UVGC_173_13,(10,3,2):C.UVGC_173_12,(10,3,3):C.UVGC_173_13,(9,3,2):C.UVGC_172_10,(9,3,3):C.UVGC_172_11,(2,1,2):C.UVGC_170_9,(2,1,3):C.UVGC_170_8,(0,1,2):C.UVGC_170_9,(0,1,3):C.UVGC_170_8,(6,1,2):C.UVGC_209_47,(6,1,3):C.UVGC_209_48,(6,1,4):C.UVGC_209_49,(4,1,2):C.UVGC_169_6,(4,1,3):C.UVGC_169_7,(3,1,2):C.UVGC_169_6,(3,1,3):C.UVGC_169_7,(8,1,1):C.UVGC_214_61,(8,1,2):C.UVGC_212_56,(8,1,3):C.UVGC_214_62,(8,1,4):C.UVGC_214_63,(7,1,0):C.UVGC_174_14,(7,1,2):C.UVGC_170_8,(7,1,3):C.UVGC_175_15,(5,1,2):C.UVGC_169_6,(5,1,3):C.UVGC_169_7,(1,1,2):C.UVGC_169_6,(1,1,3):C.UVGC_169_7,(2,2,2):C.UVGC_170_9,(2,2,3):C.UVGC_170_8,(0,2,2):C.UVGC_170_9,(0,2,3):C.UVGC_170_8,(4,2,2):C.UVGC_169_6,(4,2,3):C.UVGC_169_7,(3,2,2):C.UVGC_169_6,(3,2,3):C.UVGC_169_7,(8,2,1):C.UVGC_211_52,(8,2,2):C.UVGC_210_50,(8,2,3):C.UVGC_211_53,(8,2,4):C.UVGC_211_54,(6,2,0):C.UVGC_174_14,(6,2,3):C.UVGC_172_10,(7,2,2):C.UVGC_210_50,(7,2,3):C.UVGC_210_51,(7,2,4):C.UVGC_209_49,(5,2,2):C.UVGC_169_6,(5,2,3):C.UVGC_169_7,(1,2,2):C.UVGC_169_6,(1,2,3):C.UVGC_169_7})

V_60 = CTVertex(name = 'V_60',
                type = 'UV',
                particles = [ P.t__tilde__, P.b, P.G__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS5 ],
                loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.t] ], [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_225_76,(0,0,2):C.UVGC_225_77,(0,0,1):C.UVGC_225_78})

V_61 = CTVertex(name = 'V_61',
                type = 'UV',
                particles = [ P.b__tilde__, P.t, P.G__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.t] ], [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_226_79,(0,0,2):C.UVGC_226_80,(0,0,1):C.UVGC_226_81})

V_62 = CTVertex(name = 'V_62',
                type = 'UV',
                particles = [ P.t__tilde__, P.t, P.G0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS1 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_227_82})

V_63 = CTVertex(name = 'V_63',
                type = 'UV',
                particles = [ P.t__tilde__, P.t, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_228_83})

V_64 = CTVertex(name = 'V_64',
                type = 'UV',
                particles = [ P.u__tilde__, P.u, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.UVGC_181_24,(0,1,0):C.UVGC_162_5,(0,2,0):C.UVGC_162_5})

V_65 = CTVertex(name = 'V_65',
                type = 'UV',
                particles = [ P.c__tilde__, P.c, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_181_24,(0,1,0):C.UVGC_162_5,(0,2,0):C.UVGC_162_5})

V_66 = CTVertex(name = 'V_66',
                type = 'UV',
                particles = [ P.t__tilde__, P.t, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_181_24,(0,1,0):C.UVGC_220_69,(0,2,0):C.UVGC_216_65})

V_67 = CTVertex(name = 'V_67',
                type = 'UV',
                particles = [ P.d__tilde__, P.d, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_177_17,(0,1,0):C.UVGC_160_4,(0,2,0):C.UVGC_160_4})

V_68 = CTVertex(name = 'V_68',
                type = 'UV',
                particles = [ P.s__tilde__, P.s, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.UVGC_177_17,(0,1,0):C.UVGC_160_4,(0,2,0):C.UVGC_160_4})

V_69 = CTVertex(name = 'V_69',
                type = 'UV',
                particles = [ P.b__tilde__, P.b, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_177_17,(0,1,0):C.UVGC_160_4,(0,2,0):C.UVGC_160_4})

V_70 = CTVertex(name = 'V_70',
                type = 'UV',
                particles = [ P.u__tilde__, P.u, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.b], [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.u] ], [ [P.t] ] ],
                couplings = {(0,0,3):C.UVGC_179_23,(0,1,0):C.UVGC_178_18,(0,1,1):C.UVGC_178_19,(0,1,2):C.UVGC_178_20,(0,1,4):C.UVGC_178_21,(0,1,3):C.UVGC_178_22,(0,2,0):C.UVGC_178_18,(0,2,1):C.UVGC_178_19,(0,2,2):C.UVGC_178_20,(0,2,4):C.UVGC_178_21,(0,2,3):C.UVGC_178_22})

V_71 = CTVertex(name = 'V_71',
                type = 'UV',
                particles = [ P.c__tilde__, P.c, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.b], [P.c], [P.d], [P.s], [P.u] ], [ [P.c, P.g] ], [ [P.g] ], [ [P.ghG] ], [ [P.t] ] ],
                couplings = {(0,0,1):C.UVGC_179_23,(0,1,0):C.UVGC_178_18,(0,1,2):C.UVGC_178_19,(0,1,3):C.UVGC_178_20,(0,1,4):C.UVGC_178_21,(0,1,1):C.UVGC_178_22,(0,2,0):C.UVGC_178_18,(0,2,2):C.UVGC_178_19,(0,2,3):C.UVGC_178_20,(0,2,4):C.UVGC_178_21,(0,2,1):C.UVGC_178_22})

V_72 = CTVertex(name = 'V_72',
                type = 'UV',
                particles = [ P.t__tilde__, P.t, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.b], [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.t] ], [ [P.t] ] ],
                couplings = {(0,0,3):C.UVGC_179_23,(0,1,0):C.UVGC_178_18,(0,1,1):C.UVGC_178_19,(0,1,2):C.UVGC_178_20,(0,1,4):C.UVGC_178_21,(0,1,3):C.UVGC_221_70,(0,2,0):C.UVGC_178_18,(0,2,1):C.UVGC_178_19,(0,2,2):C.UVGC_178_20,(0,2,4):C.UVGC_178_21,(0,2,3):C.UVGC_217_66})

V_73 = CTVertex(name = 'V_73',
                type = 'UV',
                particles = [ P.d__tilde__, P.d, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.b], [P.c], [P.d], [P.s], [P.u] ], [ [P.d, P.g] ], [ [P.g] ], [ [P.ghG] ], [ [P.t] ] ],
                couplings = {(0,0,1):C.UVGC_179_23,(0,1,0):C.UVGC_178_18,(0,1,2):C.UVGC_178_19,(0,1,3):C.UVGC_178_20,(0,1,4):C.UVGC_178_21,(0,1,1):C.UVGC_178_22,(0,2,0):C.UVGC_178_18,(0,2,2):C.UVGC_178_19,(0,2,3):C.UVGC_178_20,(0,2,4):C.UVGC_178_21,(0,2,1):C.UVGC_178_22})

V_74 = CTVertex(name = 'V_74',
                type = 'UV',
                particles = [ P.s__tilde__, P.s, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.b], [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.s] ], [ [P.t] ] ],
                couplings = {(0,0,3):C.UVGC_179_23,(0,1,0):C.UVGC_178_18,(0,1,1):C.UVGC_178_19,(0,1,2):C.UVGC_178_20,(0,1,4):C.UVGC_178_21,(0,1,3):C.UVGC_178_22,(0,2,0):C.UVGC_178_18,(0,2,1):C.UVGC_178_19,(0,2,2):C.UVGC_178_20,(0,2,4):C.UVGC_178_21,(0,2,3):C.UVGC_178_22})

V_75 = CTVertex(name = 'V_75',
                type = 'UV',
                particles = [ P.b__tilde__, P.b, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.b], [P.c], [P.d], [P.s], [P.u] ], [ [P.b, P.g] ], [ [P.g] ], [ [P.ghG] ], [ [P.t] ] ],
                couplings = {(0,0,1):C.UVGC_179_23,(0,1,0):C.UVGC_178_18,(0,1,2):C.UVGC_178_19,(0,1,3):C.UVGC_178_20,(0,1,4):C.UVGC_178_21,(0,1,1):C.UVGC_178_22,(0,2,0):C.UVGC_178_18,(0,2,2):C.UVGC_178_19,(0,2,3):C.UVGC_178_20,(0,2,4):C.UVGC_178_21,(0,2,1):C.UVGC_178_22})

V_76 = CTVertex(name = 'V_76',
                type = 'UV',
                particles = [ P.d__tilde__, P.u, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.d, P.g], [P.g, P.u] ], [ [P.d, P.g, P.u] ] ],
                couplings = {(0,0,0):C.UVGC_202_33,(0,0,1):C.UVGC_202_34})

V_77 = CTVertex(name = 'V_77',
                type = 'UV',
                particles = [ P.s__tilde__, P.u, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.g, P.s], [P.g, P.u] ], [ [P.g, P.s, P.u] ] ],
                couplings = {(0,0,0):C.UVGC_204_37,(0,0,1):C.UVGC_204_38})

V_78 = CTVertex(name = 'V_78',
                type = 'UV',
                particles = [ P.d__tilde__, P.c, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.c, P.d, P.g] ], [ [P.c, P.g], [P.d, P.g] ] ],
                couplings = {(0,0,1):C.UVGC_198_25,(0,0,0):C.UVGC_198_26})

V_79 = CTVertex(name = 'V_79',
                type = 'UV',
                particles = [ P.s__tilde__, P.c, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.c, P.g], [P.g, P.s] ], [ [P.c, P.g, P.s] ] ],
                couplings = {(0,0,0):C.UVGC_200_29,(0,0,1):C.UVGC_200_30})

V_80 = CTVertex(name = 'V_80',
                type = 'UV',
                particles = [ P.b__tilde__, P.t, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.t] ], [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_222_71,(0,0,2):C.UVGC_222_72,(0,0,1):C.UVGC_222_73})

V_81 = CTVertex(name = 'V_81',
                type = 'UV',
                particles = [ P.u__tilde__, P.d, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.d, P.g], [P.g, P.u] ], [ [P.d, P.g, P.u] ] ],
                couplings = {(0,0,0):C.UVGC_203_35,(0,0,1):C.UVGC_203_36})

V_82 = CTVertex(name = 'V_82',
                type = 'UV',
                particles = [ P.c__tilde__, P.d, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.c, P.d, P.g] ], [ [P.c, P.g], [P.d, P.g] ] ],
                couplings = {(0,0,1):C.UVGC_199_27,(0,0,0):C.UVGC_199_28})

V_83 = CTVertex(name = 'V_83',
                type = 'UV',
                particles = [ P.u__tilde__, P.s, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.g, P.s], [P.g, P.u] ], [ [P.g, P.s, P.u] ] ],
                couplings = {(0,0,0):C.UVGC_205_39,(0,0,1):C.UVGC_205_40})

V_84 = CTVertex(name = 'V_84',
                type = 'UV',
                particles = [ P.c__tilde__, P.s, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.c, P.g], [P.g, P.s] ], [ [P.c, P.g, P.s] ] ],
                couplings = {(0,0,0):C.UVGC_201_31,(0,0,1):C.UVGC_201_32})

V_85 = CTVertex(name = 'V_85',
                type = 'UV',
                particles = [ P.t__tilde__, P.b, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.t] ], [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_222_71,(0,0,2):C.UVGC_222_72,(0,0,1):C.UVGC_222_73})

V_86 = CTVertex(name = 'V_86',
                type = 'UV',
                particles = [ P.t__tilde__, P.t, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_223_74,(0,1,0):C.UVGC_218_67})

V_87 = CTVertex(name = 'V_87',
                type = 'UV',
                particles = [ P.u__tilde__, P.u ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1, L.FF3, L.FF5 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.UVGC_176_16,(0,1,0):C.UVGC_159_3,(0,2,0):C.UVGC_159_3})

V_88 = CTVertex(name = 'V_88',
                type = 'UV',
                particles = [ P.c__tilde__, P.c ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1, L.FF3, L.FF5 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_176_16,(0,1,0):C.UVGC_159_3,(0,2,0):C.UVGC_159_3})

V_89 = CTVertex(name = 'V_89',
                type = 'UV',
                particles = [ P.t__tilde__, P.t ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF2, L.FF3, L.FF4, L.FF5 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_224_75,(0,2,0):C.UVGC_224_75,(0,1,0):C.UVGC_219_68,(0,3,0):C.UVGC_215_64})

V_90 = CTVertex(name = 'V_90',
                type = 'UV',
                particles = [ P.d__tilde__, P.d ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1, L.FF3, L.FF5 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_176_16,(0,1,0):C.UVGC_159_3,(0,2,0):C.UVGC_159_3})

V_91 = CTVertex(name = 'V_91',
                type = 'UV',
                particles = [ P.s__tilde__, P.s ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1, L.FF3, L.FF5 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.UVGC_176_16,(0,1,0):C.UVGC_159_3,(0,2,0):C.UVGC_159_3})

V_92 = CTVertex(name = 'V_92',
                type = 'UV',
                particles = [ P.b__tilde__, P.b ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1, L.FF3, L.FF5 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_176_16,(0,1,0):C.UVGC_159_3,(0,2,0):C.UVGC_159_3})

V_93 = CTVertex(name = 'V_93',
                type = 'UV',
                particles = [ P.g, P.g ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VV1, L.VV3 ],
                loop_particles = [ [ [P.g] ], [ [P.ghG] ], [ [P.t] ] ],
                couplings = {(0,0,0):C.UVGC_207_42,(0,0,1):C.UVGC_207_43,(0,0,2):C.UVGC_207_44,(0,1,2):C.UVGC_206_41})


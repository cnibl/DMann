# This file was automatically created by FeynRules 2.3.31
# Mathematica version: 11.0.0 for Mac OS X x86 (64-bit) (July 28, 2016)
# Date: Tue 6 Mar 2018 17:06:35


from object_library import all_vertices, all_CTvertices, Vertex, CTVertex
import particles as P
import CT_couplings as C
import lorentz as L


V_1 = CTVertex(name = 'V_1',
               type = 'R2',
               particles = [ P.b__tilde__, P.b, P.Y0 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               loop_particles = [ [ [P.b, P.g] ] ],
               couplings = {(0,0,0):C.R2GC_137_42})

V_2 = CTVertex(name = 'V_2',
               type = 'R2',
               particles = [ P.c__tilde__, P.c, P.Y0 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               loop_particles = [ [ [P.c, P.g] ] ],
               couplings = {(0,0,0):C.R2GC_142_44})

V_3 = CTVertex(name = 'V_3',
               type = 'R2',
               particles = [ P.d__tilde__, P.d, P.Y0 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               loop_particles = [ [ [P.d, P.g] ] ],
               couplings = {(0,0,0):C.R2GC_147_45})

V_4 = CTVertex(name = 'V_4',
               type = 'R2',
               particles = [ P.s__tilde__, P.s, P.Y0 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               loop_particles = [ [ [P.g, P.s] ] ],
               couplings = {(0,0,0):C.R2GC_152_46})

V_5 = CTVertex(name = 'V_5',
               type = 'R2',
               particles = [ P.t__tilde__, P.t, P.Y0 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               loop_particles = [ [ [P.g, P.t] ] ],
               couplings = {(0,0,0):C.R2GC_189_74})

V_6 = CTVertex(name = 'V_6',
               type = 'R2',
               particles = [ P.u__tilde__, P.u, P.Y0 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               loop_particles = [ [ [P.g, P.u] ] ],
               couplings = {(0,0,0):C.R2GC_159_47})

V_7 = CTVertex(name = 'V_7',
               type = 'R2',
               particles = [ P.g, P.g, P.g ],
               color = [ 'f(1,2,3)' ],
               lorentz = [ L.VVV1, L.VVV2, L.VVV3, L.VVV4, L.VVV5, L.VVV6, L.VVV8, L.VVV9 ],
               loop_particles = [ [ [P.b], [P.c], [P.d], [P.s], [P.t], [P.u] ], [ [P.g] ] ],
               couplings = {(0,0,0):C.R2GC_170_59,(0,0,1):C.R2GC_172_62,(0,1,0):C.R2GC_173_63,(0,1,1):C.R2GC_173_64,(0,3,0):C.R2GC_173_63,(0,3,1):C.R2GC_175_66,(0,5,0):C.R2GC_170_59,(0,5,1):C.R2GC_171_61,(0,6,0):C.R2GC_170_59,(0,6,1):C.R2GC_170_60,(0,7,0):C.R2GC_173_63,(0,7,1):C.R2GC_174_65,(0,2,1):C.R2GC_125_27,(0,4,1):C.R2GC_124_26})

V_8 = CTVertex(name = 'V_8',
               type = 'R2',
               particles = [ P.g, P.g, P.g, P.g ],
               color = [ 'd(-1,1,3)*d(-1,2,4)', 'd(-1,1,3)*f(-1,2,4)', 'd(-1,1,4)*d(-1,2,3)', 'd(-1,1,4)*f(-1,2,3)', 'd(-1,2,3)*f(-1,1,4)', 'd(-1,2,4)*f(-1,1,3)', 'f(-1,1,2)*f(-1,3,4)', 'f(-1,1,3)*f(-1,2,4)', 'f(-1,1,4)*f(-1,2,3)', 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
               lorentz = [ L.VVVV2, L.VVVV3, L.VVVV4 ],
               loop_particles = [ [ [P.b], [P.c], [P.d], [P.s], [P.t], [P.u] ], [ [P.g] ] ],
               couplings = {(2,0,0):C.R2GC_128_32,(2,0,1):C.R2GC_128_33,(0,0,0):C.R2GC_128_32,(0,0,1):C.R2GC_128_33,(4,0,0):C.R2GC_126_28,(4,0,1):C.R2GC_126_29,(3,0,0):C.R2GC_126_28,(3,0,1):C.R2GC_126_29,(8,0,0):C.R2GC_127_30,(8,0,1):C.R2GC_127_31,(7,0,0):C.R2GC_132_38,(7,0,1):C.R2GC_179_71,(5,0,0):C.R2GC_126_28,(5,0,1):C.R2GC_126_29,(1,0,0):C.R2GC_126_28,(1,0,1):C.R2GC_126_29,(6,0,0):C.R2GC_131_37,(6,0,1):C.R2GC_180_72,(11,0,0):C.R2GC_130_35,(11,0,1):C.R2GC_130_36,(10,0,0):C.R2GC_130_35,(10,0,1):C.R2GC_130_36,(9,0,1):C.R2GC_129_34,(2,1,0):C.R2GC_128_32,(2,1,1):C.R2GC_128_33,(0,1,0):C.R2GC_128_32,(0,1,1):C.R2GC_128_33,(6,1,0):C.R2GC_176_67,(6,1,1):C.R2GC_176_68,(4,1,0):C.R2GC_126_28,(4,1,1):C.R2GC_126_29,(3,1,0):C.R2GC_126_28,(3,1,1):C.R2GC_126_29,(8,1,0):C.R2GC_127_30,(8,1,1):C.R2GC_179_71,(7,1,0):C.R2GC_132_38,(7,1,1):C.R2GC_127_31,(5,1,0):C.R2GC_126_28,(5,1,1):C.R2GC_126_29,(1,1,0):C.R2GC_126_28,(1,1,1):C.R2GC_126_29,(11,1,0):C.R2GC_130_35,(11,1,1):C.R2GC_130_36,(10,1,0):C.R2GC_130_35,(10,1,1):C.R2GC_130_36,(9,1,1):C.R2GC_129_34,(2,2,0):C.R2GC_128_32,(2,2,1):C.R2GC_128_33,(0,2,0):C.R2GC_128_32,(0,2,1):C.R2GC_128_33,(4,2,0):C.R2GC_126_28,(4,2,1):C.R2GC_126_29,(3,2,0):C.R2GC_126_28,(3,2,1):C.R2GC_126_29,(8,2,0):C.R2GC_127_30,(8,2,1):C.R2GC_177_70,(6,2,0):C.R2GC_131_37,(7,2,0):C.R2GC_177_69,(7,2,1):C.R2GC_177_70,(5,2,0):C.R2GC_126_28,(5,2,1):C.R2GC_126_29,(1,2,0):C.R2GC_126_28,(1,2,1):C.R2GC_126_29,(11,2,0):C.R2GC_130_35,(11,2,1):C.R2GC_130_36,(10,2,0):C.R2GC_130_35,(10,2,1):C.R2GC_130_36,(9,2,1):C.R2GC_129_34})

V_9 = CTVertex(name = 'V_9',
               type = 'R2',
               particles = [ P.t__tilde__, P.b, P.G__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS4 ],
               loop_particles = [ [ [P.b, P.g, P.t] ] ],
               couplings = {(0,0,0):C.R2GC_193_77})

V_10 = CTVertex(name = 'V_10',
                type = 'R2',
                particles = [ P.b__tilde__, P.t, P.G__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.b, P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_194_78})

V_11 = CTVertex(name = 'V_11',
                type = 'R2',
                particles = [ P.t__tilde__, P.t, P.G0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS1 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_195_79})

V_12 = CTVertex(name = 'V_12',
                type = 'R2',
                particles = [ P.t__tilde__, P.t, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_196_80})

V_13 = CTVertex(name = 'V_13',
                type = 'R2',
                particles = [ P.u__tilde__, P.u, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_139_43})

V_14 = CTVertex(name = 'V_14',
                type = 'R2',
                particles = [ P.c__tilde__, P.c, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_139_43})

V_15 = CTVertex(name = 'V_15',
                type = 'R2',
                particles = [ P.t__tilde__, P.t, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_139_43})

V_16 = CTVertex(name = 'V_16',
                type = 'R2',
                particles = [ P.d__tilde__, P.d, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_134_40})

V_17 = CTVertex(name = 'V_17',
                type = 'R2',
                particles = [ P.s__tilde__, P.s, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_134_40})

V_18 = CTVertex(name = 'V_18',
                type = 'R2',
                particles = [ P.b__tilde__, P.b, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_134_40})

V_19 = CTVertex(name = 'V_19',
                type = 'R2',
                particles = [ P.u__tilde__, P.u, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_136_41})

V_20 = CTVertex(name = 'V_20',
                type = 'R2',
                particles = [ P.c__tilde__, P.c, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_136_41})

V_21 = CTVertex(name = 'V_21',
                type = 'R2',
                particles = [ P.t__tilde__, P.t, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_136_41})

V_22 = CTVertex(name = 'V_22',
                type = 'R2',
                particles = [ P.d__tilde__, P.d, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_136_41})

V_23 = CTVertex(name = 'V_23',
                type = 'R2',
                particles = [ P.s__tilde__, P.s, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_136_41})

V_24 = CTVertex(name = 'V_24',
                type = 'R2',
                particles = [ P.b__tilde__, P.b, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_136_41})

V_25 = CTVertex(name = 'V_25',
                type = 'R2',
                particles = [ P.d__tilde__, P.u, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.d, P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_164_52})

V_26 = CTVertex(name = 'V_26',
                type = 'R2',
                particles = [ P.s__tilde__, P.u, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.g, P.s, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_166_54})

V_27 = CTVertex(name = 'V_27',
                type = 'R2',
                particles = [ P.d__tilde__, P.c, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.c, P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_160_48})

V_28 = CTVertex(name = 'V_28',
                type = 'R2',
                particles = [ P.s__tilde__, P.c, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.c, P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_162_50})

V_29 = CTVertex(name = 'V_29',
                type = 'R2',
                particles = [ P.b__tilde__, P.t, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.b, P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_190_75})

V_30 = CTVertex(name = 'V_30',
                type = 'R2',
                particles = [ P.u__tilde__, P.d, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.d, P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_165_53})

V_31 = CTVertex(name = 'V_31',
                type = 'R2',
                particles = [ P.c__tilde__, P.d, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.c, P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_161_49})

V_32 = CTVertex(name = 'V_32',
                type = 'R2',
                particles = [ P.u__tilde__, P.s, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.g, P.s, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_167_55})

V_33 = CTVertex(name = 'V_33',
                type = 'R2',
                particles = [ P.c__tilde__, P.s, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.c, P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_163_51})

V_34 = CTVertex(name = 'V_34',
                type = 'R2',
                particles = [ P.t__tilde__, P.b, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.b, P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_190_75})

V_35 = CTVertex(name = 'V_35',
                type = 'R2',
                particles = [ P.u__tilde__, P.u, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_108_20,(0,1,0):C.R2GC_185_73})

V_36 = CTVertex(name = 'V_36',
                type = 'R2',
                particles = [ P.c__tilde__, P.c, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_108_20,(0,1,0):C.R2GC_185_73})

V_37 = CTVertex(name = 'V_37',
                type = 'R2',
                particles = [ P.t__tilde__, P.t, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_108_20,(0,1,0):C.R2GC_185_73})

V_38 = CTVertex(name = 'V_38',
                type = 'R2',
                particles = [ P.d__tilde__, P.d, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_107_19,(0,1,0):C.R2GC_94_86})

V_39 = CTVertex(name = 'V_39',
                type = 'R2',
                particles = [ P.s__tilde__, P.s, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_107_19,(0,1,0):C.R2GC_94_86})

V_40 = CTVertex(name = 'V_40',
                type = 'R2',
                particles = [ P.b__tilde__, P.b, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_107_19,(0,1,0):C.R2GC_94_86})

V_41 = CTVertex(name = 'V_41',
                type = 'R2',
                particles = [ P.u__tilde__, P.u ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_133_39})

V_42 = CTVertex(name = 'V_42',
                type = 'R2',
                particles = [ P.c__tilde__, P.c ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_133_39})

V_43 = CTVertex(name = 'V_43',
                type = 'R2',
                particles = [ P.t__tilde__, P.t ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF2, L.FF3, L.FF4, L.FF5 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_192_76,(0,2,0):C.R2GC_192_76,(0,1,0):C.R2GC_133_39,(0,3,0):C.R2GC_133_39})

V_44 = CTVertex(name = 'V_44',
                type = 'R2',
                particles = [ P.d__tilde__, P.d ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_133_39})

V_45 = CTVertex(name = 'V_45',
                type = 'R2',
                particles = [ P.s__tilde__, P.s ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_133_39})

V_46 = CTVertex(name = 'V_46',
                type = 'R2',
                particles = [ P.b__tilde__, P.b ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_133_39})

V_47 = CTVertex(name = 'V_47',
                type = 'R2',
                particles = [ P.g, P.g ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VV1, L.VV2, L.VV3 ],
                loop_particles = [ [ [P.b], [P.c], [P.d], [P.s], [P.t], [P.u] ], [ [P.g] ], [ [P.t] ] ],
                couplings = {(0,0,1):C.R2GC_169_58,(0,1,2):C.R2GC_90_82,(0,2,0):C.R2GC_168_56,(0,2,1):C.R2GC_168_57})

V_48 = CTVertex(name = 'V_48',
                type = 'R2',
                particles = [ P.g, P.g, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVS1 ],
                loop_particles = [ [ [P.t] ] ],
                couplings = {(0,0,0):C.R2GC_92_84})

V_49 = CTVertex(name = 'V_49',
                type = 'R2',
                particles = [ P.g, P.g, P.Y0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVS1 ],
                loop_particles = [ [ [P.t] ] ],
                couplings = {(0,0,0):C.R2GC_89_81})

V_50 = CTVertex(name = 'V_50',
                type = 'R2',
                particles = [ P.g, P.g, P.W__minus__, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVVV2, L.VVVV3, L.VVVV4 ],
                loop_particles = [ [ [P.b, P.t] ], [ [P.c, P.d] ], [ [P.c, P.s] ], [ [P.d, P.u] ], [ [P.s, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_112_21,(0,0,1):C.R2GC_112_22,(0,0,2):C.R2GC_112_23,(0,0,3):C.R2GC_112_24,(0,0,4):C.R2GC_112_25,(0,1,0):C.R2GC_112_21,(0,1,1):C.R2GC_112_22,(0,1,2):C.R2GC_112_23,(0,1,3):C.R2GC_112_24,(0,1,4):C.R2GC_112_25,(0,2,0):C.R2GC_112_21,(0,2,1):C.R2GC_112_22,(0,2,2):C.R2GC_112_23,(0,2,3):C.R2GC_112_24,(0,2,4):C.R2GC_112_25})

V_51 = CTVertex(name = 'V_51',
                type = 'R2',
                particles = [ P.a, P.g, P.g, P.Z ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.VVVV2, L.VVVV3, L.VVVV4 ],
                loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_103_11,(0,0,1):C.R2GC_103_12,(0,1,0):C.R2GC_103_11,(0,1,1):C.R2GC_103_12,(0,2,0):C.R2GC_103_11,(0,2,1):C.R2GC_103_12})

V_52 = CTVertex(name = 'V_52',
                type = 'R2',
                particles = [ P.g, P.g, P.Z, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVVV2, L.VVVV3, L.VVVV4 ],
                loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_106_17,(0,0,1):C.R2GC_106_18,(0,1,0):C.R2GC_106_17,(0,1,1):C.R2GC_106_18,(0,2,0):C.R2GC_106_17,(0,2,1):C.R2GC_106_18})

V_53 = CTVertex(name = 'V_53',
                type = 'R2',
                particles = [ P.a, P.a, P.g, P.g ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.VVVV2, L.VVVV3, L.VVVV4 ],
                loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_100_1,(0,0,1):C.R2GC_100_2,(0,1,0):C.R2GC_100_1,(0,1,1):C.R2GC_100_2,(0,2,0):C.R2GC_100_1,(0,2,1):C.R2GC_100_2})

V_54 = CTVertex(name = 'V_54',
                type = 'R2',
                particles = [ P.g, P.g, P.g, P.Z ],
                color = [ 'd(1,2,3)', 'f(1,2,3)' ],
                lorentz = [ L.VVVV1, L.VVVV2, L.VVVV3, L.VVVV4 ],
                loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                couplings = {(1,0,0):C.R2GC_105_15,(1,0,1):C.R2GC_105_16,(0,1,0):C.R2GC_104_13,(0,1,1):C.R2GC_104_14,(0,2,0):C.R2GC_104_13,(0,2,1):C.R2GC_104_14,(0,3,0):C.R2GC_104_13,(0,3,1):C.R2GC_104_14})

V_55 = CTVertex(name = 'V_55',
                type = 'R2',
                particles = [ P.a, P.g, P.g, P.g ],
                color = [ 'd(2,3,4)' ],
                lorentz = [ L.VVVV2, L.VVVV3, L.VVVV4 ],
                loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_101_3,(0,0,1):C.R2GC_101_4,(0,1,0):C.R2GC_101_3,(0,1,1):C.R2GC_101_4,(0,2,0):C.R2GC_101_3,(0,2,1):C.R2GC_101_4})

V_56 = CTVertex(name = 'V_56',
                type = 'R2',
                particles = [ P.g, P.g, P.H, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.t] ] ],
                couplings = {(0,0,0):C.R2GC_93_85})

V_57 = CTVertex(name = 'V_57',
                type = 'R2',
                particles = [ P.g, P.g, P.G0, P.G0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.t] ] ],
                couplings = {(0,0,0):C.R2GC_93_85})

V_58 = CTVertex(name = 'V_58',
                type = 'R2',
                particles = [ P.g, P.g, P.G__minus__, P.G__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.b, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_93_85})

V_59 = CTVertex(name = 'V_59',
                type = 'R2',
                particles = [ P.g, P.g, P.H, P.Y0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.t] ] ],
                couplings = {(0,0,0):C.R2GC_91_83})

V_60 = CTVertex(name = 'V_60',
                type = 'R2',
                particles = [ P.g, P.g, P.Y0, P.Y0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.s] ], [ [P.t] ], [ [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_102_5,(0,0,1):C.R2GC_102_6,(0,0,2):C.R2GC_102_7,(0,0,3):C.R2GC_102_8,(0,0,4):C.R2GC_102_9,(0,0,5):C.R2GC_102_10})

V_61 = CTVertex(name = 'V_61',
                type = 'UV',
                particles = [ P.b__tilde__, P.b, P.Y0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_137_27})

V_62 = CTVertex(name = 'V_62',
                type = 'UV',
                particles = [ P.c__tilde__, P.c, P.Y0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_142_29})

V_63 = CTVertex(name = 'V_63',
                type = 'UV',
                particles = [ P.d__tilde__, P.d, P.Y0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_147_30})

V_64 = CTVertex(name = 'V_64',
                type = 'UV',
                particles = [ P.s__tilde__, P.s, P.Y0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.UVGC_152_31})

V_65 = CTVertex(name = 'V_65',
                type = 'UV',
                particles = [ P.t__tilde__, P.t, P.Y0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_189_91})

V_66 = CTVertex(name = 'V_66',
                type = 'UV',
                particles = [ P.u__tilde__, P.u, P.Y0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.UVGC_159_32})

V_67 = CTVertex(name = 'V_67',
                type = 'UV',
                particles = [ P.g, P.g, P.g ],
                color = [ 'f(1,2,3)' ],
                lorentz = [ L.VVV1, L.VVV2, L.VVV3, L.VVV4, L.VVV5, L.VVV6, L.VVV7, L.VVV8, L.VVV9 ],
                loop_particles = [ [ [P.b], [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.t] ] ],
                couplings = {(0,0,0):C.UVGC_170_53,(0,0,1):C.UVGC_172_58,(0,0,2):C.UVGC_172_59,(0,0,3):C.UVGC_170_55,(0,1,0):C.UVGC_173_60,(0,1,1):C.UVGC_173_61,(0,1,3):C.UVGC_173_62,(0,3,0):C.UVGC_173_60,(0,3,1):C.UVGC_175_65,(0,3,2):C.UVGC_175_66,(0,3,3):C.UVGC_173_62,(0,5,0):C.UVGC_170_53,(0,5,1):C.UVGC_171_56,(0,5,2):C.UVGC_171_57,(0,5,3):C.UVGC_170_55,(0,7,0):C.UVGC_170_53,(0,7,1):C.UVGC_170_54,(0,7,2):C.UVGC_125_8,(0,7,3):C.UVGC_170_55,(0,8,0):C.UVGC_173_60,(0,8,1):C.UVGC_174_63,(0,8,2):C.UVGC_174_64,(0,8,3):C.UVGC_173_62,(0,2,1):C.UVGC_125_7,(0,2,2):C.UVGC_125_8,(0,4,1):C.UVGC_124_5,(0,4,2):C.UVGC_124_6,(0,6,1):C.UVGC_113_1})

V_68 = CTVertex(name = 'V_68',
                type = 'UV',
                particles = [ P.g, P.g, P.g, P.g ],
                color = [ 'd(-1,1,3)*d(-1,2,4)', 'd(-1,1,3)*f(-1,2,4)', 'd(-1,1,4)*d(-1,2,3)', 'd(-1,1,4)*f(-1,2,3)', 'd(-1,2,3)*f(-1,1,4)', 'd(-1,2,4)*f(-1,1,3)', 'f(-1,1,2)*f(-1,3,4)', 'f(-1,1,3)*f(-1,2,4)', 'f(-1,1,4)*f(-1,2,3)', 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.VVVV2, L.VVVV3, L.VVVV4 ],
                loop_particles = [ [ [P.b], [P.c], [P.d], [P.s], [P.t], [P.u] ], [ [P.b], [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.t] ] ],
                couplings = {(2,0,2):C.UVGC_127_12,(2,0,3):C.UVGC_127_11,(0,0,2):C.UVGC_127_12,(0,0,3):C.UVGC_127_11,(4,0,2):C.UVGC_126_9,(4,0,3):C.UVGC_126_10,(3,0,2):C.UVGC_126_9,(3,0,3):C.UVGC_126_10,(8,0,2):C.UVGC_127_11,(8,0,3):C.UVGC_127_12,(7,0,1):C.UVGC_179_75,(7,0,2):C.UVGC_179_76,(7,0,3):C.UVGC_179_77,(7,0,4):C.UVGC_179_78,(5,0,2):C.UVGC_126_9,(5,0,3):C.UVGC_126_10,(1,0,2):C.UVGC_126_9,(1,0,3):C.UVGC_126_10,(6,0,1):C.UVGC_179_75,(6,0,2):C.UVGC_180_79,(6,0,3):C.UVGC_180_80,(6,0,4):C.UVGC_179_78,(11,0,2):C.UVGC_130_15,(11,0,3):C.UVGC_130_16,(10,0,2):C.UVGC_130_15,(10,0,3):C.UVGC_130_16,(9,0,2):C.UVGC_129_13,(9,0,3):C.UVGC_129_14,(2,1,2):C.UVGC_127_12,(2,1,3):C.UVGC_127_11,(0,1,2):C.UVGC_127_12,(0,1,3):C.UVGC_127_11,(6,1,2):C.UVGC_176_67,(6,1,3):C.UVGC_176_68,(6,1,4):C.UVGC_176_69,(4,1,2):C.UVGC_126_9,(4,1,3):C.UVGC_126_10,(3,1,2):C.UVGC_126_9,(3,1,3):C.UVGC_126_10,(8,1,1):C.UVGC_181_81,(8,1,2):C.UVGC_179_76,(8,1,3):C.UVGC_181_82,(8,1,4):C.UVGC_181_83,(7,1,0):C.UVGC_131_17,(7,1,2):C.UVGC_127_11,(7,1,3):C.UVGC_132_18,(5,1,2):C.UVGC_126_9,(5,1,3):C.UVGC_126_10,(1,1,2):C.UVGC_126_9,(1,1,3):C.UVGC_126_10,(11,1,2):C.UVGC_130_15,(11,1,3):C.UVGC_130_16,(10,1,2):C.UVGC_130_15,(10,1,3):C.UVGC_130_16,(9,1,2):C.UVGC_129_13,(9,1,3):C.UVGC_129_14,(2,2,2):C.UVGC_127_12,(2,2,3):C.UVGC_127_11,(0,2,2):C.UVGC_127_12,(0,2,3):C.UVGC_127_11,(4,2,2):C.UVGC_126_9,(4,2,3):C.UVGC_126_10,(3,2,2):C.UVGC_126_9,(3,2,3):C.UVGC_126_10,(8,2,1):C.UVGC_178_72,(8,2,2):C.UVGC_177_70,(8,2,3):C.UVGC_178_73,(8,2,4):C.UVGC_178_74,(6,2,0):C.UVGC_131_17,(6,2,3):C.UVGC_129_13,(7,2,2):C.UVGC_177_70,(7,2,3):C.UVGC_177_71,(7,2,4):C.UVGC_176_69,(5,2,2):C.UVGC_126_9,(5,2,3):C.UVGC_126_10,(1,2,2):C.UVGC_126_9,(1,2,3):C.UVGC_126_10,(11,2,2):C.UVGC_130_15,(11,2,3):C.UVGC_130_16,(10,2,2):C.UVGC_130_15,(10,2,3):C.UVGC_130_16,(9,2,2):C.UVGC_129_13,(9,2,3):C.UVGC_129_14})

V_69 = CTVertex(name = 'V_69',
                type = 'UV',
                particles = [ P.t__tilde__, P.b, P.G__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS4 ],
                loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.t] ], [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_193_97,(0,0,2):C.UVGC_193_98,(0,0,1):C.UVGC_193_99})

V_70 = CTVertex(name = 'V_70',
                type = 'UV',
                particles = [ P.b__tilde__, P.t, P.G__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.t] ], [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_194_100,(0,0,2):C.UVGC_194_101,(0,0,1):C.UVGC_194_102})

V_71 = CTVertex(name = 'V_71',
                type = 'UV',
                particles = [ P.t__tilde__, P.t, P.G0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS1 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_195_103})

V_72 = CTVertex(name = 'V_72',
                type = 'UV',
                particles = [ P.t__tilde__, P.t, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_196_104})

V_73 = CTVertex(name = 'V_73',
                type = 'UV',
                particles = [ P.u__tilde__, P.u, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.UVGC_139_28,(0,1,0):C.UVGC_117_4,(0,2,0):C.UVGC_117_4})

V_74 = CTVertex(name = 'V_74',
                type = 'UV',
                particles = [ P.c__tilde__, P.c, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_139_28,(0,1,0):C.UVGC_117_4,(0,2,0):C.UVGC_117_4})

V_75 = CTVertex(name = 'V_75',
                type = 'UV',
                particles = [ P.t__tilde__, P.t, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_139_28,(0,1,0):C.UVGC_187_89,(0,2,0):C.UVGC_183_85})

V_76 = CTVertex(name = 'V_76',
                type = 'UV',
                particles = [ P.d__tilde__, P.d, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_134_20,(0,1,0):C.UVGC_115_3,(0,2,0):C.UVGC_115_3})

V_77 = CTVertex(name = 'V_77',
                type = 'UV',
                particles = [ P.s__tilde__, P.s, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.UVGC_134_20,(0,1,0):C.UVGC_115_3,(0,2,0):C.UVGC_115_3})

V_78 = CTVertex(name = 'V_78',
                type = 'UV',
                particles = [ P.b__tilde__, P.b, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_134_20,(0,1,0):C.UVGC_115_3,(0,2,0):C.UVGC_115_3})

V_79 = CTVertex(name = 'V_79',
                type = 'UV',
                particles = [ P.u__tilde__, P.u, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.b], [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.u] ], [ [P.t] ] ],
                couplings = {(0,0,3):C.UVGC_136_26,(0,1,0):C.UVGC_135_21,(0,1,1):C.UVGC_135_22,(0,1,2):C.UVGC_135_23,(0,1,4):C.UVGC_135_24,(0,1,3):C.UVGC_135_25,(0,2,0):C.UVGC_135_21,(0,2,1):C.UVGC_135_22,(0,2,2):C.UVGC_135_23,(0,2,4):C.UVGC_135_24,(0,2,3):C.UVGC_135_25})

V_80 = CTVertex(name = 'V_80',
                type = 'UV',
                particles = [ P.c__tilde__, P.c, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.b], [P.c], [P.d], [P.s], [P.u] ], [ [P.c, P.g] ], [ [P.g] ], [ [P.ghG] ], [ [P.t] ] ],
                couplings = {(0,0,1):C.UVGC_136_26,(0,1,0):C.UVGC_135_21,(0,1,2):C.UVGC_135_22,(0,1,3):C.UVGC_135_23,(0,1,4):C.UVGC_135_24,(0,1,1):C.UVGC_135_25,(0,2,0):C.UVGC_135_21,(0,2,2):C.UVGC_135_22,(0,2,3):C.UVGC_135_23,(0,2,4):C.UVGC_135_24,(0,2,1):C.UVGC_135_25})

V_81 = CTVertex(name = 'V_81',
                type = 'UV',
                particles = [ P.t__tilde__, P.t, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.b], [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.t] ], [ [P.t] ] ],
                couplings = {(0,0,3):C.UVGC_136_26,(0,1,0):C.UVGC_135_21,(0,1,1):C.UVGC_135_22,(0,1,2):C.UVGC_135_23,(0,1,4):C.UVGC_135_24,(0,1,3):C.UVGC_188_90,(0,2,0):C.UVGC_135_21,(0,2,1):C.UVGC_135_22,(0,2,2):C.UVGC_135_23,(0,2,4):C.UVGC_135_24,(0,2,3):C.UVGC_184_86})

V_82 = CTVertex(name = 'V_82',
                type = 'UV',
                particles = [ P.d__tilde__, P.d, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.b], [P.c], [P.d], [P.s], [P.u] ], [ [P.d, P.g] ], [ [P.g] ], [ [P.ghG] ], [ [P.t] ] ],
                couplings = {(0,0,1):C.UVGC_136_26,(0,1,0):C.UVGC_135_21,(0,1,2):C.UVGC_135_22,(0,1,3):C.UVGC_135_23,(0,1,4):C.UVGC_135_24,(0,1,1):C.UVGC_135_25,(0,2,0):C.UVGC_135_21,(0,2,2):C.UVGC_135_22,(0,2,3):C.UVGC_135_23,(0,2,4):C.UVGC_135_24,(0,2,1):C.UVGC_135_25})

V_83 = CTVertex(name = 'V_83',
                type = 'UV',
                particles = [ P.s__tilde__, P.s, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.b], [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.s] ], [ [P.t] ] ],
                couplings = {(0,0,3):C.UVGC_136_26,(0,1,0):C.UVGC_135_21,(0,1,1):C.UVGC_135_22,(0,1,2):C.UVGC_135_23,(0,1,4):C.UVGC_135_24,(0,1,3):C.UVGC_135_25,(0,2,0):C.UVGC_135_21,(0,2,1):C.UVGC_135_22,(0,2,2):C.UVGC_135_23,(0,2,4):C.UVGC_135_24,(0,2,3):C.UVGC_135_25})

V_84 = CTVertex(name = 'V_84',
                type = 'UV',
                particles = [ P.b__tilde__, P.b, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.b], [P.c], [P.d], [P.s], [P.u] ], [ [P.b, P.g] ], [ [P.g] ], [ [P.ghG] ], [ [P.t] ] ],
                couplings = {(0,0,1):C.UVGC_136_26,(0,1,0):C.UVGC_135_21,(0,1,2):C.UVGC_135_22,(0,1,3):C.UVGC_135_23,(0,1,4):C.UVGC_135_24,(0,1,1):C.UVGC_135_25,(0,2,0):C.UVGC_135_21,(0,2,2):C.UVGC_135_22,(0,2,3):C.UVGC_135_23,(0,2,4):C.UVGC_135_24,(0,2,1):C.UVGC_135_25})

V_85 = CTVertex(name = 'V_85',
                type = 'UV',
                particles = [ P.d__tilde__, P.u, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.d, P.g], [P.g, P.u] ], [ [P.d, P.g, P.u] ] ],
                couplings = {(0,0,0):C.UVGC_164_41,(0,0,1):C.UVGC_164_42})

V_86 = CTVertex(name = 'V_86',
                type = 'UV',
                particles = [ P.s__tilde__, P.u, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.g, P.s], [P.g, P.u] ], [ [P.g, P.s, P.u] ] ],
                couplings = {(0,0,0):C.UVGC_166_45,(0,0,1):C.UVGC_166_46})

V_87 = CTVertex(name = 'V_87',
                type = 'UV',
                particles = [ P.d__tilde__, P.c, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.c, P.d, P.g] ], [ [P.c, P.g], [P.d, P.g] ] ],
                couplings = {(0,0,1):C.UVGC_160_33,(0,0,0):C.UVGC_160_34})

V_88 = CTVertex(name = 'V_88',
                type = 'UV',
                particles = [ P.s__tilde__, P.c, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.c, P.g], [P.g, P.s] ], [ [P.c, P.g, P.s] ] ],
                couplings = {(0,0,0):C.UVGC_162_37,(0,0,1):C.UVGC_162_38})

V_89 = CTVertex(name = 'V_89',
                type = 'UV',
                particles = [ P.b__tilde__, P.t, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.t] ], [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_190_92,(0,0,2):C.UVGC_190_93,(0,0,1):C.UVGC_190_94})

V_90 = CTVertex(name = 'V_90',
                type = 'UV',
                particles = [ P.u__tilde__, P.d, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.d, P.g], [P.g, P.u] ], [ [P.d, P.g, P.u] ] ],
                couplings = {(0,0,0):C.UVGC_165_43,(0,0,1):C.UVGC_165_44})

V_91 = CTVertex(name = 'V_91',
                type = 'UV',
                particles = [ P.c__tilde__, P.d, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.c, P.d, P.g] ], [ [P.c, P.g], [P.d, P.g] ] ],
                couplings = {(0,0,1):C.UVGC_161_35,(0,0,0):C.UVGC_161_36})

V_92 = CTVertex(name = 'V_92',
                type = 'UV',
                particles = [ P.u__tilde__, P.s, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.g, P.s], [P.g, P.u] ], [ [P.g, P.s, P.u] ] ],
                couplings = {(0,0,0):C.UVGC_167_47,(0,0,1):C.UVGC_167_48})

V_93 = CTVertex(name = 'V_93',
                type = 'UV',
                particles = [ P.c__tilde__, P.s, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.c, P.g], [P.g, P.s] ], [ [P.c, P.g, P.s] ] ],
                couplings = {(0,0,0):C.UVGC_163_39,(0,0,1):C.UVGC_163_40})

V_94 = CTVertex(name = 'V_94',
                type = 'UV',
                particles = [ P.t__tilde__, P.b, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.t] ], [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_190_92,(0,0,2):C.UVGC_190_93,(0,0,1):C.UVGC_190_94})

V_95 = CTVertex(name = 'V_95',
                type = 'UV',
                particles = [ P.t__tilde__, P.t, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_191_95,(0,1,0):C.UVGC_185_87})

V_96 = CTVertex(name = 'V_96',
                type = 'UV',
                particles = [ P.u__tilde__, P.u ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1, L.FF3, L.FF5 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.UVGC_133_19,(0,1,0):C.UVGC_114_2,(0,2,0):C.UVGC_114_2})

V_97 = CTVertex(name = 'V_97',
                type = 'UV',
                particles = [ P.c__tilde__, P.c ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1, L.FF3, L.FF5 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_133_19,(0,1,0):C.UVGC_114_2,(0,2,0):C.UVGC_114_2})

V_98 = CTVertex(name = 'V_98',
                type = 'UV',
                particles = [ P.t__tilde__, P.t ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF2, L.FF3, L.FF4, L.FF5 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_192_96,(0,2,0):C.UVGC_192_96,(0,1,0):C.UVGC_186_88,(0,3,0):C.UVGC_182_84})

V_99 = CTVertex(name = 'V_99',
                type = 'UV',
                particles = [ P.d__tilde__, P.d ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1, L.FF3, L.FF5 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_133_19,(0,1,0):C.UVGC_114_2,(0,2,0):C.UVGC_114_2})

V_100 = CTVertex(name = 'V_100',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.s ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1, L.FF3, L.FF5 ],
                 loop_particles = [ [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_133_19,(0,1,0):C.UVGC_114_2,(0,2,0):C.UVGC_114_2})

V_101 = CTVertex(name = 'V_101',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.b ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1, L.FF3, L.FF5 ],
                 loop_particles = [ [ [P.b, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_133_19,(0,1,0):C.UVGC_114_2,(0,2,0):C.UVGC_114_2})

V_102 = CTVertex(name = 'V_102',
                 type = 'UV',
                 particles = [ P.g, P.g ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VV1, L.VV3 ],
                 loop_particles = [ [ [P.g] ], [ [P.ghG] ], [ [P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_169_50,(0,0,1):C.UVGC_169_51,(0,0,2):C.UVGC_169_52,(0,1,2):C.UVGC_168_49})


# This file was automatically created by FeynRules 2.3.31
# Mathematica version: 11.0.0 for Mac OS X x86 (64-bit) (July 28, 2016)
# Date: Tue 6 Mar 2018 21:49:51


from object_library import all_vertices, all_CTvertices, Vertex, CTVertex
import particles as P
import CT_couplings as C
import lorentz as L


V_1 = CTVertex(name = 'V_1',
               type = 'R2',
               particles = [ P.b__tilde__, P.b, P.GR ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               loop_particles = [ [ [P.b, P.g] ] ],
               couplings = {(0,0,0):C.R2GC_184_71})

V_2 = CTVertex(name = 'V_2',
               type = 'R2',
               particles = [ P.c__tilde__, P.c, P.GR ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               loop_particles = [ [ [P.c, P.g] ] ],
               couplings = {(0,0,0):C.R2GC_184_71})

V_3 = CTVertex(name = 'V_3',
               type = 'R2',
               particles = [ P.d__tilde__, P.d, P.GR ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               loop_particles = [ [ [P.d, P.g] ] ],
               couplings = {(0,0,0):C.R2GC_184_71})

V_4 = CTVertex(name = 'V_4',
               type = 'R2',
               particles = [ P.s__tilde__, P.s, P.GR ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               loop_particles = [ [ [P.g, P.s] ] ],
               couplings = {(0,0,0):C.R2GC_184_71})

V_5 = CTVertex(name = 'V_5',
               type = 'R2',
               particles = [ P.t__tilde__, P.t, P.GR ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               loop_particles = [ [ [P.g, P.t] ] ],
               couplings = {(0,0,0):C.R2GC_184_71})

V_6 = CTVertex(name = 'V_6',
               type = 'R2',
               particles = [ P.u__tilde__, P.u, P.GR ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               loop_particles = [ [ [P.g, P.u] ] ],
               couplings = {(0,0,0):C.R2GC_184_71})

V_7 = CTVertex(name = 'V_7',
               type = 'R2',
               particles = [ P.g, P.g, P.g ],
               color = [ 'f(1,2,3)' ],
               lorentz = [ L.VVV7, L.VVV8 ],
               loop_particles = [ [ [P.b], [P.c], [P.d], [P.s], [P.t], [P.u] ], [ [P.g] ] ],
               couplings = {(0,0,0):C.R2GC_257_111,(0,1,1):C.R2GC_141_1})

V_8 = CTVertex(name = 'V_8',
               type = 'R2',
               particles = [ P.g, P.g, P.g, P.g ],
               color = [ 'd(-1,1,3)*d(-1,2,4)', 'd(-1,1,3)*f(-1,2,4)', 'd(-1,1,4)*d(-1,2,3)', 'd(-1,1,4)*f(-1,2,3)', 'd(-1,2,3)*f(-1,1,4)', 'd(-1,2,4)*f(-1,1,3)', 'f(-1,1,2)*f(-1,3,4)', 'f(-1,1,3)*f(-1,2,4)', 'f(-1,1,4)*f(-1,2,3)', 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
               lorentz = [ L.VVVV2, L.VVVV3, L.VVVV5, L.VVVV8 ],
               loop_particles = [ [ [P.b], [P.c], [P.d], [P.s], [P.t], [P.u] ], [ [P.g] ] ],
               couplings = {(2,0,0):C.R2GC_160_59,(2,0,1):C.R2GC_160_60,(0,0,0):C.R2GC_160_59,(0,0,1):C.R2GC_160_60,(4,0,0):C.R2GC_158_55,(4,0,1):C.R2GC_158_56,(3,0,0):C.R2GC_158_55,(3,0,1):C.R2GC_158_56,(8,0,0):C.R2GC_159_57,(8,0,1):C.R2GC_159_58,(7,0,0):C.R2GC_164_65,(7,0,1):C.R2GC_261_116,(6,0,0):C.R2GC_163_64,(6,0,1):C.R2GC_263_117,(5,0,0):C.R2GC_158_55,(5,0,1):C.R2GC_158_56,(1,0,0):C.R2GC_158_55,(1,0,1):C.R2GC_158_56,(11,3,0):C.R2GC_162_62,(11,3,1):C.R2GC_162_63,(10,3,0):C.R2GC_162_62,(10,3,1):C.R2GC_162_63,(9,3,1):C.R2GC_161_61,(2,1,0):C.R2GC_160_59,(2,1,1):C.R2GC_160_60,(0,1,0):C.R2GC_160_59,(0,1,1):C.R2GC_160_60,(6,1,0):C.R2GC_259_113,(6,1,1):C.R2GC_259_114,(4,1,0):C.R2GC_158_55,(4,1,1):C.R2GC_158_56,(3,1,0):C.R2GC_158_55,(3,1,1):C.R2GC_158_56,(8,1,0):C.R2GC_159_57,(8,1,1):C.R2GC_261_116,(7,1,0):C.R2GC_164_65,(7,1,1):C.R2GC_159_58,(5,1,0):C.R2GC_158_55,(5,1,1):C.R2GC_158_56,(1,1,0):C.R2GC_158_55,(1,1,1):C.R2GC_158_56,(2,2,0):C.R2GC_160_59,(2,2,1):C.R2GC_160_60,(0,2,0):C.R2GC_160_59,(0,2,1):C.R2GC_160_60,(4,2,0):C.R2GC_158_55,(4,2,1):C.R2GC_158_56,(3,2,0):C.R2GC_158_55,(3,2,1):C.R2GC_158_56,(8,2,0):C.R2GC_159_57,(8,2,1):C.R2GC_258_112,(6,2,0):C.R2GC_163_64,(7,2,0):C.R2GC_260_115,(7,2,1):C.R2GC_258_112,(5,2,0):C.R2GC_158_55,(5,2,1):C.R2GC_158_56,(1,2,0):C.R2GC_158_55,(1,2,1):C.R2GC_158_56})

V_9 = CTVertex(name = 'V_9',
               type = 'R2',
               particles = [ P.u__tilde__, P.d, P.G__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS5 ],
               loop_particles = [ [ [P.d, P.g, P.u] ] ],
               couplings = {(0,0,0):C.R2GC_283_128,(0,1,0):C.R2GC_284_129})

V_10 = CTVertex(name = 'V_10',
                type = 'R2',
                particles = [ P.c__tilde__, P.d, P.G__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.c, P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_216_87,(0,1,0):C.R2GC_218_89})

V_11 = CTVertex(name = 'V_11',
                type = 'R2',
                particles = [ P.u__tilde__, P.s, P.G__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.g, P.s, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_286_131,(0,1,0):C.R2GC_287_132})

V_12 = CTVertex(name = 'V_12',
                type = 'R2',
                particles = [ P.c__tilde__, P.s, P.G__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.c, P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_236_98,(0,1,0):C.R2GC_235_97})

V_13 = CTVertex(name = 'V_13',
                type = 'R2',
                particles = [ P.t__tilde__, P.b, P.G__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.b, P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_253_106,(0,1,0):C.R2GC_254_107})

V_14 = CTVertex(name = 'V_14',
                type = 'R2',
                particles = [ P.d__tilde__, P.d, P.G0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS1 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_214_85})

V_15 = CTVertex(name = 'V_15',
                type = 'R2',
                particles = [ P.s__tilde__, P.s, P.G0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS1 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_233_95})

V_16 = CTVertex(name = 'V_16',
                type = 'R2',
                particles = [ P.b__tilde__, P.b, P.G0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS1 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_187_74})

V_17 = CTVertex(name = 'V_17',
                type = 'R2',
                particles = [ P.d__tilde__, P.d, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_213_84})

V_18 = CTVertex(name = 'V_18',
                type = 'R2',
                particles = [ P.s__tilde__, P.s, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_232_94})

V_19 = CTVertex(name = 'V_19',
                type = 'R2',
                particles = [ P.b__tilde__, P.b, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_186_73})

V_20 = CTVertex(name = 'V_20',
                type = 'R2',
                particles = [ P.d__tilde__, P.u, P.G__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.d, P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_278_123,(0,1,0):C.R2GC_275_120})

V_21 = CTVertex(name = 'V_21',
                type = 'R2',
                particles = [ P.s__tilde__, P.u, P.G__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.g, P.s, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_279_124,(0,1,0):C.R2GC_277_122})

V_22 = CTVertex(name = 'V_22',
                type = 'R2',
                particles = [ P.d__tilde__, P.c, P.G__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.c, P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_212_83,(0,1,0):C.R2GC_205_81})

V_23 = CTVertex(name = 'V_23',
                type = 'R2',
                particles = [ P.s__tilde__, P.c, P.G__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.c, P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_229_91,(0,1,0):C.R2GC_231_93})

V_24 = CTVertex(name = 'V_24',
                type = 'R2',
                particles = [ P.b__tilde__, P.t, P.G__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.b, P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_249_102,(0,1,0):C.R2GC_247_100})

V_25 = CTVertex(name = 'V_25',
                type = 'R2',
                particles = [ P.u__tilde__, P.u, P.G0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS1 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_280_125})

V_26 = CTVertex(name = 'V_26',
                type = 'R2',
                particles = [ P.c__tilde__, P.c, P.G0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS1 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_198_78})

V_27 = CTVertex(name = 'V_27',
                type = 'R2',
                particles = [ P.t__tilde__, P.t, P.G0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS1 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_250_103})

V_28 = CTVertex(name = 'V_28',
                type = 'R2',
                particles = [ P.u__tilde__, P.u, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_281_126})

V_29 = CTVertex(name = 'V_29',
                type = 'R2',
                particles = [ P.c__tilde__, P.c, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_199_79})

V_30 = CTVertex(name = 'V_30',
                type = 'R2',
                particles = [ P.t__tilde__, P.t, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_251_104})

V_31 = CTVertex(name = 'V_31',
                type = 'R2',
                particles = [ P.u__tilde__, P.u, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_167_68})

V_32 = CTVertex(name = 'V_32',
                type = 'R2',
                particles = [ P.c__tilde__, P.c, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_167_68})

V_33 = CTVertex(name = 'V_33',
                type = 'R2',
                particles = [ P.t__tilde__, P.t, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_167_68})

V_34 = CTVertex(name = 'V_34',
                type = 'R2',
                particles = [ P.d__tilde__, P.d, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_165_66})

V_35 = CTVertex(name = 'V_35',
                type = 'R2',
                particles = [ P.s__tilde__, P.s, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_165_66})

V_36 = CTVertex(name = 'V_36',
                type = 'R2',
                particles = [ P.b__tilde__, P.b, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_165_66})

V_37 = CTVertex(name = 'V_37',
                type = 'R2',
                particles = [ P.u__tilde__, P.u, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_166_67})

V_38 = CTVertex(name = 'V_38',
                type = 'R2',
                particles = [ P.c__tilde__, P.c, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_166_67})

V_39 = CTVertex(name = 'V_39',
                type = 'R2',
                particles = [ P.t__tilde__, P.t, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_166_67})

V_40 = CTVertex(name = 'V_40',
                type = 'R2',
                particles = [ P.d__tilde__, P.d, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_166_67})

V_41 = CTVertex(name = 'V_41',
                type = 'R2',
                particles = [ P.s__tilde__, P.s, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_166_67})

V_42 = CTVertex(name = 'V_42',
                type = 'R2',
                particles = [ P.b__tilde__, P.b, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_166_67})

V_43 = CTVertex(name = 'V_43',
                type = 'R2',
                particles = [ P.d__tilde__, P.u, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.d, P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_272_118})

V_44 = CTVertex(name = 'V_44',
                type = 'R2',
                particles = [ P.s__tilde__, P.u, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.g, P.s, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_273_119})

V_45 = CTVertex(name = 'V_45',
                type = 'R2',
                particles = [ P.d__tilde__, P.c, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.c, P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_210_82})

V_46 = CTVertex(name = 'V_46',
                type = 'R2',
                particles = [ P.s__tilde__, P.c, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.c, P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_227_90})

V_47 = CTVertex(name = 'V_47',
                type = 'R2',
                particles = [ P.b__tilde__, P.t, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.b, P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_245_99})

V_48 = CTVertex(name = 'V_48',
                type = 'R2',
                particles = [ P.u__tilde__, P.d, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.d, P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_282_127})

V_49 = CTVertex(name = 'V_49',
                type = 'R2',
                particles = [ P.c__tilde__, P.d, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.c, P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_217_88})

V_50 = CTVertex(name = 'V_50',
                type = 'R2',
                particles = [ P.u__tilde__, P.s, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.g, P.s, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_285_130})

V_51 = CTVertex(name = 'V_51',
                type = 'R2',
                particles = [ P.c__tilde__, P.s, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.c, P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_234_96})

V_52 = CTVertex(name = 'V_52',
                type = 'R2',
                particles = [ P.t__tilde__, P.b, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.b, P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_252_105})

V_53 = CTVertex(name = 'V_53',
                type = 'R2',
                particles = [ P.u__tilde__, P.u, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_197_77,(0,1,0):C.R2GC_192_76})

V_54 = CTVertex(name = 'V_54',
                type = 'R2',
                particles = [ P.c__tilde__, P.c, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_197_77,(0,1,0):C.R2GC_192_76})

V_55 = CTVertex(name = 'V_55',
                type = 'R2',
                particles = [ P.t__tilde__, P.t, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_197_77,(0,1,0):C.R2GC_192_76})

V_56 = CTVertex(name = 'V_56',
                type = 'R2',
                particles = [ P.d__tilde__, P.d, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_185_72,(0,1,0):C.R2GC_180_70})

V_57 = CTVertex(name = 'V_57',
                type = 'R2',
                particles = [ P.s__tilde__, P.s, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_185_72,(0,1,0):C.R2GC_180_70})

V_58 = CTVertex(name = 'V_58',
                type = 'R2',
                particles = [ P.b__tilde__, P.b, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_185_72,(0,1,0):C.R2GC_180_70})

V_59 = CTVertex(name = 'V_59',
                type = 'R2',
                particles = [ P.u__tilde__, P.u ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1, L.FF2, L.FF3, L.FF4 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_276_121,(0,2,0):C.R2GC_276_121,(0,1,0):C.R2GC_177_69,(0,3,0):C.R2GC_177_69})

V_60 = CTVertex(name = 'V_60',
                type = 'R2',
                particles = [ P.c__tilde__, P.c ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1, L.FF2, L.FF3, L.FF4 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_200_80,(0,2,0):C.R2GC_200_80,(0,1,0):C.R2GC_177_69,(0,3,0):C.R2GC_177_69})

V_61 = CTVertex(name = 'V_61',
                type = 'R2',
                particles = [ P.t__tilde__, P.t ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1, L.FF2, L.FF3, L.FF4 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_248_101,(0,2,0):C.R2GC_248_101,(0,1,0):C.R2GC_177_69,(0,3,0):C.R2GC_177_69})

V_62 = CTVertex(name = 'V_62',
                type = 'R2',
                particles = [ P.d__tilde__, P.d ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1, L.FF2, L.FF3, L.FF4 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_215_86,(0,2,0):C.R2GC_215_86,(0,1,0):C.R2GC_177_69,(0,3,0):C.R2GC_177_69})

V_63 = CTVertex(name = 'V_63',
                type = 'R2',
                particles = [ P.s__tilde__, P.s ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1, L.FF2, L.FF3, L.FF4 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_230_92,(0,2,0):C.R2GC_230_92,(0,1,0):C.R2GC_177_69,(0,3,0):C.R2GC_177_69})

V_64 = CTVertex(name = 'V_64',
                type = 'R2',
                particles = [ P.b__tilde__, P.b ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1, L.FF2, L.FF3, L.FF4 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_188_75,(0,2,0):C.R2GC_188_75,(0,1,0):C.R2GC_177_69,(0,3,0):C.R2GC_177_69})

V_65 = CTVertex(name = 'V_65',
                type = 'R2',
                particles = [ P.g, P.g ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VV1, L.VV2, L.VV3 ],
                loop_particles = [ [ [P.b] ], [ [P.b], [P.c], [P.d], [P.s], [P.t], [P.u] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.s] ], [ [P.t] ], [ [P.u] ] ],
                couplings = {(0,0,4):C.R2GC_256_110,(0,1,0):C.R2GC_146_13,(0,1,2):C.R2GC_146_14,(0,1,3):C.R2GC_146_15,(0,1,5):C.R2GC_146_16,(0,1,6):C.R2GC_146_17,(0,1,7):C.R2GC_146_18,(0,2,1):C.R2GC_255_108,(0,2,4):C.R2GC_255_109})

V_66 = CTVertex(name = 'V_66',
                type = 'R2',
                particles = [ P.g, P.g, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVS1 ],
                loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.s] ], [ [P.t] ], [ [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_152_33,(0,0,1):C.R2GC_152_34,(0,0,2):C.R2GC_152_35,(0,0,3):C.R2GC_152_36,(0,0,4):C.R2GC_152_37,(0,0,5):C.R2GC_152_38})

V_67 = CTVertex(name = 'V_67',
                type = 'R2',
                particles = [ P.g, P.g, P.GR ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVS1 ],
                loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.s] ], [ [P.t] ], [ [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_145_7,(0,0,1):C.R2GC_145_8,(0,0,2):C.R2GC_145_9,(0,0,3):C.R2GC_145_10,(0,0,4):C.R2GC_145_11,(0,0,5):C.R2GC_145_12})

V_68 = CTVertex(name = 'V_68',
                type = 'R2',
                particles = [ P.a, P.g, P.g, P.Z ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.VVVV2, L.VVVV3, L.VVVV5 ],
                loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_147_19,(0,0,1):C.R2GC_147_20,(0,1,0):C.R2GC_147_19,(0,1,1):C.R2GC_147_20,(0,2,0):C.R2GC_147_19,(0,2,1):C.R2GC_147_20})

V_69 = CTVertex(name = 'V_69',
                type = 'R2',
                particles = [ P.g, P.g, P.Z, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVVV2, L.VVVV3, L.VVVV5 ],
                loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_150_25,(0,0,1):C.R2GC_150_26,(0,1,0):C.R2GC_150_25,(0,1,1):C.R2GC_150_26,(0,2,0):C.R2GC_150_25,(0,2,1):C.R2GC_150_26})

V_70 = CTVertex(name = 'V_70',
                type = 'R2',
                particles = [ P.g, P.g, P.W__minus__, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVVV2, L.VVVV3, L.VVVV5 ],
                loop_particles = [ [ [P.b, P.t] ], [ [P.c, P.d] ], [ [P.c, P.s] ], [ [P.d, P.u] ], [ [P.s, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_154_45,(0,0,1):C.R2GC_154_46,(0,0,2):C.R2GC_154_47,(0,0,3):C.R2GC_154_48,(0,0,4):C.R2GC_154_49,(0,1,0):C.R2GC_154_45,(0,1,1):C.R2GC_154_46,(0,1,2):C.R2GC_154_47,(0,1,3):C.R2GC_154_48,(0,1,4):C.R2GC_154_49,(0,2,0):C.R2GC_154_45,(0,2,1):C.R2GC_154_46,(0,2,2):C.R2GC_154_47,(0,2,3):C.R2GC_154_48,(0,2,4):C.R2GC_154_49})

V_71 = CTVertex(name = 'V_71',
                type = 'R2',
                particles = [ P.a, P.a, P.g, P.g ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.VVVV2, L.VVVV3, L.VVVV5 ],
                loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_142_2,(0,0,1):C.R2GC_142_3,(0,1,0):C.R2GC_142_2,(0,1,1):C.R2GC_142_3,(0,2,0):C.R2GC_142_2,(0,2,1):C.R2GC_142_3})

V_72 = CTVertex(name = 'V_72',
                type = 'R2',
                particles = [ P.g, P.g, P.g, P.Z ],
                color = [ 'd(1,2,3)', 'f(1,2,3)' ],
                lorentz = [ L.VVVV1, L.VVVV2, L.VVVV3, L.VVVV5 ],
                loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                couplings = {(1,0,0):C.R2GC_149_23,(1,0,1):C.R2GC_149_24,(0,1,0):C.R2GC_148_21,(0,1,1):C.R2GC_148_22,(0,2,0):C.R2GC_148_21,(0,2,1):C.R2GC_148_22,(0,3,0):C.R2GC_148_21,(0,3,1):C.R2GC_148_22})

V_73 = CTVertex(name = 'V_73',
                type = 'R2',
                particles = [ P.a, P.g, P.g, P.g ],
                color = [ 'd(2,3,4)' ],
                lorentz = [ L.VVVV2, L.VVVV3, L.VVVV5 ],
                loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_143_4,(0,0,1):C.R2GC_143_5,(0,1,0):C.R2GC_143_4,(0,1,1):C.R2GC_143_5,(0,2,0):C.R2GC_143_4,(0,2,1):C.R2GC_143_5})

V_74 = CTVertex(name = 'V_74',
                type = 'R2',
                particles = [ P.g, P.g, P.H, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.s] ], [ [P.t] ], [ [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_153_39,(0,0,1):C.R2GC_153_40,(0,0,2):C.R2GC_153_41,(0,0,3):C.R2GC_153_42,(0,0,4):C.R2GC_153_43,(0,0,5):C.R2GC_153_44})

V_75 = CTVertex(name = 'V_75',
                type = 'R2',
                particles = [ P.g, P.g, P.G0, P.G0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.s] ], [ [P.t] ], [ [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_153_39,(0,0,1):C.R2GC_153_40,(0,0,2):C.R2GC_153_41,(0,0,3):C.R2GC_153_42,(0,0,4):C.R2GC_153_43,(0,0,5):C.R2GC_153_44})

V_76 = CTVertex(name = 'V_76',
                type = 'R2',
                particles = [ P.g, P.g, P.G__minus__, P.G__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.b, P.t] ], [ [P.c, P.d] ], [ [P.c, P.s] ], [ [P.d, P.u] ], [ [P.s, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_155_50,(0,0,1):C.R2GC_155_51,(0,0,2):C.R2GC_155_52,(0,0,3):C.R2GC_155_53,(0,0,4):C.R2GC_155_54})

V_77 = CTVertex(name = 'V_77',
                type = 'R2',
                particles = [ P.g, P.g, P.GR, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.s] ], [ [P.t] ], [ [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_151_27,(0,0,1):C.R2GC_151_28,(0,0,2):C.R2GC_151_29,(0,0,3):C.R2GC_151_30,(0,0,4):C.R2GC_151_31,(0,0,5):C.R2GC_151_32})

V_78 = CTVertex(name = 'V_78',
                type = 'R2',
                particles = [ P.g, P.g, P.GR, P.GR ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.b], [P.c], [P.d], [P.s], [P.t], [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_144_6})

V_79 = CTVertex(name = 'V_79',
                type = 'UV',
                particles = [ P.b__tilde__, P.b, P.GR ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_184_31})

V_80 = CTVertex(name = 'V_80',
                type = 'UV',
                particles = [ P.c__tilde__, P.c, P.GR ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_196_43})

V_81 = CTVertex(name = 'V_81',
                type = 'UV',
                particles = [ P.d__tilde__, P.d, P.GR ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_209_58})

V_82 = CTVertex(name = 'V_82',
                type = 'UV',
                particles = [ P.s__tilde__, P.s, P.GR ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.UVGC_226_85})

V_83 = CTVertex(name = 'V_83',
                type = 'UV',
                particles = [ P.t__tilde__, P.t, P.GR ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_244_115})

V_84 = CTVertex(name = 'V_84',
                type = 'UV',
                particles = [ P.u__tilde__, P.u, P.GR ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.UVGC_271_199})

V_85 = CTVertex(name = 'V_85',
                type = 'UV',
                particles = [ P.g, P.g, P.g ],
                color = [ 'f(1,2,3)' ],
                lorentz = [ L.VVV10, L.VVV7, L.VVV9 ],
                loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.s] ], [ [P.t] ], [ [P.u] ] ],
                couplings = {(0,1,0):C.UVGC_257_152,(0,1,1):C.UVGC_257_153,(0,1,2):C.UVGC_257_154,(0,1,5):C.UVGC_257_155,(0,1,6):C.UVGC_257_156,(0,1,7):C.UVGC_257_157,(0,2,3):C.UVGC_156_1,(0,0,4):C.UVGC_157_2})

V_86 = CTVertex(name = 'V_86',
                type = 'UV',
                particles = [ P.g, P.g, P.g, P.g ],
                color = [ 'd(-1,1,3)*d(-1,2,4)', 'd(-1,1,3)*f(-1,2,4)', 'd(-1,1,4)*d(-1,2,3)', 'd(-1,1,4)*f(-1,2,3)', 'd(-1,2,3)*f(-1,1,4)', 'd(-1,2,4)*f(-1,1,3)', 'f(-1,1,2)*f(-1,3,4)', 'f(-1,1,3)*f(-1,2,4)', 'f(-1,1,4)*f(-1,2,3)', 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.VVVV2, L.VVVV3, L.VVVV5, L.VVVV8 ],
                loop_particles = [ [ [P.b] ], [ [P.b], [P.c], [P.d], [P.s], [P.t], [P.u] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.s] ], [ [P.t] ], [ [P.u] ] ],
                couplings = {(2,0,4):C.UVGC_159_6,(2,0,5):C.UVGC_159_5,(0,0,4):C.UVGC_159_6,(0,0,5):C.UVGC_159_5,(4,0,4):C.UVGC_158_3,(4,0,5):C.UVGC_158_4,(3,0,4):C.UVGC_158_3,(3,0,5):C.UVGC_158_4,(8,0,4):C.UVGC_159_5,(8,0,5):C.UVGC_159_6,(7,0,0):C.UVGC_262_183,(7,0,2):C.UVGC_262_184,(7,0,3):C.UVGC_262_185,(7,0,4):C.UVGC_261_178,(7,0,5):C.UVGC_262_186,(7,0,6):C.UVGC_262_187,(7,0,7):C.UVGC_262_188,(7,0,8):C.UVGC_262_189,(6,0,0):C.UVGC_262_183,(6,0,2):C.UVGC_262_184,(6,0,3):C.UVGC_262_185,(6,0,4):C.UVGC_263_190,(6,0,5):C.UVGC_263_191,(6,0,6):C.UVGC_262_187,(6,0,7):C.UVGC_262_188,(6,0,8):C.UVGC_262_189,(5,0,4):C.UVGC_158_3,(5,0,5):C.UVGC_158_4,(1,0,4):C.UVGC_158_3,(1,0,5):C.UVGC_158_4,(11,3,4):C.UVGC_162_9,(11,3,5):C.UVGC_162_10,(10,3,4):C.UVGC_162_9,(10,3,5):C.UVGC_162_10,(9,3,4):C.UVGC_161_7,(9,3,5):C.UVGC_161_8,(2,1,4):C.UVGC_159_6,(2,1,5):C.UVGC_159_5,(0,1,4):C.UVGC_159_6,(0,1,5):C.UVGC_159_5,(6,1,0):C.UVGC_259_166,(6,1,2):C.UVGC_259_167,(6,1,3):C.UVGC_259_168,(6,1,4):C.UVGC_259_169,(6,1,5):C.UVGC_259_170,(6,1,6):C.UVGC_259_171,(6,1,7):C.UVGC_259_172,(6,1,8):C.UVGC_259_173,(4,1,4):C.UVGC_158_3,(4,1,5):C.UVGC_158_4,(3,1,4):C.UVGC_158_3,(3,1,5):C.UVGC_158_4,(8,1,0):C.UVGC_261_175,(8,1,2):C.UVGC_261_176,(8,1,3):C.UVGC_261_177,(8,1,4):C.UVGC_261_178,(8,1,5):C.UVGC_261_179,(8,1,6):C.UVGC_261_180,(8,1,7):C.UVGC_261_181,(8,1,8):C.UVGC_261_182,(7,1,1):C.UVGC_163_11,(7,1,4):C.UVGC_159_5,(7,1,5):C.UVGC_164_12,(5,1,4):C.UVGC_158_3,(5,1,5):C.UVGC_158_4,(1,1,4):C.UVGC_158_3,(1,1,5):C.UVGC_158_4,(2,2,4):C.UVGC_159_6,(2,2,5):C.UVGC_159_5,(0,2,4):C.UVGC_159_6,(0,2,5):C.UVGC_159_5,(4,2,4):C.UVGC_158_3,(4,2,5):C.UVGC_158_4,(3,2,4):C.UVGC_158_3,(3,2,5):C.UVGC_158_4,(8,2,0):C.UVGC_258_158,(8,2,2):C.UVGC_258_159,(8,2,3):C.UVGC_258_160,(8,2,4):C.UVGC_258_161,(8,2,5):C.UVGC_258_162,(8,2,6):C.UVGC_258_163,(8,2,7):C.UVGC_258_164,(8,2,8):C.UVGC_258_165,(6,2,1):C.UVGC_163_11,(6,2,5):C.UVGC_161_7,(7,2,0):C.UVGC_259_166,(7,2,2):C.UVGC_259_167,(7,2,3):C.UVGC_259_168,(7,2,4):C.UVGC_258_161,(7,2,5):C.UVGC_260_174,(7,2,6):C.UVGC_259_171,(7,2,7):C.UVGC_259_172,(7,2,8):C.UVGC_259_173,(5,2,4):C.UVGC_158_3,(5,2,5):C.UVGC_158_4,(1,2,4):C.UVGC_158_3,(1,2,5):C.UVGC_158_4})

V_87 = CTVertex(name = 'V_87',
                type = 'UV',
                particles = [ P.u__tilde__, P.d, P.G__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.u] ], [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.UVGC_283_225,(0,0,2):C.UVGC_283_226,(0,0,1):C.UVGC_283_227,(0,1,0):C.UVGC_284_228,(0,1,2):C.UVGC_284_229,(0,1,1):C.UVGC_284_230})

V_88 = CTVertex(name = 'V_88',
                type = 'UV',
                particles = [ P.c__tilde__, P.d, P.G__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.c, P.d, P.g] ], [ [P.c, P.g] ], [ [P.d, P.g] ] ],
                couplings = {(0,0,1):C.UVGC_216_69,(0,0,2):C.UVGC_216_70,(0,0,0):C.UVGC_216_71,(0,1,1):C.UVGC_218_75,(0,1,2):C.UVGC_218_76,(0,1,0):C.UVGC_218_77})

V_89 = CTVertex(name = 'V_89',
                type = 'UV',
                particles = [ P.u__tilde__, P.s, P.G__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.s, P.u] ], [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.UVGC_286_234,(0,0,2):C.UVGC_286_235,(0,0,1):C.UVGC_286_236,(0,1,0):C.UVGC_287_237,(0,1,2):C.UVGC_287_238,(0,1,1):C.UVGC_287_239})

V_90 = CTVertex(name = 'V_90',
                type = 'UV',
                particles = [ P.c__tilde__, P.s, P.G__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.s] ], [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.UVGC_236_105,(0,0,2):C.UVGC_236_106,(0,0,1):C.UVGC_236_107,(0,1,0):C.UVGC_235_102,(0,1,2):C.UVGC_235_103,(0,1,1):C.UVGC_235_104})

V_91 = CTVertex(name = 'V_91',
                type = 'UV',
                particles = [ P.t__tilde__, P.b, P.G__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.t] ], [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_253_132,(0,0,2):C.UVGC_253_133,(0,0,1):C.UVGC_253_134,(0,1,0):C.UVGC_254_135,(0,1,2):C.UVGC_254_136,(0,1,1):C.UVGC_254_137})

V_92 = CTVertex(name = 'V_92',
                type = 'UV',
                particles = [ P.d__tilde__, P.d, P.G0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS1 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_214_67})

V_93 = CTVertex(name = 'V_93',
                type = 'UV',
                particles = [ P.s__tilde__, P.s, P.G0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS1 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.UVGC_233_98})

V_94 = CTVertex(name = 'V_94',
                type = 'UV',
                particles = [ P.b__tilde__, P.b, P.G0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS1 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_187_34})

V_95 = CTVertex(name = 'V_95',
                type = 'UV',
                particles = [ P.d__tilde__, P.d, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_213_66})

V_96 = CTVertex(name = 'V_96',
                type = 'UV',
                particles = [ P.s__tilde__, P.s, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.UVGC_232_97})

V_97 = CTVertex(name = 'V_97',
                type = 'UV',
                particles = [ P.b__tilde__, P.b, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_186_33})

V_98 = CTVertex(name = 'V_98',
                type = 'UV',
                particles = [ P.d__tilde__, P.u, P.G__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.u] ], [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.UVGC_278_214,(0,0,2):C.UVGC_278_215,(0,0,1):C.UVGC_278_216,(0,1,0):C.UVGC_275_207,(0,1,2):C.UVGC_275_208,(0,1,1):C.UVGC_275_209})

V_99 = CTVertex(name = 'V_99',
                type = 'UV',
                particles = [ P.s__tilde__, P.u, P.G__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.s, P.u] ], [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.UVGC_279_217,(0,0,2):C.UVGC_279_218,(0,0,1):C.UVGC_279_219,(0,1,0):C.UVGC_277_211,(0,1,2):C.UVGC_277_212,(0,1,1):C.UVGC_277_213})

V_100 = CTVertex(name = 'V_100',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.c, P.G__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.c, P.d, P.g] ], [ [P.c, P.g] ], [ [P.d, P.g] ] ],
                 couplings = {(0,0,1):C.UVGC_212_63,(0,0,2):C.UVGC_212_64,(0,0,0):C.UVGC_212_65,(0,1,1):C.UVGC_205_52,(0,1,2):C.UVGC_205_53,(0,1,0):C.UVGC_205_54})

V_101 = CTVertex(name = 'V_101',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.c, P.G__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.s] ], [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_229_90,(0,0,2):C.UVGC_229_91,(0,0,1):C.UVGC_229_92,(0,1,0):C.UVGC_231_94,(0,1,2):C.UVGC_231_95,(0,1,1):C.UVGC_231_96})

V_102 = CTVertex(name = 'V_102',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.t, P.G__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.t] ], [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_249_124,(0,0,2):C.UVGC_249_125,(0,0,1):C.UVGC_249_126,(0,1,0):C.UVGC_247_120,(0,1,2):C.UVGC_247_121,(0,1,1):C.UVGC_247_122})

V_103 = CTVertex(name = 'V_103',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.u, P.G0 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS1 ],
                 loop_particles = [ [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_280_220})

V_104 = CTVertex(name = 'V_104',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.c, P.G0 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS1 ],
                 loop_particles = [ [ [P.c, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_198_45})

V_105 = CTVertex(name = 'V_105',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.t, P.G0 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS1 ],
                 loop_particles = [ [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_250_127})

V_106 = CTVertex(name = 'V_106',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.u, P.H ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS2 ],
                 loop_particles = [ [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_281_221})

V_107 = CTVertex(name = 'V_107',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.c, P.H ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS2 ],
                 loop_particles = [ [ [P.c, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_199_46})

V_108 = CTVertex(name = 'V_108',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.t, P.H ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS2 ],
                 loop_particles = [ [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_251_128})

V_109 = CTVertex(name = 'V_109',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.u, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_167_15,(0,1,0):C.UVGC_269_197,(0,2,0):C.UVGC_265_193})

V_110 = CTVertex(name = 'V_110',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.c, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.c, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_167_15,(0,1,0):C.UVGC_194_41,(0,2,0):C.UVGC_190_37})

V_111 = CTVertex(name = 'V_111',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.t, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_167_15,(0,1,0):C.UVGC_242_113,(0,2,0):C.UVGC_238_109})

V_112 = CTVertex(name = 'V_112',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.d, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.d, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_165_13,(0,1,0):C.UVGC_207_56,(0,2,0):C.UVGC_202_49})

V_113 = CTVertex(name = 'V_113',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.s, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_165_13,(0,1,0):C.UVGC_224_83,(0,2,0):C.UVGC_220_79})

V_114 = CTVertex(name = 'V_114',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.b, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_165_13,(0,1,0):C.UVGC_182_29,(0,2,0):C.UVGC_178_17})

V_115 = CTVertex(name = 'V_115',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.u, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.u] ], [ [P.s] ], [ [P.t] ], [ [P.u] ] ],
                 couplings = {(0,0,5):C.UVGC_166_14,(0,1,0):C.UVGC_179_18,(0,1,1):C.UVGC_179_19,(0,1,2):C.UVGC_179_20,(0,1,3):C.UVGC_179_21,(0,1,4):C.UVGC_179_22,(0,1,6):C.UVGC_179_23,(0,1,7):C.UVGC_179_24,(0,1,8):C.UVGC_179_25,(0,1,5):C.UVGC_270_198,(0,2,0):C.UVGC_179_18,(0,2,1):C.UVGC_179_19,(0,2,2):C.UVGC_179_20,(0,2,3):C.UVGC_179_21,(0,2,4):C.UVGC_179_22,(0,2,6):C.UVGC_179_23,(0,2,7):C.UVGC_179_24,(0,2,8):C.UVGC_179_25,(0,2,5):C.UVGC_266_194})

V_116 = CTVertex(name = 'V_116',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.c, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.c, P.g] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.s] ], [ [P.t] ], [ [P.u] ] ],
                 couplings = {(0,0,2):C.UVGC_166_14,(0,1,0):C.UVGC_179_18,(0,1,1):C.UVGC_179_19,(0,1,3):C.UVGC_179_20,(0,1,4):C.UVGC_179_21,(0,1,5):C.UVGC_179_22,(0,1,6):C.UVGC_179_23,(0,1,7):C.UVGC_179_24,(0,1,8):C.UVGC_179_25,(0,1,2):C.UVGC_195_42,(0,2,0):C.UVGC_179_18,(0,2,1):C.UVGC_179_19,(0,2,3):C.UVGC_179_20,(0,2,4):C.UVGC_179_21,(0,2,5):C.UVGC_179_22,(0,2,6):C.UVGC_179_23,(0,2,7):C.UVGC_179_24,(0,2,8):C.UVGC_179_25,(0,2,2):C.UVGC_191_38})

V_117 = CTVertex(name = 'V_117',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.t, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.t] ], [ [P.s] ], [ [P.t] ], [ [P.u] ] ],
                 couplings = {(0,0,5):C.UVGC_166_14,(0,1,0):C.UVGC_179_18,(0,1,1):C.UVGC_179_19,(0,1,2):C.UVGC_179_20,(0,1,3):C.UVGC_179_21,(0,1,4):C.UVGC_179_22,(0,1,6):C.UVGC_179_23,(0,1,7):C.UVGC_179_24,(0,1,8):C.UVGC_179_25,(0,1,5):C.UVGC_243_114,(0,2,0):C.UVGC_179_18,(0,2,1):C.UVGC_179_19,(0,2,2):C.UVGC_179_20,(0,2,3):C.UVGC_179_21,(0,2,4):C.UVGC_179_22,(0,2,6):C.UVGC_179_23,(0,2,7):C.UVGC_179_24,(0,2,8):C.UVGC_179_25,(0,2,5):C.UVGC_239_110})

V_118 = CTVertex(name = 'V_118',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.d, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.d, P.g] ], [ [P.g] ], [ [P.ghG] ], [ [P.s] ], [ [P.t] ], [ [P.u] ] ],
                 couplings = {(0,0,3):C.UVGC_166_14,(0,1,0):C.UVGC_179_18,(0,1,1):C.UVGC_179_19,(0,1,2):C.UVGC_179_20,(0,1,4):C.UVGC_179_21,(0,1,5):C.UVGC_179_22,(0,1,6):C.UVGC_179_23,(0,1,7):C.UVGC_179_24,(0,1,8):C.UVGC_179_25,(0,1,3):C.UVGC_208_57,(0,2,0):C.UVGC_179_18,(0,2,1):C.UVGC_179_19,(0,2,2):C.UVGC_179_20,(0,2,4):C.UVGC_179_21,(0,2,5):C.UVGC_179_22,(0,2,6):C.UVGC_179_23,(0,2,7):C.UVGC_179_24,(0,2,8):C.UVGC_179_25,(0,2,3):C.UVGC_203_50})

V_119 = CTVertex(name = 'V_119',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.s, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.s] ], [ [P.s] ], [ [P.t] ], [ [P.u] ] ],
                 couplings = {(0,0,5):C.UVGC_166_14,(0,1,0):C.UVGC_179_18,(0,1,1):C.UVGC_179_19,(0,1,2):C.UVGC_179_20,(0,1,3):C.UVGC_179_21,(0,1,4):C.UVGC_179_22,(0,1,6):C.UVGC_179_23,(0,1,7):C.UVGC_179_24,(0,1,8):C.UVGC_179_25,(0,1,5):C.UVGC_225_84,(0,2,0):C.UVGC_179_18,(0,2,1):C.UVGC_179_19,(0,2,2):C.UVGC_179_20,(0,2,3):C.UVGC_179_21,(0,2,4):C.UVGC_179_22,(0,2,6):C.UVGC_179_23,(0,2,7):C.UVGC_179_24,(0,2,8):C.UVGC_179_25,(0,2,5):C.UVGC_221_80})

V_120 = CTVertex(name = 'V_120',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.b, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b] ], [ [P.b, P.g] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.s] ], [ [P.t] ], [ [P.u] ] ],
                 couplings = {(0,0,1):C.UVGC_166_14,(0,1,0):C.UVGC_179_18,(0,1,2):C.UVGC_179_19,(0,1,3):C.UVGC_179_20,(0,1,4):C.UVGC_179_21,(0,1,5):C.UVGC_179_22,(0,1,6):C.UVGC_179_23,(0,1,7):C.UVGC_179_24,(0,1,8):C.UVGC_179_25,(0,1,1):C.UVGC_183_30,(0,2,0):C.UVGC_179_18,(0,2,2):C.UVGC_179_19,(0,2,3):C.UVGC_179_20,(0,2,4):C.UVGC_179_21,(0,2,5):C.UVGC_179_22,(0,2,6):C.UVGC_179_23,(0,2,7):C.UVGC_179_24,(0,2,8):C.UVGC_179_25,(0,2,1):C.UVGC_179_26})

V_121 = CTVertex(name = 'V_121',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.u, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.u] ], [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_272_200,(0,0,2):C.UVGC_272_201,(0,0,1):C.UVGC_272_202})

V_122 = CTVertex(name = 'V_122',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.u, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.s, P.u] ], [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_273_203,(0,0,2):C.UVGC_273_204,(0,0,1):C.UVGC_273_205})

V_123 = CTVertex(name = 'V_123',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.c, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.c, P.d, P.g] ], [ [P.c, P.g] ], [ [P.d, P.g] ] ],
                 couplings = {(0,0,1):C.UVGC_210_59,(0,0,2):C.UVGC_210_60,(0,0,0):C.UVGC_210_61})

V_124 = CTVertex(name = 'V_124',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.c, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.s] ], [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_227_86,(0,0,2):C.UVGC_227_87,(0,0,1):C.UVGC_227_88})

V_125 = CTVertex(name = 'V_125',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.t, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.t] ], [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_245_116,(0,0,2):C.UVGC_245_117,(0,0,1):C.UVGC_245_118})

V_126 = CTVertex(name = 'V_126',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.d, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.u] ], [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_282_222,(0,0,2):C.UVGC_282_223,(0,0,1):C.UVGC_282_224})

V_127 = CTVertex(name = 'V_127',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.d, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.c, P.d, P.g] ], [ [P.c, P.g] ], [ [P.d, P.g] ] ],
                 couplings = {(0,0,1):C.UVGC_217_72,(0,0,2):C.UVGC_217_73,(0,0,0):C.UVGC_217_74})

V_128 = CTVertex(name = 'V_128',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.s, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.s, P.u] ], [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_285_231,(0,0,2):C.UVGC_285_232,(0,0,1):C.UVGC_285_233})

V_129 = CTVertex(name = 'V_129',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.s, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.s] ], [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_234_99,(0,0,2):C.UVGC_234_100,(0,0,1):C.UVGC_234_101})

V_130 = CTVertex(name = 'V_130',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.b, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.t] ], [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_252_129,(0,0,2):C.UVGC_252_130,(0,0,1):C.UVGC_252_131})

V_131 = CTVertex(name = 'V_131',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.u, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_274_206,(0,1,0):C.UVGC_267_195})

V_132 = CTVertex(name = 'V_132',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.c, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.c, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_197_44,(0,1,0):C.UVGC_192_39})

V_133 = CTVertex(name = 'V_133',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.t, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_246_119,(0,1,0):C.UVGC_240_111})

V_134 = CTVertex(name = 'V_134',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.d, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.d, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_211_62,(0,1,0):C.UVGC_204_51})

V_135 = CTVertex(name = 'V_135',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.s, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_228_89,(0,1,0):C.UVGC_222_81})

V_136 = CTVertex(name = 'V_136',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.b, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_185_32,(0,1,0):C.UVGC_180_27})

V_137 = CTVertex(name = 'V_137',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.u ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1, L.FF2, L.FF3, L.FF4 ],
                 loop_particles = [ [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_276_210,(0,2,0):C.UVGC_276_210,(0,1,0):C.UVGC_268_196,(0,3,0):C.UVGC_264_192})

V_138 = CTVertex(name = 'V_138',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.c ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1, L.FF2, L.FF3, L.FF4 ],
                 loop_particles = [ [ [P.c, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_200_47,(0,2,0):C.UVGC_200_47,(0,1,0):C.UVGC_193_40,(0,3,0):C.UVGC_189_36})

V_139 = CTVertex(name = 'V_139',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.t ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1, L.FF2, L.FF3, L.FF4 ],
                 loop_particles = [ [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_248_123,(0,2,0):C.UVGC_248_123,(0,1,0):C.UVGC_241_112,(0,3,0):C.UVGC_237_108})

V_140 = CTVertex(name = 'V_140',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.d ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1, L.FF2, L.FF3, L.FF4 ],
                 loop_particles = [ [ [P.d, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_215_68,(0,2,0):C.UVGC_215_68,(0,1,0):C.UVGC_206_55,(0,3,0):C.UVGC_201_48})

V_141 = CTVertex(name = 'V_141',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.s ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1, L.FF2, L.FF3, L.FF4 ],
                 loop_particles = [ [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_230_93,(0,2,0):C.UVGC_230_93,(0,1,0):C.UVGC_223_82,(0,3,0):C.UVGC_219_78})

V_142 = CTVertex(name = 'V_142',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.b ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1, L.FF2, L.FF3, L.FF4 ],
                 loop_particles = [ [ [P.b, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_188_35,(0,2,0):C.UVGC_188_35,(0,1,0):C.UVGC_181_28,(0,3,0):C.UVGC_177_16})

V_143 = CTVertex(name = 'V_143',
                 type = 'UV',
                 particles = [ P.g, P.g ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VV1, L.VV3 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.s] ], [ [P.t] ], [ [P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_256_144,(0,0,1):C.UVGC_256_145,(0,0,2):C.UVGC_256_146,(0,0,3):C.UVGC_256_147,(0,0,4):C.UVGC_256_148,(0,0,5):C.UVGC_256_149,(0,0,6):C.UVGC_256_150,(0,0,7):C.UVGC_256_151,(0,1,0):C.UVGC_255_138,(0,1,1):C.UVGC_255_139,(0,1,2):C.UVGC_255_140,(0,1,5):C.UVGC_255_141,(0,1,6):C.UVGC_255_142,(0,1,7):C.UVGC_255_143})


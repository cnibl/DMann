"""
A file which contains the settings necessary to set up and run MadGraph for DMann. If you want to change any parameter, do it in this file.
"""

"""
The list of annihilationchannels to simulate. Channels must be from following list:
WLWL, WTWT, ZLZL, ZTZT, hh, taLtaL, taRtaR, muLmuL, muRmuR, ee, tLtL, tRtR, bb, cc, ss, uu, dd
Note: if only using one channel, it must be given in the format ANN_CHANNELS=(ann_ch,).
"""
#ANN_CHANNELS=("WLWL", "WTWT", "ZLZL", "ZTZT", "hh", 
#              "taLtaL", "taRtaR", "muLmuL", "muRmuR", "ee", 
#              "uu", "dd", "cc", "ss","tLtL", "tRtR", "bb")
ANN_CHANNELS=("tLtR","tRtL","bb","WLWL","WTWT","ZLZL","ZTZT","taLtaR","taRtaL")
#ANN_CHANNELS=("WLWL","WTWT")

"""
The number of annihilations. If below 100k, can be anything. If above 100k, must be multiple of 100k.
"""
N_ANN=100000

"""
The WIMP masses to use. Note: if only using one mass, it must be given in the format WIMP_MASSES=(mX,).
"""
WIMP_MASSES=(100,)#10000)
#WIMPMASSES=(3, 4, 5, 6, 8, 10, 15, 20, 25, 35, 
#            50, 80.3, 91.2, 100, 150, 176, 200, 
#            250, 350, 500, 750, 1000, 1500, 
#            2000, 3000, 5000, 7500, 10000) # from DarkSUSY

"""
The run tag, appended to the directory names for all the runs (the directories with LHEF). Cannot contain underscores.
"""
RUN_TAG="190424-QEDtest"

"""
The MadGraph installation directory
"""
MG_DIR="/Volumes/GoldDrive/MG5_aMC_v2_6_5_DMann_"+RUN_TAG

"""
The directory to put Pythia and Herwig files in
"""
DMANN_OUTDIR="/Volumes/GoldDrive/DMann/res_"+RUN_TAG
#DMANN_OUTDIR="/Volumes/GoldDrive/DMann/res_EWradtest"

"""
Whether to run for solar interior or not (if sun, some particles should not decay)
"""
SUN=False

"""
Whether to gzip Pythia/Herwig event files (saves space)
"""
GZIP_EVTFILE=True

"""
The number of cores to use for each MG run (don't use to many, this can cause errors), the number of parallell MG runs to do and seed to use.
"""
import multiprocessing as mp
MG_CORES=1
MG_PAR=mp.cpu_count() #number of cpu cores

"""
MG seeds
"""
MG_RNDM_SEED=False #if true, set seed randomly for each run, otherwise use default or if not None, use MG_SEED
MG_SEED=1 #ignored if MG_RNDM_SEED==True

"""
Whether to use MadSpin for decays of W, Z, t (otherwise decay chain syntax, which is significantly slower)
"""
MADSPIN=False

"""
Whether to use EvtGen for B and D decays in Herwig
"""
HER_EVTGEN=False

"""
Whether to use a QED radiation handler in Herwig
"""
HER_QRH=True

"""
Whether to use EW radiation in Pythia (W boson radiation is not included where it is already included in MG)
"""
PYT_EWRAD=False



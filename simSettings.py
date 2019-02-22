"""
A file which contains the settings necessary to set up and run MadGraph for DMann. If you want to change any parameter, do it in this file.
"""

"""
The list of annihilationchannels to simulate. Channels must be from following list:
WLWL, WTWT, ZLZL, ZTZT, hh, taLtaL, taRtaR, muLmuL, muRmuR, ee, tLtL, tRtR, bb, cc, ss, uu, dd
Note: if only using one channel, it must be given in the format ANN_CHANNELS=(ann_ch,).
"""
ANN_CHANNELS=("uu", "dd", "cc", "ss","tLtL", "tRtR", "bb", 
              "taLtaL", "taRtaR", "muLmuL", "muRmuR", "ee", 
              "WLWL", "WTWT", "ZLZL", "ZTZT", "hh"  )
#ANN_CHANNELS=("uu",)

"""
The number of annihilations. If below 100k, can be anything. If above 100k, must be multiple of 100k.
"""
N_ANN=1000000

"""
The WIMP masses to use. Note: if only using one mass, it must be given in the format WIMP_MASSES=(mX,).
"""
WIMP_MASSES=(10,100,1000,10000)
#WIMPMASSES=(3, 4, 5, 6, 8, 10, 15, 20, 25, 35, 
#            50, 80.3, 91.2, 100, 150, 176, 200, 
#            250, 350, 500, 750, 1000, 1500, 
#            2000, 3000, 5000, 7500, 10000) # from DarkSUSY

"""
The MadGraph installation directory
"""
MG_DIR="~/MG5_aMC_v2_6_3_2/"

"""
The run tag, appended to the directory names for all the runs (the directories with LHEF)
"""
RUN_TAG="190218_1M"
# Prerequisites
To run the DMann scripts, you will need:
 * python 2.7, not 3
 * Pythia8 for the Pythia part
 * Herwig7 for the Herwig part
 * ROOT

# How to set up
The file `simSettings.py` contains the settings for annihilation channels, WIMP masses, and other things that will be used by the other scripts. If you want to change what to run, do it in this file. 


# To run MadGraph
There are two scripts that set up and run MadGraph for the chosen combinations of annihilation channels and WIMP masses. These are `setupMG.py` and `runMG.py`, where the first one sets up the folder structure in a MadGraph installation directory (one folder for each annihilation channel and WIMP mass) and the latter script runs through the event generation for all these folders.

First set the desired annihilation channels, WIMP masses and number of annihilations in `simSettings.py`. If the number of events to generate is above 100000, it must be a multiple of 100000. If below 100000, it can be any number. You must also set the `MG_DIR` variable, that is the directory of the MadGraph installation you want to use. 

The `RUN_TAG` variable is a tag that is used to identify the folders belonging to this run, you can for example set it to today's date and some extra identifying tag. 

Lastly, you should set the `MG_CORES` and `MG_PAR` variables. The first of these determines the number of cores to use for each MadGraph run and the second determines how many parallell runs to run simultaneously. If using the full number of cpus on the computer for `MG_PAR`, you should not use a too large value for `MG_CORES` as this can lead to errors in the run. A reasonable number seems to be around `MG_CORES=2-4` for a 16-core machine, and probably lower on a 4-core machine.  

To set up MadGraph after having set all the relevant variables in `simSettings.py`, go to the `DMann` main directory where the scripts are and run `python setupMG.py` in a terminal. This creates one MadGraph output folder for each combination of WIMP mass and annihilation channel.

To actually run MadGraph on the created folders after setting up, simply run `python runMG.py` in the `DMann` main directory. This will run MadGraph for the chosen number of annihilations for all the folders created in the set up stage. Note that for more than 100000 events, several folders are created for each run, this is because the MadGraph command `multi_run` is used, which will here separate the run into subruns of 100000 events each. Note also that in the final states where MadSpin is used, there will not be any merged LHEF with all the events, but only the subrun LHEFs with 100000 events each. The folder names containing the LHEF with decayed events are the ones ending with "decayed_1". 

It will not work to run the scripts from another directory than the `DMann` main directory.

# To run Pythia8 on the created LHEF
To set up Pythia8 for running, you must first compile the main program `DMannPythia8LHE` that will be used, which is in the `DMann/Pythia` subdirectory. Edit the makefile to account for where ROOT and Pythia are installed on your system and run `make DMannPythia8LHE` in the `Pythia` subdirectory. Then go back to the `DMann` main directory and run `python runPythia.py`. This will first unzip all the gzipped LHE files, which can take a rather long time. Then it will run pythia on all the LHEF in parallell (using the full number of cores on the computer). 

You can also simply run the `runPythia.sh` bash script to run Pythia8, however this requires that you supply the correct ROOT installation directory in the second line of that script. 

The output directory for the histogram and event files created by Pythia are placed in the folder specified by the variable `DMANN_OUTDIR` in `simSettings.py`. 

# To run Herwig7
To be added...
# Prerequisites
To run the DMann scripts, you will need:
 * python 2.7, not 3
 * Pythia8 for the Pythia part
 * Herwig7 for the Herwig part
 * ROOT
 * A MadGraph directory with the DMann UFO model in the `models` directory

# How to set up
The file `simSettings.py` contains the settings for annihilation channels, WIMP masses, and other things that will be used by the other scripts. If you want to change what to run, do it in this file. 

# To run MadGraph
There are two scripts that set up and run MadGraph for the chosen combinations of annihilation channels and WIMP masses. These are `setupMG.py` and `runMG.py`. The former sets up the folder structure in the MadGraph installation directory provided in `simSettings.py` (creating one folder for each annihilation channel and WIMP mass) and the latter script runs through the event generation for all these folders.

First set the desired annihilation channels, WIMP masses and number of annihilations in `simSettings.py`. If the number of events to generate is above 100000, it must be a multiple of 100000. If below 100000, it can be any number. You must also set the `MG_DIR` variable, that is the directory of the MadGraph installation you want to use. In the directory corresponding to `MG_DIR` the DMann UFO model must be in the `models` subdirectory, with the folder name `DMann` (so that it can be imported in MadGraph with `import model DMann`). 

**Important**: Make sure that you have set the variable `automatic_html_opening = False` in the `input/mg5_configuration.txt` file in the MadGraph installation, in order to avoid the automatic opening of browser tabs for each separate MadGraph run. 

The `RUN_TAG` variable is a tag that is used to identify the folders belonging to this run, you can for example set it to today's date and some extra identifying tag. Note that you may not use underscores in the `RUN_TAG` variable (then it will not work to run).

You should then set the `MG_CORES` and `MG_PAR` variables. The first of these determines the number of cores to use for each MadGraph run and the second determines how many parallell runs to run simultaneously. If using the full number of cpus on the computer for `MG_PAR`, you should not use a too large value for `MG_CORES` as this can lead to errors in the run. A reasonable number seems to be around `MG_CORES=2-4` for a 16-core machine, and probably lower on a 4-core machine. 

There are then some variables related to the seeds used in MadGraph. If `MG_RNDM_SEED` is set to `True`, a random seed will be used for each run (a random integer in the interval 1-1000000). If set to `False`, and if `MG_SEED` is not set or set to `None`, the default MadGraph seed is used. If `MG_RNDM_SEED` is `False` and `MG_SEED` set to some integer, that integer will be used as the seed.  

To set up MadGraph after having set all the relevant variables in `simSettings.py`, go to the `DMann` main directory where the scripts are and run `python setupMG.py` in a terminal. This creates one MadGraph output folder for each combination of WIMP mass and annihilation channel.

To actually run MadGraph on the created folders after setting up, simply run `python runMG.py` in the `DMann` main directory. This will run MadGraph for the chosen number of annihilations for all the folders created in the set up stage. Note that for more than 100000 events, several folders are created for each run, this is because the MadGraph command `multi_run` is used, which will here separate the run into subruns of 100000 events each. Note also that in the final states where MadSpin is used, there will not be any merged LHEF with all the events, but only the subrun LHEFs with 100000 events each. The folder names containing the LHEF with decayed events are the ones ending with "decayed_1". 

It will not work to run the scripts from another directory than the `DMann` main directory.

# To run Pythia8 on the created LHEF
To set up Pythia8 for running, you must first compile the main program `DMannPythia8LHE` that will be used, which is in the `DMann/Pythia` subdirectory. Edit the makefile to account for where ROOT and Pythia are installed on your system and run `make DMannPythia8LHE` in the `Pythia` subdirectory (the GZIP locations will probably not have to be changed). You may have to activate the ROOT environment variables by typing in the terminal `source activate ROOTDIR/bin/thisroot.sh`. Then go back to the `DMann` main directory and run `python runPythia.py`. This will run pythia on all the gzipped LHEF in parallell (using the full number of cores on the computer). 

You can also simply run the `runPythia.sh` bash script to perform all the above steps and run Pythia8, however this requires that you supply the correct ROOT installation directory in the second line of that script. 

The output directory for the histogram and event files created by Pythia are placed in the folder specified by the variable `DMANN_OUTDIR` in `simSettings.py`. If the option `GZIP_EVTFILE` in `simSettings.py` is set to `True`, event files will be gzipped after running has finished. This saves a lot of space but takes time. Use of this option requires that you have succesfully compiled Pythia8 with the option `--with-gzip`.

For less than 100000 events, one output folder called `Pythia` is created in the `DMANN_OUTDIR` directory. For more than 100000 events, Pythia is run 100000 events at a time (again, not that for more than 100000 events, the number must be a multiple of 100000), and then each 100000 events gets one directory in `DMANN_OUTDIR` named as `Pythia_i` where `i` is an integer from 1 to number of events divided by 100000 (for example, 2 folders `Pythia_1` and `Pythia_2` are created if simulating 200000 events). The events in the respective folders can be combined since they are statistically independent (have different seeds).

# To run Herwig7
To be added...


# How to run Herwig on mac with the docker image 
1. Download Docker for Mac
2. Go to a terminal and type "docker pull jmcornell/herwig-bootstrap". This downloads the Herwig docker image and will take some time.
3. To run a container, type "docker run -i -t jmcornell/herwig-bootstrap". To be able to access local files, see below.
4. The container contains a Herwig installation, so once in the container, Herwig can be run with the usual commands like `read`, `run`, etc. Notably you can run the `runHerwig.py` and `runHerLHE.py` scripts if you mount the `DMann` directory in the container.

# General tips
* Go to the Docker settings and under Preferences->Advanced, increase the number of CPU:s and memory available to the container. The default is rather low.
* To mount a directory, use the `-v` flag. For example: `docker run -v dir/on/local:dir/on/container -i -t jmcornell/herwig-bootstrap` will mount the directory `dir/on/local` from the local computer to the directory `dir/in/container` in the container. You can mount several directories by using the `-v` flag multiple times.

# DMann
Project on uncertainties in production fluxes from dark matter annihilation. Simulates WIMP annihilations into various final states and produces datafiles with the yields of various secondary particles of interest binned in kinetic energy.

## How to run, PYTHIA8
Go to the folder `Pythia`. To compile, first provide the correct path to the corresponding Pythia8 directories in the variables `PREFIX_BIN/INCLUDE/LIB/SHARE` in the makefile. An installation of `ROOT` is required since `ROOT` TH1F histograms are used. Provide the `ROOT` directories in the variables `ROOT_BIN/INCLUDE/LIB`. Then simply type 'make'.

The python script `MakeRunPythia.py` is responsible to create the text files (`.cmnd`) needed to run the C++ main program. In that script one specifies the WIMP masses and annihilation channels of interest, the script then creates one `cmnd`-file for each WIMP mass and annihilation channel and puts them in the folder `Runs-todo`. Other parameters of the runs can also be changed in that file, for example changing decay properties of certain particles etc.

Running the shell script `RunPythia.sh` will, if necessary, create the run files, compile the main program  `DMannPythia8.cc` and run it for all the produced run files. 

Run files are organised in three directories: `Runs-todo`, `Runs-running` and `Runs-done`. `Runs-todo` contains `cmnd`-files corresponding to runs that have not yet been done. The runscript takes a file from `Runs-todo` and moves this to `Runs-running` and runs `DMannPythia8` with this file. When this is done the run file is moved to `Runs-done`. This process continues until there are no more files left in `Runs-todo`. This means that multiple threads running the runscript can be started simultaneously to speed up the process. 

*Note:* it is sometimes necessary to activate the `ROOT` environment variables by typing `source $ROOTDIR/bin/thisroot.sh` where `$ROOTDIR` is the `ROOT` installation directory.

The PDG codes of the yield/secondary particles of interest (gammas, neutrinos, antiprotons etc.) are defined in the main program `DMannPythia8.cc` as elements in the vector 'yieldpdgs'. 

One output file per WIMP mass, annihilation channel and yield particle is put in the folder `Pythia8Data`. In the files, the columns correspond to 1) kinetic energy bins and 2) number of particles per annihilation per energy bin (number of particles per energy bin divided by the total number of WIMP annihilations).


## How to run, Herwig7
Go to the folder `Herwig`. Provide the necessary Herwig include directory in the variable `CPP_FLAGS` in the makefile and then type `make`. This will compile the `C++` files responsible for the actual analysis of each event (`DMannYields`) and the model files corresponding to the simple model used to simulate to WIMP annihilations (`FRModel` files). Then run the shell script `RunHerwig.sh`. This will construct the necessary run files (`.in`-files) and put them in the folder `Runs-todo` and run Herwig with these files, which produces datafiles in the folder `Herwig7Data`. 

*Note:* it is sometimes necessary to activate the Herwig environment variables by typing `source $HERDIR/activate/bin` where `$HERDIR` is the Herwig installation directory.

One output file per WIMP mass, annihilation channel and yield particle is put in the folder `Herwig7Data`. In the files, the columns correspond to 1) lower limit of kinetic energy bin 2) upper limit of kinetic energy bin, 3) some normalised output (not used at all) and 4) number of particles per annihilation per energy bin (number of particles per energy bin divided by the total number of WIMP annihilations).

The run script works in the same way as the Pythia run script with regards to the folders `Runs-todo`, `Runs-running` and `Runs-done` and multiple cores can be used to speed everything up as described above.

### How to construct the new model files from UFO files
UFO files can be used to define a new BSM model in Herwig through the command line interface `ufo2herwig`. The folder `UFOfiles` contains a file with instructions on how this is done.

# DMann
Project on uncertainties in production fluxes from dark matter annihilation.

## How to run, PYTHIA8
Running the shell script runscript.sh will, upon request, create the necessary text files (.cmnd) needed to run the C++ main program dmannmain.cc in three directories: runs-todo, runs-running and runs-done, compile this program and run it for all the produced run files.

Run files are organised in three directories: `runs-todo`, `runs-running` and `runs-done`. `runs-todo` contains files corresponding to runs that have not yet been done. The runscript takes a file from `runs-todo` and moves this to `runs-running` and runs dmannmain with this file. When this is done the run file is moved to `runs-done`. This process continues until there are no more files left in `runs-todo`. This means that multiple threads running the runscript can be started simultaneously to speed up the process. 

#!/bin/bash 

set -e # The -e flag causes the script to abort if any command exits with non-handled error code 

test=0

if [ $test -ne 1 ]; then

    # Flag -p creates directories only if not already existing 
    mkdir -p Pythia8Data
    mkdir -p Runs-running
    mkdir -p Runs-done
    runsdone=(`ls Runs-done`)
    if [ ${#runsdone[@]} -ne 0 ]; then
        echo "There are files in Runs-done. You should probably check that runs are not done twice."
        echo "Continue anyway?"
        select ans in "Yes, continue" "No, abort"; do
            case $ans in
                "Yes, continue" ) break;;
                "No, abort" ) exit;;
            esac
        done  
    fi
    
    echo "Do you want to create run files with MakeRunPythia.py?" 
    select ans in "Yes" "No"; do
        case $ans in
            Yes ) echo "Creating run files..."; python MakeRunPythia.py; echo "Done!"; break;;
            No ) break;;
        esac
    done
    #make -q dmannmain # returns 0 if up to date, 1 if update needed, 2 if make error
    #case $? in
    #    0 ) echo "make: DMannPythia8 up to date"; break;;
    #    1 ) echo "make: compiling DMannPythia8"; make DMannPythia8; echo "make: done"; break;;
    #    2 ) echo "make DMannPythia8: error, aborting"; exit;;
    #esac
    make DMannPythia8 # Compiles if not already up-to-date
    
    # Now create an array containing files in Runs-todo dir (returned by ls) and 
    # first check if this is empty (# returns length of an array). Then run DMannPythia8 
    # until number of entries in the filelist is zero.
    filelist=(`ls Runs-todo`) 
    if [ ${#filelist[@]} -eq 0 ]; then # True if ls returns empty list
        echo "No files in Runs-todo. Create with MakeRunPythia.py?"
        select ans in "Yes" "No" "Abort"; do
            case $ans in
                Yes ) mkdir -p Runs-todo; echo "Creating run files..."; python MakeRunPythia.py; filelist=(`ls Runs-todo`); echo "Done!"; break;;
                No ) break;; 
                Abort ) exit;;
            esac
        done
    fi
    file=$filelist # without index this takes the first file/entry from Runs-todo
    while [ ${#filelist[@]} -gt 0 ]; do 
        echo "Running DMann with file "$file
        mv "Runs-todo/"$file Runs-running
        ./DMannPythia8 "Runs-running/"$file > tmp.out
        mv "Runs-running/"$file Runs-done
        filelist=(`ls Runs-todo`) #reset value of file list
        file=$filelist
    done
    echo "No more files in Runs-todo"
fi

if [ $test -eq 1 ]; then    
    echo "*******************"
    echo "**** TEST mode ****"    
    echo "*******************"
    make DMannPythia8
    filelist=(`ls TEST-runs`) 
    file=$filelist # without index this takes the first file/entry from TEST-runs
    while [ ${#filelist[@]} -gt 0 ]; do 
        echo "Running DMann with file "$file
        ./DMannPythia8 "TEST-runs/"$file > tmp.out
        mv "TEST-runs/"$file Runs-done
        filelist=(`ls TEST-runs`) #reset value of file list
        file=$filelist
    done
    echo "No more files in TEST-runs"
    echo "Making plots"
    python plotscript.py yield testmode
    python plotscript.py ann testmode    
fi
    

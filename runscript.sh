#!/bin/sh 

set -e # The -e flag causes the script to abort if any command exits with non-handled error code 

test=1

if [ $test -ne 1 ]; then

    # Flag -p creates directories only if not already existing 
    mkdir -p pythia8data
    mkdir -p runs-running
    mkdir -p runs-done
    runsdone=(`ls runs-done`)
    if [ ${#runsdone[@]} -ne 0 ]; then
        echo "There are files in runs-done. You should probably check that runs are not done twice."
        echo "Continue anyway?"
        select ans in "Yes, continue" "No, abort"; do
            case $ans in
                "Yes, continue" ) break;;
                "No, abort" ) exit;;
            esac
        done  
    fi
    
    echo "Do you want to create run files with makerun.py?" 
    select ans in "Yes" "No"; do
        case $ans in
            Yes ) echo "Creating run files..."; python makerun.py; echo "Done!"; break;;
            No ) break;;
        esac
    done
    #make -q dmannmain # returns 0 if up to date, 1 if update needed, 2 if make error
    #case $? in
    #    0 ) echo "make: dmannmain up to date"; break;;
    #    1 ) echo "make: compiling dmannmain"; make dmannmain; echo "make: done"; break;;
    #    2 ) echo "make dmannmain: error, aborting"; exit;;
    #esac
    make dmannmain # Compiles if not already up-to-date
    
    # Now create an array containing files in runs-todo dir (returned by ls) and 
    # first check if this is empty (# returns length of an array). Then run DMann 
    # until number of entries in the filelist is zero.
    filelist=(`ls runs-todo`) 
    if [ ${#filelist[@]} -eq 0 ]; then # True if ls returns empty list
        echo "No files in runs-todo. Create with makerun.py?"
        select ans in "Yes" "No" "Abort"; do
            case $ans in
                Yes ) mkdir -p runs-todo; echo "Creating run files..."; python makerun.py; filelist=(`ls runs-todo`); echo "Done!"; break;;
                No ) break;; 
                Abort ) exit;;
            esac
        done
    fi
    file=$filelist # without index this takes the first file/entry from runs-todo
    while [ ${#filelist[@]} -gt 0 ]; do 
        echo "Running DMann with file "$file
        mv "runs-todo/"$file runs-running
        ./dmannmain "runs-running/"$file > tmp.out
        mv "runs-running/"$file runs-done
        filelist=(`ls runs-todo`) #reset value of file list
        file=$filelist
    done
    echo "No more files in runs-todo"
fi

if [ $test -eq 1 ]; then    
    echo "*******************"
    echo "**** TEST mode ****"    
    echo "*******************"
    make dmannmain
    filelist=(`ls TEST-runs`) 
    file=$filelist # without index this takes the first file/entry from TEST-runs
    while [ ${#filelist[@]} -gt 0 ]; do 
        echo "Running DMann with file "$file
        ./dmannmain "TEST-runs/"$file > tmp.out
        mv "TEST-runs/"$file runs-done
        filelist=(`ls TEST-runs`) #reset value of file list
        file=$filelist
    done
    echo "No more files in TEST-runs"
    echo "Making plots"
    python plotscript.py yield testmode
    python plotscript.py ann testmode    
fi
    
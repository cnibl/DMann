#!/bin/bash 

set -e # The -e flag causes the script to abort if any command exits with non-handled error code 

herwigdir=/home/carlniblaeus/Herwig7 # NOTE: this may have to be changed depending on where Herwig is installed
source $herwigdir/bin/activate # set necessary Herwig environment variables 
test=0
if [ $test -ne 1 ]; then

    # Flag -p creates directories only if not already existing 
    mkdir -p Herwig7Data
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
    
    echo "Do you want to create run files with MakeRunHerwig.py?" 
    select ans in "Yes" "No"; do
        case $ans in
            Yes ) echo "Creating run files..."; python MakeRunHerwig.py; echo "Done!"; break;;
            No ) break;;
        esac
    done

    make DMannYields.so # Compiles Herwig Analysis Handler if not already up-to-date
    
    # Now create an array containing files in runs-todo dir (returned by ls) and 
    # first check if this is empty (# returns length of an array). Then run DMann 
    # until number of entries in the filelist is zero.
    filelist=(`ls Runs-todo`) 
    if [ ${#filelist[@]} -eq 0 ]; then # True if ls returns empty list
        echo "No files in Runs-todo. Create with MakeRunHerwig.py?"
        select ans in "Yes" "No" "Abort"; do
            case $ans in
                Yes ) mkdir -p Runs-todo; echo "Creating run files..."; python MakeRunHerwig.py; filelist=(`ls Runs-todo`); echo "Done!"; break;;
                No ) break;; 
                Abort ) exit;;
            esac
        done
    fi
    file=$filelist # without index this takes the first file/entry from Runs-todo
    while [ ${#filelist[@]} -gt 0 ]; do 
        echo "Running DMann with file "$file
        mv "Runs-todo/"$file Runs-running
        Herwig read "Runs-running/"$file
        echo "Done with file "$file
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
    make dmannmain
    filelist=(`ls TEST-runs`) 
    file=$filelist # without index this takes the first file/entry from TEST-runs
    while [ ${#filelist[@]} -gt 0 ]; do 
        echo "Running DMann with file "$file
        Herwig read "TEST-runs/"$file
        mv "TEST-runs/"$file Runs-done
        filelist=(`ls TEST-runs`) #reset value of file list
        file=$filelist
    done
    echo "No more files in TEST-runs"
    #echo "Making plots"
    #python plotscript.py yield testmode
    #python plotscript.py ann testmode    
fi
    

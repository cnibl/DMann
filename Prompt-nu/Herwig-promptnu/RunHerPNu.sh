#!/bin/bash 

set -e # The -e flag causes the script to abort if any command exits with non-handled error code 

herwigdir=/home/carlniblaeus/Herwig7 # NOTE: this may have to be changed depending on where Herwig is installed
source $herwigdir/bin/activate # set necessary Herwig environment variables 

# Flag -p creates directories only if not already existing 
mkdir -p Herwig7DataPromptNu
mkdir -p Runs

echo "Do you want to create run files with MakeRunHerPNu.py?" 
select ans in "Yes" "No"; do
    case $ans in
        Yes ) echo "Creating run files..."; python MakeRunHerPNu.py; echo "Done!"; break;;
        No ) break;;
    esac
done

make DMannYields.so # Compiles Herwig Analysis Handler if not already up-to-date
make FRModel.so # Compiles FeynRules model files if not already up-to-date

# Now create an array containing files in runs-todo dir (returned by ls) and 
# first check if this is empty (# returns length of an array). Then run DMann 
# until number of entries in the filelist is zero.
filelist=(`ls Runs`) 
if [ ${#filelist[@]} -eq 0 ]; then # True if ls returns empty list
    echo "No files in Runs. Create with MakeRunHerPNu.py?"
    select ans in "Yes" "No" "Abort"; do
        case $ans in
            Yes ) mkdir -p Runs; echo "Creating run files..."; python MakeRunHerPNu.py; filelist=(`ls Runs-todo`); echo "Done!"; break;;
            No ) break;; 
            Abort ) exit;;
        esac
    done
fi
file=$filelist # without index this takes the first file/entry from Runs
#if [ ${#filelist[@]} -gt 0 ]; do 
#    echo "More than one file in Runsfolder, aborting. "
#    exit
#fi
Herwig read "Runs/"$file
echo "Done with file "$file

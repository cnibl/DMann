#!/bin/bash
cd /home/carlniblaeus/DMann/Herwig
make all
cd /home/carlniblaeus/DMann
source activate py27 #must be before Herwig activation!
source /home/carlniblaeus/Herwig7/bin/activate
python runHerwig.py


import subprocess
import sys
from runMG_helpfunctions import *




homedir="/home/carlniblaeus/"
MGdir="MG5_aMC_v2_6_3_2/"
mgscrname="MGscript.txt"
evtdir="testing"

runname="ee_h_ww"
mgscrname=write_MGscript(mX=200,annPDG=24,run=runname)
subprocess.call(["mv",mgscrname,homedir+MGdir])
#subprocess.call(["./bin/mg5_aMC",mgscrname],cwd=homedir+MGdir)
pa=write_paramcard(mX=200)
r=write_runcard(nAnn=1000,mX=200)
py=write_pythiacard()
rundir=''.join((homedir,MGdir,runname))
print [rundir+x+"/Cards/" for x in [pa,r,py]]
subprocess.call(["mv",pa,rundir+"/Cards/"+pa])
subprocess.call(["mv",r,rundir+"/Cards/"+r])
subprocess.call(["mv",py,rundir+"/Cards/"+py])
subprocess.call(["./bin/generate_events","-f",runname],cwd=rundir)

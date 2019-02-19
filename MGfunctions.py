"""
A library that contains functions used in the setupMG and runMG scripts.
"""
import os
import sys
import re
import subprocess

def annch_to_MGFinState(annch):
   if annch in ["WLWL","WTWT"]:
      return "w+ w-"
   elif annch in ["ZLZL","ZTZT"]:
      return "z z"
   elif annch=="hh":
      return "h h"
   elif annch in ["tLtL","tRtR"]:
      return "t t~"
   elif annch in ["taLtaL","taRtaR"]:
      return "ta+ ta-"
   elif annch in ["muLmuL","muRmuR"]:
      return "mu+ mu-, mu+ > e+ ve vm~, mu- > e- ve~ vm"
   elif annch=="ee":
      return "e+ e-"
   elif annch=="bb":
      return "b b~"
   elif annch=="cc":
      return "c c~"   
   elif annch=="ss":
      return "s s~"
   elif annch=="uu":
      return "u u~"
   elif annch=="dd":
      return "d d~"
   else:
      sys.exit("ERROR: unknown annihilation channel provided")
      
def write_MG_setupscript(annch):
   """
   Writes the MadGraph commands for generating the folder corresponding to input annch into a text file.
   """
   folderName="".join(("DMann_",annch))
   fileName="".join(("DMann_setupMG_",annch,".txt"))
   with open(fileName,"w") as f:
      f.write("import model DMann\n")
      f.write("generate xr xr > y0 > "+annch_to_MGFinState(annch)+"\n")
      f.write("output "+folderName+"\n")
      f.write("y")
   return fileName
   
def write_MG_runscript(annch,nAnn,runTag,mwimp):
   """
   Writes the MadGraph commands for running n_ann annihilations for input annch.
   """
   fileName="".join(("DMann_runMG_",annch,".txt"))
   with open(fileName,"w") as f:
      if nAnn < 100000:
         f.write("launch run_"+runTag+"_m"+str(mwimp)+"\n")
      else:
         f.write("multi_run "+str(nAnn/100000)+" run_"+runTag+"_m"+str(mwimp)+" --multicore --nb_core=4 \n")
      f.write("analysis=OFF\n")
      if annch in ["WLWL","WTWT","ZLZL","ZTZT","tLtL","tRtR"]:
         f.write("madspin=ON\n")
   return fileName  
   
def set_beam_particles():
   """
   Reads in the old param_card and replaces the necessary coupling parameters in a new param_card, written to the Cards directory. Assumes that it operates in a subfolder corresponding to the annihilation channel annch in the MG install directory.
   Input: annch - annihilation channel
   """
   oldcard_path=os.path.abspath(os.path.join("Cards","param_card.dat"))
   try:
      with open(oldcard_path,"r") as f:
         oldcard_content=f.read()
   except IOError:
      oldcard_path=os.path.abspath(os.path.join("Cards","param_card_default.dat"))
      with open(oldcard_path,"r") as f:
         oldcard_content=f.read()
   newcard_content=oldcard_content
   
   # Set coupling between incoming beams and resonance
   searchExpr=r"(\D*\d{1,2}) \d+\.?\d*[eE]?\+?\d{1,2}"  # the part before the coupling name
   newcard_content = re.sub(searchExpr+r" # gSXr",r"\1 1.000000e+00 # gSXr",newcard_content) # must be non-zero for collisions
   
   # Set incoming beams to be massless
   newcard_content = re.sub(r"9000008.+# MXr",r"9000008 0.0 # MXr",newcard_content) 

   # Write new card content to file
   with open(os.path.abspath(os.path.join("Cards","param_card.dat")),"w") as f:
      f.write(newcard_content)
      
   return
   
def set_couplings(annch):
   """
   Reads in the old param_card and replaces the necessary coupling parameters in a new param_card, written to the Cards directory. Assumes that it operates in a subfolder corresponding to the annihilation channel annch in the MG install directory.
   Input: annch - annihilation channel
   """
   oldcard_path=os.path.abspath(os.path.join("Cards","param_card.dat"))
   try:
      with open(oldcard_path,"r") as f:
         oldcard_content=f.read()
   except IOError:
      oldcard_path=os.path.abspath(os.path.join("Cards","param_card_default.dat"))
      with open(oldcard_path,"r") as f:
         oldcard_content=f.read()
   newcard_content=oldcard_content
   
   # Set couplings for annihilation channel. Checks for numbers in integer, decimal or scientific form
   searchExpr=r"(\D*\d{1,2}) \d+\.?\d*[eE]?\+?\d{1,2}"  # the part before the coupling name
   newcard_content = re.sub(searchExpr+r" # g([a-zA-Z0-9]+)",r"\1 0.000000e+00 # g\2",newcard_content) # reset all couplings to zero

   # Electroweak bosons
   if annch in ["WLWL","ZLZL"]:
      newcard_content = re.sub(searchExpr+r" # gSWL",r"\1 1.000000e+00 # gSWL",newcard_content) 
      newcard_content = re.sub(searchExpr+r" # gSBL",r"\1 1.000000e+00 # gSBL",newcard_content) 
   if annch in ["WTWT","ZTZT"]:
      newcard_content = re.sub(searchExpr+r" # gSWT",r"\1 1.000000e+00 # gSWT",newcard_content) 
      newcard_content = re.sub(searchExpr+r" # gSBT",r"\1 1.000000e+00 # gSBT",newcard_content)
   if annch=="hh":
      newcard_content = re.sub(searchExpr+r" # gSh1",r"\1 1.000000e+00 # gSh1",newcard_content) 
      newcard_content = re.sub(searchExpr+r" # gSh2",r"\1 1.000000e+00 # gSh2",newcard_content)
   # Leptons
   if annch in ["taLtaL","taRtaR"]:
      newcard_content = re.sub(searchExpr+r" # gSta",r"\1 1.000000e+00 # gSta",newcard_content) 
      if annch=="taLtaL":
         newcard_content = re.sub(searchExpr+r" # gPta",r"\1 -1.000000e+00 # gPta",newcard_content)
      elif annch=="taRtaR":
         newcard_content = re.sub(searchExpr+r" # gPta",r"\1 1.000000e+00 # gPta",newcard_content)   
   if annch in ["muLmuL","muRmuR"]:
      newcard_content = re.sub(searchExpr+r" # gSmm",r"\1 1.000000e+00 # gSmm",newcard_content) 
      if annch=="muLmuL":
         newcard_content = re.sub(searchExpr+r" # gPmm",r"\1 -1.000000e+00 # gPmm",newcard_content)
      elif annch=="muRmuR":
         newcard_content = re.sub(searchExpr+r" # gPmm",r"\1 1.000000e+00 # gPmm",newcard_content)       
   if annch=="ee":
      newcard_content = re.sub(searchExpr+r" # gSe",r"\1 1.000000e+00 # gSe",newcard_content) 
   # Quarks
   if annch in ["tLtL","tRtR"]:
      newcard_content = re.sub(searchExpr+r" # gSu33",r"\1 1.000000e+00 # gSu33",newcard_content) 
      if annch=="tLtL":
         newcard_content = re.sub(searchExpr+r" # gPu33",r"\1 -1.000000e+00 # gPu33",newcard_content)
      elif annch=="tRtR":
         newcard_content = re.sub(searchExpr+r" # gPu33",r"\1 1.000000e+00 # gPu33",newcard_content)  
   if annch=="bb":
      newcard_content = re.sub(searchExpr+r" # gSd33",r"\1 1.000000e+00 # gSd33",newcard_content) 
   if annch=="cc":
      newcard_content = re.sub(searchExpr+r" # gSu22",r"\1 1.000000e+00 # gSu22",newcard_content) 
   if annch=="ss":
      newcard_content = re.sub(searchExpr+r" # gSd22",r"\1 1.000000e+00 # gSd22",newcard_content) 
   if annch=="uu":
      newcard_content = re.sub(searchExpr+r" # gSu11",r"\1 1.000000e+00 # gSu11",newcard_content) 
   if annch=="dd":
      newcard_content = re.sub(searchExpr+r" # gSd11",r"\1 1.000000e+00 # gSd11",newcard_content) 
   
   # Write new card content to file
   with open(os.path.abspath(os.path.join("Cards","param_card.dat")),"w") as f:
      f.write(newcard_content)

   return 
   
def set_wimp_mass(mwimp):
   """
   Reads in the old param_card and replaces the WIMP mass with input value in a new param_card, written to the Cards directory. Assumes that it operates in a subfolder corresponding to some annihilation channel in the MG install directory.
   Input: mwimp - WIMP mass
   """
   for cardType in ["param","run"]:
      oldcard_path=os.path.abspath(os.path.join("Cards",cardType+"_card.dat"))
      try:
         with open(oldcard_path,"r") as f:
            oldcard_content=f.read()
      except IOError:
         oldcard_path=os.path.abspath(os.path.join("Cards",cardType+"_card_default.dat"))
         with open(oldcard_path,"r") as f:
            oldcard_content=f.read()
      newcard_content=oldcard_content
      
      # Set WIMP mass. Checks for numbers in integer, decimal or scientific form
      if cardType=="param":
         #newcard_content = re.sub(r"\n\s*(\d+).+#\s*MD0",r"\n  \1 "+str(2*mwimp)+"  # MD0",newcard_content) # set mediator mass
         newcard_content = re.sub(r"9000006.+# MD0",r"9000006 "+str(2*mwimp)+" # MD0",newcard_content) # set mediator mass
      if cardType=="run":
	      newcard_content = re.sub(r"\n.+= ebeam1 ","".join(("\n  ",str(mwimp)," = ebeam1 ")),newcard_content)  # beam energy 1
	      newcard_content = re.sub(r"\n.+= ebeam2 ","".join(("\n  ",str(mwimp)," = ebeam2 ")),newcard_content)  # beam energy 2
         #newcard_content = re.sub(r".*= scale ","".join(("  ",str(mwimp)," = scale ")),newcard_content) # scale (set this?)
	      #newcard_content = re.sub(r".*= dsqrt_q2fact1 ","".join(("  ",str(mwimp)," = dsqrt_q2fact1 ")),newcard_content)  # scale pdf1 (prob not used) (set this?)
	      #newcard_content = re.sub(r".*= dsqrt_q2fact2 ","".join(("  ",str(mwimp)," = dsqrt_q2fact2 ")),newcard_content)  # scale pdf2 (prob not used) (set this?)
   
      # Write new card content to file
      with open(os.path.abspath(os.path.join("Cards",cardType+"_card.dat")),"w") as f:
         f.write(newcard_content)
         
   return 
   
def set_n_ann(n_ann):
   """
   Reads in the old run_card and replaces the number of events with input value in a new run_card, written to the Cards directory. Assumes that it operates in a subfolder corresponding to some annihilation channel in the MG install directory.
   Input: n_ann - number of annihilations to simulate
   """
   oldcard_path=os.path.abspath(os.path.join("Cards","run_card.dat"))
   try:
      with open(oldcard_path,"r") as f:
         oldcard_content=f.read()
   except IOError:
      oldcard_path=os.path.abspath(os.path.join("Cards","run_card_default.dat"))
      with open(oldcard_path,"r") as f:
         oldcard_content=f.read()
   newcard_content=oldcard_content
   
   # Set number of events, run max 100k events per run (for more events, multi_run is used).
   if n_ann <= 100000:
      newcard_content = re.sub(r".*= nevents ","".join( ("  ",str(n_ann)," = nevents ") ),newcard_content)  # number of events
   else:
      newcard_content = re.sub(r".*= nevents ","".join( ("  ",str(100000)," = nevents ") ),newcard_content)  # number of events
   
   # Write new card content to file
   with open(os.path.abspath(os.path.join("Cards","run_card.dat")),"w") as f:
      f.write(newcard_content)
   
   return    
   
def set_run_tag(runTag):
   """
   Reads in the old run_card and replaces the run_tag with input value in a new run_card, written to the Cards directory. Assumes that it operates in a subfolder corresponding to some annihilation channel in the MG install directory.
   Input: run_tag - name for the runs
   """
   
   oldcard_path=os.path.abspath(os.path.join("Cards","run_card.dat"))
   try:
      with open(oldcard_path,"r") as f:
         oldcard_content=f.read()
   except IOError:
      oldcard_path=os.path.abspath(os.path.join("Cards","run_card_default.dat"))
      with open(oldcard_path,"r") as f:
         oldcard_content=f.read()
   newcard_content=oldcard_content
   
   # Set run tag.
   newcard_content=re.sub(r"\n\s*\S+\s*=\s?run_tag","\n "+runTag+" = run_tag",newcard_content) # run name

   # Write new card content to file
   with open(os.path.abspath(os.path.join("Cards","run_card.dat")),"w") as f:
      f.write(newcard_content)
   
   return    
   
def set_madspin_card(annch):
   """
   Reads in the old madspin_card and replaces the necessary parameters in a new card, written to the Cards directory. Assumes that it operates in a subfolder corresponding to annihilation channel annch in the MG install directory.
   Input: annch - annihilation channel
   """
   oldcard_path=os.path.abspath(os.path.join("Cards","madspin_card.dat"))
   try:
      with open(oldcard_path,"r") as f:
         oldcard_content=f.read()
   except IOError:
      oldcard_path=os.path.abspath(os.path.join("Cards","madspin_card_default.dat"))
      with open(oldcard_path,"r") as f:
         oldcard_content=f.read()
   newcard_content = oldcard_content
   
   # Comment out all decays, then turn on decay for annihilation channel   
   newcard_content = re.sub(r"\n\s*decay( .+ > )",r"\n#decay\1",newcard_content)
   if annch in ["WLWL","WTWT"]:
      newcard_content = re.sub(r"\n#+decay w",r"\ndecay w",newcard_content) 
   if annch in ["ZLZL","ZTZT"]:
      newcard_content = re.sub(r"\n#+decay z",r"\ndecay z",newcard_content) 
   if annch in ["tLtL","tRtR"]:
      newcard_content = re.sub(r"\n#+decay t",r"\ndecay t",newcard_content) 
      newcard_content = re.sub(r"\n#+decay t~",r"\ndecay t~",newcard_content) 
   
   # Write new card content to file
   with open(os.path.abspath(os.path.join("Cards","madspin_card.dat")),"w") as f:
      f.write(newcard_content)

   return

def reset_cuts():
   """
   Reads in the old run_card and removes all standard cuts and places in a new run_card, written to the Cards directory. Assumes that it operates in a subfolder corresponding to some annihilation channel in the MG install directory.
   """
   
   oldcard_path=os.path.abspath(os.path.join("Cards","run_card.dat"))
   try:
      with open(oldcard_path,"r") as f:
         oldcard_content=f.read()
   except IOError:
      oldcard_path=os.path.abspath(os.path.join("Cards","run_card_default.dat"))
      with open(oldcard_path,"r") as f:
         oldcard_content=f.read()
   newcard_content=oldcard_content
   
   # Minimum pt's
   newcard_content=re.sub(r"\n\s*\S+\s*=\s?ptj","\n 0.0 = ptj",newcard_content) 
   newcard_content=re.sub(r"\n\s*\S+\s*=\s?ptb","\n 0.0 = ptb",newcard_content) 
   newcard_content=re.sub(r"\n\s*\S+\s*=\s?pta","\n 0.0 = pta",newcard_content)
   newcard_content=re.sub(r"\n\s*\S+\s*=\s?ptl","\n 0.0 = ptl",newcard_content)  

   # Max and min absolute rapidity
   newcard_content=re.sub(r"\n\s*\S+\s*=\s?etaj","\n -1.0 = etaj",newcard_content) 
   newcard_content=re.sub(r"\n\s*\S+\s*=\s?etaa","\n -1.0 = etaa",newcard_content) 
   newcard_content=re.sub(r"\n\s*\S+\s*=\s?etal","\n -1.0 = etal",newcard_content) 

   # Max and min deltaR distance
   newcard_content=re.sub(r"\n\s*\S+\s*=\s?drjj","\n 0.0 = drjj",newcard_content) 
   newcard_content=re.sub(r"\n\s*\S+\s*=\s?drll","\n 0.0 = drll",newcard_content) 
   newcard_content=re.sub(r"\n\s*\S+\s*=\s?draj","\n 0.0 = draj",newcard_content)
   newcard_content=re.sub(r"\n\s*\S+\s*=\s?drjl","\n 0.0 = drjl",newcard_content) 
   newcard_content=re.sub(r"\n\s*\S+\s*=\s?draa","\n 0.0 = draa",newcard_content)
   newcard_content=re.sub(r"\n\s*\S+\s*=\s?dral","\n 0.0 = dral",newcard_content) 

   # Write new card content to file
   with open(os.path.abspath(os.path.join("Cards","run_card.dat")),"w") as f:
      f.write(newcard_content)
   
   return    
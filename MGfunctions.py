"""
A library that contains functions used in the setupMG and runMG scripts.
"""
import os
import sys
import re
import subprocess

# The threshold in GeV that the WIMP mass has to exceed for annihilations to be possible
annThresholds={"WLWL" : 80.4, "WTWT" : 80.4, "ZLZL" : 91.2, "ZTZT" : 91.2, "hh" : 125.2, 
               "taLtaL" : 1.8, "taRtaR" : 1.8, "taLtaR" : 1.8, "taRtaL" : 1.8, "muLmuL" : 0.11, "muRmuR" : 0.11, "muLmuR" : 0.11, "muRmuL" : 0.11, "ee" : 5.2e-6, 
               "tLtL" : 173., "tRtR" : 173., "tLtR" : 173., "tRtL" : 173., "bb" : 4.8, "cc" : 1.3, "ss" : 0.1, "uu" : 2.6e-3, "dd" : 5.1e-3}
               
               
def annch_to_MGFinState(annch,madspin):
   if annch in ["WLWL","WTWT"]:
      if madspin==True:
         return "w+ w-"
      else:
         return "w+ w-, w+ > allsm allsm, w- > allsm allsm"
   elif annch in ["ZLZL","ZTZT"]:
      if madspin==True:
         return "z z"
      else:
         return "z z, z > allsm allsm"
   elif annch=="hh":
      return "h h"
   elif annch in ["tLtL","tRtR","tLtR","tRtL"]:
      if madspin==True:
         return "t t~"
      else:
         return "t t~, (t > b w+, w+ > allsm allsm), (t~ > b~ w-, w- > allsm allsm)"
   elif annch in ["taLtaL","taRtaR","taLtaR","taRtaL"]:
      return "ta+ ta-"
   elif annch in ["muLmuL","muRmuR","muLmuR","muRmuL"]:
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
      
def write_MG_setupscript(annch,mx,runTag,madspin):
   """
   Writes the MadGraph commands for generating the folder corresponding to ann. channel annch and wimp mass mx into a text file.
   """
   folderName="".join(("DMann_",runTag,"_",annch,"_m",str(mx)))
   fileName="".join(("log_DMann/DMann_setupMG_",runTag,"_",annch,"_m",str(mx),".txt"))
   with open(fileName,"w") as f:
      f.write("import model DMann\n")
      f.write("define allsm = u d c s b u~ d~ c~ s~ b~ e+ mu+ ta+ e- mu- ta- ve vm vt ve~ vm~ vt~\n")
      if annch not in ["taLtaR","taRtaL","tRtL","tLtR","muRmuL","muLmuR"]:
         f.write("generate xr xr > y0 > "+annch_to_MGFinState(annch,madspin)+"\n")
      else:
         f.write("generate xd xd~ > y1 > "+annch_to_MGFinState(annch,madspin)+"\n")
      f.write("output "+folderName+"\n")
      f.write("y")
   return fileName
   
def write_MG_runscript(annch,nAnn,runTag,mwimp,ncores,madspin):
   """
   Writes the MadGraph commands for running n_ann annihilations for input annch.
   """
   fileName="".join(("DMann_runMG_",annch,".txt"))
   with open(fileName,"w") as f:
      if nAnn < 100000:
         f.write("launch run_"+runTag+"\n")
      else:
         f.write("multi_run "+str(nAnn/100000)+" run_"+runTag+" --multicore --nb_core="+str(ncores)+" \n")
      f.write("analysis=OFF\n")
      if madspin==True and annch in ["WLWL","WTWT","ZLZL","ZTZT","tLtL","tRtR","tLtR","tRtL"]:
         f.write("madspin=ON\n")
      else:
         f.write("madspin=OFF\n")         
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
   newcard_content = re.sub(searchExpr+r" # gSXr",r"\1 1.000000e+00 # gSXr",newcard_content) # must be non-zero for y0 collisions
   newcard_content = re.sub(searchExpr+r" # gAXd",r"\1 1.000000e+00 # gAXd",newcard_content) # must be non-zero for y1 collisions
   
   # Set incoming beams to be massless
   newcard_content = re.sub(r"9000008.+# MXr",r"9000008 0.0 # MXr",newcard_content) 
   newcard_content = re.sub(r"9000010.+# MXd",r"9000010 0.0 # MXd",newcard_content) 

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
   if annch in ["taLtaL","taRtaR"]: #scalar
      newcard_content = re.sub(searchExpr+r" # gSta",r"\1 1.000000e+00 # gSta",newcard_content) 
      if annch=="taLtaL":
         newcard_content = re.sub(searchExpr+r" # gPta",r"\1 -1.000000e+00 # gPta",newcard_content)
      elif annch=="taRtaR":
         newcard_content = re.sub(searchExpr+r" # gPta",r"\1 1.000000e+00 # gPta",newcard_content)   
   if annch in ["taLtaR","taRtaL"]: #vector
      newcard_content = re.sub(searchExpr+r" # gVta",r"\1 1.000000e+00 # gVta",newcard_content) 
      if annch=="taLtaR":
         newcard_content = re.sub(searchExpr+r" # gAta",r"\1 -1.000000e+00 # gAta",newcard_content)
      elif annch=="taRtaL":
         newcard_content = re.sub(searchExpr+r" # gAta",r"\1 1.000000e+00 # gAta",newcard_content)   
   if annch in ["muLmuL","muRmuR"]: # scalar
      newcard_content = re.sub(searchExpr+r" # gSmm",r"\1 1.000000e+00 # gSmm",newcard_content) 
      if annch=="muLmuL":
         newcard_content = re.sub(searchExpr+r" # gPmm",r"\1 -1.000000e+00 # gPmm",newcard_content)
      elif annch=="muRmuR":
         newcard_content = re.sub(searchExpr+r" # gPmm",r"\1 1.000000e+00 # gPmm",newcard_content)       
   if annch in ["muLmuR","muRmuL"]: # vector
      newcard_content = re.sub(searchExpr+r" # gVmm",r"\1 1.000000e+00 # gVmm",newcard_content) 
      if annch=="muLmuR":
         newcard_content = re.sub(searchExpr+r" # gAmm",r"\1 -1.000000e+00 # gAmm",newcard_content)
      elif annch=="muRmuL":
         newcard_content = re.sub(searchExpr+r" # gAmm",r"\1 1.000000e+00 # gAmm",newcard_content)
   if annch=="ee":
      newcard_content = re.sub(searchExpr+r" # gSe",r"\1 1.000000e+00 # gSe",newcard_content) 
   # Quarks
   if annch in ["tLtL","tRtR"]: # scalar
      newcard_content = re.sub(searchExpr+r" # gSu33",r"\1 1.000000e+00 # gSu33",newcard_content) 
      if annch=="tLtL":
         newcard_content = re.sub(searchExpr+r" # gPu33",r"\1 -1.000000e+00 # gPu33",newcard_content)
      elif annch=="tRtR":
         newcard_content = re.sub(searchExpr+r" # gPu33",r"\1 1.000000e+00 # gPu33",newcard_content)  
   if annch in ["tLtR","tRtL"]: # vector
      newcard_content = re.sub(searchExpr+r" # gVu33",r"\1 1.000000e+00 # gVu33",newcard_content) 
      if annch=="tLtR":
         newcard_content = re.sub(searchExpr+r" # gAu33",r"\1 -1.000000e+00 # gAu33",newcard_content)
      elif annch=="tRtL":
         newcard_content = re.sub(searchExpr+r" # gAu33",r"\1 1.000000e+00 # gAu33",newcard_content)  
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
         newcard_content = re.sub(r"9000007.+# MD1",r"9000007 "+str(2*mwimp)+" # MD1",newcard_content) # set mediator mass
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
   newcard_content=re.sub(r"\n\s*\S+\s*=\s?ptj[^a-z]\s+","\n 0.0 = ptj ",newcard_content) 
   newcard_content=re.sub(r"\n\s*\S+\s*=\s?ptb[^a-z]\s+","\n 0.0 = ptb ",newcard_content) 
   newcard_content=re.sub(r"\n\s*\S+\s*=\s?pta[^a-z]\s+","\n 0.0 = pta ",newcard_content)
   newcard_content=re.sub(r"\n\s*\S+\s*=\s?ptl[^a-z]\s+","\n 0.0 = ptl ",newcard_content)  
   newcard_content=re.sub(r"\n\s*\S+\s*=\s?misset[^m]\s+","\n 0.0 = misset ",newcard_content)  
   newcard_content=re.sub(r"\n\s*\S+\s*=\s?ptjmax\s+","\n -1.0 = ptjmax ",newcard_content) 
   newcard_content=re.sub(r"\n\s*\S+\s*=\s?ptbmax\s+","\n -1.0 = ptbmax ",newcard_content) 
   newcard_content=re.sub(r"\n\s*\S+\s*=\s?ptamax\s+","\n -1.0 = ptamax ",newcard_content)
   newcard_content=re.sub(r"\n\s*\S+\s*=\s?ptlmax\s+","\n -1.0 = ptlmax ",newcard_content) 
   newcard_content=re.sub(r"\n\s*\S+\s*=\s?missetmax\s+","\n -1.0 = missetmax ",newcard_content)  

   # Max and min absolute rapidity
   newcard_content=re.sub(r"\n\s*\S+\s*=\s?etaj[^m]\s+","\n -1.0 = etaj ",newcard_content) 
   newcard_content=re.sub(r"\n\s*\S+\s*=\s?etaa[^m]\s+","\n -1.0 = etaa ",newcard_content) 
   newcard_content=re.sub(r"\n\s*\S+\s*=\s?etal[^m]\s+","\n -1.0 = etal ",newcard_content) 

   # Max and min deltaR distance
   newcard_content=re.sub(r"\n\s*\S+\s*=\s?drjj[^a-z]\s+","\n 0.0 = drjj ",newcard_content) 
   newcard_content=re.sub(r"\n\s*\S+\s*=\s?drbb[^a-z]\s+","\n 0.0 = drbb ",newcard_content) 
   newcard_content=re.sub(r"\n\s*\S+\s*=\s?drll[^a-z]\s+","\n 0.0 = drll ",newcard_content) 
   newcard_content=re.sub(r"\n\s*\S+\s*=\s?draa[^a-z]\s+","\n 0.0 = draa ",newcard_content) 
   newcard_content=re.sub(r"\n\s*\S+\s*=\s?drbj[^a-z]\s+","\n 0.0 = drbj ",newcard_content)
   newcard_content=re.sub(r"\n\s*\S+\s*=\s?draj[^a-z]\s+","\n 0.0 = draj ",newcard_content) 
   newcard_content=re.sub(r"\n\s*\S+\s*=\s?drjl[^a-z]\s+","\n 0.0 = drjl ",newcard_content)
   newcard_content=re.sub(r"\n\s*\S+\s*=\s?drab[^a-z]\s+","\n 0.0 = drab ",newcard_content) 
   newcard_content=re.sub(r"\n\s*\S+\s*=\s?drbl[^a-z]\s+","\n 0.0 = drbl ",newcard_content)
   newcard_content=re.sub(r"\n\s*\S+\s*=\s?dral[^a-z]\s+","\n 0.0 = dral ",newcard_content) 

   newcard_content=re.sub(r"\n\s*\S+\s*=\s?drjjmax","\n -1.0 = drjjmax ",newcard_content) 
   newcard_content=re.sub(r"\n\s*\S+\s*=\s?drbbmax","\n -1.0 = drbbmax ",newcard_content) 
   newcard_content=re.sub(r"\n\s*\S+\s*=\s?drllmax","\n -1.0 = drllmax ",newcard_content) 
   newcard_content=re.sub(r"\n\s*\S+\s*=\s?draamax","\n -1.0 = draamax ",newcard_content) 
   newcard_content=re.sub(r"\n\s*\S+\s*=\s?drbjmax","\n -1.0 = drbjmax ",newcard_content)
   newcard_content=re.sub(r"\n\s*\S+\s*=\s?drajmax","\n -1.0 = drajmax ",newcard_content) 
   newcard_content=re.sub(r"\n\s*\S+\s*=\s?drjlmax","\n -1.0 = drjlmax ",newcard_content)
   newcard_content=re.sub(r"\n\s*\S+\s*=\s?drabmax","\n -1.0 = drabmax ",newcard_content) 
   newcard_content=re.sub(r"\n\s*\S+\s*=\s?drblmax","\n -1.0 = drblmax ",newcard_content)
   newcard_content=re.sub(r"\n\s*\S+\s*=\s?dralmax","\n -1.0 = dralmax ",newcard_content) 

   # Max and min invariant masses
   newcard_content=re.sub(r"\n\s*\S+\s*=\s?mmjj[^a-z]\s+","\n 0.0 = mmjj ",newcard_content)
   newcard_content=re.sub(r"\n\s*\S+\s*=\s?mmbb[^a-z]\s+","\n 0.0 = mmbb ",newcard_content) 
   newcard_content=re.sub(r"\n\s*\S+\s*=\s?mmaa[^a-z]\s+","\n 0.0 = mmaa ",newcard_content)
   newcard_content=re.sub(r"\n\s*\S+\s*=\s?mmll[^a-z]\s+","\n 0.0 = mmll ",newcard_content) 
   newcard_content=re.sub(r"\n\s*\S+\s*=\s?mmnl[^a-z]\s+","\n 0.0 = mmnl ",newcard_content) 

   newcard_content=re.sub(r"\n\s*\S+\s*=\s?mmjjmax","\n -1.0 = mmjjmax ",newcard_content)
   newcard_content=re.sub(r"\n\s*\S+\s*=\s?mmbbmax","\n -1.0 = mmbbmax ",newcard_content) 
   newcard_content=re.sub(r"\n\s*\S+\s*=\s?mmaamax","\n -1.0 = mmaamax ",newcard_content)
   newcard_content=re.sub(r"\n\s*\S+\s*=\s?mmllmax","\n -1.0 = mmllmax ",newcard_content) 
   newcard_content=re.sub(r"\n\s*\S+\s*=\s?mmnlmax","\n -1.0 = mmnlmax ",newcard_content) 

   # pt of leptons
   newcard_content=re.sub(r"\n\s*\S+\s*=\s?ptllmin","\n 0.0 = ptllmin ",newcard_content) 
   newcard_content=re.sub(r"\n\s*\S+\s*=\s?ptllmax","\n -1.0 = ptllmax ",newcard_content) 

   # Write new card content to file
   with open(os.path.abspath(os.path.join("Cards","run_card.dat")),"w") as f:
      f.write(newcard_content)
   
   return    


def set_seed(inputSeed=None,rndmSeed=False):
   """
   Reads in the old run_card and sets the seed to a random integer in a new run_card, written to the Cards directory. Assumes that it operates in a subfolder corresponding to some annihilation channel in the MG install directory.
   
   """

   import random
   oldcard_path=os.path.abspath(os.path.join("Cards","run_card.dat"))
   try:
      with open(oldcard_path,"r") as f:
         oldcard_content=f.read()
   except IOError:
      oldcard_path=os.path.abspath(os.path.join("Cards","run_card_default.dat"))
      with open(oldcard_path,"r") as f:
         oldcard_content=f.read()
   newcard_content=oldcard_content
   
   if rndmSeed==True:
      seed=random.randint(1,1000000)
   elif inputSeed!=None:
      seed=inputSeed
   else: #if no inputSeed or rndmSeed==False, don't do anything
      return 
   newcard_content = re.sub(r".*= iseed ","".join( ("  ",str(seed)," = iseed ") ),newcard_content)  
   
   # Write new card content to file
   with open(os.path.abspath(os.path.join("Cards","run_card.dat")),"w") as f:
      f.write(newcard_content)
   
   return    
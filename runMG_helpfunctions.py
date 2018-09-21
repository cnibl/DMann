import sys
import re

def write_madgraphscript(annPDG,run_dir,outfile="dmann_madgraphscript.txt",outdir=""):
	with open(outfile,"w") as f:
		f.write("import model DMsimp_s_spin0\n")
		f.write("define allsm = g u c d s u~ c~ d~ s~ a ve vm vt e- mu- ve~ vm~ vt~ e+ mu+ t b t~ b~ z w+ h w- ta- ta+ \n")
		if annPDG==24:
			f.write("generate e+ e- > y0 > w+ w-, (w+ > allsm allsm), (w- > allsm allsm)\n")
		elif annPDG==15:
			f.write("generate e+ e- > y0 > ta+ ta-, (ta+ > allsm allsm), (ta- > allsm allsm)\n")
		elif annPDG==5:
			f.write("generate e+ e- > y0 > b b~ \n")
		else:
			sys.exit("try another annPDG")
		f.write("".join(("output ",run_dir)))
	return "".join((outdir,outfile))

def write_madeventscript(run_tag,outfile="dmann_madeventscript.txt",outdir=""):
	with open(outfile,"w") as f:
		f.write("".join(("generate_events ",run_tag,"\n")))
		f.write("shower=pythia8\n")
		f.write("analysis=OFF\n")
		#f.write("exit")
	return "".join((outdir,outfile))

def open_oldcard(mgoutput_path,cardtype):
	"""
	Opens a card and returns its contents as a string.
	mgoutput_path: the path to the output directory for the MadGraph run
	cardtype: "run","param" or "pythia8", type of card
	"""
	if mgoutput_path[-1]=="/":
		card = open("".join((mgoutput_path,"Cards/",cardtype,"_card_default.dat")),"r")			
	else:
		card = open("".join((mgoutput_path,"/Cards/",cardtype,"_card_default.dat")),"r")
	card_content = card.read()
	card.close()
	return card_content

def get_runname(mgoutput_path):
	"""
	Returns the run tag
	"""
	if mgoutput_path[-1]=="/":
		return mgoutput_path.split("/")[-2]
	else:
		return mgoutput_path.split("/")[-1]

def write_runcard(nAnn,mX,mgoutput_path,outdir=""):
	"""
	Reads in the default/old run_card and replaces the necessary parameters in a new card, written to the current working directory.
	mgoutput_path: the path to the output directory for the MadGraph run
	"""
	oldcard_content = open_oldcard(mgoutput_path,cardtype="run")
	newcard = open("".join((outdir,"run_card.dat")),"w")
	newcard_content = oldcard_content
	newcard_content = re.sub(r".*= run_tag ","".join(("\n","  ",get_runname(mgoutput_path)," = run_tag ")),newcard_content) # number of events
	#checks for numbers in the form xxx(.yyy) with or without decimal points, does not find scientific format numbers
	newcard_content = re.sub(r".*= nevents ","".join( ("  ",str(nAnn)," = nevents ") ),newcard_content)  # number of events
	newcard_content = re.sub(r".*= ebeam1 ","".join(("  ",str(mX)," = ebeam1 ")),newcard_content)  # beam energy 1
	newcard_content = re.sub(r".*= ebeam2 ","".join(("  ",str(mX)," = ebeam2 ")),newcard_content)  # beam energy 2
	newcard_content = re.sub(r".*= scale ","".join(("  ",str(mX)," = scale ")),newcard_content) # scale
	newcard_content = re.sub(r".*= dsqrt_q2fact1 ","".join(("  ",str(mX)," = dsqrt_q2fact1 ")),newcard_content)  # scale pdf1 (prob not used)
	newcard_content = re.sub(r".*= dsqrt_q2fact2 ","".join(("  ",str(mX)," = dsqrt_q2fact2 ")),newcard_content)  # scale pdf2 (prob not used)
	newcard.write(newcard_content)
	newcard.close()
	return "".join((outdir,"run_card.dat"))

def write_paramcard(mX,mgoutput_path,outdir=""):
	"""
	Reads in the default/old param_card and replaces the necessary parameters in a new card, written to the current working directory.
	mgoutput_path: the path to the output directory for the MadGraph run
	"""
	oldcard_content = open_oldcard(mgoutput_path,cardtype="param")
	newcard = open("".join((outdir,"param_card.dat")),"w")
	newcard_content = oldcard_content
	#checks for numbers in integer, decimal or scientific form
	#newcard_content = re.sub(r"\s*25.*#\s*MH","".join(("\n   25 ",str(mX),".0 # MH")),newcard_content)  # higgs mass
	
	newcard_content = re.sub(r"\s*(\d+).*#\s*MY0",r"\n\t \1 "+str(2*mX)+".0  # MY0",newcard_content) # set mediator mass
	newcard_content = re.sub(r"(\D*\d{1,2}) \d+\.?\d*[eE]?\+?\d{1,2} # gP",r"\1 0.000000e+00 # gP",newcard_content) # set pseudoscalar couplings to zero
	newcard.write(newcard_content)
	newcard.close()
	return "".join((outdir,"param_card.dat"))

def write_pythiacard(mgoutput_path,HEPMCfilename="pyt8evts.hepmc",outdir=""):
	"""
	Reads in the default/old pythia_card and replaces the necessary parameters in a new card, written to the current working directory.
	mgoutput_path: the path to the output directory for the MadGraph run
	HEPMCfilename: the filename of the Pythia HEPMC output file
	"""
	oldcard_content = open_oldcard(mgoutput_path,cardtype="pythia8")
	newcard = open("".join((outdir,"pythia8_card.dat")),"w")
	newcard_content = oldcard_content
	#specifies HEPMC output and adds decay of otherwise stable particles
	newcard_content = re.sub(r"\s*HEPMCoutput:file\s*=\s*.*","".join(("\n  HEPMCoutput:file       = ",HEPMCfilename,"\n")),newcard_content)  # HEPMC output
	newcard_content = re.sub(r"!partonlevel:mpi = off",r"partonlevel:mpi = off",newcard_content) 
	newcard.write(newcard_content)
	newcard.write("13:mayDecay   = true                 ! mu+-\n")
	newcard.write("211:mayDecay  = true                 ! pi+-\n")
	newcard.write("321:mayDecay  = true                 ! K+-\n")
	newcard.write("130:mayDecay  = true                 ! K0_L\n")
	newcard.write("2112:mayDecay = true                 ! n\n")
	newcard.close() 
	return "".join((outdir,"pythia8_card.dat")),HEPMCfilename


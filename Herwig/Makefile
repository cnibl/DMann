# -*- Makefile -*- (for emacs)
# src/Makefile-UserModules.  Generated from Makefile-UserModules.in by configure.
#
# Herwig 7.1.1
#
# This Makefile is intended for compiling Herwig plugins
# You can find example plugins in the Contrib directory
#
# This Makefile received very little testing, 
# any bug reports are very welcome!
#

#
# C++ flags
# 
.PRECIOUS: %.o
.PHONY: all clean

CXX = g++ -std=c++11

CXXFLAGS = -g -W -Wall -O2

# add additional package header directories here  -I/home/carlniblaeus/ROOT6.10.08/include/
CPPFLAGS = -I../../Herwig7/include/ 
# add additional libraries here
#LDFLAGS = -I../Herwig7/include/ -I../Herwig7/
#LDFLAGS = #-I../Herwig7/src/Herwig-7.1.1/Analysis/ -I../Herwig7/src/Herwig-7.1.1/Utilities/ -I/home/carlniblaeus/Herwig7/lib/Herwig/ -I../Herwig7/include/ -I../Herwig7/

ROOTCFLAGS := $(shell root-config --cflags)
ROOTGLIBS := $(shell root-config --glibs)
ROOT = $(ROOTCFLAGS) $(ROOTGLIBS)

### Below 5 lines are the old DMann rules, without the FRModel stuff
#ALLCCFILES=$(shell echo *.cc)
#all : $(ALLCCFILES:.cc=.so)
#
#%.so : %.cc %.h 
#	$(CXX) -shared -fPIC $(CPPFLAGS) $(CXXFLAGS) $(LDFLAGS) $< -o $@  

### Below is what should be used when using the FeynRules UFO model
ALLFRFILES=$(shell echo FR*.cc)
ALLDMFILES=$(shell echo DM*.cc)

all : FRModel.so DMannYields.so
ALLFROBJFILES=$(ALLFRFILES:.cc=.o)
ALLDMOBJFILES=$(ALLDMFILES:.cc=.o)

FRModel.so : $(ALLFROBJFILES) 
	$(CXX) -shared -fPIC $(CXXFLAGS) $(LDFLAGS) $^ -o $@  

DMannYields.so : $(ALLDMOBJFILES) 
	$(CXX) -shared -fPIC $(CPPFLAGS) $(CXXFLAGS) $(LDFLAGS)  $< -o $@  

%.o : %.cc
	$(CXX) -fPIC $(CPPFLAGS) $(CXXFLAGS) -c $< -o $@
##

clean:
	rm -f $(ALLFRFILES:.cc=.so) $(ALLFRFILES:.cc=.o) $(ALLDMFILES:.cc=.so) $(ALLDMFILES:.cc=.o)

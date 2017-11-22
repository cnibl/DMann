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
CXX = g++ -std=c++11

CXXFLAGS = -g -W -Wall -O2

# add additional package header directories here  -I/home/carlniblaeus/ROOT6.10.08/include/
CPPFLAGS = -I/home/carlniblaeus/Downloads/../Herwig7/include

# add additional libraries here
LDFLAGS = -I../Herwig7/src/Herwig-7.1.1/Analysis/ -I../Herwig7/src/Herwig-7.1.1/Utilities/ -I/home/carlniblaeus/Herwig7/lib/Herwig/ -I../Herwig7/include/ -I../Herwig7/

ROOTCFLAGS := $(shell root-config --cflags)
ROOTGLIBS := $(shell root-config --glibs)
ROOT = $(ROOTCFLAGS) $(ROOTGLIBS)

ALLCCFILES=$(shell echo *.cc)
all : $(ALLCCFILES:.cc=.so)

%.so : %.cc %.h 
	$(CXX) -shared -fPIC $(CPPFLAGS) $(CXXFLAGS) $(LDFLAGS) $(ROOT) $< -o $@  

clean:
	rm -f $(ALLCCFILES:.cc=.so)

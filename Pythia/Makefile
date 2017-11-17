# Makefile for the DMann part with PYTHIA8.
# dmannmain.cc needs to be compiled with ROOT as well

#PYTDIR=/Users/carlniblaeus/pythia8226/ #on mac
#PYTDIR=/home/carlniblaeus/pythia8230/ #on ubuntu desktop

# Install directory prefixes.
#PREFIX_BIN=$(PYTDIR)bin
#PREFIX_INCLUDE=$(PYTDIR)include
#PREFIX_LIB=$(PYTDIR)lib
#PREFIX_SHARE=$(PYTDIR)share/Pythia8

# Install directory prefixes. Ubuntu desktop.
PREFIX_BIN=/home/carlniblaeus/pythia8230/bin
PREFIX_INCLUDE=/home/carlniblaeus/pythia8230/include
PREFIX_LIB=/home/carlniblaeus/pythia8230/lib
PREFIX_SHARE=/home/carlniblaeus/pythia8230/share/Pythia8

# Compilation flags (see ./configure --help for further documentation).
ENABLE_SHARED=false
CXX=g++
CXX_COMMON=-O2 -std=c++98 -pedantic -W -Wall -Wshadow -fPIC
CXX_SHARED=-dynamiclib
CXX_SONAME=-Wl,-dylib_install_name,@rpath/
LIB_SUFFIX=.dylib

# ROOT configuration on mac.
#ROOT_USE=true
#ROOT_BIN=/usr/local/Cellar/root/6.10.04/bin//
#ROOT_INCLUDE=/usr/local/Cellar/root/6.10.04/include/root/
#ROOT_LIB=/usr/local/Cellar/root/6.10.04/lib/root/

# ROOT configuration on ubuntu desktop.
ROOT_USE=true
ROOT_BIN=../ROOT6.10.08/bin/
ROOT_INCLUDE=../ROOT6.10.08/include
ROOT_LIB=../ROOT6.10.08/lib

CXX_COMMON:=-I$(PREFIX_INCLUDE) $(CXX_COMMON)
CXX_COMMON+= -L$(PREFIX_LIB) -Wl,-rpath,$(PREFIX_LIB) -lpythia8 -ldl 

################################################################################
# RULES: Definition of the make rules used to build.
################################################################################

# Rules without physical targets (secondary expansion for specific rules).
.SECONDEXPANSION:
.PHONY: all clean

# All targets (no default behavior).
all:
	@echo "Usage: make dmannmain"

# dmann program, with ROOT included.
# If in the future there are several dmannmainX.cc (X=0,1,...), this rule can
# still be used by replacing "dmannmain" by "dmannmain%" in the two 
# occurences in the first line of the rule.
dmannmain : dmannmain.cc $(PREFIX_LIB)/libpythia8.a
ifeq ($(ROOT_USE),true)
	$(CXX) $< -o $@ -w -I$(ROOT_INCLUDE) $(CXX_COMMON)\
	 `$(ROOTBIN)root-config --cflags`\
	 -Wl,-rpath,$(ROOT_LIB) `$(ROOT_BIN)root-config --glibs`
else
	@echo "Error: $@ requires ROOT"
endif

# Clean.
clean:
	@rm -f dmannmain;
	rm -f *~; rm -f \#*; rm -f core*; rm -f *Dct.*; rm -f *.so;

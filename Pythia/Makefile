# Makefile for the DMann part with PYTHIA8.
# dmannmain.cc needs to be compiled with ROOT as well

#on mac:
#PYTDIR=/Users/carlniblaeus/pythia8226/
#on ubuntu desktop:
#PYTDIR=/home/carlniblaeus/pythia8230/
#on 16-core mac in Joakims office
PYTDIR=/Users/cniblaeus/pythia8240/

# Install directory prefixes.
PREFIX_BIN=$(PYTDIR)bin
PREFIX_INCLUDE=$(PYTDIR)include
PREFIX_LIB=$(PYTDIR)lib
PREFIX_SHARE=$(PYTDIR)share/Pythia8

# Install directory prefixes. Ubuntu desktop.
#PREFIX_BIN=/home/carlniblaeus/pythia8230/bin
#PREFIX_INCLUDE=/home/carlniblaeus/pythia8230/include
#PREFIX_LIB=/home/carlniblaeus/pythia8230/lib
#PREFIX_SHARE=/home/carlniblaeus/pythia8230/share/Pythia8

# Compilation flags (see ./configure --help for further documentation).
ENABLE_SHARED=false
CXX=g++
#CXX_COMMON=-O2 -std=c++98 -pedantic -W -Wall -Wshadow -fPIC
CXX_COMMON=-O2 -std=c++11 -pedantic -W -Wall -Wshadow -fPIC
CXX_SHARED=-dynamiclib
CXX_SONAME=-Wl,-dylib_install_name,@rpath/
LIB_SUFFIX=.dylib

# ROOT configuration on mac.
#ROOT_USE=true
#ROOT_BIN=/usr/local/Cellar/root/6.12.06_2/bin/
#ROOT_INCLUDE=/usr/local/Cellar/root/6.12.06_2/include/root/
#ROOT_LIB=/usr/local/Cellar/root/6.12.06_2/lib/root/

# ROOT configuration on ubuntu desktop.
#ROOT_USE=true
#ROOT_BIN=../../ROOT6.10.08/bin/
#ROOT_INCLUDE=../../ROOT6.10.08/include
#ROOT_LIB=../../ROOT6.10.08/lib

# ROOT configuration on 16-core mac in Joakims office
ROOT_USE=true
ROOT_BIN=/Users/cniblaeus/root-6.11.02/bin/
ROOT_INCLUDE=/Users/cniblaeus/root-6.11.02/include
ROOT_LIB=/Users/cniblaeus/root-6.11.02/lib

CXX_COMMON:=-I$(PREFIX_INCLUDE) $(CXX_COMMON)
CXX_COMMON+= -L$(PREFIX_LIB) -Wl,-rpath,$(PREFIX_LIB) -lpythia8 -ldl 

GZIP_BIN=
GZIP_INCLUDE=./
GZIP_LIB=./
# Handle GZIP support.
GZIP_INC=
GZIP_FLAGS=
GZIP_INC+= -DGZIPSUPPORT -I$(GZIP_INCLUDE)
GZIP_FLAGS+= -L$(GZIP_LIB) -Wl,-rpath,$(GZIP_LIB) -lz

################################################################################
# RULES: Definition of the make rules used to build.
################################################################################

# Rules without physical targets (secondary expansion for specific rules).
.SECONDEXPANSION:
.PHONY: all clean

# All targets (no default behavior).
all:
	@echo "Usage: make DMannPythia"

# dmann program, with ROOT included.
# If in the future there are several dmannmainX.cc (X=0,1,...), this rule can
# still be used by replacing "dmannmain" by "dmannmain%" in the two 
# occurences in the first line of the rule.
DMannPythia8 : DMannPythia8.cc $(PREFIX_LIB)/libpythia8.a
ifeq ($(ROOT_USE),true)
	$(CXX) $< -o $@ -w -I$(ROOT_INCLUDE) $(CXX_COMMON)\
	 `$(ROOTBIN)root-config --cflags`\
	 -Wl,-rpath,$(ROOT_LIB) `$(ROOT_BIN)root-config --glibs`
else
	@echo "Error: $@ requires ROOT"
endif

DMannPythia8LHE : DMannPythia8LHE.cc $(PREFIX_LIB)/libpythia8.a
ifeq ($(ROOT_USE),true)
	$(CXX) $< -o $@ -w -I$(ROOT_INCLUDE) $(CXX_COMMON) $(GZIP_INC) $(GZIP_FLAGS)\
	 `$(ROOTBIN)root-config --cflags`\
	 -Wl,-rpath,$(ROOT_LIB) `$(ROOT_BIN)root-config --glibs`
else
	@echo "Error: $@ requires ROOT"
endif

# Clean.
clean:
	@rm -f DMannPythia8 DMannPythia8LHE;
	rm -f *~; rm -f \#*; rm -f core*; rm -f *Dct.*; rm -f *.so;

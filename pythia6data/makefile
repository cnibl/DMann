# Makefile for the getpythia6data file, that ensures correct linking to DarkSUSY6 (copied from examples/aux dir in DarkSUSY6 trunk)
#FF=$(FC)
FF=gfortran

### Compiler options ###

# Options for linux
FOPT = -O -ffixed-line-length-none -fopenmp

### Setups for the DarkSUSY install directory ###

# Determine where to install stuff (prefix is set in configure)
prefix=/Users/carlniblaeus/DarkSUSY6/library_6plus/trunk
# DS_INSTALL is where the library and data files will be installed
DS_INSTALL=${prefix}

LIB=$(DS_INSTALL)/lib
INC=-I./ -I$(DS_INSTALL)/src/include -I$(DS_INSTALL)/src_models/include -I$(DS_INSTALL)/contrib/include -I$(DS_INSTALL)/src/templates
INC_GENERIC=-I$(DS_INSTALL)/src_models/generic_wimp/include
cfitsio=.
ADD_SCR=$(DS_INSTALL)/scr/add_libs.pl

### choose particle module to include ###
#DS_MODULE=mssm
#DS_MODULE=empty

# User libraries with user replaced functions (this only works on OS X, and is
# NOT the default building method anymore)
#USER_LIB=-lds_core_user -lds_$(DS_MODULE)_user

# Libraries. List here the libraries and object files you want to link to
# IN THE ORDER in which you want them to be searched
#ALL_LIB = $(LIB)/libds_core_user.a $(LIB)/libds_core.a $(LIB)/libds_$(DS_MODULE)_user.a $(LIB)/libds_$(DS_MODULE).a

### you must set GALPROP_LIBS if you have compiled galprop

all: getpythia6data

getpythia6data : DS_MODULE = generic_wimp
getpythia6data : getpythia6data.f $(LIB)/libisajet.a $(LIB)/libHS.a $(LIB)/libHB.a $(LIB)/libFH.a
	printf "#define MODULE_CONFIG MODULE_"$(DS_MODULE)  > module_compile.F
	printf "$(LIB)/libds_core_user.a\n"$(LIB)"/libds_core.a\n"$(LIB)"/libds_"$(DS_MODULE)"_user.a\n"$(LIB)"/libds_"$(DS_MODULE)".a" > module_link.txt
	$(ADD_SCR) libds_tmp.a module_link.txt
	$(FF) $(FOPT) $(INC) $(INC_GENERIC) -L$(LIB) -o getpythia6data getpythia6data.f \
	libds_tmp.a -lHS -lHB -lFH -lisospin -lisajet
	rm -f module_compile.F
	rm -f module_link.txt
	rm -f libds_tmp.a

.NOTPARALLEL:
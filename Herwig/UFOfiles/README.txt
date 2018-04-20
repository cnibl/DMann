To be able to use the FeynRules simple general resonance model in Herwig, follow these steps:

1) run in terminal: "source $HERWIGDIR/bin/activate" where $HERWIGDIR is the Herwig installation directory

2) run in terminal: "ufo2herwig $UFODIR" where $UFODIR is the directory with the UFO .py-files

3) move the created FRModel*.cc/.model/.h/.template-files one directory up

4) add to the Makefile in the directory one step up the rule for making the FRModel.so shared library (see below for how the Makefile should look)

5) make the necessary changes in the MakeRunHerwig.py script. Add the "insert ResConstructor Incoming/Outgoing/Intermediates" statement to give initial and final state.


(The latter part of the Makefile should look like this:

ALLFRFILES=$(shell echo FR*.cc)
ALLDMFILES=$(shell echo DM*.cc)

all : FRModel.so 
ALLFROBJFILES=$(ALLFRFILES:.cc=.o)
ALLDMOBJFILES=$(ALLDMFILES:.cc=.o)

FRModel.so : $(ALLFROBJFILES)
	$(CXX) -shared -fPIC $(CXXFLAGS) $(LDFLAGS) $^ -o $@  

DMannYields.so : $(ALLDMOBJFILES)
	$(CXX) -shared -fPIC $(CPPFLAGS) $(CXXFLAGS) $(LDFLAGS) $< -o $@  

%.o : %.cc
	$(CXX) -fPIC $(CPPFLAGS) $(CXXFLAGS) -c $< -o $@

) 
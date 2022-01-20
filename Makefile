CCX=g++
CXXFLAGS=-Wall -fPIC -O3 -std=c++11 -march=native -fopenmp -DEIGEN_DONT_PARALLELIZE
LDFLAGS=-shared  
INC=-I${CONDA_PREFIX}/include/eigen3 $(shell python3 -m pybind11 --includes) 

# Call as make openblas=1 to compile against openblas
ifeq ($(openblas),1)
	LDFLAGS+=-lopenblas
	CXXFLAGS+=-DEIGEN_USE_LAPACKE -DEIGEN_USE_BLAS  
endif

all: 
	$(CCX) $(CXXFLAGS) $(LDFLAGS) $(INC) demo.cpp -o demo$(shell python3-config --extension-suffix) 

clean:
	rm *.so

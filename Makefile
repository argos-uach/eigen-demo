CCX=g++
CXXFLAGS=-Wall -fPIC -O3 -std=c++11 -march=native -fopenmp -DEIGEN_DONT_PARALLELIZE
LDFLAGS=-shared -lm
INC=-I${CONDA_PREFIX}/include -I${CONDA_PREFIX}/include/eigen3 $(shell python3 -m pybind11 --includes) 

# Call as make openblas=1 to compile against openblas
ifeq ($(openblas),1)
	LDFLAGS+=-lopenblas
	CXXFLAGS+=-DEIGEN_USE_LAPACKE -DEIGEN_USE_BLAS  
endif

# Call as make mkl=1 to compile against MKL
ifeq ($(mkl),1)
	LDFLAGS+=-lmkl_rt -Wl,--no-as-needed -lpthread -ldl
	CXXFLAGS+=-DEIGEN_USE_MKL_ALL -m64 -DMKL_LP64
endif

foo.o:
	como cpilar

bar.so:
	como compilar

demo.so:
	$(CCX) $(CXXFLAGS) $(LDFLAGS) $(INC) demo.cpp -o demo$(shell python3-config --extension-suffix) 

clean:
	rm *.so *.o

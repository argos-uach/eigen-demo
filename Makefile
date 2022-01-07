all:
	g++ -O3 -Wall -shared -std=c++11 -fPIC $(shell python3 -m pybind11 --includes) demo.cpp -o demo$(shell python3-config --extension-suffix) -I${CONDA_PREFIX}/include/eigen3

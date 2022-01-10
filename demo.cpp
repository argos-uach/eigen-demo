#include <iostream>
#include <Eigen/Dense>
#include <pybind11/pybind11.h>
#include <pybind11/eigen.h>

using namespace Eigen;
namespace py = pybind11;

Eigen::MatrixXf sumMatrix(MatrixXf matriz)
{
     MatrixXf c;
     c = 2*matriz;
     std::cout << "2*matriz =\n" << c << std::endl;

     return c;
}


PYBIND11_MODULE(demo, m) {
     m.doc() = "pybind11 example plugin"; // optional module docstring
     m.def("sumMatrix", &sumMatrix, "Funcion con un argumento",
          py::arg("m"));
     //m.attr("vector") = 69;

}

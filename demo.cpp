#include <iostream>
#include <Eigen/Dense>
#include <pybind11/pybind11.h>
#include <pybind11/eigen.h>

using namespace Eigen;
namespace py = pybind11;

Eigen::MatrixXf sumMatrix()
{

     Matrix2f a;
     a << 1, 2,
          3, 4;
     MatrixXf b(2,2);
     b << 2, 3,
          1, 4;
     MatrixXf c;
     c = a + b;
     
     std::cout << "a + b =\n" << c << std::endl;

     return c;
}


PYBIND11_MODULE(demo, m) {
     m.doc() = "pybind11 example plugin"; // optional module docstring
     m.def("sumMatrix", &sumMatrix, "Probando Eigen");
     //m.attr("vector") = 69;

}

#include <iostream>
#include <Eigen/Dense>
#include <pybind11/pybind11.h>
#include <pybind11/eigen.h>

using namespace Eigen;
namespace py = pybind11;

using RowMatrixXf = Eigen::Matrix<float, Eigen::Dynamic, Eigen::Dynamic, Eigen::RowMajor>;

Eigen::MatrixXf multMatrix(MatrixXf matriz)
{
     MatrixXf c;
     c = 2*matriz;
     std::cout << "2*matriz =\n" << c << std::endl;

     return c;
}

void multMatrix_Ref(Eigen::Ref<MatrixXf> matriz)
{
     matriz = 2*matriz;
     std::cout << "2*matriz =\n" << matriz << std::endl;
}

void multRowMatrix_Ref(Eigen::Ref<RowMatrixXf> matriz)
{
     matriz = 2*matriz;
     std::cout << "2*matriz =\n" << matriz << std::endl;
}

Eigen::MatrixXf multMatrixByMatrix_Ref(Eigen::Ref<MatrixXf> matriz1, Eigen::Ref<MatrixXf> matriz2)
{

     MatrixXf mult = matriz1 * matriz2.transpose();
     //std::cout << "matriz1*matriz2 =\n" << mult << std::endl;
     return mult;
}

PYBIND11_MODULE(demo, m) {
     m.doc() = "pybind11 example plugin"; // optional module docstring
     m.def("multMatrix", &multMatrix, "Funcion con un argumento",
          py::arg("m"));
     m.def("multMatrixRef", &multMatrix_Ref, "Funcion con un argumento pasado por referencia",
          py::arg("m"));
     m.def("multRowMatrixRef", &multRowMatrix_Ref, "Funcion con un argumento pasado por referencia con rowMajor",
          py::arg("m"));
     m.def("multMatrixByMatrix_Ref", &multMatrixByMatrix_Ref, "Funcion con 2 argumento pasado por referencia",
          py::arg("matriz1"), py::arg("matriz2"));
}

#include <pybind11/pybind11.h>

namespace py = pybind11;
using namespace pybind11::literals;

class Vector2D {
public:
    Vector2D(double x = 0.0, double y = 0.0) : x(x), y(y) {}
    double x, y;
};

class Vector3D {
public:
    Vector3D(double x = 0.0, double y = 0.0, double z = 0.0) : x(x), y(y), z(z) {}
    double x, y, z;
};

PYBIND11_MODULE(math, mod) {
    mod.doc() = "Math module for pygomo";
    py::class_<Vector2D>(mod, "Vector2D")
        .def(py::init<double, double>(), "x"_a = 0.0, "y"_a = 0.0)
        .def_readwrite("x", &Vector2D::x)
        .def_readwrite("y", &Vector2D::y);
    py::class_<Vector3D>(mod, "Vector3D")
        .def(py::init<double, double, double>(), "x"_a = 0.0, "y"_a = 0.0, "z"_a = 0.0)
        .def_readwrite("x", &Vector3D::x)
        .def_readwrite("y", &Vector3D::y)
        .def_readwrite("z", &Vector3D::z);
}

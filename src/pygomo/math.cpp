#include <pybind11/pybind11.h>

namespace py = pybind11;
using namespace pybind11::literals;

class Vector2D {
public:
    Vector2D(double x = 0.0, double y = 0.0) : x(x), y(y) {}
    double x, y;
};

PYBIND11_MODULE(math, mod) {
    mod.doc() = "Math module for pygomo";
    py::class_<Vector2D>(mod, "Vector2D")
        .def(py::init<double, double>(), "x"_a = 0.0, "y"_a = 0.0)
        .def_readwrite("x", &Vector2D::x)
        .def_readwrite("y", &Vector2D::y);
}

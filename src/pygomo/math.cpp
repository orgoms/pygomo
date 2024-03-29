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

class Point2D {
public:
    Point2D(double x = 0.0, double y = 0.0) : x(x), y(y) {}
    double x, y;
};

class Point3D {
public:
    Point3D(double x = 0.0, double y = 0.0, double z = 0.0) : x(x), y(y), z(z) {}
    double x, y, z;
};

class Dimension2D {
public:
    Dimension2D(double width = 0.0, double height = 0.0) : width(width), height(height) {}
    double width, height;
};

class Dimension3D {
public:
    Dimension3D(double width = 0.0, double height = 0.0, double depth = 0.0) : width(width), height(height), depth(depth) {}
    double width, height, depth;
};

class Rect2D {
public:
    Rect2D(double x, double y, double width, double height) : x(x), y(y), width(width), height(height) {}
    double x, y, width, height;
};

class Rect3D {
public:
    Rect3D(double x, double y, double z, double width, double height, double depth) : x(x), y(y), z(z), width(width), height(height), depth(depth) {}
    double x, y, z, width, height, depth;
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
    py::class_<Point2D>(mod, "Point2D")
        .def(py::init<double, double>(), "x"_a = 0.0, "y"_a = 0.0)
        .def_readwrite("x", &Point2D::x)
        .def_readwrite("y", &Point2D::y);
    py::class_<Point3D>(mod, "Point3D")
        .def(py::init<double, double, double>(), "x"_a = 0.0, "y"_a = 0.0, "z"_a = 0.0)
        .def_readwrite("x", &Point3D::x)
        .def_readwrite("y", &Point3D::y)
        .def_readwrite("z", &Point3D::z);
    py::class_<Dimension2D>(mod, "Dimension2D")
        .def(py::init<double, double>(), "width"_a = 0.0, "height"_a = 0.0)
        .def_readwrite("width", &Dimension2D::width)
        .def_readwrite("height", &Dimension2D::height);
    py::class_<Dimension3D>(mod, "Dimension3D")
        .def(py::init<double, double, double>(), "width"_a = 0.0, "height"_a = 0.0, "depth"_a = 0.0)
        .def_readwrite("width", &Dimension3D::width)
        .def_readwrite("height", &Dimension3D::height)
        .def_readwrite("depth", &Dimension3D::depth);
    py::class_<Rect2D>(mod, "Rect2D")
        .def(py::init<double, double, double, double>(), "x"_a = 0.0, "y"_a = 0.0, "width"_a = 0.0, "height"_a = 0.0)
        .def_readwrite("x", &Rect2D::x)
        .def_readwrite("y", &Rect2D::y)
        .def_readwrite("width", &Rect2D::width)
        .def_readwrite("height", &Rect2D::height);
    py::class_<Rect3D>(mod, "Rect3D")
        .def(py::init<double, double, double, double, double, double>(), "x"_a = 0.0, "y"_a = 0.0, "z"_a = 0.0, "width"_a = 0.0, "height"_a = 0.0, "depth"_a = 0.0)
        .def_readwrite("x", &Rect3D::x)
        .def_readwrite("y", &Rect3D::y)
        .def_readwrite("z", &Rect3D::z)
        .def_readwrite("width", &Rect3D::width)
        .def_readwrite("height", &Rect3D::height)
        .def_readwrite("depth", &Rect3D::depth);
}

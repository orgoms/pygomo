#include <pybind11/pybind11.h>

PYBIND11_MODULE(glfw, m) {
    m.doc() = "Python bindings for GLFW.";
}

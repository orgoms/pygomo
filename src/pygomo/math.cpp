#include <pybind11/pybind11.h>

namespace py = pybind11;

PYBIND11_MODULE(math, mod) {
    mod.doc() = "Math module for pygomo";
}

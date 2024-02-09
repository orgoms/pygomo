#include <pybind11/pybind11.h>

PYBIND11_MODULE(window, mod) {
    mod.doc() = "Window module for pygomo.";
}

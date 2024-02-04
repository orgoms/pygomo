#include <pybind11/pybind11.h>

PYBIND11_MODULE(core, mod) {
    mod.doc() = "Core module for pygomo.";
}

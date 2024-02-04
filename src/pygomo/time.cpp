#include <pybind11/pybind11.h>

PYBIND11_MODULE(time, mod) {
    mod.doc() = "Time module for pygomo.";
}

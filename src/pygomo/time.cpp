#include <pybind11/pybind11.h>

namespace py = pybind11;

class Clock {
public:
    Clock() {}
};

PYBIND11_MODULE(time, mod) {
    mod.doc() = "Time module for pygomo.";
    py::class_<Clock>(mod, "Clock");
}

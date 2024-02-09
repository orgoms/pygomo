#include <pybind11/pybind11.h>

namespace py = pybind11;

class Window {
public:
    Window() {}
};

PYBIND11_MODULE(window, mod) {
    mod.doc() = "Window module for pygomo.";
    py::class_<Window>(mod, "Window");
}

#define GLFW_INCLUDED_NONE

#include <GLFW/glfw3.h>

#include <pybind11/pybind11.h>

namespace py = pybind11;

class Window {
public:
    Window() {
        this->window = glfwCreateWindow(640, 480, "Window", NULL, NULL);
    }

    GLFWwindow *window;
};

PYBIND11_MODULE(window, mod) {
    mod.doc() = "Window module for pygomo.";
    py::class_<Window>(mod, "Window")
        .def(py::init<>());
}

#define GLFW_INCLUDED_NONE
#include <GLFW/glfw3.h>
#include <pybind11/pybind11.h>

#include <string>

namespace py = pybind11;

class Window {
public:
    Window(std::string title = "Window", int width = 640, int height = 480) {
        this->window = glfwCreateWindow(width, height, title.c_str(), NULL, NULL);
    }

    void destroy() {
        glfwDestroyWindow(this->window);
    }

    GLFWwindow *window;
};

PYBIND11_MODULE(window, mod) {
    mod.doc() = "Window module for pygomo.";
    py::class_<Window>(mod, "Window")
        .def(py::init<>())
        .def("destroy", &Window::destroy);
}

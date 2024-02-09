#define GLFW_INCLUDE_NONE

#include <glad/glad.h>
#include <GLFW/glfw3.h>

#include <pybind11/pybind11.h>

void init() {
    glfwInit();
    gladLoadGL();
}

PYBIND11_MODULE(core, mod) {
    mod.doc() = "Core module for pygomo.";
    mod.def("init", &init);
}

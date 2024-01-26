cmake_minimum_required(VERSION 3.12)
project(pyndow)

find_package(Python COMPONENTS Interpreter Development REQUIRED)
find_package(pybind11 CONFIG REQUIRED)

include(ExternalProject)

if (NOT BUILD_DIR)
    set(BUILD_DIR "${CMAKE_HOME_DIRECTORY}/build")
endif()

ExternalProject_Add(_glfw
    GIT_REPOSITORY https://github.com/glfw/glfw
    PREFIX "${BUILD_DIR}/extern/glfw"
    CMAKE_ARGS
        -DBUILD_SHARED_LIBS=ON
        -DGLFW_BUILD_EXAMPLES=OFF
        -DGLFW_BUILD_TESTS=OFF
        -DGLFW_BUILD_DOCS=OFF
    INSTALL_COMMAND ""
)

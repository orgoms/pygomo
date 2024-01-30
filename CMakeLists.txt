cmake_minimum_required(VERSION 3.12)
project(pyndow)

set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

set(BUILD_SHARED_LIBS ON)
set(GLFW_BUILD_EXAMPLES OFF)
set(GLFW_BUILD_TESTS OFF)
set(GLFW_BUILD_DOCS OFF)

include(FetchContent)

find_package(Python COMPONENTS Interpreter Development REQUIRED)
find_package(pybind11 CONFIG REQUIRED)

FetchContent_Declare(glfw
    GIT_REPOSITORY https://github.com/glfw/glfw.git
    GIT_TAG 3.3-stable
)
FetchContent_MakeAvailable(glfw)

set(CMAKE_LIBRARY_OUTPUT_DIRECTORY ${PACKAGE_DIR})

pybind11_add_module(pyndow-glfw src/pyndow/glfw.cpp)

target_link_libraries(pyndow-glfw PRIVATE glfw)
set_target_properties(pyndow-glfw
    PROPERTIES
    OUTPUT_NAME glfw
)

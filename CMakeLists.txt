cmake_minimum_required(VERSION 3.12)
project(pygomo)

set(BUILD_SHARED_LIBS ON)

set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

find_package(Python COMPONENTS Interpreter Development REQUIRED)
find_package(pybind11 CONFIG REQUIRED)

include_directories("${PACKAGE_DIR}/include")
link_directories("${PACKAGE_DIR}/lib")

pybind11_add_module(pygomo-core src/pygomo/core.cpp)
pybind11_add_module(pygomo-math src/pygomo/math.cpp)
pybind11_add_module(pygomo-time src/pygomo/time.cpp)
pybind11_add_module(pygomo-window src/pygomo/window.cpp)

set_target_properties(pygomo-core
    PROPERTIES
    BUILD_WITH_INSTALL_RPATH TRUE
    INSTALL_RPATH "${PACKAGE_DIR}/lib"
    OUTPUT_NAME core
)
set_target_properties(pygomo-math
    PROPERTIES
    OUTPUT_NAME math
)
set_target_properties(pygomo-time
    PROPERTIES
    OUTPUT_NAME time
)
set_target_properties(pygomo-window
    PROPERTIES
    BUILD_WITH_INSTALL_RPATH TRUE
    INSTALL_RPATH "${PACKAGE_DIR}/lib"
    OUTPUT_NAME window
)

target_link_libraries(pygomo-core PRIVATE glad glfw)
target_link_libraries(pygomo-window PRIVATE glfw)

install(
    TARGETS
    pygomo-core
    pygomo-math
    pygomo-time
    pygomo-window
    DESTINATION
    ${PACKAGE_DIR}
)

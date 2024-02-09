# ruff: noqa: N801

from __future__ import annotations

from pathlib import Path
from typing import ClassVar

import pybind11
import setuptools
from setuptools import Command
from setuptools.command.build import build as _build
from setuptools.command.build_ext import build_ext as _build_ext


class build(_build):
    def finalize_options(self: build) -> None:
        super().finalize_options()

        # This is essential to move the built extensions to a directory
        # where it will be eventually be copied to the directory where
        # the package will be installed
        self.build_lib = self.build_platlib

        for index, cmd in enumerate(self.sub_commands):
            self.sub_commands[index] = (cmd[0], None)

    def run(self: build) -> None:
        for cmd in self.sub_commands:
            self.run_command(cmd[0])


class build_ext(_build_ext):
    def run(self: build_ext) -> None:
        # Run the sub-commands before running 'build_ext', some extensions
        # may need to be built in the sub-commands prior to running 'build_ext'
        for cmd_name in self.get_sub_commands():
            self.run_command(cmd_name)

        # Run the base 'build_ext' command after running the sub-commands
        super().run()

    sub_commands: ClassVar = [
        ("build_ext_cmake", None),
    ]


class build_ext_cmake(Command):
    description = "build C/C++ extensions with CMake"
    user_options: ClassVar = []

    def initialize_options(self: build_ext_cmake) -> None:
        pass

    def finalize_options(self: build_ext_cmake) -> None:
        pass

    def run(self: build_ext_cmake) -> None:
        build_ext = self.get_finalized_command("build_ext")
        build_py = self.get_finalized_command("build_py")

        # The 'source_dir' is typically the current working directory
        source_dir = Path().absolute()

        # If not inplace, set the build and output directories to the
        # provided directories from 'build_ext', otherwise set the build
        # and output directories to the 'build' directory from 'source_dir'
        # and where the pygomo package is stored
        if not build_ext.inplace:
            build_dir = Path(build_ext.build_temp).absolute()
            package_dir = Path(build_ext.build_lib).absolute() / "pygomo"
        else:
            build_dir = Path(source_dir / "build").absolute()
            package_dir = Path(build_py.get_package_dir("pygomo")).absolute()

        # Ensure that these directories exists
        package_dir.mkdir(parents=True, exist_ok=True)
        source_dir.mkdir(parents=True, exist_ok=True)
        build_dir.mkdir(parents=True, exist_ok=True)

        # fmt: off
        # Configure the project's extern with CMake
        self.spawn([
            "cmake",
            "-S", str(source_dir / "extern"),
            "-B", str(build_dir / "extern"),
            "-G", "Ninja",
            "-D", f"PACKAGE_DIR={package_dir}",
            "-D", "GLAD_PROFILE=core",
            "-D", "GLAD_API=gl=3.3",
            "-D", "GLAD_GENERATOR=c",
            "-D", "GLAD_INSTALL=ON",
            "-D", "GLFW_BUILD_EXAMPLES=OFF",
            "-D", "GLFW_BUILD_TESTS=OFF",
            "-D", "GLFW_BUILD_DOCS=OFF",
            "-D", "GLFW_INSTALL=ON",
            "-D", "CMAKE_EXPORT_COMPILE_COMMANDS=ON",  # for LSP
        ])

        # Build and install the project's extern with CMake
        self.spawn(["cmake", "--build",   str(build_dir / "extern")])
        self.spawn(["cmake", "--install", str(build_dir / "extern"),
                             "--prefix",  str(package_dir)])

        # Configure the project with CMake
        self.spawn([
            "cmake",
            "-S", str(source_dir),
            "-B", str(build_dir),
            "-G", "Ninja",
            "-D", f"pybind11_DIR={pybind11.get_cmake_dir()}",
            "-D", f"PACKAGE_DIR={package_dir}",
            "-D", "CMAKE_EXPORT_COMPILE_COMMANDS=ON",  # for LSP
        ])

        # Build and install the project with CMake
        self.spawn(["cmake", "--build",   str(build_dir)])
        self.spawn(["cmake", "--install", str(build_dir),
                             "--prefix",  str(package_dir)])
        # fmt: on


def setup() -> None:
    setuptools.setup(
        cmdclass={
            "build": build,
            "build_ext": build_ext,
            "build_ext_cmake": build_ext_cmake,
        },
    )


if __name__ == "__main__":
    setup()

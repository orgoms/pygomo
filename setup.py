from __future__ import annotations

from pathlib import Path

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


class build_ext(_build_ext):
    def run(self: build_ext) -> None:
        # Run the sub-commands before running build_ext, some extensions
        # may need to be built in the sub-commands prior to running build_ext
        for cmd_name in self.get_sub_commands():
            self.run_command(cmd_name)

        super().run()

    sub_commands = [
        ("build_ext_cmake", None),
    ]


class build_ext_cmake(Command):
    description = "build C/C++ extensions with CMake"
    user_options = []

    def initialize_options(self: build_ext_cmake) -> None:
        pass

    def finalize_options(self: build_ext_cmake) -> None:
        pass

    def run(self: build_ext_cmake) -> None:
        # Needs other commands for specific attributes
        build_ext = self.get_finalized_command("build_ext")
        build_py = self.get_finalized_command("build_py")

        # Configure and build the extensions with CMake in the
        # provided temporary build directory from build_ext
        self.spawn(["cmake",
                    "-S", ".",
                    "-B", build_ext.build_temp,
                    "-G", "Ninja",
                    "-D", f"pybind11_DIR={pybind11.get_cmake_dir()}"])
        self.spawn(["cmake", "--build", build_ext.build_temp])

        # Determine the destination directory for the built extensions
        # If building in-place, set the destination to the package directory
        # Otherwise, set the destination where the build artifacts should be
        # stored, which will eventually be copied to the directory where
        # the package will be installed
        if build_ext.inplace:
            package_dir = Path(build_py.get_package_dir("pyndow"))
        else:
            package_dir = Path(build_ext.build_lib) / "pyndow"

        # Ensure that the destination directory exists
        package_dir.mkdir(parents=True, exist_ok=True)

        # Collection of the built extensions
        exts = [
            *Path(build_ext.build_temp).rglob("*.pyd"),
            *Path(build_ext.build_temp).rglob("*.dll"),
            *Path(build_ext.build_temp).rglob("*.so"),
            *Path(build_ext.build_temp).rglob("*.so.*"),
            *Path(build_ext.build_temp).rglob("*.dylib"),
        ]

        # Move the extensions to the destination directory
        for ext in exts:
            ext.replace(package_dir / ext.name)


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
from __future__ import annotations

from pathlib import Path
from typing import Any

from pybind11.setup_helpers import build_ext as _build_ext
from setuptools import Command
from setuptools.command.build import build as _build


class cmake(Command):
    def initialize_options(self: cmake) -> None:
        pass

    def finalize_options(self: cmake) -> None:
        pass

    def run(self: cmake) -> None:
        # Needs other commands for specific attributes
        build_ext = self.get_finalized_command("build_ext")
        build_py = self.get_finalized_command("build_py")

        # Configure and build the extensions with CMake in the
        # provided temporary build directory from build_ext
        self.spawn(["cmake", "-S", ".", "-B", build_ext.build_temp])
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


class build(_build):
    def finalize_options(self: build) -> None:
        super().finalize_options()

        # This is essential to move the built extensions to a directory
        # where it will be eventually be copied to the directory where
        # the package will be installed
        self.build_lib = self.build_platlib

    def run(self: build) -> None:
        for command in self.sub_commands:
            self.run_command(command[0])


class build_ext(_build_ext):
    def run(self: build_ext) -> None:
        self.run_command("cmake")
        super().run()


def pdm_build_update_setup_kwargs(_, kwargs: dict[str, Any]) -> None:
    kwargs.update(
        cmdclass={
            "build": build,
            "build_ext": build_ext,
            "cmake": cmake,
        },
    )

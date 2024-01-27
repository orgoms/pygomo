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
        build_ext = self.get_finalized_command("build_ext")
        build_py = self.get_finalized_command("build_py")

        self.spawn(["cmake", "-S", ".", "-B", build_ext.build_temp])
        self.spawn(["cmake", "--build", build_ext.build_temp])

        if build_ext.inplace:
            package_dir = Path(build_py.get_package_dir("pyndow"))
        else:
            package_dir = Path(build_ext.build_lib) / "pyndow"
        package_dir.mkdir(parents=True, exist_ok=True)

        exts = [
            *Path(build_ext.build_temp).rglob("*.pyd"),
            *Path(build_ext.build_temp).rglob("*.dll"),
            *Path(build_ext.build_temp).rglob("*.so"),
            *Path(build_ext.build_temp).rglob("*.so.*"),
            *Path(build_ext.build_temp).rglob("*.dylib"),
        ]

        for ext in exts:
            ext.replace(package_dir / ext.name)


class build(_build):
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

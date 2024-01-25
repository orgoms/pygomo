from __future__ import annotations

from pathlib import Path
from typing import Any

from setuptools.command.build_ext import build_ext as _build_ext
from setuptools.extension import Extension


class CMakeExtension(Extension):
    def __init__(self: CMakeExtension) -> None:
        super().__init__("cmake", sources=[])


class build_ext(_build_ext):
    def build_extension(self: build_ext, ext: Extension) -> None:
        if isinstance(ext, CMakeExtension):
            self.build_cmake()
            self.extensions.remove(ext)
            return
        super().build_extension(ext)

    def build_cmake(self: build_ext) -> None:
        cwd = Path().absolute()
        root_dir = str(cwd)
        build_dir = str(cwd / "build")

        self.spawn(["cmake", "-S", root_dir, "-B", build_dir])
        self.spawn(["cmake", "--build", build_dir])

        if self.inplace:
            build_py = self.get_finalized_command("build_py")
            package_dir = Path(build_py.get_package_dir("pyndow"))
        else:
            package_dir = Path(self.build_lib) / "pyndow"

        ext_path = cwd / "build" / "ext"
        exts = ext_path.rglob("*")

        for ext in exts:
            ext.rename(package_dir / ext.name)


ext_modules = [CMakeExtension()]


def pdm_build_update_setup_kwargs(_, kwargs: dict[str, Any]) -> None:
    kwargs.update(
        ext_modules=ext_modules,
        cmdclass={
            "build_ext": build_ext,
        },
    )

from pathlib import PureWindowsPath, Path, PurePosixPath
from pysemble.compilers import Compiler
from pysemble.archivers import Archiver
from pysemble.logger.log import log
from shutil import copyfile
import platform
import os.path
import os
import shutil

def is_posix() -> bool:
    return platform.system() == "Linux" or platform.system() == "Darwin"

build_dir: Path
if is_posix():
    build_dir = Path(PurePosixPath(os.getcwd())) / "__pysembled__/"
else:
    build_dir = Path(PureWindowsPath(os.getcwd())) / "__pysembled__/"


def create_cache():
    if not os.path.isdir(build_dir):
        log("No build directory found, creating a new one at: " + str(build_dir), info=True)
        os.mkdir(build_dir)

class Project:
    def __init__(self, name: str, compiler: Compiler):
        create_cache()
        self.name = name
        self.compiler = compiler
        self.executables: list[str] = []
        self.static_libraries: list[str] = []
        self.dynamic_libraries: list[str] = []
        self.include_directories: list[str] = []
        self.link_paths: list[str] = []

    # executables
    def add_executable(self, path: str):
        self.executables.append(str(Path(path)))

    def add_executables(self, paths: list[str]):
        for path in paths:
            self.executables.append(str(Path(path)))

    def add_static_lib(self, path: str):
        self.static_libraries.append(str(Path(path)))

    def add_static_libs(self, paths: list[str]):
        for path in paths:
            self.static_libraries.append(str(Path(path)))

    def add_dynamic_lib(self, name: str):
        self.dynamic_libraries.append(name)

    def add_dynamic_libs(self, names: list[str]):
        self.dynamic_libraries += names

    def add_link_path(self, path: str):
        self.link_paths.append(str(Path(path)))

    def add_include_directory(self, path: str):
        self.include_directories.append(str(Path(path)))

    def build(self):
        object_files = self.compiler.build_to_objects(build_dir, self.executables, includes=self.include_directories)
        self.compiler.build(Path(self.name), object_files, includes=self.include_directories,
                            link_paths=self.link_paths, shared_objects=self.dynamic_libraries,
                            static_libraries=self.static_libraries
                            )

    def run(self):
        if is_posix():
            final_command = "./" + self.name
        else:
            final_command = ".\\" + self.name

        log(final_command, debug=True)
        os.system(final_command)

class Library:
    def __init__(self, name: str, compiler: Compiler, archiver: Archiver):
        create_cache()
        self.name = name
        self.compiler = compiler
        self.archiver = archiver
        self.libraries: list[str] = []
        self.objects: list[str] = []
        self.headers: list[str] = []
        self.include_directories: list[str] = []

        if not name.startswith("lib"):
            log("Library name should be structured lib<name>", warn=True)

    def add_source(self, path):
        self.libraries.append(str(Path(path)))

    def add_sources(self, paths):
        for path in paths:
            self.libraries.append(str(Path(path)))

    def add_header(self, path):
        self.headers.append(str(Path(path)))

    def add_headers(self, paths):
        for path in paths:
            self.headers.append(str(Path(path)))

    def add_include_directory(self, path: str):
        self.include_directories.append(str(Path(path)))

    def build(self):
        self.objects = self.compiler.build_to_objects(build_dir, self.libraries)
        self.archiver.archive(build_dir / self.name, self.objects)

    def build_shared(self):
        self.objects = self.compiler.build_sharable_objects(build_dir, self.libraries, self.include_directories)
        self.compiler.build_shared_object(build_dir / (self.name + ".so"), self.objects)

    def package(self, dynamic=False):
        # setting up folder for package
        if os.path.isdir(self.name):
            shutil.rmtree(self.name)

        os.mkdir(self.name)
        lib_path: Path = Path(self.name) / "lib/"
        include_path: Path = Path(self.name) / "include/"
        os.mkdir(lib_path)
        os.mkdir(include_path)

        # copy header files over
        for header in self.headers:
            file_name = os.path.basename(header)
            copyfile(header, include_path / file_name)

        # build shared objects
        self.objects = self.compiler.build_sharable_objects(build_dir, self.libraries, self.include_directories)

        if len(self.headers) == 0:
            log("Packaging library with not header files, is this intentional?", warn=True)

        if dynamic:
            self.compiler.build_shared_object(lib_path / (self.name + ".so"), self.objects)
        else:
            self.archiver.archive(lib_path / self.name, self.objects)

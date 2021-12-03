from shutil import copyfile
import os.path
import os
import shutil
import logging
from pysemble.logger.log import log

build_dir = os.getcwd() + "/__pysembled__/"
logging.basicConfig(format='\033[1;37;40m %(levelname)s :: (%(asctime)s) :: %(message)s', datefmt='%H:%M:%S', level=logging.DEBUG)

def create_cache():
    if not os.path.isdir(build_dir):
        log("No build directory found, creating a new one at: " + build_dir, info=True)
        os.mkdir(build_dir)

class Project:
    def __init__(self, name, compiler):
        create_cache()
        self.name = name
        self.compiler = compiler
        self.executables = []
        self.static_libraries = []
        self.dynamic_libraries = []
        self.include_directories = []
        self.link_path = ""

    # executables
    def add_executable(self, path):
        self.executables.append(path)

    def add_executables(self, paths):
        self.executables = self.executables + paths

    def add_static_lib(self, path):
        self.static_libraries.append(path)

    def add_static_libs(self, paths):
        self.static_libraries += paths

    def add_dynamic_lib(self, name):
        self.dynamic_libraries.append(name)

    def add_dynamic_libs(self, names):
        self.dynamic_libraries += names

    def set_link_path(self, path):
        self.link_path = path

    def add_include_directory(self, path):
        self.include_directories.append(path)

    def build(self):
        object_files = self.compiler.build_to_objects(build_dir, self.executables, includes=self.include_directories)
        self.compiler.build(self.name, object_files, includes=self.include_directories,
                            link_path=self.link_path, shared_objects=self.dynamic_libraries,
                            static_libraries=self.static_libraries
                            )

    def run(self):
        os.system("./" + self.name)

class Library:
    def __init__(self, name, compiler, archiver):
        create_cache()
        self.name = name
        self.compiler = compiler
        self.archiver = archiver
        self.libraries = []
        self.objects = []
        self.headers = []

    def add_source(self, path):
        self.libraries.append(path)

    def add_sources(self, paths):
        self.libraries += paths

    def add_header(self, path):
        self.headers.append(path)

    def add_headers(self, paths):
        self.headers += paths

    def build(self):
        self.objects = self.compiler.build_to_objects(build_dir, self.libraries)
        self.archiver.archive(build_dir + self.name, self.objects)

    def build_shared(self):
        self.objects = self.compiler.build_sharable_objects(build_dir, self.libraries)
        self.compiler.build_shared_object(build_dir + self.name + ".so", self.objects)

    def package(self, dynamic=False):
        # setting up folder for package
        if os.path.isdir(self.name):
            shutil.rmtree(self.name)

        os.mkdir(self.name)
        lib_path = self.name + "/lib/"
        include_path = self.name + "/include/"
        os.mkdir(lib_path)
        os.mkdir(include_path)

        # copy header files over
        for header in self.headers:
            file_name = os.path.basename(header)
            copyfile(header, include_path + file_name)

        # build shared objects
        self.objects = self.compiler.build_sharable_objects(build_dir, self.libraries)

        if dynamic:
            self.compiler.build_shared_object(lib_path + self.name + ".so", self.objects)
        else:
            self.archiver.archive(lib_path + self.name, self.objects)
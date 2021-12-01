import os.path
import os

build_dir = os.getcwd() + "/__pycc_cache__/"

def concat_list_prefix(str_list, prefix):
    str = ""
    for s in str_list:
        str = str + " " + prefix + s

    return str

def concat_list(str_list):
    str = ""
    for s in str_list:
        str = str + " " + s

    return str

def create_cache():
    if not os.path.isdir(build_dir):
        os.mkdir(build_dir)


class Project:
    def __init__(self, name, compiler):
        self.name = name
        self.compiler = compiler
        self.executables = []
        self.static_libraries = []
        self.dynamic_libraries = []
        self.link_path = ""

    # executables
    def add_executable(self, path):
        self.executables.append(path)

    def add_executables(self, paths):
        self.executables = self.executables + paths

    def add_static_lib(self, path):
        self.static_libraries.append(path)

    def add_dynamic_lib(self, name):
        self.dynamic_libraries.append(name)

    def set_link_path(self, path):
        self.link_path = path

    def build(self):
        object_files = self.compiler.build_to_objects(build_dir, self.executables)
        if len(self.dynamic_libraries) > 0:
            self.compiler.build(self.name, object_files, link_path=self.link_path, shared_objects=self.dynamic_libraries)
        elif len(self.static_libraries) > 0:
            self.compiler.build(self.name, object_files + self.static_libraries)
        else:
            self.compiler.build(self.name, object_files)

    def run(self):
        os.system("./" + self.name)

class Library:
    def __init__(self, name, compiler, archiver):
        self.name = name
        self.compiler = compiler
        self.archiver = archiver
        self.libraries = []
        self.objects = []

    def add_source(self, path):
        self.libraries.append(path)

    def add_sources(self, paths):
        self.libraries += paths

    def build(self):
        create_cache()
        self.objects = self.compiler.build_to_objects(build_dir, self.libraries)
        self.archiver.archive(build_dir + self.name, self.objects)

    def build_shared(self):
        create_cache()
        self.objects = self.compiler.build_sharable_objects(build_dir, self.libraries)
        self.compiler.build_shared_object(build_dir + self.name + ".so", self.objects)


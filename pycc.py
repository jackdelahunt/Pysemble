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

    # executables
    def add_executable(self, path):
        self.executables.append(path)

    def add_executables(self, paths):
        self.executables = self.executables + paths

    def add_static(self, path):
        self.static_libraries.append(path)

    def build(self):
        if len(self.static_libraries) > 0:
            object_file = self.compiler.build_to_object(build_dir + self.name + ".o", self.executables)
            self.compiler.build(self.name, [object_file] + self.static_libraries)
        else:
            self.compiler.build(self.name, self.executables)

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

    def build(self):
        create_cache()
        object = self.compiler.build_to_object(build_dir + self.name + ".o", self.libraries)
        self.objects.append(object)
        self.archiver.archive(build_dir + self.name, self.objects)
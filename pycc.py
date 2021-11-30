import os.path
import os

build_dir = os.getcwd() + "/__pymake_cache__/"

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
    def __init__(self, name):
        self.name = name
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
            os.system("g++ -c " + concat_list(self.executables) + " -o " + build_dir + self.name + ".o")
            os.system("g++ -o " + self.name + " " + build_dir + self.name + ".o " + concat_list_prefix(self.static_libraries, build_dir))
        else:
            os.system("g++" + concat_list(self.executables) + " -o " + self.name)

    def run(self):
        os.system("./" + self.name)

class Library:
    def __init__(self, name):
        self.name = name
        self.libraries = []
        self.objects = []

    def add_source(self, path):
        self.libraries.append(path)

    def build(self):
        create_cache()
        for l in self.libraries:
            os.system("g++ -c " + l + " -o " + l + ".o")
            self.objects.append(l + ".o")

        object_list = concat_list(self.objects)
        os.system("ar rcs " + build_dir + self.name + ".a " + object_list)
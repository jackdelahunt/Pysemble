from pycc import Project, Library
from enviroment import Gpp, Ar

compiler = Gpp()
archiver = Ar()

library = Library("mylib", compiler, archiver)
library.add_source("mylib/multi_vector.cpp")
library.add_source("mylib/vector.cpp")
library.build()

project = Project("myproject", compiler)
project.add_executables([
    "main.cpp"
])
project.add_static("__pycc_cache__/mylib.a")
project.build()
project.run()
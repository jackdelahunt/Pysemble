from pycc import Project, Library
from enviroment import Gpp, Ar
import os

compiler = Gpp()
archiver = Ar()

os.environ["LD_LIBRARY_PATH"] = "/home/jackdelahunt/Projects/pymake/__pycc_cache__"


library = Library("libvector", compiler, archiver)
library.add_sources([
    "mylib/multi_vector.cpp",
    "mylib/vector.cpp"
])
library.build_shared()

project = Project("myproject", compiler)
project.add_executables([
    "main.cpp"
])
project.set_link_path("/home/jackdelahunt/Projects/pymake/__pycc_cache__/")
project.add_dynamic_lib("vector")
project.build()
project.run()
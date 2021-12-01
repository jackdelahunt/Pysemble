from pycc import Project, Library
from enviroment import Gpp, Ar
import os

compiler = Gpp()
archiver = Ar()

os.environ["LD_LIBRARY_PATH"] = "/home/jackdelahunt/Projects/pymake/SFML/lib"

project = Project("myproject", compiler)
project.add_executables([
    "main.cpp"
])
project.set_link_path("/home/jackdelahunt/Projects/pymake/SFML/lib")
project.add_include_directory("/home/jackdelahunt/Projects/pymake/SFML/include")
project.add_dynamic_libs([
    "sfml-graphics",
    "sfml-window",
    "sfml-system",
    "sfml-audio",
])
project.build()
project.run()
from pycc import Project, Library
from enviroment import Gpp, Ar
import os

compiler = Gpp()
archiver = Ar()

dir_path = os.path.dirname(os.path.realpath(__file__))
os.environ["LD_LIBRARY_PATH"] = dir_path + "/SFML/lib"

project = Project("myproject", compiler)
project.add_executables([
    "main.cpp",
])
project.set_link_path("SFML/lib")
project.add_include_directory("SFML/include")
project.add_dynamic_libs([
    "sfml-graphics",
    "sfml-window",
    "sfml-system",
    "sfml-audio",
])
project.build()
project.run()
from pysemble.builders import Project, Library
from pysemble.compilers import Gpp
from pysemble.archivers import Ar
import os

compiler = Gpp()
archiver = Ar()

# lib = Library("liblogger", compiler, archiver)
# lib.add_source("src/logger.cpp")
# lib.add_header("src/logger.h")
# lib.package(dynamic=True)

working_directory = os.path.dirname(os.path.realpath(__file__))
os.environ["LD_LIBRARY_PATH"] = working_directory + "/liblogger/lib"

project = Project("main", compiler)
project.add_executables([
    "src/main.cpp",
])
project.add_dynamic_lib("logger")
project.add_include_directory("liblogger/include")
project.set_link_path("liblogger/lib")
project.build()
project.run()
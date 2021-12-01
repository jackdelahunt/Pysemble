from pycc import Project, Library
from enviroment import Gpp, Ar

compiler = Gpp()
archiver = Ar()

library = Library("mylib", compiler, archiver)
library.add_sources([
    "mylib/multi_vector.cpp",
    "mylib/vector.cpp"
])
library.build_shared()

# project = Project("myproject", compiler)
# project.add_executables([
#     "main.cpp"
# ])
# project.add_static("__pycc_cache__/mylib.a")
# project.build()
# project.run()
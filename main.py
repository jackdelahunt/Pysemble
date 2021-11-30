from pycc import Project, Library
from enviroment import Gpp, Ar

compiler = Gpp()
archiver = Ar()

lib = Library("lib", compiler, archiver)
lib.add_source("/home/jackdelahunt/Projects/pymake/lib/preson.cpp")
lib.build()

game = Project("game", compiler)
game.add_executable("main.cpp")
game.add_static("__pycc_cache__/lib.a")
game.build()
game.run()
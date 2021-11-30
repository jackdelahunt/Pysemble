from pycc import Project, Library

lib = Library("lib")
lib.add_source("/home/jackdelahunt/Projects/pymake/lib/preson.cpp")
lib.build()

game = Project("game")
game.add_executables([
    "main.cpp",
])
game.add_static("lib.a")
game.build()
game.run()
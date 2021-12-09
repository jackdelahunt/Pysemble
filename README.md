# Pysemble

Custom build system for C/C++ for use with python for configuration.

## Features
### Supported Compilers
- G++
- Gcc
- Clang

Any compiler or archiver used must be accessible in the PATH with its standard name.

### Supported Archivers
- Ar

### Supported OS
- Windows
- Unix like

### Build Types
- Build to binary
  - with static or dynamic linking
- Static library
  - with static linking
- Dynamic Library
  - with static linking

## Install
```python
pip install pysemble
```

## Modules
```python
from pysemble.builders import Project, Library
from pysemble.compilers import Gpp
from pysemble.archivers import Ar
```

## Hello world Build
```python
compiler = Gpp() # g++

myapp = Project("myapp", compiler)
myapp.add_executable("hello_world.cpp")
myapp.build()
myapp.run()
```

## Building a Library
```python
compiler = Gpp() # g++
archiver = Ar()  # ar

mylibrary = Library("libmylibrary", compiler, archiver)
mylibrary.add_sources([
    "dependency_1.cpp",
    "dependency_2.cpp",
    "dependency_3.cpp",
    "dependency_4.cpp",
])
mylibrary.buid()         # static library
mylibrary.build_shared() # dynamic library
```

## Add External Libraries to Project

```python
compiler = Gpp()  # g++

working_directory = os.path.dirname(os.path.realpath(__file__))
os.environ["LD_LIBRARY_PATH"] = working_directory + "/SFML/lib"

project = Project("myproject", compiler)
project.add_executables([
  "main.cpp",
])
project.add_link_path("SFML/lib")
project.add_include_directory("SFML/include")
project.add_dynamic_libs([
  "sfml-graphics",
  "sfml-window",
  "sfml-system",
  "sfml-audio",
])
project.build()
project.run()
```

## Package a Library for Distrobution
```python
compiler = Gpp() # g++
archiver = Ar()  # ar

loggerlib = Library("liblogger", compiler, archiver)
loggerlib.add_sources([
    "logger.cpp",
])
loggerlib.add_header("logger.h")
loggerlib.package(dynamic=True)
```

### Final package
```
liblogger
    |_ include
          |_ logger.h
    |_ lib
        |_ liblogger.so
```

## Troubleshooting
### Clang & GCC
- If you are building c++ try to link with stdc++ if you are having problems

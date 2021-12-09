from pysemble.lists.helpers import concat_list
from pathlib import Path
import os.path
import os
from pysemble.logger.log import log

class Compiler:

    def build(self, out: Path, files: list[str], includes: list[str] = [], link_path = "", shared_objects: list[str] = [], static_libraries: list[str]=[]):
        pass

    def build_to_objects(self, location: Path, files: list[str], includes: list[str] = []) -> list[str]:
        pass

    def build_sharable_objects(self, location: Path, files: list[str], includes: list[str] = []) -> list[str]:
        pass

    def build_shared_object(self, out: Path, files: list[str]) -> str:
        pass


class GCC_API(Compiler):

    def __init__(self, compiler_name: str, version: str, optimization: int):
        self.compiler_name = compiler_name
        self.flags: list[str] = ["-std=" + version, "-O" + str(optimization)]

    def build(self, out: Path, files: list[str], includes: list[str] = [], link_paths: list[str] = [], shared_objects: list[str] = [], static_libraries: list[str]=[]):
        file_list = concat_list(files)
        flag_list = concat_list(self.flags)
        final_command = self.compiler_name + \
                        flag_list + \
                        " -o " + str(out) + " " \
                        + file_list + " "

        if len(includes) > 0:
            for i in includes:
                final_command += "-I" + i + " "

        if len(link_paths) > 0:
            for i in link_paths:
                final_command += "-L" + i + " "

        if len(shared_objects) > 0:
            for so in shared_objects:
                final_command += "-l" + so + " "

        if len(static_libraries) > 0:
            for ar in static_libraries:
                final_command += ar + " "

        log(self.compiler_name + " building " + file_list + " -> " + str(out))

        log(final_command, debug=True)
        os.system(final_command)

    def build_to_objects(self, location: Path, files: list[str], includes: list[str] = []) -> list[str]:
        object_files: list[str] = []
        for file in files:
            # file is the file location
            # base file is the file name
            base_file: str = os.path.basename(file)
            object_file = str(location / (base_file + ".o"))
            final_command = self.compiler_name + concat_list(self.flags) + " -c -o " + object_file + " " + file

            if len(includes) > 0:
                for i in includes:
                    final_command += " -I" + i + " "

            log(self.compiler_name + " building the following as an object file: " + base_file + " -> " + object_file, info=True)
            log(final_command, debug=True)
            os.system(final_command)
            object_files.append(object_file)

        return object_files

    def build_sharable_objects(self, location: Path, files: list[str], includes: list[str] = []) -> list[str]:
        object_files: list[str] = []
        for file in files:
            base_file: str = os.path.basename(file)
            object_file = str(location / (base_file + ".o"))
            final_command = self.compiler_name + concat_list(self.flags) + " -fpic -c -o " + object_file + " " + file
            if len(includes) > 0:
                for i in includes:
                    final_command += " -I" + i + " "

            os.system(final_command)
            log(self.compiler_name + " building the following as sharable object files: " + base_file + " -> " + object_file, info=True)
            log(final_command, debug=True)
            object_files.append(object_file)
        return object_files

    def build_shared_object(self, out: Path, files: list[str]) -> str:
        final_command = self.compiler_name + concat_list(self.flags) + " -shared "
        out_str = str(out)
        file_list = concat_list(files)
        final_command += file_list
        final_command += " -o " + out_str
        log(self.compiler_name + " building the following as a shared object: " + file_list + " -> " + out_str,
            info=True)
        log(final_command, debug=True)
        os.system(final_command)
        return out_str


class Gcc(GCC_API):
    def __init__(self, version: str = "c++17", optimization: int = 2):
        if optimization < 0 or optimization > 4:
            log("Optimization level needs to be between 0 -> 4", err=True)

        super().__init__("gcc", version, optimization)


class Gpp(GCC_API):
    def __init__(self, version: str = "c++17", optimization: int = 2):
        super().__init__("g++", version, optimization)


class Clang(GCC_API):
    def __init__(self, version: str = "c++17", optimization: int = 2):
        super().__init__("clang", version, optimization)

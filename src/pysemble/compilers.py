from pysemble.lists.helpers import concat_list
import os.path
import os
from pysemble.logger.log import log

class Compiler:

    def build(self, out, files, link_path="", shared_objects=[]):
        pass

    def build_to_objects(self, location, files) -> list[str]:
        pass

    def build_sharable_objects(self, location, files) -> list[str]:
        pass

    def build_shared_object(self, out, files) -> str:
        pass


class Gpp(Compiler):

    def build(self, out, files, includes=[], link_path="", shared_objects=[], static_libraries=[]):
        file_list = concat_list(files)
        final_command = "g++ -o " + out + " " + file_list + " "

        if len(includes) > 0:
            for i in includes:
                final_command += "-I" + i + " "

        if link_path != "":
            final_command += "-L" + link_path + " "

        if len(shared_objects) > 0:
            for so in shared_objects:
                final_command += "-l" + so + " "

        if len(static_libraries) > 0:
            for ar in static_libraries:
                final_command += ar + " "

        log("\ng++ building " + file_list + " -> " + out + " with:\n"
            "Includes: " + str(includes) + "\n"
            "Link path: " + link_path + "\n"
            "Link libraries: " + str(shared_objects) + "\n"
            "Static libraries: " + str(static_libraries), info=True)

        log(final_command, debug=True)
        os.system(final_command)

    def build_to_objects(self, location, files, includes=[]) -> list[str]:
        object_files = []
        for file in files:
            # file is the file location
            # base file is the file name
            base_file = os.path.basename(file)
            final_command = "g++ -c " + file

            object_file = location + base_file + ".o"

            if len(includes) > 0:
                for i in includes:
                    final_command += " -I " + i + " "

            final_command += " -o " + object_file

            log("g++ building the following as an object file: " + base_file + " -> " + object_file, info=True)
            log(final_command, debug=True)
            os.system(final_command)
            object_files.append(object_file)

        return object_files

    def build_sharable_objects(self, location, files) -> list[str]:
        object_files = []
        for file in files:
            base_file = os.path.basename(file)
            object_file = location + base_file + ".o"
            log("g++ building the following as sharable object files: " + base_file + " -> " + object_file, info=True)
            os.system("g++ -c " + file + " -o " + object_file + " -fpic")
            object_files.append(object_file)
        return object_files

    def build_shared_object(self, out, files) -> str:
        final_command = "g++ -shared "
        file_list = concat_list(files)
        final_command += file_list
        final_command += " -o " + out
        log("g++ building the following as a shared object: " + file_list + " -> " + out, info=True)
        log(final_command, debug=True)
        os.system(final_command)
        return out
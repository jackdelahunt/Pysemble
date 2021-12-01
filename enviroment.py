import os.path
import os


def concat_list(str_list) -> str:
    str = ""
    for s in str_list:
        str = str + " " + s
    return str


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
        final_command = "g++ -o " + out + " " + concat_list(files) + " "

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

            os.system(final_command)
            object_files.append(object_file)
        return object_files

    def build_sharable_objects(self, location, files) -> list[str]:
        object_files = []
        for file in files:
            # file is the file location
            # base file is the file name
            base_file = os.path.basename(file)

            object_file = location + base_file + ".o"
            os.system("g++ -c " + file + " -o " + object_file + " -fpic")
            object_files.append(object_file)
        return object_files

    def build_shared_object(self, out, files) -> str:
        os.system("g++ -shared " + concat_list(files) + " -o " + out)
        return out


class Archiver:

    def archive(self, out, files) -> str:
        pass


class Ar(Archiver):

    def archive(self, out, files) -> str:
        final_out = out + ".a"
        os.system("ar rcs " + final_out + concat_list(files))
        return final_out

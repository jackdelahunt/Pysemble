import os.path
import os

def concat_list(str_list) -> list[str]:
    str = ""
    for s in str_list:
        str = str + " " + s
    return str

class Compiler:

    def build(self, out, files):
        pass

    def build_to_objects(self, location, files) -> list[str]:
        pass

    def build_from_objects(self, out, files) -> str:
        pass


class Gpp(Compiler):

    def build(self, out, files):
        os.system("g++ " + concat_list(files) + " -o " + out)

    def build_to_objects(self, location, files) -> list[str]:
        object_files = []
        for file in files:

            # file is the file location
            # base file is the file name
            base_file = os.path.basename(file)

            object_file = location + base_file + ".o"
            os.system("g++ -c " + file + " -o " + object_file)
            object_files.append(object_file)
        return object_files

    def build_from_objects(self, out, files) -> str:
        os.system("g++ -o " + out + " " + concat_list(files))
        return out

class Archiver:

    def archive(self, out, files) -> str:
        pass

class Ar(Archiver):

    def archive(self, out, files) -> str:
        final_out = out + ".a"
        os.system("ar rcs " + final_out + concat_list(files))
        return final_out
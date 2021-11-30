import os.path
import os

def concat_list(str_list):
    str = ""
    for s in str_list:
        str = str + " " + s
    return str

class Compiler:

    def build(self, out, files):
        pass

    def build_to_object(self, out, files):
        pass

    def build_from_objects(self, out, files):
        pass


class Gpp(Compiler):

    def build(self, out, files):
        os.system("g++ " + concat_list(files) + " -o " + out)

    def build_to_object(self, out, files):
        os.system("g++ -c " + concat_list(files) + " -o " + out)
        return out

    def build_from_objects(self, out, files):
        os.system("g++ -o " + out + " " + concat_list(files))
        return out

class Archiver:

    def archive(self, out, files):
        pass

class Ar(Archiver):

    def archive(self, out, files):
        final_out = out + ".a"
        os.system("ar rcs " + final_out + concat_list(files))
        return final_out
from pysemble.builders import concat_list
import os.path
import os



class Archiver:

    def archive(self, out, files) -> str:
        pass


class Ar(Archiver):

    def archive(self, out, files) -> str:
        final_out = out + ".a"
        os.system("ar rcs " + final_out + concat_list(files))
        return final_out

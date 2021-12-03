from lists.helpers import concat_list
import os.path
import os
from logger.log import log

class Archiver:

    def archive(self, out, files) -> str:
        pass


class Ar(Archiver):

    def archive(self, out, files) -> str:
        final_out = out + ".a"
        file_list = concat_list(files)
        log("ar archiving the following: " + file_list + " -> " + final_out, info=True)
        final_command = "ar rcs " + final_out + file_list
        os.system(final_command)

        return final_out

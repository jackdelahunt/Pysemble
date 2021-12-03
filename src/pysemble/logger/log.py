import logging

def log(message, info=False, debug=False, warn=False, err=False):

    if info:
        logging.info("\033[1;32;40m " + message + "\033[1;37;40m")

    if debug:
        logging.debug("\033[1;34;40m " + message + "\033[1;37;40m")

    if warn:
        logging.warning("\033[1;33;40m " + message + "\033[1;37;40m")

    if err:
        logging.error("\033[1;31;40m " + message + "\033[1;37;40m")
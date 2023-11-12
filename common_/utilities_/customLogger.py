import logging
from datetime import date
import os
from pathlib import Path

def get_root_dir_name():
    command = "Path(__file__).absolute()"
    while True:
        rootDir = str(eval(command))
        if rootDir.split(sep="\\")[-1] == "AmazonTestEnvirnment_AGBU":
            return rootDir
        else:
            command += ".parent"

def logger(level, message, fileName=os.path.join(get_root_dir_name(), '_logs_', f'log_{date.today()}.log')):
    logging.basicConfig(level=logging.INFO, filename=fileName, filemode="w",
                        format="%(asctime)-12s %(levelname)s %(message)s",
                        datefmt="%d-%m-%Y %H:%M:%S")
    if level == "INFO":
        logging.info(message)
        print(message)
        return
    elif level == "DEBUG":
        logging.debug(message)
        print(message)

    elif level == "WARNING":
        logging.warning(message)
        print(message)

    elif level == "ERROR":
        logging.error(message)
        print(message)

    elif level == "CRITICAL":
        logging.critical(message)
        print(message)

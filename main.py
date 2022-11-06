# Main file for automation of Moodle synchonization

import os
import logging
from datetime import datetime


def init():
    print("Intialization application for moodle export")
    #_current_date = datetime.today().strftime('%Y%m%d')
    _filename = 'log_moodle_automated.log'
    try:
        logging.basicConfig(filename=_filename, encoding='utf-8', level=logging.DEBUG)
    except FileExistsError:
        logging.info("Log file " + _filename + " already exists.")
        pass
def main():
    # Init application
    init()

    try:
        os.makedirs('parentdirectory/mydirectory')
    except FileExistsError:
        logging.error("Directory was not able do be created.")
        pass


if __name__ == '__main__':
    main()

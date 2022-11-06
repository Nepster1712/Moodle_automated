# Main file for automation of Moodle synchonization

import os
import logging
from datetime import datetime


def init():
    print("Intialization application for moodle export")
    _filename = 'log_moodle_automated.log'
    try:
        logging.basicConfig(filename=_filename, encoding='utf-8', level=logging.DEBUG)
    except FileExistsError:
        logging.info("Log file " + _filename + " already exists.")
        pass
    finally:
        del _filename

# Main function
def main():
    # Init application
    init()

    try:
        _dirName = 'Test'
        os.makedirs(_dirName)
    except FileExistsError:
        logging.error(datetime.today().strftime('[%Y-%m-%d %H:%M:%S]') + ' Directory ' + _dirName + ' was not able do be created.')
        pass
    finally:
        del _dirName


if __name__ == '__main__':
    main()

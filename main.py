# Main file for automation of Moodle synchonization
import os
import logging
from warnings import warn
from datetime import datetime


def init(_filename = 'log_moodle_automated.log'):
    warn(f'The module {__name__} is deprecated.', DeprecationWarning, stacklevel=2)
    print("Intialization application for moodle export")
    try:
        logging.basicConfig(filename=_filename, encoding='utf-8', level=logging.DEBUG)
    except FileExistsError:
        logging.info("Log file " + _filename + " already exists.")
        pass
    except FileNotFoundError:
        raise FileNotFoundError
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

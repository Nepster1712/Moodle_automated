# Testing
import pytest
import logging
from os.path import exists as file_exists
from main import init

def test_init():
    _filename = 'log_moodle_automated.log'
    try:
        init(_filename)
    finally:
        assert file_exists(_filename) == True


         
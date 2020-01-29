# coding: utf-8
"""
This will add the executable to your PATH so it will be found.
The filename of the binary is stored in `geckodriver_filename`.
"""

import os
from . import utils


def add_geckodriver_to_path():
    """
    Appends the directory of the geckodriver binary file to PATH.
    """
    geckodriver_dir = os.path.abspath(os.path.dirname(__file__))
    if 'PATH' not in os.environ:
        os.environ['PATH'] = geckodriver_dir
    elif geckodriver_dir not in os.environ['PATH']:
        os.environ['PATH'] = geckodriver_dir + utils.get_variable_separator() + os.environ['PATH']


geckodriver_filename = os.path.join(os.path.abspath(os.path.dirname(__file__)), utils.get_geckodriver_filename())
add_geckodriver_to_path()

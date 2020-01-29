# coding: utf-8
"""
Helper functions for filename and URL generation.
"""

import sys
import os
import subprocess
import re

__author__ = 'Ramon Medeiros <ramon.medeiros@gmail.com>'


def get_geckodriver_filename():
    """
    Returns the filename of the binary for the current platform.
    :return: Binary filename
    """
    if sys.platform.startswith('win'):
        return 'geckodriver.exe'
    return 'geckodriver'


def get_geckodriver_url(version):
    """
    Generates the download URL for current platform , architecture and the given version.
    Supports Linux, MacOS and Windows.
    :param version: geckodriver version string
    :return: Download URL for geckodriver
    """
    base_url = 'https://github.com/mozilla/geckodriver/releases/download/'

    # get arch
    architecture = 32
    if sys.maxsize > 2 ** 32:
        architecture = 64

    # get platform
    extension = '.tar.gz'
    if sys.platform.startswith('linux'):
        platform = 'linux'
    elif sys.platform == 'darwin':
        platform = 'macos'
        architecture = ''
        return base_url + version + '/geckodriver-' + version + '-' + platform  + extension
    elif sys.platform.startswith('win'):
        platform = 'win'
        extension = '.zip'
    else:
        raise RuntimeError('Could not determine geckodriver download URL for this platform.')
    return base_url + version + '/geckodriver-' + version + '-'+ platform +  architecture + extension



def get_variable_separator():
    """
    Returns the environment variable separator for the current platform.
    :return: Environment variable separator
    """
    if sys.platform.startswith('win'):
        return ';'
    return ':'


def find_binary_in_path(filename):
    """
    Searches for a binary named `filename` in the current PATH. If an executable is found, its absolute path is returned
    else None.
    :param filename: Filename of the binary
    :return: Absolute path or None
    """
    if 'PATH' not in os.environ:
        return None
    for directory in os.environ['PATH'].split(get_variable_separator()):
        binary = os.path.abspath(os.path.join(directory, filename))
        if os.path.isfile(binary) and os.access(binary, os.X_OK):
            return binary
    return None


def check_version(binary, required_version):
    try:
        version = subprocess.check_output([binary, '-v'])
        version = re.match(r'.*?([\d.]+).*?', version.decode('utf-8'))[1]
        if version == required_version:
            return True
    except Exception:
        return False
    return False


def get_geckodriver_path():
    """
    :return: path of the geckodriver binary
    """
    return os.path.abspath(os.path.dirname(__file__))


def print_geckodriver_path():
    """
    Print the path of the geckodriver binary.
    """
    print(get_geckodriver_path())

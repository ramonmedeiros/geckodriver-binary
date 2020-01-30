from setuptools import setup
from setuptools.command.build_py import build_py
from geckodriver_binary.utils import get_geckodriver_filename, get_geckodriver_url, find_binary_in_path, check_version

import os
import tarfile
import zipfile

try:
    from io import BytesIO
    from urllib.request import urlopen, URLError
except ImportError:
    from StringIO import StringIO as BytesIO
    from urllib2 import urlopen, URLError

__author__ = 'Ramon Medeiros <ramon.rnm@gmail.com>'


with open('README.md') as readme_file:
    long_description = readme_file.read()


class DownloadGeckodriver(build_py):
    def run(self):
        """
        Downloads, unzips and installs geckodriver.
        If a geckodriver binary is found in PATH it will be copied, otherwise downloaded.
        """
        geckodriver_version="v0.25.0"
        geckodriver_dir = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'geckodriver_binary')
        geckodriver_filename = find_binary_in_path(get_geckodriver_filename())
        if geckodriver_filename and check_version(geckodriver_filename, geckodriver_version):
            print("\ngeckodriver already installed at {}...\n".format(geckodriver_filename))
            new_filename = os.path.join(geckodriver_dir, get_geckodriver_filename())
            self.copy_file(geckodriver_filename, new_filename)
        else:
            geckodriver_bin = get_geckodriver_filename()
            geckodriver_filename = os.path.join(geckodriver_dir, geckodriver_bin)
            if not os.path.isfile(geckodriver_filename) or not check_version(geckodriver_filename, geckodriver_version):
                print("\nDownloading geckodriver...\n")
                if not os.path.isdir(geckodriver_dir):
                    os.mkdir(geckodriver_dir)
                url = get_geckodriver_url(version=geckodriver_version)
                try:
                    response = urlopen(url)
                    if response.getcode() != 200:
                        raise URLError('Not Found')
                except URLError:
                    raise RuntimeError('Failed to download geckodriver archive: {}'.format(url))
                archive = BytesIO(response.read())
                if url.endswith(".zip") is True:
                    with zipfile.ZipFile(archive) as zip_file:
                        zip_file.extract(geckodriver_bin, geckodriver_dir)
                elif url.endswith(".tar.gz") is True:
                    with tarfile.open(fileobj=archive, mode="r:gz") as tar_file:
                        tar_file.extractall(path=geckodriver_dir)
            else:
                print("\ngeckodriver already installed at {}...\n".format(geckodriver_filename))
            if not os.access(geckodriver_filename, os.X_OK):
                os.chmod(geckodriver_filename, 0o744)
        build_py.run(self)


setup(
    name="geckodriver-binary",
    version="v0.25.0",
    author="Ramon Medeiros",
    author_email="ramon.rnm@gmail.com",
    description="Installer for geckodriver.",
    license="MIT",
    keywords="geckodriver gecko browser selenium splinter",
    url="https://github.com/ramonmedeiros/geckodriver-binary",
    packages=['geckodriver_binary'],
    package_data={
        'geckodriver_binary': ['geckodriver*']
    },
    entry_points={
        'console_scripts': ['geckodriver-path=geckodriver_binary.utils:print_geckodriver_path'],
    },
    long_description_content_type='text/markdown',
    long_description=long_description,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Topic :: Software Development :: Testing",
        "Topic :: System :: Installation/Setup",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",
    ],
    cmdclass={'build_py': DownloadGeckodriver}
)

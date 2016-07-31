#!/usr/bin/env python

import os
from setuptools import find_packages

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

metadata = {}
metadata_file = "{{cookiecutter.directory_name}}/metadata.py"
exec(compile(open(metadata_file).read(), metadata_file, 'exec'), metadata)

# http://pypi.python.org/pypi?:action=list_classifiers
classifiers = [
    "Development Status :: 5 - Production/Stable",
    "Environment :: Console",
    "Intended Audience :: Developers",
    "Natural Language :: English",
    "Operating System :: POSIX :: Linux",
    "Programming Language :: Python :: 2.7",
    "Topic :: Software Development :: Libraries",
    "Topic :: Utilities",
    "License :: OSI Approved :: Apache Software License",
]

setup(
    name='{{cookiecutter.project_name}}',
    version=metadata['__version__'],
    description="",
    long_description="",
    classifiers=classifiers,
    keywords='harvestapp timetracking api',
    author=metadata['__author__'],
    author_email=metadata['__email__'],
    url='https://github.com/lionheart/{{cookiecutter.project_name}}',
    license=metadata['__license__'],
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    include_package_data=True,
    zip_safe=True,
    install_requires=read("requirements.txt").split("\n")
)

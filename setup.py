#-*- encoding: utf-8 -*-
import os
from setuptools import setup, find_packages

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "citidata",
    version = "0.0.1",
    author = "Philip Feuerschütz",
    author_email = "feph@mailbox.org",
    description = ("A package to handle ascii CITI data files"),
    license = "BSD",
    keywords = "rf psw data numpy",
    url = "http://example.com",
    packages=find_packages(),
    entry_points = {
        'console_scripts': [
            ],
        },
    test_suite="nose.collector",
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],
)

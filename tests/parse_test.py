#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import citidata 
import os
import numpy as np
import glob
from nose.tools import with_setup, assert_raises

THIS_DIR = os.path.dirname(os.path.abspath(__file__))

def rel_path(filename):
    return os.path.join(THIS_DIR, filename)

def test_citi():
    testfile_list = glob.glob(rel_path("test_data/*citi"))
    for fn in testfile_list:
        citidata.genfromtxt(fn)


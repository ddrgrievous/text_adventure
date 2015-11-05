'''
Created on Nov 5, 2015

@author: Jared
'''
from distutils.core import setup
import py2exe
import sys

if len(sys.argv) == 1:
    sys.argv.append("py2exe")

setup(console=['main.py'])
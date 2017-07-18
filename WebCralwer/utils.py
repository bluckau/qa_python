from __future__ import print_function
import sys

"""Utility method to print to stderr"""
def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)
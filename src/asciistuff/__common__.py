# -*- coding: UTF-8 -*-
import re
from os.path import dirname, join
from random import choice, randint
from shutil import get_terminal_size
from textwrap import wrap


__all__ = ["choice", "get_terminal_size", "randint", "re", "strip_escape_codes", "wrap", "Object", "ObjectTooLarge", \
           "FONTS"]


with open(join(dirname(__file__), "fonts.txt")) as f:
    FONTS = list(set(f.read().splitlines()))


strip_escape_codes = lambda s: re.sub(r"(\x9B|\x1B\[)[0-?]*[ -\/]*[@-~]", "", s)


class Object(object):
    def __repr__(self):
        """ Represent the object with every ASCII escape code removed. """
        return strip_escape_codes(str(self))
    
    @staticmethod
    def check_width(text, width=None):
        """ Generic method for checking if the ASCII art object does not exceed the configured width. """
        width = width or get_terminal_size().columns
        if any(len(l) > width for l in text.splitlines()):
            raise ObjectTooLarge("Object does not fit the given width")
    
    @staticmethod
    def wrap(text, width=None):
        """ Simply return original wrap's result as a string. """
        return "\n".join(wrap(text, width or get_terminal_size().columns))


class ObjectTooLarge(ValueError):
    pass


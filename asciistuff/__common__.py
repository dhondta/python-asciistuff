# -*- coding: UTF-8 -*-
import re
from os.path import dirname, join
from random import choice
from terminaltables.terminal_io import terminal_size
from termcolor import ATTRIBUTES, colored
from textwrap import wrap


__all__ = ["choice", "colored", "re", "strip_escape_codes", "term_width",
           "wrap", "Object", "ObjectTooLarge", "FONTS"]

# little patch to available attributes ; may not work for some terminals
ATTRIBUTES['italic'] = 3
ATTRIBUTES['strikethrough'] = 9


with open(join(dirname(__file__), "fonts.txt")) as f:
    FONTS = list(set(f.read().splitlines()))


strip_escape_codes = lambda s: re.sub(r"(\x9B|\x1B\[)[0-?]*[ -\/]*[@-~]", "", s)
term_width = lambda: terminal_size()[0]


class Object(object):
    def __repr__(self):
        """ Represent the object with every ASCII escape code removed. """
        return strip_escape_codes(str(self))
    
    @staticmethod
    def check_width(text, width=term_width()):
        """ Generic method for checking if the ASCII art object does not exceed
             the configured width. """
        if any(len(l) > width for l in text.splitlines()):
            raise ObjectTooLarge("Object does not fit the given width")
    
    @staticmethod
    def wrap(text, width=term_width()):
        """ Simply return original wrap's result as a string. """
        return "\n".join(wrap(text, width))


class ObjectTooLarge(ValueError):
    pass

# -*- coding: UTF-8 -*-
"""AsciiStuff package information.

"""
import os

__author__    = "Alexandre D'Hondt"
__copyright__ = "© 2021 A. D'Hondt"
__license__   = "GPLv3 (https://www.gnu.org/licenses/gpl-3.0.html)"

with open(os.path.join(os.path.dirname(__file__), "VERSION.txt")) as f:
    __version__ = f.read().strip()

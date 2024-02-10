#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""Banner class tests.

"""
from asciistuff import *
from unittest import TestCase


TEXT     = "text"
BAD_FONT = "does_not_exist"


class TestBanner(TestCase):
    def test_banner_font_setting(self):
        # banner object with default options
        b = Banner(TEXT)
        self.assertRaises(ValueError, Banner, "")
        # text and font size
        for i in range(1, 2 * len(TEXT)):
            self.assertRaises(ValueError, Banner, TEXT, i)
        for i in range(1, 2 * len(TEXT), 24):
            self.assertRaises(ValueError, Banner, TEXT, i, "rounded")
        self.assertRaises(ValueError, Banner, TEXT, 20, "dotmatrix")
        self.assertIsNotNone(Banner(TEXT, 20, "dotmatrix", autofont=True))
        # setting a bad font
        try:
            b.font = BAD_FONT
            failed = True
        except ValueError:
            failed = False
        self.assertFalse(failed)
        # refactor the banner by choosing a new font
        b.refactor()
        # reset the text (also checks that the current font still suits)
        b.text = TEXT
    
    def test_banner_parameters(self):
        # automatic font selection when bad one is given
        self.assertRaises(ValueError, Banner, TEXT, 20, BAD_FONT)
        b = Banner(TEXT, 20, BAD_FONT, autofont=True, fontset=[BAD_FONT] + FONTS)
        # multiline banner support
        _ = TEXT + " " + TEXT
        self.assertRaises(ValueError, Banner, _, 25, "rounded")
        b = Banner(_, 25, "rounded", autofont=True)
        b = Banner(_, 25, "rounded", multiline=True)
        self.assertRaises(ValueError, Banner, _, 25, "dotmatrix")
        self.assertRaises(ValueError, Banner, _, 25, "dotmatrix")
        self.assertRaises(ValueError, Banner, _, 25, "dotmatrix")
        self.assertRaises(ValueError, Banner, _, 25, "dotmatrix")
    
    def test_banner_fontset(self):
        self.assertRaises(ValueError, Banner, TEXT, 50, "rounded", False, True, [BAD_FONT])
        self.assertRaises(ValueError, Banner, TEXT, 50, "rounded", False, True, [])


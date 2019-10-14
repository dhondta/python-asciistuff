#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""Functions (from __init__) class tests.

"""
import os
import sys
from asciistuff import *
from asciistuff import main
from PIL import Image as PILImage, ImageDraw
from unittest import TestCase


ASC = "test.asc"
BAD1 = "bad1.csv"
BAD2 = "bad2.csv"
BAD3 = "bad3.csv"
CSV = "quotes.csv"
IMG = "hello.png"


class TestInit(TestCase):
    @classmethod
    def setUpClass(cls):
        f = AsciiFile()
        f['main'] = Banner("TEST")
        f += {'quote': Quote("Test string", "John Doe")}
        f.save(ASC)
        i = PILImage.new('RGB', (100, 30), color=(73, 109, 137))
        d = ImageDraw.Draw(i)
        d.text((10,10), "Hello World", fill=(255, 255, 0))
        i.save(IMG)
        with open(BAD1, 'w') as f:
            f.write("\"quote\",\"author\"")
        with open(BAD2, 'w') as f:
            f.write("\"bad\",\"author\"\n")
            f.write("\"Test quote\",\"John Doe\"")
        with open(BAD3, 'w') as f:
            f.write("\"quote\",\"author\"\n")
            f.write("\"Test quote\xfe\",\"John Doe\"")
        with open(CSV, 'w') as f:
            f.write("\"quote\",\"author\"\n")
            f.write("\"Test quote\",\"John Doe\"")
    
    @classmethod
    def tearDownClass(cls):
        os.remove(ASC)
        os.remove(BAD1)
        os.remove(BAD2)
        os.remove(BAD3)
        os.remove(CSV)
        os.remove(IMG)
    
    def test_from_file(self):
        self.assertIsInstance(from_file(ASC), str)
    
    def test_get_banner(self):
        self.assertIsNone(get_banner())
        self.assertIsInstance(get_banner("TITLE"), str)
        self.assertIsInstance(get_banner("TITLE", path=ASC), str)
        self.assertIsInstance(get_banner(path="."), str)
        self.assertIsInstance(get_banner("TITLE", path=IMG), str)
        self.assertIsInstance(get_banner("TITLE", path=CSV), str)
    
    def test_get_quote(self):
        self.assertIsInstance(get_quote(), str)
        self.assertRaises(ValueError, get_quote, ASC)
        self.assertRaises(ValueError, get_quote, BAD1)
        self.assertRaises(ValueError, get_quote, BAD2)
        self.assertRaises(ValueError, get_quote, BAD3)
    
    def test_main(self):
        sys.argv = ["asciistuff", "does_not_exist"]
        self.assertRaises(IOError, main)
        sys.argv = ["asciistuff", ASC]
        self.assertIsNone(main())
        sys.argv = ["asciistuff", os.path.splitext(ASC)[0]]
        self.assertIsNone(main())

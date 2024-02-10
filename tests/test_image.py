#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""Image class tests.

"""
from asciistuff import *
from asciistuff.image import FONT_TYPES
from os import remove
from PIL import Image as PILImage, ImageDraw, ImageFont
from shutil import get_terminal_size
from unittest import TestCase


IMG = "hello.png"


class TestImage(TestCase):
    @classmethod
    def setUpClass(cls):
        i = PILImage.new('RGB', (100, 30), color=(73, 109, 137))
        ImageDraw.Draw(i).text((10,10), "Hello World", fill=(255, 255, 0))
        i.save(IMG)
    
    @classmethod
    def tearDownClass(cls):
        remove(IMG)
    
    def setUp(self):
        self.i = Image(IMG)
    
    def test_image(self):
        self.assertIsInstance(self.i.image, PILImage.Image)
        self.assertEqual(self.i.width, get_terminal_size().columns)
        w, h = self.i.charsize
        ar = (100.0 / w) / (30.0 / h)
        self.assertEqual(self.i.height, round(get_terminal_size().columns / ar))
        self.i.height = 10
        self.assertEqual(self.i.width, round(self.i.height * ar))
        self.i.size = (100, 30)
        self.assertEqual(self.i.size, [100, 30])
        self.i.charset += "X"
        self.assertIsNotNone(str(self.i))
        self.assertIsInstance(self.i.font, FONT_TYPES)
        self.assertIsNotNone(repr(self.i))
    
    def test_image_parameters(self):
        self.i.font = None
        try:
            self.i.font = "/does/not/exist"
            failed = True
        except IOError:
            failed = False
        self.assertFalse(failed)
        try:
            self.i.font = 0
            failed = True
        except ValueError:
            failed = False
        self.assertFalse(failed)
        self.i.strip = True
        for i in range(5):
            self.i.brightness += .5
            self.i.contrast -= .1
            str(self.i)


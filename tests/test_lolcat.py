#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""Lolcat class tests.

"""
from asciistuff import *
from unittest import TestCase


TEXT = "Text"


class TestLolcat(TestCase):
    def test_lolcat_parameters(self):
        # lolcat object with default options
        l = Lolcat(TEXT)
        self.assertIsNotNone(str(l))
        self.assertRaises(ValueError, Lolcat, "")
        # change parameters to invalid values
        self.assertRaises(ValueError, setattr, l, "freq", -1)
        self.assertRaises(ValueError, setattr, l, "mode", 1337)
        self.assertRaises(ValueError, setattr, l, "spread", -1)
        # change mode
        for m in [8, 16]:
            l.mode = m
            self.assertIsNotNone(str(l))
    
    def test_lolcat_on_other_objects(self):
        self.assertIsNotNone(str(Lolcat(Banner(TEXT), mode=16)))
        self.assertIsNotNone(str(Lolcat(Cowsay(TEXT))))


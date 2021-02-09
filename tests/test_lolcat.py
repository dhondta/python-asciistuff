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
        self.assertRaises(ValueError, setattr, l, "seed", "BAD")
        self.assertRaises(ValueError, setattr, l, "spread", -1)
        # change mode
        for m in [8, 16]:
            l.mode = m
            self.assertIsNotNone(str(l))
    
    def test_lolcat_on_other_objects(self):
        # set seed
        l = Lolcat(Banner(TEXT), mode=16, seed=123)
        # print objects, checking the counter
        self.assertEqual(Lolcat.ctr, 123)
        ctr = Lolcat.ctr + len(str(l).split("\n"))
        self.assertEqual(Lolcat.ctr, ctr)
        l = Lolcat(Cowsay(TEXT))
        ctr = Lolcat.ctr + len(str(l).split("\n"))
        self.assertEqual(Lolcat.ctr, ctr)
        l = Lolcat(Banner(TEXT), mode=16, seed=1)
        self.assertEqual(Lolcat.ctr, 1)


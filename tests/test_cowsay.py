#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""Cowsay class tests.

"""
from asciistuff import *
from unittest import TestCase


TEXT         = "Text"
BAD_COWACTER = "does_not_exist"


class TestCowsay(TestCase):
    def test_cowsay_cowacter_setting(self):
        # cowsay object with default options
        c = Cowsay(TEXT)
        self.assertRaises(ValueError, Cowsay, "")
        # text and width
        for i in range(1, 80):
            if i < 25:
                self.assertRaises(ValueError, Cowsay, TEXT, i, "default")
            else:
                Cowsay(TEXT, i, "default")
        # setting a bad font
        try:
            c.cowacter = BAD_COWACTER
            failed = True
        except ValueError:
            failed = False
        self.assertFalse(failed)
        # refactor the cowsay by choosing a new cowacter
        c.refactor()
        # reset the text (also checks that the current cowacter still suits)
        c.text = TEXT
    
    def test_cowsay_parameters(self):
        # automatic cowacter selection when bad one is given
        self.assertRaises(ValueError, Cowsay, TEXT, 20, BAD_COWACTER)
        c = Cowsay(TEXT, 20, "default", True)
        c = Cowsay(TEXT, 20, BAD_COWACTER, True)
        c = Cowsay(TEXT, 20, BAD_COWACTER, True, cowacterset=[BAD_COWACTER] + COWACTERS)
    
    def test_cowsay_cowacterset(self):
        self.assertRaises(ValueError, Cowsay, TEXT, 50, "default", True, [BAD_COWACTER])
        self.assertRaises(ValueError, Cowsay, TEXT, 50, "default", True, [])


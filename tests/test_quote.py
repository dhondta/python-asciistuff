#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""Quote class tests.

"""
from asciistuff import *
from unittest import TestCase


TEXT = "Text"


class TestQuote(TestCase):
    def test_quote_setting(self):
        Quote(TEXT).text
        Quote(TEXT, None)
        self.assertRaises(ValueError, Quote, TEXT, "john", 1)
        self.assertRaises(ValueError, Quote, TEXT, "john", 80, .8)
        self.assertRaises(ValueError, Quote, TEXT, "john", 80, -.1)
    
    def test_quote_with_cowsay(self):
        Quote(TEXT, cowsay="random")
        Quote(TEXT, cowsay="default")
        self.assertRaises(ValueError, Quote, TEXT, None, 80, .1, "BAD")
        Quote(TEXT, cowsay=["default", {'thoughts': True}])
        self.assertRaises(ValueError, Quote, TEXT, None, 80, .1, {"test": []})


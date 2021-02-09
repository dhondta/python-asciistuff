#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""AsciiFile class tests.

"""
import os
from asciistuff import *
from unittest import TestCase


ASC = "test.asc"
BAD_SEC = "does-not-exist"


class TestAsciiFile(TestCase):
    @classmethod
    def setUpClass(cls):
        f = AsciiFile()
        f['title'] = Banner("TEST")
        f += {'quote': Quote("Test string", "John Doe")}
        f += "this shall go to 'main' section"
        f += ["this shall also go to 'main' section"]
        f.save(ASC)
    
    @classmethod
    def tearDownClass(cls):
        os.remove(ASC)
    
    def setUp(self):
        self.f = AsciiFile(ASC)
    
    def tearDown(self):
        delattr(self, "f")
    
    def test_ascii_file_format(self):
        self.assertIn('main', self.f.sections)
        self.assertIn('title', self.f.sections)
        self.assertIn('quote', self.f.sections)
        self.assertIn(".section: main", repr(self.f))
        self.assertIn(".section: title", repr(self.f))
        self.assertIn(".section: quote", repr(self.f))
        self.assertNotIn(".section: main", str(self.f))
        self.assertNotIn(".section: title", str(self.f))
        self.assertNotIn(".section: quote", str(self.f))
        self.assertIsNotNone(self.f.text)
        
    def test_ascii_file_sections(self):
        self.assertEqual(self.f.__sub__('quote'), self.f)
        self.assertEqual(self.f.__sub__(BAD_SEC), self.f)
        self.assertNotIn(".section: quote", repr(self.f))
        self.assertEqual(self.f.__add__({'quote[adjust=right]':
                                         Quote("Test string", "Joe")}), self.f)
        self.assertRaises(ValueError, self.f.__add__,
                          {'quote{adjust:right}': "test"})
        self.assertIsNone(self.f.__delitem__('quote'))
        self.assertRaises(KeyError, self.f.__delitem__, BAD_SEC)
        self.assertIsNone(self.f.get(BAD_SEC))
        self.assertRaises(KeyError, self.f.__getitem__, BAD_SEC)
        _ = self.f['main']
        self.assertEqual(len(_), 2)
        self.assertIsInstance(_[0], str)
        self.assertIsInstance(_[1], dict)
        self.assertIsInstance(self.f['title'][0], str)
        self.assertIsNone(self.f.__setitem__('title', Banner("TEST")))
        self.assertIsInstance(self.f['title'][0], Banner)
    
    def test_ascii_file_section_parameters(self):
        self.assertRaises(ValueError, self.f.__setitem__,
                          ['test', "BAD_PARAMS"], "TEST")
        p = {'adjust': "left"}
        self.assertIsNone(self.f.__setitem__(['test', p], "TEST"))
        self.assertIsNotNone(self.f.text)
        p['adjust'] = "BAD"
        self.assertRaises(ValueError, self.f.__setitem__, ['test', p], "TEST")
        p['adjust'] = "center"
        self.assertIsNone(self.f.__setitem__(['test', p], "TEST"))
        self.assertIsNotNone(self.f.text)
        p['bgcolor'] = "random"
        self.assertIsNone(self.f.__setitem__(['test', p], Quote("TEST")))
        self.assertIsNotNone(self.f.text)
        self.assertRaises(KeyError, self.f.param, BAD_SEC, 'test', "test")
        self.assertRaises(ValueError, self.f.param, 'test', 'test', "test")
        self.assertRaises(ValueError, self.f.param, 'test', 'fgcolor', "test")
        self.assertIsNone(self.f.param('test', 'fgcolor', "blue"))
        self.assertIsNone(self.f.param('test', 'bgcolor', "green"))
        self.assertIsNotNone(self.f.text)
        p['fgcolor'] = "lolcat"
        self.assertIsNone(self.f.__setitem__(['test', p], "TEST"))
        self.assertIsNotNone(self.f.text)


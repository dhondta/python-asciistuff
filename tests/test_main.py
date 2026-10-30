#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""Main function tests.

"""
import os
import sys
from asciistuff import *
from asciistuff.__main__ import main
from unittest import TestCase


ASC = "test-main.asc"


class TestMain(TestCase):
    @classmethod
    def setUpClass(cls):
        f = AsciiFile()
        f['main'] = Banner("TEST")
        f.save(ASC)
    
    @classmethod
    def tearDownClass(cls):
        os.remove(ASC)
    
    def test_main(self):
        sys.argv = ["asciistuff", "does_not_exist"]
        self.assertRaises(IOError, main)
        sys.argv = ["asciistuff", ASC]
        self.assertIsNone(main())
        sys.argv = ["asciistuff", os.path.splitext(ASC)[0]]
        self.assertIsNone(main())

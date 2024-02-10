# -*- coding: UTF-8 -*-
from cowpy.cow import COWACTERS as COWACTERS_OBJ

from .__common__ import *

__all__ = ["Cowsay", "COWACTERS"]


COWACTERS = list(COWACTERS_OBJ.keys())


class Cowsay(Object):
    """ Cowsay ASCII art.
    
    This converts a text to an ASCII art using CowPy.
     
    :param text:         text to be displayed
    :param width:        desired text width in characters
    :param cowacter:     cowsay character
    :param autocowacter: automatically choose a replacement when the cowacter does not suit for rendering
    :param cowacterset:  set of cowacters to be considered
    :param options:      cowpy parameters
    """
    def __init__(self, text, width=None, cowacter=None, autocowacter=False, cowacterset=COWACTERS, **options):
        self.__cowacter = None
        self.__cowacterset = [c for c in cowacterset if Cowsay.cowacter_exists(c)]
        self._autocowacter = cowacter is None or cowacter == "random" or autocowacter
        self.width = width or get_terminal_size().columns
        self.options = options
        self.text = text
        self.cowacter = cowacter
        str(self)
        self._autocowacter = autocowacter
    
    def __str__(self):
        return self.__render()

    def __get_new_cowacter(self, old=None):
        if old in self.__cowacters:
            self.__cowacters.remove(old)
        if len(self.__cowacters) == 0:
            raise ValueError("No suitable cowacter found")
        return choice(self.__cowacters)
    
    def __render(self, cowacter=None, check=True, **options):
        t = "\n".join(wrap(self.text, width=self.width-6))
        t = COWACTERS_OBJ[cowacter or self.cowacter](**(options or self.options)).milk(t)
        if check:
            Object.check_width(t, self.width)
        return t
    
    @property
    def cowacter(self):
        return self.__cowacter
    
    @cowacter.setter
    def cowacter(self, name):
        def _raise_or_get(e):
            c = self.__get_new_cowacter(name)
            if self._autocowacter:
                return c
            else:
                raise ValueError(e)
        # first, get a random font name if None
        if name is None or name == "random":
            name = self.__get_new_cowacter()
        # 1. check if the font is in the given fontset
        if name not in self.__cowacters:
            name = _raise_or_get("Cowacter not handled")
        # then, remove every non-suitable cowacter encountered given the text
        while True:
            # 2. test for rendering the cowsay
            try:
                self.__render(name)
                break
            except ValueError as e:
                name = _raise_or_get(str(e))
        self.__cowacter = name
    
    @property
    def text(self):
        return self.__text
    
    @text.setter
    def text(self, text):
        if len(text) == 0:
            raise ValueError("Empty text")
        self.__text = text
        self.__cowacters = [_ for _ in self.__cowacterset]
        if self.cowacter:
            self.cowacter = self.cowacter  # check if the current cowacter still applies given the new text
    
    def refactor(self):
        _ = self._autocowacter
        self._autocowacter = True
        self.cowacter = None
        self._autocowacter = _
    
    @staticmethod
    def cowacter_exists(cowacter):
        try:
            COWACTERS_OBJ[cowacter]
            return True
        except KeyError:
            return False


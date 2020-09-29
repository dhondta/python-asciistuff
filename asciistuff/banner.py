# -*- coding: UTF-8 -*-
from pyfiglet import CharNotPrinted, Figlet, FontNotFound

from .__common__ import *


__all__ = ["Banner", "FONTS"]


class Banner(Object):
    """ Banner as an ASCII art.
    
    This converts a text to an ASCII banner using PyFiglet.
     
    This class is inspired from: https://github.com/ajalt/pyasciigen/blob/master/asciigen.py
    
    :param text:       text to be displayed
    :param width:      desired width in characters
    :param font:       name of a custom font
    :param multiline:  whether the output should be accepted even if the text is generated on multiple lines
    :param autofont:   automatically choose a replacement when the font does not suit for rendering
    :param fontset:    set of fonts to be considered
    """
    def __init__(self, text, width=term_width(), font=None, multiline=False, autofont=False, fontset=FONTS):
        self.__font = None
        # this line does not immediately filter fonts with Banner.font_exists() as, e.g. when fontset=FONTS, it takes a
        #  large amounts of time to test all available fonts with PyFiglet ; therefore check 2 is needed in font's
        #  property setter
        self.__fontset = fontset
        self._autofont = font is None or autofont
        self.width = width
        self.text = text
        self.multiline = multiline
        self.font = font
        str(self)
        self._autofont = autofont
    
    def __str__(self):
        return self.__render()
    
    def __get_new_font(self, old=None):
        if old in self.__fonts:
            self.__fonts.remove(old)
        if len(self.__fonts) == 0:
            raise ValueError("No suitable font found")
        return choice(self.__fonts)
    
    def __render(self, font=None, check=True):
        t = str(Figlet(font=font or self.font, width=self.width).renderText(self.text))
        if check:
            Object.check_width(t, self.width)
        return t
    
    @property
    def font(self):
        return self.__font
    
    @font.setter
    def font(self, name):
        def _raise_or_get(e):
            f = self.__get_new_font(name)
            if self._autofont:
                return f
            else:
                raise ValueError(e)
        # first, get a random font name if None
        if name is None:
            name = self.__get_new_font()
        # 1. check if the font is in the given fontset
        if name not in self.__fonts:
            name = _raise_or_get("Font not handled")
        # then, remove every non-suitable font encountered given the input text
        while True:
            # 2. check if the font exists
            if not Banner.font_exists(name):
                name = _raise_or_get("Font does not exist")
                continue
            # 3. test for rendering the banner
            try:
                s = self.__render(name)
            except CharNotPrinted as e:
                name = _raise_or_get(str(e))
                continue
            # 4. test for the height of the rendered banner (if not multiline)
            if not self.multiline:
                # get the height of a single character
                _ = Figlet(font=name).renderText("X")
                h = len(str(_).splitlines())
                try:
                    # then compare it with the height of the rendered text
                    if len(s.splitlines()) > int(h * 1.5):
                        raise CharNotPrinted("")
                except CharNotPrinted:
                    name = _raise_or_get("Font too big or text too large for a single line")
                    continue
            break
        self.__font = name
    
    @property
    def text(self):
        return self.__text
    
    @text.setter
    def text(self, text):
        if len(text) == 0:
            raise ValueError("Empty text")
        # consider that, whatever the font, the text will always have a width of at least 2 characters per letter ;
        #  therefore, in order to save time, figlets computation can be spared by checking first the length with regard
        #  to the width before setting any font with PyFiglet
        if max(map(len, wrap(text))) > .5 * self.width:
            raise ValueError("Text is too big or width is too small")
        self.__text = text
        if len(self.__fontset) == 0:
            raise ValueError("Empty font set")
        self.__fonts = [_ for _ in self.__fontset]
        if self.font:
            self.font = self.font  # check if the current font still applies given the new text
    
    def refactor(self):
        _ = self._autofont
        self._autofont = True
        self.font = None
        self._autofont = _
    
    @staticmethod
    def font_exists(font):
        try:
            Figlet(font=font)
            return True
        except FontNotFound:
            try:
                FONTS.remove(font)
            except ValueError:
                pass
            return False


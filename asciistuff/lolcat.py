# -*- coding: UTF-8 -*-
from math import pi, sin
from os import environ
from random import randint

from .__common__ import *


__all__ = ["Lolcat"]


ANSI_REGEX  = re.compile(r'\x1b\[(\d+)(;\d+)?(;\d+)?[m|K]')
ANSI_COLORS = [(0, 0, 0), (205, 0, 0), (0, 205, 0), (205, 205, 0), (0, 0, 238), (205, 0, 205), (0, 205, 205),
               (229, 229, 229), (127, 127, 127), (255, 0, 0), (0, 255, 0), (255, 255, 0), (92, 92, 255),
               (255, 0, 255), (0, 255, 255), (255, 255, 255)]

distance = lambda c1, c2:  sum(map(lambda c: (c[0] - c[1]) ** 2, zip(c1, c2)))
rainbow  = lambda freq, i: [sin(freq * i) * 127 + 128, sin(freq * i + 2 * pi / 3) * 127 + 128,
                            sin(freq * i + 4 * pi / 3) * 127 + 128]


class Lolcat(Object):
    """ Lolcat colored ASCII art (as of the Ruby implementation at https://github.com/busyloop/lolcat/).
    
    This converts a text to rainbow colored ASCII.
     
    This class is inspired from: https://github.com/tehmaze/lolcat/blob/master/lolcat
    Thanks to:                   <maze@pyth0n.org>
    
    :param text:   text to be displayed
    :param mode:   set of fonts to be considered
    :param spread: rainbow spread factor
    :param freq:   rainbow colors frequency
    :param seed:   seed for color randomization
    """
    mode = 16 if "ANSICON" in environ or environ.get('TERM', "xterm").endswith("-color") else 256
    
    def __init__(self, text, mode=None, spread=3., freq=.1, seed=0):
        self.text = str(text)
        if mode is not None:
            self.mode = mode
        self.spread = spread
        self.freq = freq
        self.seed = seed
    
    def __setattr__(self, name, value):
        if name in ["freq", "spread"] and (not isinstance(value, (float, int)) or value <= 0):
            raise ValueError("Bad %s ; should be strictly greater than zero" % name)
        elif name == "mode" and value not in [8, 16, 256]:
            raise ValueError("Bad mode ; should 8, 16 or 256")
        elif name == "seed":
            self.__n = randint(0, 256) if value == 0 else value % 256
        elif name == "text" and len(value) == 0:
            raise ValueError("Empty text")
        super(Lolcat, self).__setattr__(name, value)
    
    def __str__(self):
        s = ""
        for line in self.text.split("\n"):
            self.__n += 1
            l = ""
            for i, char in enumerate(ANSI_REGEX.sub("", line.rstrip())):
                r, g, b = rgb = rainbow(self.freq, self.__n + i / self.spread)
                if self.mode in [8, 16]:
                    matches = [(distance(c, map(int, rgb)), i) for i, c in enumerate(ANSI_COLORS[:self.mode])]
                    matches.sort()
                    color = matches[0][1]
                    seq = "3%d" % color
                else:
                    gray_possible = True
                    sep = 2.5
                    while gray_possible:
                        if r < sep or g < sep or b < sep:
                            gray = r < sep and g < sep and b < sep
                            gray_possible = False
                        sep += 42.5
                    color = 232 + int(float(sum(rgb) / 33.0)) if gray else \
                            sum([16] + [int(6 * float(v)/256) * m for v, m in zip(rgb, [36, 6, 1])])
                    seq = "38;5;%d" % color
                l += "\x1b[%sm" % seq + char
            s += l + "\n"
        return s + "\x1b[0m"


# -*- coding: UTF-8 -*-
from .__common__ import *
from .cowsay import Cowsay

__all__ = ["Quote"]


class Quote(Object):
    """ Quote formatted in a nice-looking fashion.
    
    This can convert the quote to a Cowsay if specified.
     
    :param quote:  quote to be displayed
    :param source: quote's source
    :param width:  desired text width in characters
    :param margin: margin [0, .5[
    :param cowsay: cowsay settings ; character (cowacter) or 
                                     (cowacter, dict of parameters)
    """
    def __init__(self, quote, source=None, width=term_width(), margin=.1,
                 cowsay=None):
        if not 0 <= margin < .5:
            raise ValueError("Bad margin value (should belong to [0,.5[)")
        self.quote = quote
        self.source = source or "unknown"
        self.width = int(width * (1 - 2 * margin))
        self.cowsay = cowsay
        str(self)
    
    def __str__(self):
        c = self.cowsay
        if c:
            t = strip_escape_codes(self.text)
            if isinstance(c, str):
                t = str(Cowsay(t, self.width, c))
            elif isinstance(c, (list, tuple)) and len(c) == 2 and \
                 isinstance(c[1], dict):
                t = str(Cowsay(t, self.width - 2, c[0], **c[1]))
            else:
                raise ValueError("Bad cowsay parameters")
        else:
            t = self.text
        Object.check_width(t, self.width)
        return t
    
    @property
    def text(self):
        w = self.width-5
        q = colored(self.quote, attrs=['italic'])
        t = "\"{}\",".format(q)
        l = wrap(t, w)
        t, s = Object.wrap(t, w), Object.wrap(self.source, w)
        w = max(map(len, l))
        t += "\n" + colored(s, attrs=['dark']).rjust(w)
        return t

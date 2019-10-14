import argparse
import csv
import os
import random
import string
import warnings

from .__common__ import FONTS
from .banner import *
from .banner import __all__ as _banner
from .cowsay import *
from .cowsay import __all__ as _cowsay
from .file import *
from .file import __all__ as _file
from .image import *
from .image import __all__ as _image
from .quote import *
from .quote import __all__ as _quote


__all__ = _banner + _cowsay + _file + _image + _quote + \
          ["from_file", "get_banner", "get_quote", "FONTS"]

warnings.filterwarnings("ignore")


def from_file(path=None):
    """
    Get an ASCII art from an ASCII file.
    """
    return get_banner(path=path, img_ext=())


def get_banner(text=None, path=None, img_ext=(".jpg", ".jpeg", ".png"),
               styles={}):
    """
    Display an ASCII art from a given text and/or a path.
    
    :param text:    text to be displayed
    :param path:    where a ASCII art could be found (folder or file)
    :param img_ext: image extensions to be considered (must be readable by PIL)
    :param styles:  section styles, taking default sections "title" and "logo"
                     into consideration
    """
    if path is None:
        if text is None:
            return
        asc = AsciiFile()
        asc["title", styles.get("title", {})] = Banner(text)
    else:
        # if path is a folder, randomly choose a valid file
        if os.path.isdir(path):
            _ = [f for f in os.listdir(path) \
                 if os.path.isfile(os.path.join(path, f)) and \
                 any(f.endswith(e) for e in (".asc", ) + img_ext)]
            if len(_) > 0:
                path = os.path.join(path, random.choice(_))
        # now handle valid file extensions
        if path.endswith(".asc"):
            asc = AsciiFile(path)
            if asc.get("title") is None and text is not None:
                _ = AsciiFile()
                _["title", styles.get("title", {})] = Banner(text)
                for k, v, p in asc.items():
                    _[k, p] = v
                asc = _
        elif any(path.endswith(e) for e in img_ext):
            asc = AsciiFile()
            if text is not None:
                asc["title", styles.get("title", {})] = Banner(text)
            s = styles.get("logo", {})
            asc["logo", s] = Image(path)
            i = asc["logo"][0]
            i.height = min(i.height, s.get('max_height', 20))
        # or retry only using the provided text
        else:
            return get_banner(text, None, styles)
    return str(asc)


def get_quote(path="quotes.csv", style={}):
    """
    Get a random file from the given folder and, if it only consists of
     printable characters, consider it as a banner to be returned.
    
    :param folder: where the quotes.csv file shall be searched for
    :param style:  main section style
    """
    if not os.path.isfile(path) or not path.endswith(".csv"):
        raise ValueError("Not a valid file")
    # first, count number of rows
    with open(path) as f:
        l = sum(1 for row in csv.reader(f))
    if l <= 1:
        raise ValueError("Empty quotes file")
    # then choose a random row index and get it
    i = random.randrange(0, l - 1)
    with open(path) as f:
        reader = csv.reader(f)
        headers = next(reader)
        try:
            i_a, i_q = headers.index('author'), headers.index('quote')
        except ValueError:
            raise ValueError("Bad quotes file format")
        for j, row in enumerate(reader):
            if i == j:
                quote = row[i_q], row[i_a]
                break
    if not all(c in string.printable for x in quote for c in x):
        raise ValueError("Invalid quote (bad characters)")
    asc = AsciiFile()
    cowsay = style.get('cowsay')
    asc['main', style] = Quote(*quote, cowsay=cowsay)
    return str(asc)


def main():
    import argparse, os
    parser = argparse.ArgumentParser()
    parser.add_argument("ascii_file")
    args = parser.parse_args()
    f = args.ascii_file
    if os.path.isfile(f):
        print(from_file(f))
    elif os.path.isfile(f + ".asc"):
        f += ".asc"
        print(from_file(f))
    else:
        raise OSError("'{}' does not exist".format(f))

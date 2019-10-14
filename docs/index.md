## Introduction

AsciiStuff is a tiny library that gathers some funny ASCII-art-related features from various sources. It leverages:

- [`PyFiglet`](https://github.com/pwaller/pyfiglet) for converting text to a nice banner.
- [`Pillow`](https://github.com/python-pillow/Pillow) and [`pyasciigen`](https://raw.githubusercontent.com/ajalt/pyasciigen/master/asciigen.py) for converting JPG or PNG images to ASCII arts.
- [`termcolor`](https://pypi.org/project/termcolor/) for formatting quotes.
- [`cowpy`](https://github.com/jeffbuttars/cowpy) for drawing Cowsay characters.

It also features an ASCII file format (`.asc`) with a small set of useful options for styling combinations of these ASCCI art objects.


## Setup

This library is available on [PyPi](https://pypi.python.org/pypi/asciistuff/) and can be simply installed using Pip:

```sh
sudo pip install asciistuff
```

or

```sh
sudo pip3 install asciistuff
```

# -*- coding: UTF-8 -*-
import os
from argparse import ArgumentParser

from . import from_file


def main():
    parser = ArgumentParser()
    parser.add_argument("ascii_file")
    args = parser.parse_args()
    f = args.ascii_file
    if os.path.isfile(f):
        print(from_file(f))
    elif os.path.isfile(f + ".asc"):
        f += ".asc"
        print(from_file(f))
    else:
        raise IOError("'{}' does not exist".format(f))


if __name__ == "__main__":
    main()

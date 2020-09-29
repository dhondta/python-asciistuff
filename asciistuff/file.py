# -*- coding: UTF-8 -*-
import colorama
from collections import OrderedDict

from .__common__ import *


__all__ = ["AsciiFile"]


BGCOLORS = list(vars(colorama.Back).values())
BGCOLOR_NAMES = list(_.lower() for _ in vars(colorama.Back).keys())
FGCOLORS = list(vars(colorama.Fore).values())
FGCOLOR_NAMES = list(_.lower() for _ in vars(colorama.Fore).keys())

DEFAULT_PARAMS = {'adjust': "center"}
PARAM_VALUES = {
    'adjust':  ["left", "center", "right"],
    'bgcolor': ["random"] + BGCOLOR_NAMES,
    'fgcolor': ["random"] + FGCOLOR_NAMES,
}
SECTION_LINE = re.compile(r"^\.section\:\s(?P<section>[a-z0-9]+)(?:\[(?P<params>([a-z]+\=[a-z]+)"
                          r"(\,[a-z]+\=[a-z]+)*)\])?\s*$")

center = lambda t, w: "\n".join(l.center(w) for l in t.split("\n"))


class AsciiFile(object):
    """ ASCII art custom file format (with sections).
    
    This organizes ASCII art contents as sections in a custom file format for applying different style parameters.
    
    :param path: path to the ASCII art file
    """
    def __init__(self, path=None):
        self.__sections = OrderedDict()
        self.__params = {}
        self.load(path)
    
    def __add__(self, section):
        if isinstance(section, (list, tuple)):
            section = "\n".join(map(str, section))
        elif isinstance(section, dict):
            section = "\n".join(".section: {}\n{}".format(k, v) for k, v in section.items())       
        else:
            section = str(section)
        self._parse(section)
        return self

    def __delitem__(self, section):
        del self.__sections[section]
        del self.__params[section]
    
    def __getitem__(self, section):
        return self.__sections[section], self.__params[section]
    
    def __repr__(self):
        s = ""
        for section, text in self.__sections.items():
            p = ",".join("{}={}" % kv for kv in self.__params[section].items() if kv not in DEFAULT_PARAMS.items())
            p = ["", "[{}]".format(p)][len(p) > 0]
            s += ".section: {}{}\n".format(section, p)
            s += str(text) + "\n"
        return s
    
    def __setitem__(self, section, content):
        params = {k: v for k, v in DEFAULT_PARAMS.items()}
        if isinstance(section, (list, tuple)):
            section, _ = section
            AsciiFile.check_params(_)
            params.update(_)
        self.__sections[section] = content
        self.__params[section] = params
    
    def __str__(self):
        t, color_changed = "", False
        for section, content, params in self.items():
            text = str(content)
            # apply parameters in the following order
            for param in ["adjust", "bgcolor", "fgcolor"]:
                value = params.get(param)
                if value is None:
                    continue
                if param == "adjust":
                    s = ""
                    if value in ["left", "right"]:
                        m = ["rjust", "ljust"][value == "left"]
                        for l in text.split("\n"):
                            s += getattr(l, m)(term_width()) + "\n"
                    elif value == "center":
                        for l in text.split("\n"):
                            s += center(l, term_width()) + "\n"
                    text = s
                elif param in ["bgcolor", "fgcolor"]:
                    if value == "random":
                        COLORS = [FGCOLORS, BGCOLORS][param == "bgcolor"]
                        _, it = "", iter(text)
                        for c in it:
                            if c in "\x9b\x1b":
                                c = next(it)
                                while c != "m":
                                    c = next(it)
                                continue
                            elif c in " '\"":
                                _ += COLORS[-3] + c
                            elif c == "\n":
                                _ += c + COLORS[-3]
                            else:
                                _ += choice(COLORS) + c
                        text = _
                    else:
                        _ = getattr(colorama, ["Fore", "Back"][param == "bgcolor"])
                        text = getattr(_, value.upper(), None) or "" + text
                    color_changed = True
            # then add the text to the final string
            t += text
            if color_changed:
                t += BGCOLORS[-3] + FGCOLORS[-3]
        return t + " "
    
    def __sub__(self, section):
        if section in self.__sections:
            del self.__sections[section]
        if section in self.__params:
            del self.__params[section]
        return self
    
    def _parse(self, text):
        s, p = self.__sections, self.__params
        section = "main"
        s.setdefault(section, "")
        p.setdefault(section, {})
        for l in text.split("\n"):
            if l.startswith(".section: "):
                try:
                    _ = SECTION_LINE.search(l).groupdict()
                except AttributeError:
                    raise ValueError("Bad section line format")
                section = _["section"]
                s[section] = ""
                p[section] = {}
                params = {}
                for pair in (_["params"] or "").split(","):
                    pair = pair.strip()
                    if pair == "":
                        continue
                    name, value = pair.split("=")
                    params[name.strip()] = value.strip()
                AsciiFile.check_params(params)
                p[section] = params
            else:
                s[section] += l + "\n"
        s[section] = s[section][:-1]
        if s["main"] == "":
            del s["main"]    
    
    def get(self, section, default=None):
        try:
            return self[section]
        except KeyError:
            return default
    
    def items(self):
        for section, content in self.__sections.items():
            yield section, content, self.__params[section]
    
    def load(self, path=None):
        path = path or getattr(self, "path", None)
        self.path = str(path)
        if path is not None:
            with open(path) as f:
                _ = f.read()
            self.text = _
    
    def param(self, section, param, value):
        if section not in self.sections:
            raise KeyError("Section '{}' does not exist".format(section))
        AsciiFile.check_params({param: value})
        self.__params[section][param] = value
    
    def save(self, path=None):
        path = path or getattr(self, "path", None)
        self.path = str(path)
        if path is not None:
            path = path if path.endswith(".asc") else path + ".asc"
            with open(path, 'w') as f:
                f.write(repr(self))
    
    @property
    def sections(self):
        return self.__sections.keys()
    
    @property
    def text(self):
        return str(self)
    
    @text.setter
    def text(self, text):
        self.__sections = OrderedDict()
        self.__params = {}
        self._parse(text)
    
    @staticmethod
    def check_params(params):
        if not isinstance(params, dict):
            raise ValueError("'{}' shall be a dictionary".format(params))
        for k, v in params.items():
            try:
                choices = PARAM_VALUES[k]
            except KeyError:
                raise ValueError("Bad parameter name [{}]".format("|".join(PARAM_VALUES.keys())))
            if v not in choices:
                raise ValueError("Bad parameter value [{}]".format("|".join(choices)))


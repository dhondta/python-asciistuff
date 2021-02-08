[![PyPi](https://img.shields.io/pypi/v/asciistuff.svg)](https://pypi.python.org/pypi/asciistuff/)
[![Read The Docs](https://readthedocs.org/projects/python-asciistuff/badge/?version=latest)](https://python-asciistuff.readthedocs.io/en/latest/?badge=latest)
[![Build Status](https://travis-ci.org/dhondta/python-asciistuff.svg?branch=master)](https://travis-ci.org/dhondta/python-asciistuff)
[![Coverage Status](https://coveralls.io/repos/github/dhondta/python-asciistuff/badge.svg?branch=master)](https://coveralls.io/github/dhondta/python-asciistuff?branch=master)
[![Python Versions](https://img.shields.io/pypi/pyversions/asciistuff.svg)](https://pypi.python.org/pypi/asciistuff/)
[![Requirements Status](https://requires.io/github/dhondta/python-asciistuff/requirements.svg?branch=master)](https://requires.io/github/dhondta/python-asciistuff/requirements/?branch=master)
[![Known Vulnerabilities](https://snyk.io/test/github/dhondta/python-asciistuff/badge.svg?targetFile=requirements.txt)](https://snyk.io/test/github/dhondta/python-asciistuff?targetFile=requirements.txt)
[![License](https://img.shields.io/pypi/l/asciistuff.svg)](https://pypi.python.org/pypi/asciistuff/)

## Introduction

This library gathers some useful ASCII art features relying on [PyFiglet](https://github.com/pwaller/pyfiglet/), [Pillow](https://github.com/python-pillow/Pillow/) and [cowpy](https://github.com/jeffbuttars/cowpy/).

## Setup

```sh
pip install asciistuff
```

## Usage

### Banner

Creating a banner:

```
>>> from asciistuff import Banner
>>> print(Banner("Test"))
'########:'########::'######::'########:
... ##..:: ##.....::'##... ##:... ##..::
::: ##:::: ##::::::: ##:::..::::: ##::::
::: ##:::: ######:::. ######::::: ##::::
::: ##:::: ##...:::::..... ##:::: ##::::
::: ##:::: ##:::::::'##::: ##:::: ##::::
::: ##:::: ########:. ######::::: ##::::
:::..:::::........:::......::::::..:::::

```

## Image

```
>>> from asciistuff import Image
>>> print(Image("hello.png", 80))
@@@@@@@@@@@@@@@@@@@@@@@@    @@@@@@@@@@(/,,,,,,/(@@@@@@@@@@    @@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@   @@@@@@(,..                    .,*@@@@@@  @@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@* @@@@@/..      .,**((%%#####%((*/,.      .,*@@@ @@@@@@@@@@@@@@
@@@@@@@@@@@@@@@* @@@/.     ,/(%###%%(*//,,,,,//**%####%((/.   .,@@@ @@@@@@@@@@@@
@@@@@@@@@@@@@@ @@*.    ,(###%(/,.                   .,/*(%##%,   ,@@ @@@@@@@@@@@
@@@@@@@@@@@@ @@/.   *#@#(/.                                ,(@#/  ./@ @@@@@@@@@@
@@@@@@@@@@@ @@.  .(@#*.                                      .(@%.  ,@ @@@@@@@@@
@@@@@@@@@@ @/.  *@#/                                           .#@/  .@ @@@@@@@@
@@@@@@@@@ @,  .%@(                            /%.                (@*  ,@ @@@@@@@
@@@@@@@@ @,  /@#,                       *#.   (@,                 (@/  /@ @@@@@@
@@@@@@@ @,  /@#.  ..                    *@,   *@,                 .#@. .(@ @@@@@
@@@@@@ @/  /@#.   (@,                   ,@/   /@,     /((/.        .@%. ,@ @@@@@
@@@@@@ @. .#@,    ,@*                   .@(   ,@/   .%@(*#@/        %@. .@ @@@@@
@@@@@ @/  *@*      ##           ,%##*    #%   ,@*   %@.   %@,       %@. .@ @@@@@
@@@@@ @. .##.      (@(%##(,    /#(.,@(.  %#   .@(  .@(    ,@*       %@. ,@ @@@@@
@@@@@@@. /@(       /@#/.,%@/  ,@(,*(#@(  (@.   ##  .@(    %@.       ##  ,@ @@@@@
@@@@@@@. /@(       .@%    #@. #@#%(/,.   /@,   (@.  %@/./#@/       .@%  /@ @@@@@
@@@@@@@. ,@(        ##    /@* @%         /@/   *@/  .(###(.        *@/ .%@ @@@@@
@@@@@ @. .@#        %@.    ##.@%         ,@(   ,@(                ,@%  .@ @@@@@@
@@@@@ @,  %@.       (@.    (@./@#*(##(    ##    */               ,##. .(  @@@@@@
@@@@@ @(. ,@%       (@/    *@, .*((/..    (@/                   *@%.  /@ @@@@@@@
@@@@@@ @,  (@/      ./.    ,@*            .*,                 /#@*  ./@ @@@@@@@@
@@@@@@@ @. .%@,            .#(                             .*#@(.  .@@ @@@@@@@@@
@@@@@@@ @*. .(@(.                                       ./%@#*   ./@@ @@@@@@@@@@
@@@@@@@@ @*.  ,#@(.                                  .*%##(,   .*@@ @@@@@@@@@@@@
@@@@@@@@@*@@,.  /#@%,                           .,/(###*.   .,@@@ *@@@@@@@@@@@@@
@@@@@@@@@@  @@,   ,%@@%*,                     ,###%(/    ./@@@@  @@@@@@@@@@@@@@@
@@@@@@@@@@@@/@@@,.   ,*%##%%(**//***(*        /@(     ./@@@@ /@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@ @@@*,.    ./*((%%%%%%%@(       *@/ .(@@@@@  @@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@  @@@@(,.            (@,     .#@. .@    @@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@*  @@@@@@@@((///%. ,@*     %@/  /  @@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@     @@@@@@@@. .@(    (@*  ,@ @@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@   *   . .@%   (@*  .@ @@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@. ,@(  (@*  .@ @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  *  *@,.#@/  .@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ @.  ##/@#,  .@  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ @*  /@@@%. .,@ @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ @. .@@#/  .*@ @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@. ,%*  .,@@ @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ @,     .%@ *@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*,*%@@ @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
```

## Lolcat

![](https://raw.githubusercontent.com/dhondta/python-asciistuff/master/docs/img/lolcat-example.png)

## Quote

```
>>> from asciistuff import AsciiQuote
>>> print(AsciiQuote("This is a nice quote", "me"))
"This is a nice quote",
                     me
```

```
>>> from asciistuff import Quote
>>> print(Quote("This is another nice quote", "John Doe", cowsay="random"))
 _______________________________ 
/ "This is another nice quote", \
\                      John Doe /
 ------------------------------- 
    \
     \
    ^__^         /
    (oo)\_______/  _________
    (__)\       )=(  ____|_ \_____
      ||----w |  \ \     \_____ |
        ||     ||   ||           ||
```

## File

```
from asciistuff import *

file = AsciiFile("test.asc")

```


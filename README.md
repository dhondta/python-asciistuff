[![PyPi](https://img.shields.io/pypi/v/asciistuff.svg)](https://pypi.python.org/pypi/asciistuff/)
[![Read The Docs](https://readthedocs.org/projects/asciistuff/badge/?version=latest)](https://asciistuff.readthedocs.io/en/latest/?badge=latest)
[![Build Status](https://travis-ci.org/dhondta/asciistuff.svg?branch=master)](https://travis-ci.org/dhondta/asciistuff)
[![Coverage Status](https://coveralls.io/repos/github/dhondta/asciistuff/badge.svg?branch=master)](https://coveralls.io/github/dhondta/asciistuff?branch=master)
[![Python Versions](https://img.shields.io/pypi/pyversions/asciistuff.svg)](https://pypi.python.org/pypi/asciistuff/)
[![Requirements Status](https://requires.io/github/dhondta/asciistuff/requirements.svg?branch=master)](https://requires.io/github/dhondta/asciistuff/requirements/?branch=master)
[![Known Vulnerabilities](https://snyk.io/test/github/dhondta/asciistuff/badge.svg?targetFile=requirements.txt)](https://snyk.io/test/github/dhondta/asciistuff?targetFile=requirements.txt)
[![License](https://img.shields.io/pypi/l/asciistuff.svg)](https://pypi.python.org/pypi/asciistuff/)

# ASCII Stuff

This library gathers some useful ASCII art features relying on [PyFiglet](https://github.com/pwaller/pyfiglet), [Pillow](https://github.com/python-pillow/Pillow) and [cowpy](https://github.com/jeffbuttars/cowpy).

## Setup

This library is available on [PyPi](https://pypi.python.org/pypi/asciistuff/) and can be simply installed using Pip:

```sh
pip install asciistuff
```

or

```sh
pip3 install asciistuff
```

## Objects

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


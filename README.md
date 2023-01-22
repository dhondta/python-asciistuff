<p align="center"><img src="https://github.com/dhondta/python-asciistuff/raw/main/docs/img/logo.png"></p>
<h1 align="center">ASCIIstuff <a href="https://twitter.com/intent/tweet?text=ASCIIstuff%20-%20Fancy%20styled%20banner%20for%20your%20CLI%20tool.%0D%0APython%20library%20for%20making%20ASCII%20banners%20relying%20on%20PyFiglet,%20Pillow%20and%20cowpy.%0D%0Ahttps%3a%2f%2fgithub%2ecom%2fdhondta%2fpython-asciistuff%0D%0A&hashtags=python,programming,asciiart,banners"><img src="https://img.shields.io/badge/Tweet--lightgrey?logo=twitter&style=social" alt="Tweet" height="20"/></a></h1>
<h3 align="center">Make a styled banner for your CLI tool.</h3>

[![PyPi](https://img.shields.io/pypi/v/asciistuff.svg)](https://pypi.python.org/pypi/asciistuff/)
[![Read The Docs](https://readthedocs.org/projects/python-asciistuff/badge/?version=latest)](https://python-asciistuff.readthedocs.io/en/latest/?badge=latest)
[![Build Status](https://github.com/dhondta/python-asciistuff/actions/workflows/python-package.yml/badge.svg)](https://github.com/dhondta/python-asciistuff/actions/workflows/python-package.yml)
[![Coverage Status](https://raw.githubusercontent.com/dhondta/python-asciistuff/main/docs/coverage.svg)](#)
[![Python Versions](https://img.shields.io/pypi/pyversions/asciistuff.svg)](https://pypi.python.org/pypi/asciistuff/)
[![Known Vulnerabilities](https://snyk.io/test/github/dhondta/python-asciistuff/badge.svg?targetFile=requirements.txt)](https://snyk.io/test/github/dhondta/python-asciistuff?targetFile=requirements.txt)
[![License](https://img.shields.io/pypi/l/asciistuff.svg)](https://pypi.python.org/pypi/asciistuff/)

This library gathers some useful ASCII art features relying on [PyFiglet](https://github.com/pwaller/pyfiglet/), [Pillow](https://github.com/python-pillow/Pillow/) and [cowpy](https://github.com/jeffbuttars/cowpy/).

```sh
pip install asciistuff
```

## :sunglasses: Usage

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

### Image

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

### Lolcat

![](https://raw.githubusercontent.com/dhondta/python-asciistuff/main/docs/img/lolcat-example.png)

### Quote

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

### File

```
from asciistuff import *

file = AsciiFile("test.asc")

```


## :clap:  Supporters

[![Stargazers repo roster for @dhondta/python-asciistuff](https://reporoster.com/stars/dark/dhondta/python-asciistuff)](https://github.com/dhondta/python-asciistuff/stargazers)

[![Forkers repo roster for @dhondta/python-asciistuff](https://reporoster.com/forks/dark/dhondta/python-asciistuff)](https://github.com/dhondta/python-asciistuff/network/members)

<p align="center"><a href="#"><img src="https://img.shields.io/badge/Back%20to%20top--lightgrey?style=social" alt="Back to top" height="20"/></a></p>

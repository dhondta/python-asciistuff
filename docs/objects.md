Multiple objects can be defined:

- `Banner`: This is a specially formatted text, e.g. for displaying the name of a tool in a nice fashion.
- `Cowsay`: This wraps the text into an ASCII art using a [*cowsay*](https://linux.die.net/man/1/cowsay) character.
- `Image`: This allows to represent a JPG/PNG image as a text.
- `Quote`: This allows to format a quote as an italic text framed by double quotes and showing the name of its author.

## `Banner`

This object has the following options:

- `text` (string ; required): text to be displayed
- `width` (integer ; default is the terminal size): desired width in characters
- `font` (string ; default is `None`, meaning a randomly chosen font): name of a custom font ; the available font names are stored in `fonts.txt`, provide with the package
- `multiline` (boolean ; defaults to `False`): whether the output should be accepted even if the text is generated on multiple lines
- `autofont` (boolean ; defaults to `True`): automatically choose a replacement font if `multiline` is `False` and the output has multiple lines

The following example shows attributes and methods' outputs as it appears using Idle-Python:

```
>>> from asciistuff import Banner
>>> b = Banner("MyText")
>>> b.font
'xcour'
>>> print(b)
                                   
                                   
                              #    
#   #       #####             #    
## ## ## ## # # #  ##  ## ## ####  
# # #  #  #   #   #  #  # #   #    
# # #  #  #   #   ###    #    #    
#   #  #  #   #   #     # #   #  # 
## ##   ##   ###   ### ## ##   ##  
        #                          
      ##                           

>>> b.rebrand()
>>> print(b)
  ^    ^    ^    ^    ^    ^  
 /M\  /y\  /T\  /e\  /x\  /t\ 
<___><___><___><___><___><___>

>>> Banner.font_exists("does_not_exist")
False
>>> Banner.font_exists("xcour")
True
>>> b.font = "stacey"
>>> b.font = "does_not_exist"
Traceback (most recent call last):
  [...]
ValueError: Bad font name
>>> 
```

## `Cowsay`

This object has the following options:

- `text` (string ; required): text to be displayed
- `width` (integer ; default is the terminal size): desired width in characters
- `cowacter` (string ; defaults to "`default`"): the Cowsay character to be used
- `options` (dictionary): parameters for setting the CowPy object selected using `cowacter`

For a complete list of cowacter and option values, please refer to [CowPy's documentation](https://github.com/jeffbuttars/cowpy).

The following example shows attributes and methods' outputs as it appears using Idle-Python:

```
>>> from asciistuff import Cowsay
>>> c = Cowsay("MyText")
>>> c
 ________ 
< MyText >
 -------- 
     \   ^__^
      \  (oo)\_______
         (__)\       )\/\
           ||----w |
           ||     ||
>>> c.cowacter = "ghostbusters"
>>> c
 ________ 
< MyText >
 -------- 
          \
           \
            \          __---__
                    _-       /--______
               __--( /     \ )XXXXXXXXXXX\v.
             .-XXX(   O   O  )XXXXXXXXXXXXXXX-
            /XXX(       U     )        XXXXXXX\
          /XXXXX(              )--_  XXXXXXXXXXX\
         /XXXXX/ (      O     )   XXXXXX   \XXXXX\
         XXXXX/   /            XXXXXX   \__ \XXXXX
         XXXXXX__/          XXXXXX         \__---->
 ---___  XXX__/          XXXXXX      \__         /
   \-  --__/   ___/\  XXXXXX            /  ___--/=
    \-\    ___/    XXXXXX              '--- XXXXXX
       \-\/XXX\ XXXXXX                      /XXXXX
         \XXXXXXXXX   \                    /XXXXX/
          \XXXXXX      >                 _/XXXXX/
            \XXXXX--__/              __-- XXXX/
             -XXXXXXXX---------------  XXXXXX-
                \XXXXXXXXXXXXXXXXXXXXXXXXXX/
                  ""VXXXXXXXXXXXXXXXXXXV""
>>> c.cowacter = "bunny"
>>> c.options['thoughts'] = True
>>> c
 ________ 
< MyText >
 -------- 
  o
   o   \
        \ /\
        ( )
      .( o ).
```

## `Image`

This object has the following options:

- `path` (string ; required): path to the image
- `width` (integer ; default is the terminal size): desired width in characters
- `font` (string ; defaults to `None`, meaning `ImageFont.load_default()`): name of a custom font to be considered for rendering the ASCII image
- `brightness` (float `<=1` ; defaults to `1.0`): image's brightness, used to setup original image using `ImageEnhance.Brightness`
- `contrast` (float `<=1` ; defaults to `1.0`): image's contrast, used to setup original image using `ImageEnhance.Contrast`
- `charset` (string ; defaults to '`.,*@%#/( `'): character set for the ASCII art (will be sorted and used by pixel density)

The following example shows attributes and methods' outputs as it appears using Idle-Python:

```
>>> from asciistuff import Image
>>> i = Image("hello.png")
>>> i
@@@@@@@@@@@@@@@@@@@@@@@ /   @@@@@@@@@%*,,,,,,,*#@@@@@@@@@   *@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@    @@@@@@/,.                    ../#@@@@@@  @@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@  @@@@#,.      .,/**(%%%####%%((/,.      .,*@@@  @@@@@@@@@@@@@
@@@@@@@@@@@@@@@  @@@,.    .,*%%###%(**//,,,,,/**(%####%(*,    ,%@@ @@@@@@@@@@@@
@@@@@@@@@@@@@  @@/.   ./(###%*,..                   .,/(%##%/   .#@ @@@@@@@@@@@
@@@@@@@@@@@@/@@,.  .(##%*,.                               ,*##*  .,@@@@@@@@@@@@
@@@@@@@@@@@ @(.  ,%@#/.                                      *@#,  .@@ @@@@@@@@
@@@@@@@@@@ @,.  (@%,                                          .%@*  .@  @@@@@@@
@@@@@@@@@ @,  ,#@*                           .%/                *@(  ,@ @@@@@@@
@@@@@@@@ @.  *@%.                      .#(   ,@(                 *@*  ,@ @@@@@@
@@@@@@@ @,  *@%   ..                   .@%   .@(                  %@,  *@ @@@@@
@@@@@@ @/  /@%    %#                    %#   .@%     ,((*.        .##. .@ @@@@@
@@@@@@ @. .@#.    *@,                   *@.   #%    *@%*%@(        (@, .@ @@@@@
@@@@@ @/  (@/     .@(           /##%,   /@,   %#   *@/   *@*       *@. .@ @@@@@
@@@@@ @. .@#       %@(###*.    (#/.(@/  ,@/   (@.  %#    .@%       (@, .@ @@@@@
@@@@ @@. /@*       *@%,./@#.  (@//*%@@, .@*   /@,  %#    *@/       %@. ,@ @@@@@
@@@@ @@. *@*       /@/   .@% ,@#%%*/..   @%   ,@*  /@(.,%@(        ##  ,@ @@@@@
@@@@ @@. /@*       .@(    (@./@/         ##   .@%   /###%,        /@*  (@ @@@@@
@@@@@ @. ,@%        @%    ,@*/@/         %@.   #@.               .##. .@ @@@@@@
@@@@@ @, .##.       ##    .@% %@((%#%,   *@/   ,*.              .#@, .*@ @@@@@@
@@@@@ @*  /@(       #@.    ##  ,*(*,.    ,@%                   /@#,  ,@ @@@@@@@
@@@@@@ @,  %@,      ,/     (@.            **                 ,#@(  .,@ @@@@@@@@
@@@@@@  %. .##,            /#/                             /%@(.  .(@ @@@@@@@@@
@@@@@@@ @/  .%@*            .                           ,(#@(.  ./@@ @@@@@@@@@@
@@@@@@@@ @/.  /##*                                  ./(##(,   ./@@  @@@@@@@@@@@
[...]
>>> i.charset
'@#%(*/,. '
>>> i.charset = "@#¼½^([()\\"
>>> i
@@@@@@@@@@@@@@@@@@@@@@@^(^^^@@@@@@@@@½¼)))))))¼#@@@@@@@@@^^^¼@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@^^^^@@@@@@()\^^^^^^^^^^^^^^^^^^^^\\(#@@@@@@^^@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@^^@@@@#)\^^^^^^\)(¼¼[½½½####½½[[()\^^^^^^\)¼@@@^^@@@@@@@@@@@@@
@@@@@@@@@@@@@@@^^@@@)\^^^^\)¼½½###½[¼¼(()))))(¼¼[½####½[¼)^^^^)½@@^@@@@@@@@@@@@
@@@@@@@@@@@@@^^@@(\^^^\([###½¼)\\^^^^^^^^^^^^^^^^^^^\)([½##½(^^^\#@^@@@@@@@@@@@
@@@@@@@@@@@@(@@)\^^\[##½¼)\^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^)¼##¼^^\)@@@@@@@@@@@@
@@@@@@@@@@@^@[\^^)½@#(\^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^¼@#)^^\@@^@@@@@@@@
@@@@@@@@@@^@)\^^[@½)^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\½@¼^^\@^^@@@@@@@
@@@@@@@@@^@)^^)#@¼^^^^^^^^^^^^^^^^^^^^^^^^^^^\½(^^^^^^^^^^^^^^^^¼@[^^)@^@@@@@@@
@@@@@@@@^@\^^¼@½\^^^^^^^^^^^^^^^^^^^^^^\#[^^^)@[^^^^^^^^^^^^^^^^^¼@¼^^)@^@@@@@@
@@@@@@@^@)^^¼@½^^^\\^^^^^^^^^^^^^^^^^^^\@½^^^\@[^^^^^^^^^^^^^^^^^^½@)^^¼@^@@@@@
@@@@@@^@(^^(@½^^^^½#^^^^^^^^^^^^^^^^^^^^½#^^^\@½^^^^^)[[¼\^^^^^^^^\##\^\@^@@@@@
@@@@@@^@\^\@#\^^^^¼@)^^^^^^^^^^^^^^^^^^^¼@\^^^#½^^^^¼@½¼½@[^^^^^^^^[@)^\@^@@@@@
@@@@@^@(^^[@(^^^^^\@[^^^^^^^^^^^(##½)^^^(@)^^^½#^^^¼@(^^^¼@¼^^^^^^^¼@\^\@^@@@@@
@@@@@^@\^\@#^^^^^^^½@[###¼\^^^^[#(\[@(^^)@(^^^[@\^^½#^^^^\@½^^^^^^^[@)^\@^@@@@@
@@@@^@@\^(@¼^^^^^^^¼@½)\(@#\^^[@((¼½@@)^\@¼^^^(@)^^½#^^^^¼@(^^^^^^^½@\^)@^@@@@@
@@@@^@@\^¼@¼^^^^^^^(@(^^^\@½^)@#½½¼(\\^^^@½^^^)@¼^^(@[\)½@[^^^^^^^^##^^)@^@@@@@
@@@@^@@\^(@¼^^^^^^^\@[^^^^[@\(@(^^^^^^^^^##^^^\@½^^^(###½)^^^^^^^^(@¼^^[@^@@@@@
@@@@@^@\^)@½^^^^^^^^@½^^^^)@¼(@(^^^^^^^^^½@\^^^#@\^^^^^^^^^^^^^^^\##\^\@^@@@@@@
[...]
>>> i.contrast = .5
>>> i
@@@@@@@@@@@@@@@@@@@@@@@^()^^@@@@@@@@@[¼¼¼¼¼¼¼¼¼½@@@@@@@@@^^(¼@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@^(^@@@@@#¼((()))))))))))))))))))((¼½@@@@@@(@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@¼^@@@@½¼(()))))((¼¼[[[½½½½½½½[[[¼(())))))((¼@@@(@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@¼^@@#¼())))((¼[½½½½[[[¼¼¼((((¼¼¼¼[½½½½½[[¼()))((½@@^@@@@@@@@@@@@
@@@@@@@@@@@@@^^@@¼()))(¼[½½½[¼¼(())))))))))))))))))((¼¼[[½½½¼)))(½@(@@@@@@@@@@@
@@@@@@@@@@@@(@@¼())([½½½[(()))))))))))))))))))))))))))))))([½½¼))(¼@@@@@@@@@@@@
@@@@@@@@@@@(@[())([#½¼()))))))))))))))))))))))))))))))))))))(¼½½())(@@@@@@@@@@@
@@@@@@@@@@^@¼())[#½¼))))))))))))))))))))))))))))))))))))))))))([#¼))(@^@@@@@@@@
@@@@@@@@@^@())(½#¼))))))))))))))))))))))(()))([¼))))))))))))))))[#[))(@(@@@@@@@
@@@@@@@@^@())¼#½())))))))))))))))))))))(½[)))(#[)))))))))))))))))[#¼))¼@^@@@@@@
@@@@@@@¼@())¼#[))((()))))))))))))))))))(½[)))(½[))))))))))))))))))[#()(¼@^@@@@@
@@@@@@^@¼))¼#[))))½½()))))))))))))))))))½½())(½[)))))([[¼())))))))(½½()(@^@@@@@
@@@@@@^@()(#½())))¼#¼)))))))))))))()))))[½()))½½))))¼#[¼[½[))))))))[#()(@^@@@@@
@@@@@^@¼))[#¼)()))(#[))())))))))¼½½½()))¼#()))½½())¼#¼)))¼#¼)))))))[#()(@^@@@@@
@@@@@^@()(#½)))))))½½[½½½[())))[½¼([½¼))(#¼)()[½())½½))()(½[)))))))[#()(@^@@@@@
@@@@@@½()¼#¼)))))))[#[((¼½½())[#¼¼¼[½½()(#¼)()¼#())[½))))[#¼)))))))[½()(@^@@@@@
@@@@@@½()¼#¼)))))))¼#¼)))(#[)(#½½[[¼(())(½[)()(#¼))¼#[(([#[))))))))½½))¼@^@@@@@
@@@@@@#()¼#[)))))))(#[))()[#(¼#¼)))))))))½½)))(½[)))¼½½½[())))))()¼#¼)([@^@@@@@
@@@@@^@()(#[)))))))(½[))))¼#¼¼#¼)))(())))[½()))½#())))())))))))()(½½()(@^@@@@@@
@@@@@^@()(½½()))))))½½))))(½[)[#[[[½½()()¼#¼)()¼¼())))))))))))))(½#¼)([@^@@@@@@
[...]
```

## `Quote`

This object has the following options:

- `quote` (string ; required): quote to be displayed
- `source` (string ; default to '`unknown`'): quote's source/author
- `width` (integer ; default is the terminal size): desired text width in characters
- `margin` (float ; defaults to `.1`): value (belongs to [0, .5[) for symmetrical left/right margins
- `cowsay` (string ; defaults to `None`, meaning no cowsay): cowsay character (cowacter) to be considered

The following example shows attributes and methods' outputs as it appears using Idle-Python (note that, using Idle, text does not appear as italic):

```
>>> from asciistuff import Quote
>>> q = Quote("A nice quote", "John Doe")
>>> q 
"A nice quote",
       John Doe
>>> q = Quote("A nice quote", "John Doe", cowsay="random")
>>> q
 _________________ 
/ "A nice quote", \
\        John Doe /
 ----------------- 
     \
      \  (__)  
         (\/)  
  /-------\/    
 / | 666 ||    
*  ||----||      
   ~~    ~~
>>> q
 _________________ 
/ "A nice quote", \
\        John Doe /
 ----------------- 
     \   ^__^
      \  (oo)\_______
         (__)\       )\/\
           ||----w |
           ||     ||
```

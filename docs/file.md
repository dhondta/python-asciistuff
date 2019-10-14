A small file format named `.asc` represents ASCII arts in *sections*, suitable for styling.


## `AsciiFile`

An *ASCII File* is defined using the `AsciiFile` class. Its only argument is `path` and defaults to `None` (if defined, it allows to immediately load content from a file). The class mostly behaves as a dictionary, supporting a getter/setter but also a few operators. Its string representation provides the rendering while saving to a file will produce a format with section headers holding the styling parameters.

**Adding/Getting sections**

The class, regarding its sections, acts as a dictionary, supporting a getter/setter but also a few operators:

- Setting an item:

        >>> from asciistuff import *
        >>> f = AsciiFile()
        >>> f['title'] = Banner("TEST")
        >>> f['myquote', {'adjust': "right"}] = Quote("A nice quote", "me")
    
- Getting an item (returns section's text and dictionary of parameters):

        >>> f['title']
        >>> f['title']
        ( ___                          ___        
        -   ---___-   ,- _~,   -_-/  -   ---___- 
           (' ||     (' /| /  (_ /      (' ||    
          ((  ||    ((  ||/= (_ --_    ((  ||    
         ((   ||    ((  ||     --_ )  ((   ||    
          (( //      ( / |    _/  ))   (( //     
            -____-    -____- (_-_-       -____-  
                                                 
                                                 
        , {'adjust': 'right'})
        >>> f['myquote']
        ("A nice quote",
                     me, {'adjust': 'right'})

- Adding/replacing a section (if no section specified, the text is added to "`main`"):

        >>> f += Banner("test2")
        >>> print(f['main'][0])
                                        ####    
        ####### # ####  ###### ####### ##  ##   
        ##   ## #   ## ##   ## ##   ## ##  ##   
           #    #      ##         #      ###    
           #   ## ##    #####     #     ##      
           ##  ##           ##    ##   ##  ##   
           ##  ##  ### ##   ##    ##   ######   
           ##  ## ###  ### ##     ##            
        
        >>> f += {'test': Banner("test3")}
        >>> print(f['test'][0])
          #                    #     ####  
         ####    ###    ####  ####       # 
          #     #####  ###     #      ###  
          #     #        ###   #         # 
           ##    ###   ####     ##   ####  
                                           

- Removing a section (using `del` or the substraction operator):

        >>> f -= "test"
        >>> del f['main']


**Section headers**

Each section, in its final string representation, has the following format:

        .section: {name}[{styling_parameters}]

Examples:

- `.section: title`
- `.section: quote[bgcolor=blue]`
- `.section: logo[adjust=left,fgcolor=random]`

By default, when not specifying a section from the beginning of the file, the default section name is "`main`" and it has no styling.

**Attributes and methods**

The `AsciiFile` class has the following attributes:

- `sections`: the ASCII sections, defined to specify styling
- `text`: the rendered text

This class has the following methods:

- `get`: similar to the `get` method of ´dict´ ; this returns the section or `default`'s value if the section does not exist
- `items`: iterate over sections ; this returns a 3-tuple with the section name, text and parameters
- `load`: load data from an ASCII file
- `save`: save the current data to an ASCII file


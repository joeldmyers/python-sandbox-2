# python-sandbox-2 #

This is my own personal comprehensive review of Python from the ground up, since I have mainly been using Node / JS as of late, except for various cron scripts.

## VS Code Notes ##

Shift Command P in VS Code gets the command palette.

Type in "Shell" to make sure that I can write `code .` in terminal to open project.

## Python notes ##

Always have a virtual environment for every project

`dir([thing])` gets a list of all methods on the type of the variable. 
For example
`name="Joel"`
`dir(name)`
Will show the list of all string methods available.


### Variables ###

Cannot start with a number.

Pep8 best practices - name should be all lower case, whole words, separated by an underscore.
`type(x)` will give the variable type.

`None` is the general equivalent of `Null`, class `NoneType`

To make a number variable floating type, just have a variable, like

`x = 5.0`

You can convert a value to a different type using `int(5)`, `float(3.0)`, etc. 

#### Strings ####

With strings, it's best practice to use double quotes, to avoid issues when using an apostrophe.

One can concatenate strings with a +: `name = "Joel " + "Myers"`yields "Joel Myers"

### Syntax Error ###

Read any syntax errors that show in the command line from bottom to top.

### Different applications of Python ###

* AI/ML
    * SciPy
    * NumPy
    * Pandas
    * PyTorch
* Hardware & Micro-controllers
    * Raspberry Pi
    * MicroPython
    * CircuitPython
* Web Development
    * Django
    * Flask
* Scripting
    * Dev Ops Configuration Scripts

### Conventions ###

#### Pep 8 ####

Pep8 - Style Guide for Python Code

[Pep8 Website](https://pep8.org/ "Pep8 Website")
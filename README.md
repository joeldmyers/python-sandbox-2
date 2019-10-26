# python-sandbox-2

This is my own personal comprehensive review of Python from the ground up, since I have mainly been using Node / JS as of late, except for various cron scripts.  Starting from the basics for the sake of thoroughness.

## VS Code Notes

Shift Command P in VS Code gets the command palette.

Type in "Shell" to make sure that I can write `code .` in terminal to open project.

## Python notes

Always have a virtual environment for every project

`dir([thing])` gets a list of all methods on the type of the variable. 
For example
`name="Joel"`
`dir(name)`
Will show the list of all string methods available.


### Variables

Cannot start with a number.

Pep8 best practices - name should be all lower case, whole words, separated by an underscore.
`type(x)` will give the variable type.

`None` is the general equivalent of `Null`, class `NoneType`

To make a number variable floating type, just have a variable, like

`x = 5.0`

You can convert a value to a different type using `int(5)`, `float(3.0)`, etc. 

#### Strings

With strings, it's best practice to use double quotes, to avoid issues when using an apostrophe.

One can concatenate strings with a +: `name = "Joel " + "Myers"`yields "Joel Myers"

To declare a long string, use `"""` to start and end.

##### F String

F Strings are like template literals in Es6 - they do string interpolation: 

`name = Joel`
`f"Hello, {name}` yields 'Hello, Joel'.

#### Functions

To define a function, use `def function_name(param_1, param_2, etc):`

Example function: 

```
def print_my_name(name):
    print(f"My name is {name}")


def meaning_of_life():
    return 42

def add_numbers(x, y):
    return x + y
```

To use default values, use equals (like with ES6):

``` 
def say_greeting(greeting="Hello", name="John Doe"):
    print(f"{greeting}, {name}")
```

** Note: default arguments must always come last.** 

### Data Structures

The main data structures used in Python are lists, tuples, and dictionaries.  

#### Lists

Lists are like "arrays" in javascript. 
`[]` to create an empty list. 
You can also use `list()` to instantiate.  

Typically use plural - `names = ["Alice Coltrane", "Buffie Saint Marie", "Dorothy Ashby"]`

To find the length, use `len(names)`

To get the second item, do `names[1]` (which returns in this case "Buffie Saint Marie")

To re-assign, use `names[1] = 'Janis Joplin'`.  

You can also insert - takes index first, object after.

`insert(0, "Karen Dalton")`

To combine lists, use `extend` method.  

Lists retain the order of items (just like arrays in Javascript).

To sort a list - 

`sorted(list)` returns a copy and leaves the original list alone.  so `x = sorted(list)`

`list.sort()` changes the original list.  
 
 To get type of it, type `type(list)` (returns <class 'list'>)

 To get list of methods on a data type, you can use `dir(list)`

 to get help, you can type `help(list)`, or `help(list.reverse)`, for ex.

##### Lookups for lists

It's generally O(n) to look up in list.  `"Joel" in names` -> `false`

To get the first index of an item, you can do `names.index("Karen Dalton")`

`names.count("Karen Dalton")` -> 1

Other methods - 

Removing - 

say `names = ["Joel", "Bob"]`

`names.remove["Bob"]` -> it removes first instance.  

`name.pop()` removes last item and returns it; you can also pop at a certain index by putting index into parentheses

`names.push()`

#### Tuples

Tuples are immutable lists

They are generally faster. 

to create a tuple, you can just go `a = ()`

One needs to be careful though - `a = (1,)` - here you need a comma at the end.

`student = ("Jane", 8, "History", 3.5)`

`student[0] = "Jane"`

you can 'unpack' them, like destructuring in es6: 

`name, age, subject, gpa = student`



### Syntax Errors

Read any syntax errors that show in the command line from bottom to top.

### Different applications of Python

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

### Conventions

#### Pep 8

Pep8 - Style Guide for Python Code

[Pep8 Website](https://pep8.org/ "Pep8 Website")


### Control Flow

#### Lists

```
colors ['red', 'green', 'blue']
for color in colors:
    print(color)
```

Note, no block scope in for loop. 

If we want to go through a sequence of numbers, we can use `range(5)` which 

```
for num in range(1,5):
    print(num)
```
prints :
`
1
2
3
4
`

You can include a third parameter which is the step.

```
for num in range(1,7,2):
   print(range)
```

### Iterating through Dictionaries

Generally to iterate through dictionaries, we should use .items() to convert the key-value pairs into tuples.  

Then we can use unpacking to pass those into a for loop: 

```
hex_colors = {"red": "#f00", "green":"#008"}
for label, hex in hex_colors.items():
    print(label, hex)
```


### Control Flow

```
if 5 > 3:
    print("Hallo")
elif 3 == 3:
    print "equality"
else:
    print("uh oh")
```


```
counter = 0
max = 10

while counter < max:
    print(f"the count is: {counter}")
    counter = counter + 1
```


##### Break, Continue and Return

These are pretty straightforward / like other languages.  

Break breaks out of the whole for loop; continue goes on to the next iteration at the top of the loop; return is like break.  

Fun example from stack overflow re: return: 

```
def get_index(needle, haystack):
    for x in range(len(haystack)):
        if haystack[x] == needle:
            return x
```


### Pip

Packages!

`pip install requests`


### Easter Eggs In Python

import this

yields 'The Zen of Python'
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!

`import antigravity`

#### Some methods

`csv_row = "John,Math,8"`
`name, subject, age = csv_row.split(',')`
example of CSV parsing - using unpacking and the split method.

Joins is like - 

list = csv_row.split(',')
joined_list = " ".join(list)
print joined_list


## OOP

Everything is an object in Python.  Note: My overall review of OOP is in oop_exercise.py, oop_review.py, and vehicle.py

Generally this review is pretty obvious OOP fundamentals.  

## Handling Exceptions 

Unhandled exceptions are fatal to an application.  We need to make sure we handle all exceptions.  

Generally use try / except. 

```
try:
    num = int(user_input)
    print("cool, all good", num)
except ValueError:
    print("Bad Input!")

```
We can use a tuple to handle multiple error types:

```
d = {1:1}
user_input = "a"

try:
    int(user_input)
    d[user]
except (ValueError, KeyError)
    print("Didn't work")
```

From this stack overflow article - https://stackoverflow.com/questions/14797375/should-i-always-specify-an-exception-type-in-except-statements

From the PEP-8 Style Guide for Python :

When catching exceptions, mention specific exceptions whenever possible instead of using a bare except: clause.

For example, use:
```
 try:
     import platform_specific_module 
 except ImportError:
     platform_specific_module = None 
```
A bare except: clause will catch SystemExit and KeyboardInterrupt exceptions, making it harder to interrupt a program with Control-C, and can disguise other problems. If you want to catch all exceptions that signal program errors, use except Exception: (bare except is equivalent to except BaseException:).

A good rule of thumb is to limit use of bare 'except' clauses to two cases:

If the exception handler will be printing out or logging the traceback; at least the user will be aware that an error has occurred. If the code needs to do some cleanup work, but then lets the exception propagate upwards with raise. try...finally can be a better way to handle this case.

### Custom Exceptions

Just extend from the Exception class.  

```
class MyCustomException(Exception):
    pass

...

raise MyCustomException()
```
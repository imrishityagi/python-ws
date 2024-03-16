# Indentation - Python uses whitespace and indentation to construct the code structure.
# define main function to print out something
def main():
    i = 1
    max = 10
    while (i < max):
        print(i)
        i = i + 1
# call function main 
main()

# Comments
# python single line comments starts with #
# in python we can also create multiline comments using docstring (triple quotes basically)
# eg:
"""
this is a multi-line 
comment"""

# Continuation of statements
"""
Python uses a newline character to separate statements. It places each statement on one line.

However, a long statement can span multiple lines by using the backslash (\) character."""
# eg:
a = 2
b = 0
c = 3
if (a == 2) and (b == 0) and \
   (c == 3):
    print("Continuation of statements")

# Identifiers - Identifiers are names that identify variables, functions, modules, classes, and other objects in Python.
"""
The name of an identifier needs to begin with a letter or underscore (_). The following characters can be alphanumeric or underscore.

Python identifiers are case-sensitive. For example, the counter and Counter are different identifiers.

In addition, you cannot use Python keywords for naming identifiers."""

# Keywords - Some words have special meanings in Python. They are called keywords.
# List of keywords in python:
"""
False      class      finally    is         return
None       continue   for        lambda     try
True       def        from       nonlocal   while
and        del        global     not        with
as         elif       if         or         yield
assert     else       import     pass
break      except     in         raise"""
"""
Python provides a special module for listing its keywords called keyword. 

To find the current keyword list, you use the following code:"""
import keyword

print(keyword.kwlist) 

# String literals
#Python uses single quotes ('), double quotes ("), triple single quotes (''') and triple-double quotes (""") to denote a string literal.
s = 'This is a string'
print(s)
s = "Another string using double quotes"
print(s)
s = ''' string can span
        multiple line '''
print(s)

"""
Summary
A Python statement ends with a newline character.
Python uses spaces and indentation to organize its code structure.
Identifiers are names that identify variables, functions, modules, classes, etc. in Python.
Comments describe why the code works. They are ignored by the Python interpreter.
Use the single quote, double-quotes, triple-quotes, or triple double-quotes to denote."""
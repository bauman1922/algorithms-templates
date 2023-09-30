"""
Modify the spacify function so that it returns the given string with spaces 
inserted between each character.

spacify("hello world") # returns "h e l l o   w o r l d"
"""


def spacify(string):
    return ' '.join(list(string))


print(spacify("hello world"))  # "h e l l o   w o r l d"
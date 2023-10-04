"""
Write a function that accepts a string, and returns true if
it is in the form of a phone number.
Assume that any integer from 0-9 in any of the spots will
produce a valid phone number.

Only worry about the following format:
(123) 456-7890 (don't forget the space after the close parentheses)

Examples:

"(123) 456-7890"  => true
"(1111)555 2345"  => false
"(098) 123 4567"  => false
"""

def valid_phone_number(phone):
    example = '(xxx) xxx-xxxx'
    new_number = ''
    for x in phone:
        if x.isdigit():
            new_number += 'x'
        else:
            new_number += x
    return new_number == example


print(valid_phone_number("(123) 456-7890"))  #  True
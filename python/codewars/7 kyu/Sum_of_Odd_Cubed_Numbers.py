"""
Find the sum of the odd numbers within an array, after cubing the initial
integers.
The function should return undefined/None/nil/NULL if any of the values aren't
numbers.
Note: Booleans should not be considered as numbers.
"""


def cube_odd(arr):
    for x in arr:
        if type(x) is not int:
            return None
    return sum(x ** 3 for x in arr if x ** 3 % 2 != 0)


print(cube_odd(["a", 12, 9, "z", 42]))   # 28

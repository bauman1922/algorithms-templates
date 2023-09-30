"""
Write a function that can return the smallest value of an array
or the index of that value. The function's 2nd parameter
will tell whether it should return the value or the index.
Assume the first parameter will always be an array filled
with at least 1 number and no duplicates. Assume the
second parameter will be a string holding one of two values:
 'value' and 'index'.

min([1,2,3,4,5], 'value') // => 1
min([1,2,3,4,5], 'index') // => 0
"""


def find_smallest(numbers, to_return):
    if to_return == "value":
        return min(numbers)
    if to_return == "index":
        idx = 0
        min_val = numbers[0]
        for x in range(len(numbers)):
            if numbers[x] < min_val:
                min_val = numbers[x]
                idx = x
        return idx



print(find_smallest([8, 0, 9], "index"))   # 1
print(find_smallest([5, 4, 3, 2, 1], "value"))   # 1


# def find_smallest(numbers,to_return):
#     return min(numbers) if to_return == 'value' else numbers.index(min(numbers))

"""
Your task is to sum the differences between consecutive pairs in
he array in descending order.

Example
[2, 1, 10]  -->  9
In descending order: [10, 2, 1]

Sum: (10 - 2) + (2 - 1) = 8 + 1 = 9

If the array is empty or the array has only one element the result should
be 0 (Nothing in Haskell, None in Rust).
"""


def sum_of_differences(arr):
    if len(arr) < 2:
        return 0
    arr = sorted(arr)[::-1]
    new_arr = []
    for x in range(0, len(arr) - 1):
        new_arr.append(arr[x] - arr[x + 1])
    return sum(new_arr)


# def sum_of_differences(arr):
#     arr.sort(reverse=True)
#     i = 0
#     res = 0
#     while i < len(arr)-1:
#         res += arr[i] - arr[i+1]
#         i += 1
#     return res


print(sum_of_differences([1, 2, 10]))  # 9
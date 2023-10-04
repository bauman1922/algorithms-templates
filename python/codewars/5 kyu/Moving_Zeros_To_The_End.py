"""
Write an algorithm that takes an array and moves all
of the zeros to the end, preserving the order of the other elements.

move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0]
"""


def move_zeros(lst):
    # zero_count = 0
    # new_lst = []
    # for x in lst:
    #     if x == 0:
    #         zero_count += 1
    #     else:
    #         new_lst.append(x)
    # return new_lst + [0] * zero_count
    for x in lst:
        if x == 0:
            lst.remove(x)
            lst.append(x)
    return lst




print(move_zeros([9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9]))
# [9, 9, 1, 2, 1, 1, 3, 1, 9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
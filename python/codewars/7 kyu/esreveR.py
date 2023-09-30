"""
Write a function reverse which reverses a list 
(or in clojure's case, any list-like data structure)

(the dedicated builtin(s) functionalities are deactivated)
"""


# # def reverse(lst):
# #     left = 0
# #     right = len(lst) - 1
# #     while left <= right:
# #         lst[left], lst[right] = lst[right], lst[left]
# #         left += 1
# #         right -= 1
# #     return lst


# print(reverse([1,None,14,"two"])) #["two",14,None,1])

def reverse(lst):
    empty_list = list()
    while lst:
        empty_list.append(lst.pop())
    return empty_list


print(reverse([1, None, 14, "two"]))  # ["two",14,None,1])

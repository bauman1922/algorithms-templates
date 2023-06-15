def sum_of_minimums(numbers):
    min_sum = 0
    for row in numbers:
        min_sum += min(row)
    return min_sum


print(sum_of_minimums([ [ 7,9,8,6,2 ], [6,3,5,4,3], [5,8,7,4,5] ]))
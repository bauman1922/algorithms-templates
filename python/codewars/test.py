def solve(arr):
    new_arr = []
    for x in arr[::-1]:
        new_arr.append(x)
        if new_arr.count(x) > 1:
            new_arr.pop()
    return new_arr[::-1]



print(solve([3,4,4,3,6,3]))  #[4,6,3]
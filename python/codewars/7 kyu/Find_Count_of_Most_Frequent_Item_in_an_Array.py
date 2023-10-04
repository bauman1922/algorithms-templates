"""
Complete the function to find the count of the most frequent item of an array.
You can assume that input is an array of integers. For an empty array return 0

Example
input array: [3, -1, -1, -1, 2, 3, -1, 3, -1, 2, 4, 9, 3]
ouptut: 5 
The most frequent number in the array is -1 and it occurs 5 times.
"""


def most_frequent_item_count(collection):
    data = {key: 0 for key in collection}
    for x in collection:
        if x in data:
            data[x] += 1
    return max(data.values()) if collection else 0





print(most_frequent_item_count([3, -1, -1, -1, 2, 3, -1, 3, -1, 2, 4, 9, 3]))  # 5
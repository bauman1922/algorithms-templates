# ID: 88812217
def broken_search(nums, target) -> int:
    start_index = 0
    end_index = len(nums) - 1
    while start_index <= end_index:
        middle_index = (start_index + end_index) // 2
        if nums[middle_index] == target:
            return middle_index
        elif nums[start_index] <= nums[middle_index]:
            if nums[start_index] <= target < nums[middle_index]:
                end_index = middle_index - 1
            else:
                start_index = middle_index + 1
        else:
            if nums[middle_index] < target <= nums[end_index]:
                start_index = middle_index + 1
            else:
                end_index = middle_index - 1
    return -1


def test():
    arr = [19, 21, 100, 101, 1, 4, 5, 7, 12]
    assert broken_search(arr, 5) == 6

# ID: 88833046
import random
from dataclasses import dataclass


@dataclass
class Participant:
    login: str
    points: int
    penalty: int


def partition(nums, left, right):
    pivot_index = random.randint(left, right)
    pivot = nums[pivot_index]
    nums[pivot_index], nums[right] = nums[right], nums[pivot_index]

    i = left
    for j in range(left, right):
        if nums[j].points > pivot.points:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
        elif nums[j].points == pivot.points:
            if nums[j].penalty < pivot.penalty:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
            elif nums[j].penalty == pivot.penalty:
                if nums[j].login < pivot.login:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1

    nums[i], nums[right] = nums[right], nums[i]

    return i


def quicksort(nums, left, right):
    if left < right:
        pivot_index = partition(nums, left, right)
        quicksort(nums, left, pivot_index - 1)
        quicksort(nums, pivot_index + 1, right)


if __name__ == "__main__":
    number = int(input())
    participants = []
    for _ in range(number):
        login, points, penalty = input().split()
        participants.append(Participant(login, int(points), int(penalty)))

    nums = [p for p in participants]
    quicksort(nums, 0, len(nums) - 1)

    print('\n'.join([participant.login for participant in nums]))

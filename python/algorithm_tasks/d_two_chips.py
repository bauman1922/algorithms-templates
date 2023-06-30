"""
Рита и Гоша играют в игру. У Риты есть n фишек, на каждой из которых написано количество очков. 
Сначала Гоша называет число k, затем Рита должна выбрать две фишки, сумма очков на которых равна заданному числу.
Рите надоело искать фишки самой, и она решила применить свои навыки программирования для решения этой задачи. 
Помогите ей написать программу для поиска нужных фишек.

Формат ввода
В первой строке записано количество фишек n, 2 ≤ n ≤ 104.
Во второй строке записано n целых чисел —– очки на фишках Риты в диапазоне от -105 до 105.
В третьей строке —– загаданное Гошей целое число k, -105 ≤ k ≤ 105.

Формат вывода
Нужно вывести два числа —– очки на двух фишках, в сумме дающие k.
Если таких пар несколько, то можно вывести любую из них.
Если таких пар не существует, то вывести «None».

Пример 1
Ввод	Вывод
6
-1 -1 -9 -7 3 -6
2
-1 3
"""
from typing import List, Tuple, Optional


def two_sum(arr: List[int], target_sum: int) -> Optional[Tuple[int, int]]:
    arr.sort()
    left = 0
    right = len(arr) - 1
    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == target_sum:
            return arr[left], arr[right]
        if current_sum < target_sum:
            left += 1
        else:
            right -= 1
    return None


def read_input() -> Tuple[List[int], int]:
    n = int(input())
    arr = list(map(int, input().strip().split()))
    target_sum = int(input())
    return arr, target_sum


def print_result(result: Optional[Tuple[int, int]]) -> None:
    if result is None:
        print(None)
    else:
        print(" ".join(map(str, result)))

arr, target_sum = read_input()
print_result(two_sum(arr, target_sum))


# решение через set
def two_sum(arr: List[int], target_sum: int) -> Optional[Tuple[int, int]]:
    result = set()
    for row in arr:
        elem = target_sum - row
        if elem in result:
            return row, elem
        else:
            result.add(row)
    return None

# наивный алгоритм
def two_sum(arr: List[int], target_sum: int) -> Optional[Tuple[int, int]]:
    for i in range(0, len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == target_sum:
                return arr[i], arr[j]
    return None
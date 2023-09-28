"""
Даны два массива чисел длины n. Составьте из них один массив длины 2n,
 в котором числа из входных массивов чередуются (первый — второй — первый — второй — ...).
При этом относительный порядок следования чисел из одного массива должен быть сохранён.

Формат ввода
В первой строке записано целое число n –— длина каждого из массивов, 1 ≤ n ≤ 1000.
Во второй строке записано n чисел из первого массива, через пробел.
В третьей строке –— n чисел из второго массива.
Значения всех чисел –— натуральные и не превосходят 1000.

Формат вывода
Выведите 2n чисел из объединённого массива через пробел.

Пример 1
Ввод	Вывод
3
1 2 3
4 5 6
1 4 2 5 3 6
"""
from typing import List, Tuple


def zipper(a: List[int], b: List[int]) -> List[int]:
    result = []
    n = len(a)
    for i in range(n):
        result.append(a[i])
        result.append(b[i])
    return result


def read_input() -> Tuple[List[int], List[int]]:
    n = int(input())
    a = list(map(int, input().strip().split()))
    b = list(map(int, input().strip().split()))
    return a, b


a, b = read_input()
print(" ".join(map(str, zipper(a, b))))

# Второй способ
def zipper(a: List[int], b: List[int]) -> List[int]:
    result = []
    for x in zip(a, b):
        result.extend(x)
    return result
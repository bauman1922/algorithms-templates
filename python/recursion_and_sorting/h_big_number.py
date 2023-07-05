"""
Вечером ребята решили поиграть в игру «Большое число».
Даны числа. Нужно определить, какое самое большое число можно из них составить.

Формат ввода
В первой строке записано n — количество чисел. Оно не превосходит 100.
Во второй строке через пробел записаны n неотрицательных чисел, каждое из которых не превосходит 1000.

Формат вывода
Нужно вывести самое большое число, которое можно составить из данных чисел.

Пример 1
Ввод	Вывод
3
15 56 2
56215
Пример 2
Ввод	Вывод
3
1 783 2
78321
"""


def comparate(num1, num2):
    return num1 < num2


def insertion_sort_by_comparator(array, less):
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and less(int(array[j] + key), int(key + array[j])):
            array[j], array[j + 1] = array[j + 1], array[j]
            j -= 1
    print(''.join(array))


if __name__ == '__main__':
    number = int(input())
    insertion_sort_by_comparator(input().split(), comparate)

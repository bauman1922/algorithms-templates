"""
Вам дана статистика по числу запросов в секунду к вашему любимому рекомендательному сервису.
Измерения велись n секунд.
В секунду i поступает qi запросов.
Примените метод скользящего среднего с длиной окна k к этим данным и выведите результат.
Формат ввода
В первой строке передаётся натуральное число n, количество секунд, в течение которых велись измерения. 1 ≤ n ≤ 105
Во второй строке через пробел записаны n целых неотрицательных чисел qi, каждое лежит в диапазоне от 0 до 103.
В третьей строке записано натуральное число k (1 ≤ k ≤ n) —– окно сглаживания.
Примечание для Go:
Заметьте, что в данной задаче достаточно большой размер ввода. Поэтому необходимо задавать
 размер буфера для сканнера хотя бы 600 Кб.

Формат вывода
Выведите через пробел результат применения метода скользящего среднего к серии измерений. 
Должно быть выведено n - k + 1 элементов, каждый элемент -— вещественное (дробное) число.

Пример 1
Ввод	Вывод
7
1 2 3 4 5 6 7
4
2.5 3.5 4.5 5.5 
"""


from typing import List, Tuple


def moving_average(arr: List[int], window_size: int) -> List[float]:
    result = []
    current_sum = sum(arr[0:window_size])
    result.append(current_sum / window_size)
    for i in range(0, len(arr) - window_size):
        current_sum -= arr[i]
        current_sum += arr[i+window_size]
        current_avg = current_sum / window_size
        result.append(current_avg)
    return result


def read_input() -> Tuple[List[int], int]:
    n = int(input())
    arr = list(map(int, input().strip().split()))
    window_size = int(input())
    return arr, window_size


arr, window_size = read_input()
print(" ".join(map(str, moving_average(arr, window_size))))

# наивный алгоритм
def moving_average(arr: List[int], window_size: int) -> List[float]:
    result = []
    for begin_index in range(0, len(arr) - window_size + 1):
        end_index = begin_index + window_size
        current_sum = 0
        for x in arr[begin_index:end_index]:
            current_sum += x
        current_avg = current_sum / window_size
        result.append(current_avg)
    return result
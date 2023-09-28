"""
На IT-конференции присутствовали студенты из разных вузов со всей страны. 
Для каждого студента известен ID университета, в котором он учится.
Тимофей предложил Рите выяснить, из каких k вузов на конференцию пришло больше всего учащихся.

Формат ввода
В первой строке дано количество студентов в списке —– n (1 ≤ n ≤ 15 000).
Во второй строке через пробел записаны n целых чисел —– ID вуза каждого студента. 
Каждое из чисел находится в диапазоне от 0 до 10 000.
В третьей строке записано одно число k.

Формат вывода
Выведите через пробел k ID вузов с максимальным числом участников. Они должны быть отсортированы по убыванию популярности (по количеству гостей от конкретного вуза). Если более одного вуза имеет одно и то же количество учащихся, то выводить их ID нужно в порядке возрастания.

Пример 1
Ввод	Вывод
7
1 2 3 1 2 3 4
3
1 2 3
"""

def get_rating(array, k):
    data = {}
    for x in array:
        if x in data:
            data[x] += 1
        else:
            data[x] = 1
    sorted_data = sorted(data.items(), key=lambda x: (-x[1], x[0]))
    top = [x[0] for x in sorted_data[:k]]
    return top




if __name__ == "__main__":
    n = int(input())
    array = [int(x) for x in input().split()]
    k = int(input())
    print(*get_rating(array, k))
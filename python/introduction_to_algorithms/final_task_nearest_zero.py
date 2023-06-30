# ID: 88093011
from typing import List


def calculate_distances(street: List[int]) -> List[int]:
    length_street = len(street)
    distances = [length_street] * length_street
    previous_empty = -length_street

    for index, value in enumerate(street):
        if value == 0:
            distances[index] = 0
            previous_empty = index
        else:
            distances[index] = min(index - previous_empty, distances[index])

    next_empty = 2 * length_street

    for index, value in enumerate(range(length_street - 1, -1, -1)):
        if street[value] == 0:
            next_empty = value
        else:
            distances[value] = min(distances[value], next_empty - value)

    return distances


if __name__ == '__main__':
    length_street = int(input())
    street = [int(x) for x in input().split()]

    distances = calculate_distances(street)
    print(' '.join(map(str, distances)))

    def test_calculate_distances():
        result = calculate_distances([0, 1, 4, 9, 0])
        assert result == [0, 1, 2, 1, 0], f'Wrong answer: {result}'
        result = calculate_distances([0, 7, 9, 4, 8, 20])
        assert result == [0, 1, 2, 3, 4, 5], f'Wrong answer: {result}'
        result = calculate_distances([1, 0, 3, 2])
        assert result == [1, 0, 1, 2], f'Wrong answer: {result}'
        print('Все тесты пройдены!')

    test_calculate_distances()




def calculate(numbers: List[int], length: int) -> List[int]:
    distance = []
    zero_position = None
    for i, value in enumerate(numbers):
        if value == 0:
            zero_position = i
            distance.append(0)
            continue
        if zero_position is not None:
            distance.append(i - zero_position)
        else:
            distance.append(length)
    return distance

# Второй вариант решения задча
def nearest_zero(length: int, number_street: List[int]) -> List[int]:
    distance = calculate(number_street, length)
    r_distance = (calculate(number_street[::-1], length))[::-1]
    result = []
    for step in range(length):
        result.append(min(distance[step], r_distance[step]))
    return result


def read_input() -> Tuple[int, List[int]]:
    length = int(input())
    number_street = [int(num) for num in input().split(' ')]
    return length, number_street


if __name__ == '__main__':
    length, number_street = read_input()
    print(' '.join([str(x) for x in nearest_zero(length, number_street)]))
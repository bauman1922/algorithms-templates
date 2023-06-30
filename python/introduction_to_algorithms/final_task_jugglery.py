# ID: 88093412
import time
from typing import List


def calculate_score(buttons: List[str], number: int) -> int:
    score = 0
    counter = [0] * 10
    max_count = 2 * number

    for row in buttons:
        for value in row:
            if value.isdigit():
                counter[int(value)] += 1

    for value in range(1, 10):
        if 0 < counter[value] <= max_count:
            score += 1

    return score


if __name__ == '__main__':

    number = int(input())
    buttons = [input() for _ in range(4)]

    result = calculate_score(buttons, number)
    print(result)

    start_time = time.time()
    result = calculate_score(buttons, number)
    end_time = time.time()

    execution_time = end_time - start_time
    print(f"Время выполнения: {execution_time} секунд.")

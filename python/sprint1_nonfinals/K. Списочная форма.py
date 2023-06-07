from typing import List, Tuple

def get_sum(number_list: List[int], k: int) -> List[int]:
    return [int(digit) for digit in str(int("".join(map(str, number_list))) + k)]

def read_input() -> Tuple[List[int], int]:
    n = int(input())
    number_list = list(map(int, input().strip().split()))
    k = int(input())
    return number_list, k

number_list, k = read_input()
print(" ".join(map(str, get_sum(number_list, k))))



#return [int(digit) for digit in str(int("".join(map(str, number_list))) + k)]

number = int("".join(map(str, number_list))) + k) # перевод строки чисел в число int
lst = [int(digit) for digit in str(number)]  # перевод строки чисел в список чисел int
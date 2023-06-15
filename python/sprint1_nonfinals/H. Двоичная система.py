from typing import Tuple


def get_sum(first_number: str, second_number: str) -> str:
    return bin(int(first_number, 2) + int(second_number, 2))[2:]


def read_input() -> Tuple[str, str]:
    first_number = input().strip()
    second_number = input().strip()
    return first_number, second_number


first_number, second_number = read_input()
print(get_sum(first_number, second_number))



def binary_addition(num1, num2):
    # Установка указателей на последние разряды чисел
    ptr1 = len(num1) - 1
    ptr2 = len(num2) - 1

    carry = 0
    result = ""

    while ptr1 >= 0 or ptr2 >= 0:
        # Получение текущих разрядов чисел
        digit1 = int(num1[ptr1]) if ptr1 >= 0 else 0
        digit2 = int(num2[ptr2]) if ptr2 >= 0 else 0

        # Сложение текущих разрядов и переноса
        current_sum = digit1 + digit2 + carry

        if current_sum == 0 or current_sum == 1:
            result = str(current_sum) + result
            carry = 0
        elif current_sum == 2:
            result = "0" + result
            carry = 1
        elif current_sum == 3:
            result = "1" + result
            carry = 1

        # Перемещение указателей на следующие разряды
        ptr1 -= 1
        ptr2 -= 1

    # Добавление оставшегося переноса
    if carry == 1:
        result = "1" + result

    return result
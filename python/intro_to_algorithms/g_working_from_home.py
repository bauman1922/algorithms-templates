"""
Работа из дома

Вася реализовал функцию, которая переводит целое число из десятичной системы в 
двоичную. Но, кажется, она получилась не очень оптимальной.
Попробуйте написать более эффективную программу.
Не используйте встроенные средства языка по переводу чисел в бинарное представление.

Формат ввода
На вход подаётся целое число в диапазоне от 0 до 10000.

Формат вывода
Выведите двоичное представление этого числа.

Пример 1
Ввод	    Вывод
5           101

"""


def to_binary(number: int) -> str:
    # Здесь реализация вашего решения
    if number == 0:
        return 0
    date = ''
    while number > 0:
        date = str(number % 2) + date
        number = number // 2
    return date


def read_input() -> int:
    return int(input().strip())

print(to_binary(read_input()))


# рекурсивный метод
def as_binary_string(n):
    if n < 0:
        return "-" + as_binary_string(-n)
    if n == 0 or n == 1:
        return str(n)
    last_digit = n % 2
    return as_binary_string(n // 2) + str(last_digit)

def read_input() -> int:
    return int(input().strip())

print(to_binary(read_input()))

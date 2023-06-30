"""
Лишняя буква

Васе очень нравятся задачи про строки, поэтому он придумал свою. 
Есть 2 строки s и t, состоящие только из строчных букв. Строка t 
получена перемешиванием букв строки s и добавлением 1 буквы в случайную 
позицию. Нужно найти добавленную букву.

Формат ввода
На вход подаются строки s и t, разделённые переносом строки. 
Длины строк не превосходят 1000 символов. Строки не бывают пустыми.

Формат вывода
Выведите лишнюю букву.

Пример 1
Ввод	            Вывод
abcd                e
abcde
"""


from typing import Tuple


def get_excessive_letter(shorter: str, longer: str) -> str:
    data = {}
    for char in longer:
        if char in data:
            data[char] += 1
        else:
            data[char] = 1

    for char in shorter:
        if char in data:
            data[char] -= 1
    for char, count in data.items():
        if count != 0:
            return char


def read_input() -> Tuple[str, str]:
    shorter = input().strip()
    longer = input().strip()
    return shorter, longer

shorter, longer = read_input()
print(get_excessive_letter(shorter, longer))

"""
Палиндром

Помогите Васе понять, будет ли фраза палиндромом. Учитываются только буквы и
цифры, заглавные и строчные буквы считаются одинаковыми.

Решение должно работать за O(N), где N — длина строки на входе.

Формат ввода
В единственной строке записана фраза или слово. Буквы могут быть только 
латинские. Длина текста не превосходит 20000 символов.
Фраза может состоять из строчных и прописных латинских букв, цифр, 
знаков препинания.

Формат вывода
Выведите «True», если фраза является палиндромом, и «False», если не является.

Пример 1
Ввод	                            Вывод
A man, a plan, a canal: Panama      True
"""


def is_palindrome(line: str) -> bool:
    new_line = ''.join(x.lower() for x in line if x.isalpha())
    return new_line == new_line[::-1]


print(is_palindrome(input().strip()))

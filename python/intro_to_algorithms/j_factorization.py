"""
Факторизация

Основная теорема арифметики говорит: любое число раскладывается на 
произведение простых множителей единственным образом, с точностью до их 
перестановки. Например:

Число 8 можно представить как 2 × 2 × 2.
Число 50 –— как 2 × 5 × 5 (или 5 × 5 × 2, или 5 × 2 × 5). 
Три варианта отличаются лишь порядком следования множителей.
Разложение числа на простые множители называется факторизацией числа.

Напишите программу, которая производит факторизацию переданного числа.

Формат ввода
В единственной строке дано число n (2 ≤ n ≤ 109), которое нужно факторизовать.

Формат вывода
Выведите в порядке неубывания простые множители, на которые раскладывается число n.

Пример 1
Ввод	            Вывод
8                   2 2 2
"""

from typing import List


def factorize(number: int) -> List[int]:
    lst = []
    chislo = 2
    while chislo * chislo <= number:
        if number % chislo == 0:
            lst.append(chislo)
            number = number // chislo
        else:
            chislo += 1
    if number > 1:
        lst.append(number)
    return lst


result = factorize(int(input()))
print(" ".join(map(str, result)))



# from typing import List

# # # ДОЛГОЕ ВРЕМЯ ИСПОЛНЕНИЯ КОДА
# # def factorize(number: int) -> List[int]:
# #     lst = []
# #     chislo = 2
# #     while number > 1:
# #         if number % chislo == 0:
# #             lst.append(chislo)
# #             number = number / chislo
# #         else:
# #             chislo += 1
# #     return lst


# # result = factorize(int(input()))
# # print(" ".join(map(str, result)))
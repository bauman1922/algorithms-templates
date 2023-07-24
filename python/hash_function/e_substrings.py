"""
На вход подается строка. Нужно определить длину наибольшей подстроки, 
которая не содержит повторяющиеся символы.

Формат ввода
Одна строка, состоящая из строчных латинских букв. Длина строки не превосходит 10 000.

Формат вывода
Выведите натуральное число —– ответ на задачу.

Пример 1
Ввод	Вывод
abcabcbb
3
Пример 2
Ввод	Вывод
bbbbb
1
"""

# исходная строка
string = input()
# здесь будет наш ответ
result = 0
# на старте у нас пустая подстрока
data = ''
# перебираем все символы в исходной строке
for char in string:
    # если символа нет в подстроке
    if char not in data:
        # добавляем его туда
        data += char
        # добавляем его туда
        result = max(result, len(data))
    # если символ в подстроке есть
    else:
        # получаем индекс текущего символа в подстроке
        idx = data.index(char)
        # сокращаем нашу подстроку: оставляем только то, что идёт после 
        # символа-дубликата, и добавляем к строке текущий символ
        data = data[idx + 1:] + char
        # выводим результат на экран
print(result)


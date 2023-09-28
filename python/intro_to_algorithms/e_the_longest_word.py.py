"""
Самое длинное слово

Чтобы подготовиться к семинару, Гоше надо прочитать статью по эффективному 
менеджменту. Так как Гоша хочет спланировать день заранее, ему необходимо 
оценить сложность статьи.

Он придумал такой метод оценки: берётся случайное предложение из текста и в нём 
ищется самое длинное слово. Его длина и будет условной сложностью статьи.

Помогите Гоше справиться с этой задачей.

Формат ввода
В первой строке дана длина текста L (1 ≤ L ≤ 105).
В следующей строке записан текст, состоящий из строчных латинских букв и 
пробелов. Слово —– последовательность букв, не разделённых пробелами. Пробелы 
могут стоять в самом начале строки и в самом её конце. Текст заканчивается 
переносом строки, этот символ не включается в число остальных L символов.

Формат вывода
В первой строке выведите самое длинное слово. Во второй строке выведите его 
длину. Если подходящих слов несколько, выведите то, которое встречается раньше.

Пример 1
Ввод	                Вывод
19                      segment
i love segment tree     7
"""


def get_longest_word(line: str) -> str:
    # Здесь реализация вашего решения
    return max(line.split(), key=len)

def read_input() -> str:
    _ = input()
    line = input().strip()
    return line

def print_result(result: str) -> None:
    print(result)
    print(len(result))

print_result(get_longest_word(read_input()))


def get_longest_word(line: str) -> str:
    arr = line.split()
    max_length = len(arr)
    if max_length == 1:
        return ''.join(arr)
    current_word = arr[0]
    for i in range(1, max_length):
        if len(arr[i]) > len(current_word):
            current_word = arr[i]
    return current_word
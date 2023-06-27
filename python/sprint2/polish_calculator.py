# ID: 88595712
import operator


class Stack:
    def __init__(self):
        self.array = []

    def push(self, element):
        self.array.append(element)

    def pop(self):
        try:
            return self.array.pop()
        except IndexError:
            raise IndexError("Стек пустой!")


def get_polish_expression(expression, stack=None,
                          operations=None, converter=None):
    polish_expression = expression.split()
    if stack is None:
        stack = Stack()
    if operations is None:
        operations = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': operator.floordiv
        }
    if converter is None:
        converter = int
    for value in polish_expression:
        operation = operations.get(value)
        if operation is None:
            try:
                stack.push(converter(value))
            except ValueError:
                raise ValueError(f"Некорректное значение: {value}")
        else:
            try:
                operand_2, operand_1 = stack.pop(), stack.pop()
                stack.push(operation(operand_1, operand_2))
            except ValueError:
                raise ValueError("Некорректное выражение")
    return stack.pop()


if __name__ == "__main__":
    print(get_polish_expression(input()))

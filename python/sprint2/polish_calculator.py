# ID: 88601907
import operator

OPERATIONS = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.floordiv
}


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
                          operations=OPERATIONS, converter=int):
    if stack is None:
        stack = Stack()
    for value in expression:
        operation = operations.get(value)
        if operation is None:
            try:
                stack.push(converter(value))
            except ValueError:
                raise ValueError(f"Некорректное значение: {value}")
            continue
        operand_2, operand_1 = stack.pop(), stack.pop()
        stack.push(operation(operand_1, operand_2))

    return stack.pop()


if __name__ == "__main__":
    expression = input().split()
    print(get_polish_expression(expression))

# ID: 88561482
OPERATIONS = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x // y
}


class EmptyStackError(Exception):
    """Исключение, возникающее при доступе к пустому стеку."""
    pass


class Stack:
    def __init__(self):
        self.array = []

    def is_empty(self):
        return len(self.array) == 0

    def push(self, element):
        self.array.append(element)

    def pop(self):
        if self.is_empty():
            raise EmptyStackError("Стек пустой. Невозможно извлечь элемент.")
        return self.array.pop()


if __name__ == "__main__":
    phrase = input().split(' ')
    stack = Stack()
    for value in phrase:
        if value in OPERATIONS:
            operation = OPERATIONS.get(value)
            operand2, operand1 = stack.pop(), stack.pop()
            result = operation(operand1, operand2)
            stack.push(result)
        else:
            stack.push(int(value))

    print(stack.pop())

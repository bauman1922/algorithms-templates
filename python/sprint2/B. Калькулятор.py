# ID: 88492916
def calculate_polish_notation(phrase):
    stack = []
    operators = {'+': lambda x, y: x + y,
                 '-': lambda x, y: x - y,
                 '*': lambda x, y: x * y,
                 '/': lambda x, y: x // y}

    try:
        for token in phrase.split():
            if token.isdigit() or (
                 token.startswith('-') and token[1:].isdigit()):
                stack.append(int(token))
            elif token in operators:
                if len(stack) < 2:
                    raise ValueError("Недостаточно операндов "
                                     "для операции '{}'".format(token))

                b = stack.pop()
                a = stack.pop()
                result = operators[token](a, b)
                stack.append(result)
            else:
                raise ValueError("Некорректная операция: '{}'".format(token))

        if len(stack) > 1:
            result = stack[-1]
            stack = [result]

        return stack

    except (ValueError, ZeroDivisionError) as e:
        raise ValueError("Ошибка при вычислении выражения: {}".format(str(e)))


if __name__ == "__main__":
    phrase = input()
    try:
        result = calculate_polish_notation(phrase)
        print(*result)
    except ValueError as e:
        print(e)

def evaluate_function(a: int, x: int, b: int, c: int) -> int:
    # Здесь реализация вашего решения
    return a * x ** 2 + b * x + c

a, x, b, c = map(int, input().strip().split())
print(evaluate_function(a, x, b, c))
assert evaluate_function(-8, -5, -2, 7) == 183, ('Функция работает некорректно!')

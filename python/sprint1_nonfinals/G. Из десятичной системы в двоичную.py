def to_binary(number: int) -> str:
    # Здесь реализация вашего решения
    if number == 0:
        return 0
    date = ''
    while number > 0:
        date = str(number % 2) + date
        number = number // 2
    return date


def read_input() -> int:
    return int(input().strip())

print(to_binary(read_input()))

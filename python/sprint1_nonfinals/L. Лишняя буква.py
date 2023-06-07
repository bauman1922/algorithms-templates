from typing import Tuple


def get_excessive_letter(shorter: str, longer: str) -> str:
    data = {}
    for char in longer:
        if char in data:
            data[char] += 1
        else:
            data[char] = 1

    for char in shorter:
        if char in data:
            data[char] -= 1
    for char, count in data.items():
        if count != 0:
            return char


def read_input() -> Tuple[str, str]:
    shorter = input().strip()
    longer = input().strip()
    return shorter, longer

shorter, longer = read_input()
print(get_excessive_letter(shorter, longer))

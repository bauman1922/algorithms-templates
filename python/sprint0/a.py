def get_excessive_letter(shorter: str, longer: str) -> str:
    data = {}
    for char in shorter:
        if char in data:
            data[char] += 1
        else:
            data[char] = 1

    for char in longer:
        if char in data:
            data[char] -= 1
    for char, count in data.items():
        if count != 0:
            return char



print(get_excessive_letter('go', 'ogg'))
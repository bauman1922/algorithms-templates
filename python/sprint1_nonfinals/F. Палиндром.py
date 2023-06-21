def is_palindrome(line: str) -> bool:
    new_line = ''.join(x.lower() for x in line if x.isalpha())
    return new_line == new_line[::-1]


print(is_palindrome(input().strip()))

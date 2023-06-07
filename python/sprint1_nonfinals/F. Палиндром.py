def is_palindrome(line: str) -> bool:
    import re
    line = re.sub('[:!@#$\n-.,]', '', line)
    return line.lower() == line[::-1].lower()

print(is_palindrome(input().strip()))

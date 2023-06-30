# Решение 1
def is_correct_bracket(text):
    while '()' in text or '[]' in text or '{}' in text:
        text = text.replace('()', '').replace('[]', '').replace('{}', '')
    if text == '':
        return True
    else:
        return False


text = input()
print(is_correct_bracket(text))

# Решение 2
text = input()
stack = []
flag = True

for x in text:
    if x in "([{":
        stack.append(x)
    elif x in ")]}":
        if len(stack) == 0:
            flag = False
            break

        p = stack.pop()
        if p == "(" and x == ")":
            continue
        if p == "[" and x == "}":
            continue
        if p == "{" and x == "}":
            continue

        flag = False
        break

if flag and len(stack) == 0:
    print("True")
else:
    print("False")

# Решение 3
PATTERN = {
    '(': ')',
    '[': ']',
    '{': '}',
}


class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        if self.isEmpty():
            return None
        return self.items[-1]


if __name__ == '__main__':
    inp_line = list(input())
    stack = Stack()
    for value in inp_line:
        if value in PATTERN.keys():
            stack.push(value)
        elif not stack.isEmpty() and PATTERN.get(stack.peek()) == value:
            stack.pop()
        else:
            stack.push(value)
    if stack.isEmpty():
        print('True')
    else:
        print('False')
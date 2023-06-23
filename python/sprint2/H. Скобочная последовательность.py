# def is_correct_bracket(text):
#     while '()' in text or '[]' in text or '{}' in text:
#         text = text.replace('()', '').replace('[]', '').replace('{}', '')
#     if text == '':
#         return True
#     else:
#         return False


# text = input()
# print(is_correct_bracket(text))

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

class StackMax:
    def __init__(self) -> None:
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if len(self.items) == 0:
            return "error"
        self.items.pop()

    def get_max(self):
        if len(self.items) == 0:
            return None
        return max(self.items)


stack = StackMax()
n = int(input())
answer = []
for _ in range(n):
    input_command = input().split()
    if input_command[0] == "push":
        stack.push(int(input_command[1]))
    elif input_command[0] == "pop":
        if stack.pop() == 'error':
            answer.append('error')
    elif input_command[0] == "get_max":
        answer.append(stack.get_max())

print(*answer, sep='\n')

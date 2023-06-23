class MaxEffective:
    def __init__(self) -> None:
        self.items = []
        self.max_items = []

    def push(self, x):
        self.items.append(x)
        if len(self.items) == 1:
            self.max_items.append(x)
            return
        if x > self.max_items[-1]:
            self.max_items.append(x)
        else:
            self.max_items.append(self.max_items[-1])

    def pop(self):
        if not self.items:
            return "error"
        self.items.pop()
        self.max_items.pop()

    def get_max(self):
        return self.max_items[-1] if self.max_items else None


stack = MaxEffective()
n = int(input())
answer = []
for _ in range(n):
    input_command = input().split()
    if input_command[0] == "push":
        stack.push(int(input_command[1]))
    elif input_command[0] == "pop":
        p = stack.pop()
        if p is not None:
            answer.append(p)
    elif input_command[0] == "get_max":
        answer.append(stack.get_max())

print(*answer, sep='\n')
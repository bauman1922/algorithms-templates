class MyQueueSized:
    def __init__(self, n) -> None:
        self.queue = [None] * n
        self.max_n = n
        self.head = 0
        self.tail = 0
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def push(self, x):
        if self.size < self.max_n:
            self.queue[self.tail] = x
            self.tail = (self.tail + 1) % self.max_n
            self.size += 1
        else:
            return 'error'

    def pop(self):
        if self.is_empty():
            return None
        x = self.queue[self.head]
        self.queue[self.head] = None
        self.head = (self.head + 1) % self.max_n
        self.size -= 1
        return x

    def peek(self):
        if self.is_empty():
            return None
        return self.queue[self.head]


p = int(input())
length_queue = int(input())
q = MyQueueSized(length_queue)
answer = []
for _ in range(p):
    command = input().split()
    if command[0] == "push":
        a = q.push(command[1])
        if a == "error":
            answer.append(a)
    if command[0] == "pop":
        answer.append(q.pop())
    if command[0] == "peek":
        answer.append(q.peek())
    if command[0] == 'size':
        answer.append(q.size)

print(*answer, sep='\n')

class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def is_empty(self):
        return self.head is None

    def put(self, x):
        new_node = Node(x)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def get(self):
        if self.is_empty():
            return "error"
        value = self.head.value
        self.head = self.head.next
        self.size -= 1
        return value

    def get_size(self):
        return self.size

n = int(input())
queue = Queue()
answer = []

for _ in range(n):
    command = input().split()
    if command[0] == "put":
        queue.put(int(command[1]))
    elif command[0] == "get":
        answer.append(queue.get())
    elif command[0] == "size":
        answer.append(queue.get_size())

print(*answer, sep='\n')

# ID: 88489148
class MyDeque:
    """Класс двусторонней очереди."""
    def __init__(self, max_size):
        self.deque = [None] * max_size
        self.max_size = max_size
        self.head = 0
        self.tail = 0
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def push_back(self, value):
        """Добавляет значение в конец очереди."""
        if self.size < self.max_size:
            self.deque[self.tail] = value
            self.tail = (self.tail + 1) % self.max_size
            self.size += 1
        else:
            return "error"

    def pop_back(self):
        """Удаляет значение из конца очереди и возвращает его."""
        if self.is_empty():
            return "error"
        x = self.deque[self.tail - 1]
        self.deque[self.tail - 1] = None
        self.tail = (self.tail - 1) % self.max_size
        self.size -= 1
        return x

    def push_front(self, value):
        """Добавляет значение в начало очереди."""
        if self.size < self.max_size:
            self.deque[self.head - 1] = value
            self.head = (self.head - 1) % self.max_size
            self.size += 1
        else:
            return "error"

    def pop_front(self):
        """Удаляет значение из начала очереди и возвращает его."""
        if self.is_empty():
            return "error"
        x = self.deque[self.head]
        self.deque[self.head] = None
        self.head = (self.head + 1) % self.max_size
        self.size -= 1
        return x


if __name__ == "__main__":
    count_command = int(input())
    max_size = int(input())
    answer = []
    queue = MyDeque(max_size)
    for _ in range(count_command):
        command = input().split()
        if command[0] == "push_back":
            p = queue.push_back(int(command[1]))
            if p == "error":
                answer.append(p)
        if command[0] == "push_front":
            p = queue.push_front(int(command[1]))
            if p == "error":
                answer.append(p)
        if command[0] == "pop_back":
            answer.append(queue.pop_back())
        if command[0] == "pop_front":
            answer.append(queue.pop_front())

    print(*answer, sep='\n')

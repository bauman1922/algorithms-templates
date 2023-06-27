# ID: 88594638
class BoundedDeque:
    """Класс двусторонней очереди."""
    def __init__(self, max_size):
        self.elements = [None] * max_size
        self.max_size = max_size
        self.head = 0
        self.tail = 0
        self.size = 0

    def reached_empty_size(self):
        if self.size == 0:
            raise IndexError("Дек пустой!")

    def reached_max_size(self):
        if self.size == self.max_size:
            raise IndexError("Дек заполнен!")

    def push_back(self, value):
        """Добавляет значение в конец очереди."""
        self.reached_max_size()
        self.elements[self.tail] = value
        self.tail = (self.tail + 1) % self.max_size
        self.size += 1

    def pop_back(self):
        """Удаляет значение из конца очереди и возвращает его."""
        self.reached_empty_size()
        self.tail = (self.tail - 1) % self.max_size
        value = self.elements[self.tail]
        self.size -= 1
        return value

    def push_front(self, value):
        """Добавляет значение в начало очереди."""
        self.reached_max_size()
        self.head = (self.head - 1) % self.max_size
        self.elements[self.head] = value
        self.size += 1

    def pop_front(self):
        """Удаляет значение из начала очереди и возвращает его."""
        self.reached_empty_size()
        value = self.elements[self.head]
        self.head = (self.head + 1) % self.max_size
        self.size -= 1
        return value


if __name__ == "__main__":
    count_command = int(input())
    answers = []
    deque = BoundedDeque(int(input()))
    for _ in range(count_command):
        command, *parameters = input().split()
        try:
            result = getattr(deque, command)(*parameters)
            if result is not None:
                answers.append(result)
        except IndexError:
            answers.append("error")
        except AttributeError:
            raise ValueError(f"Некорректная команда ввода: {command}")

    print(*answers, sep='\n')

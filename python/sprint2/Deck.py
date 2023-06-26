# ID: 88559735
class OverflowError(Exception):
    """Исключение, возникающее при переполнении дека."""
    pass


class IndexError(Exception):
    """Исключение, возникающее при доступе к пустому деку."""
    pass


class Deck:
    """Класс двусторонней очереди."""
    def __init__(self, max_size):
        self.elements = [None] * max_size
        self.max_size = max_size
        self.head = 0
        self.tail = 0
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.max_size

    def push_back(self, value):
        """Добавляет значение в конец очереди."""
        if self.is_full():
            raise OverflowError("Дек заполнен. Невозможно добавить элемент!")
        self.elements[self.tail] = value
        self.tail = (self.tail + 1) % self.max_size
        self.size += 1

    def pop_back(self):
        """Удаляет значение из конца очереди и возвращает его."""
        if self.is_empty():
            raise IndexError("Дек пустой. Невозможно удалить элемент.")
        self.tail = (self.tail - 1) % self.max_size
        value = self.elements[self.tail]
        self.size -= 1
        return value

    def push_front(self, value):
        """Добавляет значение в начало очереди."""
        if self.is_full():
            raise OverflowError("Дек заполнен. Невозможно добавить элемент!")
        self.head = (self.head - 1) % self.max_size
        self.elements[self.head] = value
        self.size += 1

    def pop_front(self):
        """Удаляет значение из начала очереди и возвращает его."""
        if self.is_empty():
            raise IndexError("Дек пустой. Невозможно удалить элемент.")
        value = self.elements[self.head]
        self.head = (self.head + 1) % self.max_size
        self.size -= 1
        return value


if __name__ == "__main__":
    count_command = int(input())
    answers = []
    deck = Deck(int(input()))
    for _ in range(count_command):
        cmd, *prms = input().split()
        try:
            method = getattr(deck, cmd)
            result = method(*prms)
            if result is not None:
                answers.append(result)
        except OverflowError:
            answers.append("error")
        except IndexError:
            answers.append("error")
        except AttributeError:
            print("Некорректная команда ввода!")

    print(*answers, sep='\n')

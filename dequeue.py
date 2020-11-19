
class Dequeue:

    def __init__(self):
        self.data = []

    def add_front(self, record):
        self.data.append(record)

    def add_rear(self, record):
        self.data.insert(0, record)

    def remove_front(self):
        self.data.pop()

    def remove_last(self):
        self.data.pop(0)

    def size(self):
        return len(self.data)

    def is_empty(self):
        return len(self.data) == 0

    def __str__(self):
        return f'Dequeue({self.data})'


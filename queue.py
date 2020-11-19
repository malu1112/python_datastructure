
class Queue:

    def __init__(self):
        self.data = []

    def is_empty(self):
        return len(self.data) == 0

    def enqueue(self, record):
        self.data.insert(0, record)

    def dequeue(self):
        self.data.pop()

    def size(self):
        return len(self.data)


class Stack:
    def __init__(self):
        self.data = []

    def push(self, record):
        self.data.append(record)

    def peek(self):
        if self.data:
            return self.data[-1]
        else:
            return None

    def size(self):
        return len(self.data)

    def pop(self):
        if self.data:
            del self.data[-1]
        else:
            raise IndexError('No records found')

    def is_empty(self):
        return len(self.data) == 0

    def __str__(self):
        return f'Stack({self.data})'




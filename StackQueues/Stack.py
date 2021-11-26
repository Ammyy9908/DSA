class Stack:
    def __init__(self):
        self.items = []
        self.capacity = 10

    def push(self, item):
        if len(self.items) == self.capacity:
            return "Stack is full"
        self.items.append(item)

    def pop(self):
        if len(self.items) == 0:
            return "Stack is empty"
        return self.items.pop()

    def peek(self):
        if len(self.items) == 0:
            return "Stack is empty"
        return self.items[-1]

    def isEmpty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)








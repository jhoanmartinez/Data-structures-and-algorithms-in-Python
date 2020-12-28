class Stack:
    def __init__(self):
        self.items = []

    def push(self, data):
        self.items.append(data)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return len(self.items) == []

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def get_stack(self):
        return self.items

s = Stack()
s.push("A")
s.push("B")
s.push("C")
print(s.get_stack())

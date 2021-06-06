class Stack:
    def __init__(self):
        self.data = []

    def __str__(self):
        return f"[{', '.join(str(el) for el in reversed(self.data))}]"

    def push(self, item):
        return self.data.append(item)

    def pop(self):
        return self.data.pop()

    def peek(self):
        return self.data[-1]

    def is_empty(self):
        return len(self.data) == 0


stack = Stack()
stack.push(3)
stack.push(4)
stack.push(5)
print(stack)
print(stack.pop())
print(stack)
print(stack.peek())
print(stack)
print(stack.is_empty())
print(stack)
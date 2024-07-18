from collections import deque


class Stack:
    def __init__(self):
        self.container = deque()

    def push(self, value):
        self.container.append(value)

    def pop(self):
        try:
            return self.container.pop()
        except:
            return ""

    def __len__(self):
        return len(self.container)

    def __repr__(self):
        return f'stack({str(self.container)[7:-2]})'

    def isEmpty(self):
        return len(self.container) == 0

    def peek(self):
        try:
            return self.container[-1]
        except:
            return ""

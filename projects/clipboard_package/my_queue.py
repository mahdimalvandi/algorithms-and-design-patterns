from collections import deque


class Queue:
    def __init__(self):
        self.container = deque()

    def enqueue(self, value):
        self.container.appendleft(value)

    def dequeue(self):
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

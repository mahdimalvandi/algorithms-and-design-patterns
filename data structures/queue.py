from collections import deque


class Queue:
    def __init__(self):
        self.container = deque()

    def enqueue(self, val):
        self.container.appendleft(val)

    def dequeue(self):
        return self.container.pop()

    def __len__(self):
        return len(self.container)

    def __repr__(self):
        return f'queue({str(self.container)[1:-1]})'


qu = Queue()

qu.enqueue(3)
qu.enqueue(5)
qu.enqueue(1)

print(qu)

print(qu.dequeue())
print(qu.dequeue())

print(qu)

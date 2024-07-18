from collections import deque
import logging

logging.basicConfig(level=logging.WARNING, format='%(levelname): %(message)s')


class CStack:
    def __init__(self):
        self.container = deque()

    def push(self, value):
        self.container.append(value)

    def pop(self):
        try:
            return self.container.pop()
        except:
            logging.warning('Stack is empty')

    def peek(self):
        try:
            return self.container[-1]
        except:
            logging.warning('Stack is empty')

    def __len__(self):
        return len(self.container)

    def __repr__(self):
        return f'stack({str(self.container)[7:-2]})'


my_stack = CStack()

my_stack.push(4)
my_stack.push(2)
my_stack.push(5)

print(my_stack)

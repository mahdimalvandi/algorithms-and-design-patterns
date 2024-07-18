import clipboard as cb
import keyboard as kb
import time
import os
from my_stack import Stack
from my_queue import Queue


def greetings():
    print('Welcome to the clipboard master program : Version 1.0')


def use_file_or_not():
    while True:
        try:
            use_file = int(input("Would you like to use file or not? \n1.Yes\n2.No"))
            if use_file == 1 or use_file == 2:
                if use_file == 1:
                    file = input('Please enter your file:')

                    return file
                if use_file == 2:
                    return None

            else:
                print('Invalid number')
        except:
            continue


def get_memory_type():
    while True:
        try:
            memory_type = int(input("Please enter a memory type : \n 1.Stack \n 2.Queue\n"))
            if memory_type == 1 or memory_type == 2:
                if memory_type == 1:
                    _memory = Stack()
                    _memory_label = 'Stack'
                    _file = use_file_or_not()

                    return _memory, _memory_label, _file
                if memory_type == 2:
                    _memory = Queue()
                    _memory_label = 'Queue'
                    _file = use_file_or_not()

                    return _memory, _memory_label, _file
            else:
                print('Invalid memory type')
        except:
            continue


def memory_handler(val=None):
    global memory
    global m_label

    if val is not None:
        if m_label == "Stack":
            memory.push(val)
        else:
            memory.enqueue(val)
    else:
        if m_label == "Stack":
            return memory.pop()
        else:
            return memory.dequeue()


def copy_func():
    global memory
    global m_label
    global pasting

    time.sleep(0.05)
    memory_handler(val=cb.paste())
    cb.copy(memory.peek())
    pasting = False


def paste_func():
    global memory
    global m_label
    global pasting

    time.sleep(0.05)
    print(memory)
    if len(memory) == 0:
        cb.copy('')
    else:
        if not pasting:
            cb.copy('')
            pasting = True

        cb.copy(memory_handler())



def file_handler(file):
    global pasting
    with open(file, 'r') as f:
        for line in f.readlines():
            memory_handler(line)
    pasting = False


if __name__ == '__main__':
    greetings()
    memory, m_label, file = get_memory_type()
    pasting = False
    if file is not None:
        file_handler(file=file)


    kb.add_hotkey('ctrl+c', copy_func)
    kb.add_hotkey('ctrl+v', paste_func)

    input()





from typing import Any


class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.before = None
        self.next = None


class LinkedList:
    def __init__(self) -> None:
        self.head: Node = None
        self.front: Node = None
        self.length: int = 0

    def push(self, data: Any):
        """
        push a data object at the head of the linked list
        :param data:
        :return:

        example:
            >>> ll = LinkedList()
            >>> ll.push(5)
            >>> ll.push(7)
            >>> ll.push(4)
            >>> print(ll)
                '4 => 7 => 5'
        """
        # creating a new node
        new_node: Node = Node(data)
        new_node.next = self.head

        if not self.length:
            self.front = new_node
        else:
            self.head.before = new_node
        self.head = new_node

        self.length += 1

    def __len__(self):
        return self.length

    def append(self, data: Any):
        """
        append data object at the last of linked list
        :param data:
        :return:

        example:
            >>> ll = LinkedList()
            >>> ll.append(5)
            >>> ll.append(7)
            >>> ll.append(4)
            >>> print(ll)
                '5 => 7 => 4'
        """
        # creating a new node
        new_node: Node = Node(data)

        if self.head is None:
            return self.push(data)
        new_node.before = self.front
        self.front.next = new_node
        self.front = new_node
        self.length += 1

    def pop(self) -> Node:
        """
        return the last object of linked list and remove it from the list
        :return:
        """
        data: Node = self.front
        if not self.length:

            self.head = None
            self.front = None
            self.length = 0
        else:
            self.front = self.front.before
            self.front.next = None

        return data.data

    def __repr__(self) -> str:
        _str: str = ''
        temp: Node = self.head

        if temp is None:
            return _str
        else:
            while temp.next:
                _str += str(temp.data) + ' => '
                temp = temp.next
            else:
                _str += str(temp.data)
            return _str


class Queue:
    def __init__(self):
        self.container = LinkedList()

    def enqueue(self, value):
        self.container.push(value)

    def dequeue(self):
        try:
            return self.container.pop()
        except:
            return ""


class Stack:
    def __init__(self):
        self.container = LinkedList()

    def push(self, value):
        self.container.append(value)

    def pop(self):
        try:
            return self.container.pop()
        except:
            return ""

    def __len__(self):
        return len(self.container)



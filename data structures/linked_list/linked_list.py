class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.length += 1
        return self.head

    def __repr__(self):
        _str = ''
        temp = self.head
        if temp is None:
            return _str
        else:
            while temp.next:
                _str += str(temp.data) + ' => '
                temp = temp.next
            else:
                _str += str(temp.data)
            return _str

    def append(self, data):
        temp = self.head
        if temp is None:
            return self.push(data)
        new_node = Node(data)

        while temp.next:
            temp = temp.next
        else:
            temp.next = new_node
            self.length += 1

    def __len__(self):
        return self.length

    def insert(self, data, index):
        pre = self.head

        if pre is None:
            return self.push(data)

        temp = pre.next
        new_node = Node(data)

        count = 1
        while count != index:

            try:
                pre, temp = temp, temp.next
            except:
                return self.append(data)

            count += 1
        else:
            pre.next = new_node
            new_node.next = temp

    def __reversed__(self):
        pre = None
        cur = self.head
        while cur:
            _next = cur.next
            cur.next = pre
            pre = cur
            cur = _next

        self.head = pre


ll = LinkedList()

ll.push(5)
ll.push(8)
ll.push(2)
ll.push(6)
print(ll)

print(reversed(ll))

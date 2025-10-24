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
        _str = 'LinkedList('
        temp = self.head
        if temp is None:
            return _str
        else:
            while temp.next:
                _str += str(temp.data) + ' => '
                temp = temp.next
            else:
                _str += str(temp.data)
            return _str + ")"

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

    def insert(self, data: any, index: int):
        if index<=0:
            self.push(data)
        elif index>=self.length:
            self.append(data)
        else:
            if self.head is None:
                self.push(data)
            else:
                i = 0
                new_node = Node(data)
                temp = self.head
                while i < index-1:
                    temp = temp.next      
                    i +=1        
                else:
                    next_node = temp.next
                    temp.next = new_node
                    new_node.next = next_node



    def __reversed__(self):
        pre = None
        cur = self.head
        while cur:
            _next = cur.next
            cur.next = pre
            pre = cur
            cur = _next

        self.head = pre

    def has_loop(self) -> bool:
        slow = fast = self.head
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        else:
            return False
        # items = set()
        # temp = self.head.next
        # while temp.next:
        #     if temp in items:
        #         return True
        #     items.add(temp)
        #     temp = temp.next 
        # return False
        


    def pop(self, index: int = None) -> Node:
        if index is None or index > self.length:
            index = self.length
        elif index == -1:
            temp = self.head
            while temp.next.next:
                temp = temp.next
            else:
                returned_node = temp.next
                temp.next = None
                return returned_node
        elif index == 0:
            first = self.head
            self.head = self.head.next
            return first
        else:
            index -= 1 
            temp = self.head
            while index > 0:
                temp = temp.next
                index -= 1
            returned_node = temp.next
            temp.next = returned_node.next
            returned_node.next = None
            return returned_node



ll = LinkedList()

n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n2

ll.head = n1

print(ll.has_loop())
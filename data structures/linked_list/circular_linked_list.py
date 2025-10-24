class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
        
class ClinkedList:
    def __init__(self):
        self.head = None
        self.length = 0
    
    
    def push(self, value):
        new_node = Node(value)
        if self.head:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            else:
                new_node.next = self.head
                self.head = new_node
                temp.next = new_node 
        else:
            self.head = new_node
            new_node.next = self.head
            self.length = 1
            
            
    
    def __repr__(self):
        _str = 'LinkedList('
        temp = self.head
        if temp is None:
            return _str
        else:
            while temp.next != self.head:
                _str += str(temp.value) + ' => '
                temp = temp.next
            else:
                _str += str(temp.value) + " -> [LOOP]"
            return _str + ")"
        
        

ll = ClinkedList()


ll.push(1)
ll.push(2)
ll.push(3)
ll.push(4)


print(ll)
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None

    def add_child(self, data):
        if type(data) != BinaryTreeNode:
            data = BinaryTreeNode(data)
        if self.left is None:
            self.left = data
            data.parent = self
        elif self.right is None:
            self.right = data
            data.parent = self
        else:
            self.left.add_child(data)


    def is_strict(self):
        if self.parent is not None:
            raise ValueError("Send root")

        if self.left is None and self.right is None:
            return True

        if self.left is not None and self.right is not None:
            return self.left.is_strict() and self.right.is_strict()

        return False

    def count_nodes(self):
        if self.parent is not None:
            raise ValueError("Send root")
        if self is None:
            return 0
        return (1+self.left.count_nodes()+self.right.count_nodes())

    def is_complete(self, index, number_nodes):
        if self.parent is not None:
            raise ValueError("Send root")

        if self is None:
            return True

        if index >= number_nodes:
            return (self.left.is_complete(2*index+1, number_nodes) and self.right.is_complete(2*index+2, number_nodes))
        return None



import binary_tree

lst = [4,9,1,3,7,5]



def add_node(data, node: binary_tree.BinaryTreeNode):
    if data < node.data:
        if node.left:
            add_node(data, node.left)
        else:
            node.left = binary_tree.BinaryTreeNode(data)
    else:
        if node.right:
            add_node(data, node.right)
        else:
            node.right = binary_tree.BinaryTreeNode(data)




class BinarySearchTree(binary_tree.BinaryTreeNode):
    def add_child(self, data):
        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTree(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTree(data)

    def search(self, data):
        found, node = False, None
        if data == self.data:
            found = True
            node = self
        elif data < self.data:
            if self.left:
                found, node = self.left.search(data)
        else:
            if self.right:
                found, node = self.right.search(data)
        return found, node

parent_tree_node = BinarySearchTree(lst[0])
for data in lst[1:]:
    parent_tree_node.add_child(data)


print(parent_tree_node.search(5))
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None
        self.level = 0

    def add_child(self, child):
        self.children.append(child)
        child.parent = self
        child.level = child.parent.level + 1

    def print_tree(self):
        print(f"{self.level * '-'} {self.data}")
        for child in self.children:
            child.print_tree()

    def search_child(self, data):
        if self.data == data:
            return True
        else:
            for child in self.children:
                if child.search_child(data):
                    return True

        return False


def create_tree():
    root = TreeNode("electronics")
    laptop = TreeNode("laptops")
    mobile = TreeNode("mobiles")

    root.add_child(laptop)
    root.add_child(mobile)

    samsung_laptop_node = TreeNode('samsung_laptop')
    apple_laptop_node = TreeNode('apple_laptop')
    iphone = TreeNode("iphone")

    laptop.add_child(samsung_laptop_node)
    laptop.add_child(apple_laptop_node)

    mobile.add_child(iphone)

    samsung = TreeNode("samsung")
    mobile.add_child(samsung)

    return root


if __name__ == '__main__':
    root = create_tree()
    root.print_tree()
    print(root.search_child("laptops"))
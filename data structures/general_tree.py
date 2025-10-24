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
    def height(self):

        if len(self.children) == 0:
            return 0
        max_height = -1
        for child in self.children:
            max_height = max(max_height, child.height())

        return max_height+1

    def is_binary_tree(self):
        if len(self.children) > 2 :
            return False
        if len(self.children) == 0:
            return True

        for child in self.children:
            if not child.is_binary_tree():
                return False
        return True


def create_tree():
    root = TreeNode("electronics")
    laptop = TreeNode("laptops")
    mobile = TreeNode("mobiles")

    root.add_child(laptop)
    root.add_child(mobile)

    samsung_laptop_node = TreeNode('samsung_laptop')
    apple_laptop_node = TreeNode('apple_laptop')
    apple_laptop_node2 = TreeNode('apple_laptop2')
    iphone = TreeNode("iphone")

    laptop.add_child(samsung_laptop_node)
    laptop.add_child(apple_laptop_node)
    laptop.add_child(apple_laptop_node2)

    mobile.add_child(iphone)

    samsung = TreeNode("samsung")
    mobile.add_child(samsung)
    return root


if __name__ == '__main__':
    root = create_tree()
    root.print_tree()

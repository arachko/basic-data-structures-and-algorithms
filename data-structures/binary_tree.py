class BinaryTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinaryTree(data)
        elif data > self.data:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinaryTree(data)

    def get_in_order_traversal(self):
        elements = []
        elements.extend(self.left.get_in_order_traversal() if self.left else [])
        elements.append(self.data)
        elements.extend(self.right.get_in_order_traversal() if self.right else [])
        return elements

    def get_pre_order_traversal(self):
        elements = [self.data]
        elements.extend(self.left.get_pre_order_traversal() if self.left else [])
        elements.extend(self.right.get_pre_order_traversal() if self.right else [])
        return elements

    def get_post_order_traversal(self):
        elements = []
        elements.extend(self.left.get_post_order_traversal() if self.left else [])
        elements.extend(self.right.get_post_order_traversal() if self.right else [])
        return elements

    def search(self, value):
        if value == self.data:
            return self
        elif self.left and value < self.data:
            return self.left.search(value)
        elif self.right and value > self.data:
            return self.right.search(value)
        else:
            msg = f'No such value in the tree error, value={value}'
            print(msg)
            raise Exception(msg)

    def find_min(self):
        return self.left.find_min() if self.left else self.data

    def find_max(self):
        return self.right.find_max() if self.right else self.data

    def delete(self, value):
        if value < self.data:
            self.left = self.left.delete(value) if self.left else None
        elif value > self.data:
            self.right = self.right.delete(value) if self.right else None
        else:
            if self.left is None and self.right is None:
                return None
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.left
            else:
                self.data = self.right.find_min()
                self.right.delete(self.data)
        return self


if __name__ == '__main__':
    tree = BinaryTree(15)
    for val in [7, 4, 18, 9, 25, 8, 29, 46, 3]:
        tree.add_child(val)

    tree.delete(3)
    tree.delete(25)
    tree.delete(46)
    in_order_values_list = tree.get_in_order_traversal()
    pre_order_values_list = tree.get_pre_order_traversal()
    post_order_values_list = tree.get_post_order_traversal()
    search_1 = tree.search(9)
    # search_2 = tree.search(10)
    print(in_order_values_list)
    print(tree.find_max())
    print(tree.find_min())

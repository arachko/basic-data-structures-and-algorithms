class Tree:
    def __init__(self, data, parent=None):
        self.children = []
        self.parent = parent
        self.data = data

    def add_child(self, data):
        child = Tree(data, parent=self)
        self.children.append(child)
        return child

    def remove_child(self, child_to_delete):
        for i, child in enumerate(self.children):
            if child == child_to_delete:
                self.children.pop(i)
                break

    @staticmethod
    def get_level_of_deep(parent, i=0):
        return i if parent is None else parent.get_level_of_deep(parent.parent, i + 1)

    def print_tree(self):
        prefix = '' if not self.parent else f'{" " * 3 * (self.get_level_of_deep(self.parent) - 1)}|{"__"}'
        print(f'{prefix}{self.data}')
        for child in self.children:
            child.print_tree()


if __name__ == "__main__":
    store = Tree('STORE')

    fruits_in_store = store.add_child('Fruits')
    bakery_in_store = store.add_child('Bakery')
    milk_in_store = store.add_child('Milk')

    banana_in_fruits = fruits_in_store.add_child('Banana')
    pear_in_fruits = fruits_in_store.add_child('Pear')

    cookies_in_bakery = bakery_in_store.add_child('Cookies')

    yogurt_in_milk = milk_in_store.add_child('Yogurt')
    cheese_in_milk = milk_in_store.add_child('Cheese')

    store.print_tree()

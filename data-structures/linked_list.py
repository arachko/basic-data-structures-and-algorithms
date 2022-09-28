class Element:
    def __init__(self, data, prev_element=None, next_element=None):
        self.data = data
        self.prev: Element = prev_element
        self.next: Element = next_element

    def insert_element_next(self, element):
        element.prev = self
        element.next = self.next
        if self.next:
            self.next.prev = element
        self.next = element

    def insert_element_prev(self, element):
        if not self.prev:
            raise Exception("You can't insert elements before head. "
                            "Use insert_at_the_beginning method of LinkedList class object instead")
        element.prev = self.prev
        element.next = self
        self.prev.next = element
        self.prev = element

    def delete(self):
        if not self.prev:
            raise Exception("You can't delete the head element")
        else:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev

    def print_data(self):
        print(self.data)


class LinkedList:
    def __init__(self, head: Element = None):
        self.head = head

    def check_head(self):
        if not self.head:
            raise Exception("Head must not be empty")

    def get_length(self):
        if self.head:
            i = 1
            elem = self.head
            while elem.next:
                elem = elem.next
                i += 1
            return i
        else:
            return 0

    def insert_at_the_beginning(self, element: Element):
        if self.head:
            self.head.prev = element
            element.next = self.head
        self.head = element

    def insert_at_the_end(self, element: Element):
        if self.head:
            elem = self.head
            while elem.next:
                elem = elem.next
            elem.next = element
        else:
            self.head = element

    def insert_at_position(self, element: Element, position: int):
        self.check_head()
        elem = self.head
        for i in range(position-1):
            elem = elem.next
        elem.insert_element_next(element)

    def delete_head_element(self):
        self.head = self.head.next
        self.head.prev = None

    def delete_at_position(self, position: int):
        if position == 0:
            self.delete_head_element()
        else:
            self.check_head()
            elem = self.head
            for i in range(position):
                elem = elem.next
            elem.delete()

    def print_list(self):
        elem = self.head
        elem.print_data()
        while elem.next:
            elem = elem.next
            elem.print_data()


if __name__ == '__main__':
    linked_list = LinkedList(Element('first'))
    first = linked_list.head
    second = Element('second')
    first.insert_element_next(second)
    third = Element('third')
    first.insert_element_next(third)
    fourth = Element('fourth')
    second.insert_element_prev(fourth)
    linked_list.insert_at_the_beginning(Element('fifth'))
    linked_list.insert_at_the_end(Element('sixth'))
    linked_list.insert_at_position(Element('seventh'), 2)
    linked_list.delete_at_position(3)

    linked_list.print_list()

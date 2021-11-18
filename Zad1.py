class Node:
    def __init__(self, value):
        self.value = value
        self.next = None



class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __repr__(self):
        s = ""
        repr = self.head
        while repr:
            s += str(repr.value) + " -> "
            repr = repr.next
        return s[:-4]

    def push(self, value):
        elem = Node(value)
        elem.next = self.head
        self.head = elem
        if self.tail == None:
            self.tail = elem

    def append(self, value):
        elem = Node(value)
        if self.head == None:
            self.head = elem
            self.tail = elem
        else:
            self.tail.next = elem
            self.tail = elem

    def node(self, value):
        if len(self) < value:
            return "Error"
        poz = value
        if poz < 0:
            poz = 0
        elem = self.head
        while poz:
            elem = elem.next
            poz -= 1
        return elem

    def insert(self, value, after):
        elem = Node(value)
        n = self.head
        while n != after:
            n = n.next
        elem.next = n.next
        n.next = elem

    def pop(self):
        first = self.head
        self.head = first.next
        return first.value

    def remove_last(self):
        last = self.tail
        node = self.head
        while node.next != last:
            node = node.next
        node.next = None
        self.tail = node
        return last.value

    def remove(self, node):
        deleted = node.next
        node.next = deleted.next

    def __print__(self):
        return self.__repr__()

    def __len__(self):
        v = 0
        node = self.head
        while node:
            v += 1
            node = node.next
        return v






list_ = LinkedList()
assert list_.head == None

list_.push(1)
list_.push(0)

assert str(list_) == '0 -> 1'
list_.append(9)
list_.append(10)

assert str(list_) == '0 -> 1 -> 9 -> 10'

middle_node = list_.node(1)
list_.insert(5, after=middle_node)

assert str(list_) == '0 -> 1 -> 5 -> 9 -> 10'

first_element = list_.node(0)
returned_first_element = list_.pop()

assert first_element.value == returned_first_element

last_element = list_.node(3)
returned_last_element = list_.remove_last()

assert last_element.value == returned_last_element
assert str(list_) == '1 -> 5 -> 9'

second_node = list_.node(1)
list_.remove(second_node)

assert str(list_) == '1 -> 5'
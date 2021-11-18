from Zad2 import LinkedList

class Stack:
    _storage: LinkedList

    def push(self, element: Any):


    def pop(self):








stack = Stack()

assert len(stack) == 0

stack.push(3)
stack.push(10)
stack.push(1)

assert len(stack) == 3

top_value = stack.pop()

assert top_value == 1

assert len(stack) == 2
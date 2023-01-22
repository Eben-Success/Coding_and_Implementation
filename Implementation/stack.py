"""
Stack is First In Last Out DSA.
It can be implemented using an array.
It has two major operations: push and pop.
Both push and pop operations have time complexity of O(1)
"""

class Stack:
    def __init__(self):
        self.stack = []

    # add and element to the stack
    def push(self, item):
        self.stack.append(item)

    def pop(self):
        print("Popped the last element")
        return self.stack.pop()

    def is_empty(self):
        return len(self.stack) == 0

    def print_stack(self):
        print(self.stack)



stack = Stack()
stack.push(str(1))
stack.push(str(2))
stack.push(str(3))
stack.push(str(4))
stack.push(str(5))

stack.print_stack()

stack.pop()

stack.print_stack()
    
    
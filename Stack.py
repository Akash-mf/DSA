#Working with stacks
#In this exercise, you will follow two steps to implement a stack with the push() operation using a
# singly linked list. You will also define a new attribute called size to track the number of items in the stack.
# You will start coding the class to build a Stack(), and after that, you will implement the push() operation.
class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, data):
        # Create a node with the data
        new_node = Node(data)
        if self.top:
            new_node.next = self.top
        # Set the created node to the top node
        self.top = new_node
        # Increase the size of the stack by one
        self.size += 1

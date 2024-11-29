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

    def pop(self):
        # Check if there is a top element
        if self.top is None:
            return None
        else:
            popped_node = self.top
            # Decrement the size of the stack
            self.size -= 1
            # Update the new value for the top node
            self.top = self.top.next
            popped_node.next = None
            return popped_node.data

    def peek(self):
        if self.top:
            return self.top.data
        else:
            return None


Stack_test = Stack()
Stack_test.push(1)

# Print the top element using peek
print(Stack_test.peek())  # Should print 1

Stack_test.push(5)

# Print the top element using peek
print(Stack_test.peek())  # Should print 5

Stack_test.push(2)

# Print the top element using peek
print(Stack_test.peek())  # Should print 2

# Pop the top element and print it
print(Stack_test.pop())  # Should print 2

# Print the new top element using peek
print(Stack_test.peek())  # Should print 5

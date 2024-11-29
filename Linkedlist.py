class Node:
    def __init__(self, data):
        self.value = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head:
            new_node.next = self.head
            self.head = new_node
        else:
            self.tail = new_node
            self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head:
            self.tail.next = new_node
            self.tail = new_node
        else:
            self.head = new_node
            self.tail = new_node

    def search(self, data):
        current_node = self.head
        while current_node:
            if current_node.value == data:
                return True
            else:
                current_node = current_node.next
        return False


LinkedList_example = LinkedList()
LinkedList_example.insert_at_end(1)
LinkedList_example.insert_at_end(2)
LinkedList_example.insert_at_beginning(3)

# Searching for elements and printing the results
print(LinkedList_example.search(1))  # Should print True
print(LinkedList_example.search(0))  # Should print False
print(LinkedList_example.search(2))  # Should print True
print(LinkedList_example.search(3))  # Should print True
print(LinkedList_example.search(5))  # Should print False




#Working with queues
#In this exercise, you will implement a class called PrinterTasks(),
# which will represent a simplified queue for a printer.
# Queue() clasы includes the following methods:

#enqueue(data): adds an element to the queue
#dequeue(): removes an element from the queue
#has_elements(): checks if the queue has elements.
#You will start coding the PrinterTasks() class with its add_document() and print_documents() methods.
# After that, you will simulate the execution of a program that uses the PrinterTasks() class

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        print("Head: " + str(self.head.data) + " Tail: " + str(self.tail.data))

    def dequeue(self):
        if self.head:
            current_node = self.head
            self.head = current_node.next
            current_node.next = None

            if self.head is None:
                self.tail = None

            return current_node.data  # Return the data instead of the node object

    def has_elements(self):
        return self.head is not None


class PrinterTasks:
    def __init__(self):
        self.queue = Queue()

    def add_document(self, document):
        # Add the document to the queue
        self.queue.enqueue(document)

    def print_documents(self):
        # Iterate over the queue while it has elements
        while self.queue.has_elements():
            # Remove the document from the queue and print it
            print("Printing", self.queue.dequeue())


printer_tasks = PrinterTasks()

# Add some documents to print
printer_tasks.add_document("Document 1")
# Output: Head: Document 1 Tail: Document 1

printer_tasks.add_document("Document 2")
# Output: Head: Document 1 Tail: Document 2

printer_tasks.add_document("Document 3")
# Output: Head: Document 1 Tail: Document 3

# Print all the documents in the queue
printer_tasks.print_documents()
# Expected Output:
# Printing Document 1
# Printing Document 2
# Printing Document 3

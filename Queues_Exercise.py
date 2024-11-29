#Question

#The following code shows you how to enqueue() an element into a queue and dequeue() an element from a queue using singly linked lists.
# Can you calculate the complexity of both methods using Big O Notation?

  def enqueue(self, data):
    new_node = Node(data)
    if self.head == None:
      self.head = new_node
      self.tail = new_node
    else:
      self.tail.next = new_node
      self.tail = new_node
  def dequeue(self):
    if self.head:
      current_node = self.head
      self.head = current_node.next
      current_node.next = None

      if self.head == None:
        self.tail = None
Answer: O(1)
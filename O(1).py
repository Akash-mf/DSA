def insert_at_beginning(self,data):
    new_node = Node(data)
    if self.head:
      new_node.next = self.head
      self.head = new_node
    else:
      self.tail = new_node
      self.head = new_node
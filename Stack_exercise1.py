#The following code shows you how to push() an element onto a stack and pop() an element from a stack using singly linked lists.
# Can you calculate the complexity of both methods using Big O Notation?

def push(self, data):
    new_node = Node(data)
    if self.top:
      new_node.next = self.top
    self.top = new_node
def pop(self):
    if self.top is None:
      return None
    else:
      popped_node = self.top
      self.top = self.top.next
      popped_node.next = None
      return popped_node.data

    #Answer : O(1)
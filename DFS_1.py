#Depth First Search (DFS)
#Printing book titles in alphabetical order

#This video taught you three ways of implementing the depth first search traversal into binary trees: in-order, pre-order, and post-order.

#In the following binary search tree, you have stored the titles of some books.

#Can you apply the in-order traversal so that the titles of the books appear alphabetically ordered?


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def in_order(self, current_node):
        # Check if current_node exists
        if current_node:
            # Call recursively with the appropriate half of the tree
            self.in_order(current_node.left_child)
            # Print the value of the current_node
            print(current_node.data)
            # Call recursively with the appropriate half of the tree
            self.in_order(current_node.right_child)


bst = CreateTree()
bst.in_order(bst.root)
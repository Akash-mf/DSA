#Inserting a node into a binary search tree

#In the video, you learned what binary search trees (BSTs) are and how to implement their main operations.

#In this exercise, you will implement a function to insert a node into a BST.

#The nodes contain titles of books, building a BST based on alphabetical order.

#This tree has been preloaded in the bst variable:

#bst = CreateTree()
#You can check if the node is correctly inserted with this code:

#bst.insert("Pride and Prejudice")
#print(search(bst, "Pride and Prejudice"))

class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left_child = left
        self.right_child = right

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        new_node = TreeNode(data)
        if self.root is None:
            self.root = new_node
            return
        else:
            current_node = self.root
            while True:
                if data < current_node.data:
                    if current_node.left_child is None:
                        current_node.left_child = new_node
                        return
                    else:
                        current_node = current_node.left_child
                elif data > current_node.data:
                    if current_node.right_child is None:
                        current_node.right_child = new_node
                        return
                    else:
                        current_node = current_node.right_child

def search(bst, search_value):
    current_node = bst.root
    while current_node:
        if search_value == current_node.data:
            return True
        elif search_value < current_node.data:
            current_node = current_node.left_child
        else:
            current_node = current_node.right_child
    return False

def CreateTree():
    dracula = TreeNode("Dracula")
    jane = TreeNode("Jane Eyre")
    moby = TreeNode("Moby Dick")
    vanity = TreeNode("Vanity")
    heidi = TreeNode("Heidi", dracula, jane)
    oliver = TreeNode("Oliver Twist", moby, vanity)
    root_node = TreeNode("Little women", heidi, oliver)
    bst = BinarySearchTree()
    bst.root = root_node
    return bst

# Example usage
bst = CreateTree()
bst.insert("Pride and Prejudice")
print(search(bst, "Pride and Prejudice"))  # Output: True

print(search(bst, "Jenkins"))  # Output: False

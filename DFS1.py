class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left_child = left
        self.right_child = right


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def in_order(self, current_node):
        # Check if current_node exists
        if current_node:
            # Traverse the left subtree
            self.in_order(current_node.left_child)
            # Print the value of the current_node
            print(current_node.data)
            # Traverse the right subtree
            self.in_order(current_node.right_child)


def CreateTree():
    # Create nodes representing book titles
    dracula = TreeNode("Dracula")
    jane = TreeNode("Jane Eyre")
    moby = TreeNode("Moby Dick")
    vanity = TreeNode("Vanity")
    heidi = TreeNode("Heidi", dracula, jane)
    oliver = TreeNode("Oliver Twist", moby, vanity)
    root_node = TreeNode("Little women", heidi, oliver)

    # Create and return the binary search tree
    bst = BinarySearchTree()
    bst.root = root_node
    return bst


# Create the BST and print book titles in alphabetical order
bst = CreateTree()
bst.in_order(bst.root)

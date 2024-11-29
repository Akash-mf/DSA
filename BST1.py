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

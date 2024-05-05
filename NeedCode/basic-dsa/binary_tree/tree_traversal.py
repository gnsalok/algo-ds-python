'''
Tree : A tree is "connected acyclic undirected graph". 

'''

class Node:
    def __init__(self, data):
        self.left = None
        self.data = data
        self.right = None

# In-order traversal 
def inorder(node):
    if node:
        inorder(node.left)
        print(node.data, end=" ")
        inorder(node.right)

# Pre-order traversal 
def preorder(node):
    if node:
        print(node.data, end=" ")
        inorder(node.left)
        inorder(node.right)

# Post-order traversal 
def postorder(node):
    if node:
        inorder(node.left)
        inorder(node.right)
        print(node.data, end=" ")

if __name__ == '__main__':
    root = Node(4)
    root.left = Node(3)
    root.right = Node(6)
    root.left.left = Node(2)
    root.right.right = Node(7)
    root.right.left = Node(5)

    inorder(root)

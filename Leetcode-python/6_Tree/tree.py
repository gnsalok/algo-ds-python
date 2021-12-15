'''
Tree : A tree in connected acyclic undirected graph. 


'''

class Node:
    def __init__(self, data):
        self.left = None
        self.data = data
        self.right = None

# In-order traversal 
def inorder(node):
    if(node is not None):
        inorder(node.left)
        print(node.data)
        inorder(node.right)

# Pre-order traversal 
def preorder(node):
    if(node is not None):
        print(node.data)
        inorder(node.left)
        inorder(node.right)

# post-order traversal 
def postorder(node):
    if(node is not None):
        inorder(node.left)
        inorder(node.right)
        print(node.data)





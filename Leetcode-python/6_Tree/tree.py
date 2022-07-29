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
    if(node is not None):
        inorder(node.left)
        print(node.data, end=" ")
        inorder(node.right)

# Pre-order traversal 
def preorder(node):
    if(node is not None):
        print(node.data, end=" ")
        inorder(node.left)
        inorder(node.right)

# Post-order traversal 
def postorder(node):
    if(node is not None):
        inorder(node.left)
        inorder(node.right)
        print(node.data, end=" ")

if __name__ == "__main__":
   root =  Node(5)
   root.left = Node(4)
   root.right = Node(5)
   root.left.left = Node(7)

   preorder(root)
   print("\n")

   inorder(root)
   print("\n")
   
   postorder(root) 
   print("\n")
   
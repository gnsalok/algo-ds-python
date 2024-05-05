class TreeNode:
    def __init__(self, val):
        self.val = val 
        self.left = None
        self.right = None 

def preorder(node):
    if node:
        print(node.val, end=" ")
        preorder(node.left)
        preorder(node.right)

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)


preorder(root)
print("\n")
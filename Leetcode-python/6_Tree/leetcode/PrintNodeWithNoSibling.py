
'''
program to find singles in a given binary tree

This is a typical tree traversal question. We start from the root and check if the node has one child,
if yes then print the only child of that node. 
If the node has both children, then recur for both the children.
'''

# A Binary Tree Node
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

# Function to print all non-root nodes that don't have
# a sibling
def printSingles(root):
    # Base Case
    if root is None:
        return 

    # If this is an internal node , recur for left
    # and right subtrees
    if root.left is not None and root.right is not None:
        printSingles(root.left)
        printSingles(root.right)

    # If left child is NULL, and right is not, print
    # right child and recur for right child
    elif root.right is not None:
        print(root.right.key)
        printSingles(root.right)

    # If right child is NULL and left is not, print
    # left child and recur for left child
    elif root.left is not None:
        print(root.left.key)
        printSingles(root.left)

# Driver program to test above function
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.right = Node(4)
root.right.left = Node(5)
root.right.left.left = Node(6)
printSingles(root)

'''
BST Operations:
- inserting : log(N)
- removing node : log(N)
'''

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# Insert a new node and return the root of the BST.
def insert(root, val):
    if not root:
        # Creating Node with value to later attach to left or right pointer of tree
        return TreeNode(val)
    
    if val > root.val:
        root.right = insert(root.right, val)
    elif val < root.val:
        root.left = insert(root.left, val)
    return root

# Return the minimum value node of the BST.
# Min value alway exist in leaf node (left side end node) 
def minValueNode(root):
    curr = root
    while curr and curr.left:
        curr = curr.left
    return curr

# Remove a node and return the root of the BST.
def remove(root, val):
    if not root:
        return None
    
    if val > root.val:
        root.right = remove(root.right, val)
    elif val < root.val:
        root.left = remove(root.left, val)
    else:
        # case 0 ->  if only right child exist; return right
        if not root.left:
            return root.right
        # case 0 -> if only left child exist; return right
        elif not root.right:
            return root.left
        # case 1 -> when both child exist
        else:
            minNode = minValueNode(root.right)
            root.val = minNode.val
            root.right = remove(root.right, minNode.val)
    return root


'''
BST Implementation
'''

class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

def insertNode(root, node):
    if(root is None):   # First Node insertion 
        root = node
        return 
    
    if(root.data < node.data):
        # Insert right side in the tree
        if(root.right is None):
            root.right = node
        else:
            insertNode(root.right, node)
    else:
        # Insert left side in the tree
        if(root.left is None):
            root.left = node
        else:
            insertNode(root.left, node)

# Searching key in the tree
def searchKey(node, key):
    if(node is not None): # if node exist then only print data
        print("Current Node", node.data)

    if(node is None):
        print("No node found!!")
        return None
    if(node.data == key):
        print("Node Found")
        return node
    if(node.data < key):
        return searchKey(node.right, key) #search right side of the tree
    return searchKey(node.left, key) #search left side of the tree
    

def minValueNode(node):
    while(node.left is not None):
        node = node.left
    return node

# Delete Node
def deleteNode(node, key):
    if(node is None):
        return None
    
    if(node.data < key):
        node.right = deleteNode(node.right, key)
    elif(node.data > key):
        node.left = deleteNode(node.left, key)
    else:  #key is found 
        if(node.left is None):
            temp = node.right 
            node = None
            return temp 
        elif(node.right is None):
            temp = node.left 
            node = None 
            return temp 
        temp = minValueNode(node.right)
        node.data = temp.data
        node.right = deleteNode(node.right, temp.data)
    return node
    

# Pre-order traversal of the tree     
def preorder(node):
    if(node is not None):
        print(node.data)
        preorder(node.left)
        preorder(node.right)


if __name__ == "__main__":
    #	         5
    #       /  	      \
    #     3	            7
    #   /   \        /     \
    #  2     4      6        8

    tree = Node(5) # Create root node

    insertNode(tree, Node(3))
    insertNode(tree, Node(2))
    insertNode(tree, Node(4))
    insertNode(tree, Node(7))
    insertNode(tree, Node(6))
    insertNode(tree, Node(8))


    print("*********Preorder************")
    # # 5 3 2 4 7 6 8
    preorder(tree)

    print("*********Searching************")
    searchKey(tree, 6)
   

    print("*********Deletion************")
    deleteNode(tree,7)
    preorder(tree)

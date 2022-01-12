'''
Code a Binary Tree

'''

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def inorder(node):
    if(node is None):
        return 
    else:
        inorder(node.left)
        print(node.val)
        inorder(node.right)



if __name__ == "__main__":
    root = Node(5)
    root.left = Node(4)
    root.right = Node(6)
    root.left.left = Node(9)
    root.right.right = Node(10)

    inorder(root)   # 




    
        
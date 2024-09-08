
'''
Level Order using Recursion 
'''

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None 


def printLevelOrder(root):
    h = height(root)
    print("height", h)
    for i in range(0, h):
        printCurrentLevel(root, i)


def printCurrentLevel(root, level):
    if root is None:
        return
    if level == 0:
        print(root.val, end=" ")
    elif level > 0:
        printCurrentLevel(root.left, level-1) 
        printCurrentLevel(root.right, level-1)

def height(root):
    if(root is None):
        return 0
    else:
        lsh = height(root.left)
        rsh = height(root.right)


        if(lsh > rsh):
            return lsh + 1
        return rsh + 1
     
        
if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    printLevelOrder(root)
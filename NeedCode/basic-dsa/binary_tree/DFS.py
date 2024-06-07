'''
DFS in binary search tree 

Note:-
Using Inorder, preorder and postorder traversal recursively are the Depth-first seach examples ;
you can use any based on your requirement.

T.C. : O(N)
'''

# Tree Node
class Node:
    def __init__(self, val):
        self.val = val 
        self.left = None
        self.right = None

## RECURSIVE : It will give the sorted array output 
def inorder(node):
    if node:
        inorder(node.left)
        print(node.val, end=" ")
        inorder(node.right)

## ITERATIVELY :  inorder traversal
def DFS(root):
    stack = []
    result = []
    cur = root

    while cur or stack:
        if cur:
            stack.append(cur)
            cur = cur.left
        else:
            cur = stack.pop()
            result.append(cur.val)
            cur = cur.right
    return result

        

if __name__ == '__main__':
    root = Node(4)
    root.left = Node(3)
    root.right = Node(6)
    root.left.left = Node(2)
    root.right.right = Node(7)
    root.right.left = Node(5)

    # In order traversal
    print(DFS(root))
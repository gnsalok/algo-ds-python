

'''
1,2,3,4 

        3
    2       4
1
'''


class Node:
    def __init__(self, d):
        self.data = d
        self.left = None
        self.right = None

# function to convert sorted array in BST


def sortedArrayToBST(arr):
    if not arr:
        return None
    mid = (len(arr))//2
    root = Node(arr[mid])
    root.left = sortedArrayToBST(arr[:mid])
    root.right = sortedArrayToBST(arr[mid+1:])
    return root

# Utility function of to print tree in preorder


def preOrder(node):
    if not node:
        return
    print(node.data)
    preOrder(node.left)
    preOrder(node.right)


if __name__ == "__main__":
    arr = [1, 2, 3, 4]
    root = sortedArrayToBST(arr)
    print("Preorder traversal of constructed BST")
    preOrder(root)

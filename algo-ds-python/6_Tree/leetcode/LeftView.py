'''
Print Left View of Binary Tree
'''

class newNode:
    # Construct to create a newNode
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

def printLeftView(root):
    if (root is None):
        return

    queue = []
    queue.append(root)

    while(queue):
        # number of nodes at current level
        n = len(queue)
        # Traverse all nodes of current level
        for i in range(0, n):
            temp = queue[0]
            queue.pop(0)

            # Print the left most element
            # at the level
            if (i == 0):
                print(temp.data)

            # Add left node to queue
            if (temp.left is not None):
                queue.append(temp.left)

            # Add right node to queue
            if (temp.right is not None):
                queue.append(temp.right)




if __name__ == '__main__':
    root = newNode(10)
    root.left = newNode(2)
    root.right = newNode(3)
    root.left.left = newNode(7)
    root.left.right = newNode(8)
    root.right.right = newNode(15)
    root.right.left = newNode(12)
    root.right.right.left = newNode(14)
    printLeftView(root)   # OUTPUT : 10 2 7 14 
'''
BFS / Level Order Traversal
'''

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def bfs(root):
    queue = []

    if root:
        queue.append(root)
    
    level = 0
    while len(queue) > 0:
        for i in range(len(queue)):
            curr = queue.pop(0)
            print(curr.val)
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
        level += 1


if __name__ == '__main__':
    root = Node(4)
    root.left = Node(3)
    root.right = Node(6)
    root.left.left = Node(2)
    root.right.right = Node(7)
    root.right.left = Node(5)

    # bfs
    bfs(root)
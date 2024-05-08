'''
DFS in binary search tree 

T.C. : O(N)
'''

# Tree Node
class Node:
    def __init__(self, val):
        self.val = val 
        self.left = None
        self.right = None

## ITERATIVELY : 
def DFS(root):
    # inner function
    def getPathSum(node, pathSum, curSum):
        if not node:
            return False

        curSum += node.val
        # at leaf node
        if not node.left and not node.right:
            pathSum.append(curSum)

        
        getPathSum(node.left, pathSum, curSum)
        getPathSum(node.right, pathSum, curSum)

        return pathSum
    
    return getPathSum(root, [], 0)
    

if __name__ == '__main__':
    root = Node(4)
    root.left = Node(3)
    root.right = Node(6)
    root.left.left = Node(2)
    root.right.right = Node(7)
    root.right.left = Node(5)

    # inorderInteratively(root)
    print(DFS(root))

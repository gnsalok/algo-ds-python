'''
Write Code for Level Order Travesal using Iterative Method. 
'''

# Tree Node
class Node:
    def __init__(self, val):
        self.val = val 
        self.left = None
        self.right = None


# Iterative method using Queue
# Time O(N) | Space : O(N)
def printLeveOrderTraversal(node):
    queue = []
    queue.append(node)

    while(queue):
       curNode = queue.pop(0)
       print(curNode.val, end=" ")

       if(curNode.left is not None):
           queue.append(curNode.left)
        
       if(curNode.right is not None):
           queue.append(curNode.right)


# Recursive Method to show level order traversal





if __name__ == '__main__':
    root = Node(10)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(7)
    root.left.right = Node(8)
    root.right.right = Node(15)
    root.right.left = Node(12)
    
    printLeveOrderTraversal(root)   # OUTPUT : 10,2,3,7,8,12,15
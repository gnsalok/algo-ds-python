'''
TC : O (N)
SC : O (N)


Write a function to connect all the adjacent nodes at the same level in a binary tree. 
Structure of the given Binary Tree node is like following. 
'''

class newnode:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None
        self.next = None

def connect(root):
        if not root:
            return root

        q = []
        q.append(root)
        
        while(q):
            size = len(q)
            prev = None  # to keep track of prev node
            
            while(size > 0):
                currentNode = q.pop(0)
                
                if(prev is not None):
                    prev.next = currentNode
                prev = currentNode
                
                if(currentNode.left is not None):
                    q.append(currentNode.left)
            
                if(currentNode.right is not None):
                    q.append(currentNode.right)
                size -= 1
        return root
        

# Driver Code
if __name__ == '__main__':
 
    # Constructed binary tree is
    #      10
    #     / \
    # 8     2
    # /
    # 3
    root = newnode(10)
    root.left = newnode(8)
    root.right = newnode(2)
    root.left.left = newnode(3)
 
    # Populates next pointer in all nodes
    connect(root)
 
    # Let us check the values of next pointers
    print("Following are populated next",
          "pointers in the tree (-1 is printed",
          "if there is no next)")
    print("next of", root.data, "is ", end="")
    if root.next:
        print(root.next.data)
    else:
        print(-1)
    print("next of", root.left.data, "is ", end="")
    if root.left.next:
        print(root.left.next.data)
    else:
        print(-1)
    print("next of", root.right.data, "is ", end="")
    if root.right.next:
        print(root.right.next.data)
    else:
        print(-1)
    print("next of", root.left.left.data, "is ", end="")
    if root.left.left.next:
        print(root.left.left.next.data)
    else:
        print(-1)

# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right



def inorder(root, nodeValues):
	if(root is None):
		return 
	
	inorder(root.left,nodeValues)
	nodeValues.append(root.value)
	inorder(root.right,nodeValues)
	
	

def findKthSmallestValueInBst(root, k):
    nodeValues = []
    if(root is None):
        return 
    inorder(root, nodeValues)
    print("Node values",nodeValues)
    return nodeValues[k-1]



if __name__ == "__main__":
    root =  BST(15)
    root.left = BST(5)
    root.left.left = BST(2)
    root.left.left.left = BST(1)
    root.left.left.right = BST(3)
    root.left.right = BST(5)
    root.right = BST(20)
    root.right.left = BST(17)
    root.right.right = BST(22)
    k = 3

    result = findKthSmallestValueInBst(root, k)
    print("Kth smallest value :", result)

	

class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def branchSums(root):
	sums = []
	calculateBranchSum(root, 0, sums)
	return sums
	
def calculateBranchSum(node, runningSum, sums):
	if(node is None): #Base Condition 
		return   
	
	newRunningSum = runningSum + node.value # Add logic 
	
	if(node.left is None and node.right is None): # At the leaf Node
		sums.append(newRunningSum)
		
	calculateBranchSum(node.left, newRunningSum, sums)
	calculateBranchSum(node.right, newRunningSum, sums)
		
	
b = BinaryTree(1)
b.left = BinaryTree(2)
b.right = BinaryTree(3)
b.left.left =  BinaryTree(4)
b.left.right = BinaryTree(5)
b.right.right = BinaryTree(7)
b.right.left = BinaryTree(6)
b.left.right.left = BinaryTree(10)
b.left.left.left =  BinaryTree(8)
b.left.left.right =  BinaryTree(9)


ans = branchSums(b)
print(ans)



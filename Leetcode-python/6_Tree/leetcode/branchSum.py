'''
It uses DFS approach and if it finds left and right node as None, it will append the Sum.
'''
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
		
	
		
	
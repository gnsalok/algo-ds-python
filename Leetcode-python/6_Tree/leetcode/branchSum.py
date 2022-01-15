def branchSums(root):
	sums = []
	calculateBranchSum(root, 0, sums)
	return sums
	
def calculateBranchSum(node, runningSum, sums):
	if(node is None): #Base Condition 
		return   
	
	newRunningSum = runningSum + node.value # Summing value at each node
	
	if(node.left is None and node.right is None): # When at the leaf node
		sums.append(newRunningSum)
		
	calculateBranchSum(node.left, newRunningSum, sums)
	calculateBranchSum(node.right, newRunningSum, sums)
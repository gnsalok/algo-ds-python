'''
Maximum sum subarray using Kadan's algorithm.
'''
# Time O(N), Space O(1)
def kadanesAlgorithm(arr):
	maxEndingHere = arr[0]
	maxSoFor = arr[0]
	
	for i in range(1, len(arr)):
		num = arr[i]
		maxEndingHere = max(num, maxEndingHere + num)
		maxSoFor = max(maxSoFor, maxEndingHere)
	return maxSoFor
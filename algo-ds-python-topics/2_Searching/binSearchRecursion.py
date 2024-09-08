def binarySearch(arr, target):
	return binarySearchHelper(arr, target, 0, len(arr)-1)

def binarySearchHelper(arr, tar, left, right):
	if(left > right):
		return -1 
	
	mid = (left + right) // 2
	potentialMatch = arr[mid]
	
	if(tar == potentialMatch):
		return mid  # return the index 
 
	elif(tar < potentialMatch): # check left 
		return binarySearchHelper(arr, tar, left, mid-1)

	else: # check right 
		return binarySearchHelper(arr, tar, mid + 1, right)
		


list = [1,2,3,4,5]
print(binarySearch(list, 4))   # ans : 3
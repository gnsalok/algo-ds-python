def bubbleSort(array):
	isSorted = False
	
	while(not isSorted):
		isSorted = True
		for i in range(len(array) - 1):
			if(array[i] > array[i+1]):
				swap(i, i+1, array)
				isSorted = False
	return array 

def swap(i, j, arr):
	arr[i], arr[j] = arr[j], arr[i]
				
				



arr = [8, 5, 2, 9, 5, 6, 3]
ans = bubbleSort(arr)
print(ans)
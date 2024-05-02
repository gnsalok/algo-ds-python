'''
Bucket Sort Implementation 

- Bucket sort works well when the dataset to be sorted has values within a specific range.

'''

def bucketSort(arr):
    counts = [0,0,0]

    for n in arr:
        counts[n] += 1
    
    k=0 # keep track of main arr idx
    for i in range(len(counts)):
        for j in range(counts[i]):
            arr[k] = i
            k += 1
    return arr



input = [2,1,2,0,0,2]
result = bucketSort(input)
print(result)
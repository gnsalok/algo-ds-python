'''
# Merge Sort Simplify with Python

TC : Log N (best and avg case) ; Worst Case : N^2
SC : O(N)

'''

def merge_sort(data):
    if len(data) <= 1:
        return data
    
    mid = len(data) // 2
    left_half = data[:mid]
    right_half =  data[mid:]

    # recursively sort left and right half
    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)

    # merge the sorted half
    merged_data = []
    i = 0
    j = 0

    while i < len(left_sorted) and j < len(right_sorted):
        if left_sorted[i] <= right_sorted[j]:
            merged_data.append(left_sorted[i])
            i += 1
        else:
            merged_data.append(right_sorted[j])
            j += 1
    
    # append the remaining element from either half
    merged_data += left_sorted[i:]
    merged_data += right_sorted[j:]

    return merged_data




input = [3,2,4,1,6]
sortedArr = merge_sort(input)
print(sortedArr)
# '''

# Google Interview question
# find pair of no. that add up to certain target.
# Ex :
# arr = [1,2,3,9] , target = 10 ; Result : {9,1}

# '''




# def getPairSum(arr, target):
#     pairs = []
#     for i in range(0, len(arr)):
#         for j in range(1, len(arr)):
#             sum = arr[i] + arr[j]
#             if(sum == target):
#                 pairs.append([arr[i], arr[j]])
#     if(pairs):
#         return pairs
#     return -1


# n log n solution 
# sort the array and apply high low two pointer technique

def getPairSum(arr, target):
    arr.sort()
    low = 0
    hi = len(arr)-1

    while(low < hi):
        sum = arr[low] + arr[hi]
        if(sum == target):
           return True
        elif(sum < target):
            low += 1
        elif(sum > target):
            hi -= 1
    return False
    




arr = [1,2,9,3]
target = 10

result = getPairSum(arr, target)
print(result)
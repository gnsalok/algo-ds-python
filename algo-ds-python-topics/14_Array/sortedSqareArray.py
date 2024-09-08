

'''
Approach-1
TC : O(n log n) (calculate square & sorting)
SP : O(n)
'''
# def sortedSquaredArray(array):
#     output = []
#     for i in array:
#         square = i * i
#         output.append(square)
#     output.sort()
#     return output


'''
Approach-2
Use the fact that Input array is sorted

TC : O(n) 
SP : O(n)
'''

def sortedSquaredArray(array):
    size = len(arr)
    output = [0] * size
    start = 0
    end = size - 1 

    for i in reversed(range(size)):
        if(abs(arr[start]) < abs(arr[end])):
            output[i] = arr[end] * arr[end]
            end -= 1
        else:
            output[i] = arr[start] * arr[start]
            start += 1
    return output



arr = [-7,-5,-4,3,6,8,9]
ans = sortedSquaredArray(arr)
print(ans)
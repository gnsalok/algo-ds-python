# def twoSum(nums, target):
#     seen = {}
#     for i, n in enumerate(nums):
#         print("i and n",i,n)
#         comp = target - n
#         if comp in seen:
#             print("comp is, Got indexes",comp,seen)
#             return [seen[comp], i]
#         else:
#             seen[n] = i
#             print("upating dict", seen)
#         print('seen is', seen)
            

def twoSum(arr, target):
    seen = {}
    for i,n in enumerate(arr):
        comp = target - n
        if comp in seen:
            return [seen[comp],i]
        else:
            seen[n]=i

            
#Brute force approach 

# def twoSum(arr, target):
#     n = len(arr)
#     print(n)
#     for i in range(0,n):
#         for j in range(i+1, n):
#             comp = target - arr[i]
#             if arr[j] == comp:
#                 return [i, j]
#     return "Not found!"

            


list = [2,11,7,15]
target = 9

res = twoSum(list, target)
print(res)
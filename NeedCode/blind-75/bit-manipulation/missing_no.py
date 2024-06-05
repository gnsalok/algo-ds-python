'''

https://leetcode.com/problems/missing-number/description/

Find missing no. in array.
Formula:
missing number = (sum of N no.) - (sum of array ele)
'''

def missingNo(arr):
    n = len(arr)
    sumOfArr = 0

    for i in range(0,n):
        sumOfArr = sumOfArr + arr[i]
  
    sumOfNno = (n * (n+1)) // 2
    missNumber = sumOfNno - sumOfArr

    return missNumber


arr = [3,0,1]
print(missingNo(arr))

'''
Two sum
'''

def twoSum(arr, sum):
    map = {}

    for i in range(0, len(arr)):
        x = arr[i]
        goal = sum - x

        if goal in map:
            return True
        else:
            map[x] = i

if __name__ == "__main__":
    arr = [5,7,1,2,8,4,3]
    sum = 12    

    value = twoSum(arr, sum)
    print(value)
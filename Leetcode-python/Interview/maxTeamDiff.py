'''
skill = 3, 4, 3, 1, 6, 5, teamSize = 3, maxDiff = 2: At most, 2 teams can be formed: 3, 3, 1 and 4, 6, 5. 
The difference between the maximum and minimum skill levels is 2 in each case, which does not exceed the threshold value of 2.
'''

from typing import List

def teams(arr: List[int], size: int, diff: int) -> int:
    n = len(arr)
    res = 0

    for i in range(0,n):
        ll , ls = 0, 0
        rl , rs = 0, 0
        for j in range(0,i):
            if(arr[j] > arr[i]):
                ll += 1
            if(arr[j] < arr[i]):
                ls += 1
        for j in range(i+1, n):
            if(arr[j]>arr[i]):
                rl += 1
            if(arr[j] < arr[i]):
                rs += 1
        res += (ls * rl) + (rs * ll)
    return res


if __name__ == "__main__":
    skill = [3, 4, 3, 1, 6, 5]
    result = teams(skill, 3, 2)
    print(result)
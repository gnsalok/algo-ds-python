
'''
1,2,3,4,5,6... n-1 , n

TRUST --> Recursion 1.... (n-1) + n

'''

def sum(n):
    if(n == 0):
        return 0

    return sum(n-1) + n



result = sum(10)
print(result)
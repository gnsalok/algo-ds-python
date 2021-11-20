
'''
1,2,3,4,5,6... n-1 , n

TRUST --> Recursion 1.... (n-1) + n

'''



def sum(n):
    if(n == 1):
        return 1
    
    return sum(n-1) + n


print(sum(10))

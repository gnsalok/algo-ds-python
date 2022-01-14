'''
1,2,3,4,5 =  10 + 5 = 15

'''

def sum(n):
    if(n == 0):
        return 0
    else:
        return sum(n-1) + n


print(sum(5))
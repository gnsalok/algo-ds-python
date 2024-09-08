'''
TRUST you function 


[1 + 2 + 3 + ....... + n-1 ]  +   n
'''



def sumN(n):

    if(n == 0):
        return 0

    left_part = sumN(n-1)
    print("left part = ",left_part, " + n=", n)
    return left_part + n



print(sumN(10))
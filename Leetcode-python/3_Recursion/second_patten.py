'''

1 2 3 ... n
1 2
1
1 2
1 2 3 ... n

'''
# TRUST the function
def pattern(n):

    if(n == 1):
        print("1\n")
        return 

    for i in range(0, n):
        print(i+1, end=" ")
    print("\n")
        
    pattern(n-1)

    for i in range(0, n):
        print(i+1, end=" ")
    print("\n")

    
pattern(10)
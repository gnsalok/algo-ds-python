'''

1 2 3 ... n
1 2
1
1 2
1 2 3 ... n

'''
# TRUST the function
def pattern(n):

    # Base case should 1 here
    if(n == 1):
        print("1\n")
        return 

    #Upper Pattern 
    for i in range(0, n):
        print(i+1, end=" ")
    print("\n")
        
    pattern(n-1)

    # Lower Pattern 
    for i in range(0, n):
        print(i+1, end=" ")
    print("\n")

    
pattern(5)

'''
1,2,3,4,5,6... n-1 , n

TRUST --> Recursion 1.... (n-1) + n




'''



def hello(n):

    if(n == 1):
        print("1")
        return 
    print(n)     # End to Top 
    hello(n-1)
    print(n)     # Top to End






hello(10)


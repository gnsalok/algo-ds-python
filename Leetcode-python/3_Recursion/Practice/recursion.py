'''
Master Recursion 
- Trust your function  / Recursive Leap of Faith
- Make sure of base case

if(n == 0) : STOP 
PRINT: 

hello - n
hello - (n-1)
hello - 8
.
.
.
hello - 1
'''

# # Trusting my function
# def print_hello(n):
#     if(n == 0): #Stopping Case / Base Case
#         return  # Stopped
#     print(f"Hello - {n}")
#     print_hello(n-1)


# TRUST the function
'''
INPUT - 10 

Output :
if (n == 0): stop  # Base case

PRINT : 
hello - 1
hello - 2
hello - 3
.
.
.
hello - (n-1)
hello - n
'''


def print_hello(n):
    if(n == 0):
        return
    print_hello(n-1) 
    print(f"Hello - {n} ")
    


if __name__ == "__main__":
   print_hello(10)






'''

5! = 5 * fact(5-1)

Base case :
1! = 1
0! = 1

Make sure always to take care of base case 
'''


def fact(n):
    if n <= 1:
        return 1
    return n * fact(n-1)


output = fact(5)
print(output)

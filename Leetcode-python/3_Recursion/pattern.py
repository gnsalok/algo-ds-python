'''
1
1 2
1 2 3
1 2 3 4
1 2  3 4... n

'''


def print_pattern(n):
    if(n == 0):
        return 

    print_pattern(n - 1)  # TRUST 

    for i in range(0, n):
        print(i+1, end=" ")
    print("\n")

    

print_pattern(6)
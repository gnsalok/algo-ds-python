'''

# Array and Find sum of element
arr = [2,2,3]
res = sum(arr[i] for i in range(len(arr)))
print(res)


# Create 2D array  :: [  [col] * row ]

matrix = [[0 for x in range(4)]
        for y in range(3)]
print(matrix)
matrix[0][1] = 2
print(matrix)

# start, stop, hop
for i in range(1, 11, 2):
    print(i, end=" ")  # 1 3 5 7 9 

# print in reverse
for i in range(10,-1,-1):
    print(i, end=" ") # 10 9 8 7 6 5 4 3 2 1 0 

#List manipulation

arr = [1,2,3,4,6,7,8,9,10]
print([str(x) for x in arr])

# use-case
ll = [x for x in arr if(x%2)]
print(ll)

#print array backward
arr= [1,2,3,4,5,6]
for i in range(len(arr)-1, -1, -1):
    print(arr[i])


# Formatting print strings
n = 12
print("Hello {0} {1}".format(n, n+1))
print(f"Hello {n}")
print("Hello %d"%n)

'''




    








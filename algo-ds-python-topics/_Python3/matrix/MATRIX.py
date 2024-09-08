'''
In Python :

While define >> col and row 
While Iterating ?? row and col

[[[]for x in range(row)] for y in range(col)]
'''


matrix = [[[] for col in range(5)]
             for row in range(3)]

print(matrix)

for i in range(3): # row 
    for j in range(5): # col
        print(matrix[i][j])

# ------ 
## This will also work -- Dry Run
# 2-D lists / Matrix
# Mat start with 0,0
arr = [[0] * 4 for i in range(4)]
print(arr)
print(arr[0][0], arr[3][3])

# This won't work
# arr = [[0] * 4] * 4

# 3 * 4 matrix 
mat = [[0] * 4 for i in range(3)]
print(mat)







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







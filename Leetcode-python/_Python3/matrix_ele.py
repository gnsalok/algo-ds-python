'''
- Working with Matrix in Python3. 
Syntax : [[0 for x in range(col)]
            for y in range(row)]


for i in range(2): # row 
    for j in range(3): #col


'''


matrix = [[1 for x  in range(3)]
           for y in range(2)]


print(matrix)

sumFirstrow = 0

matrix[0][1] = 5

for i in range(2): # row 
    for j in range(3): #col
        if(i == 1):
            break

        sumFirstrow += matrix[i][j]
        print(matrix[i][j])
        

print("Sum of first row :", sumFirstrow)

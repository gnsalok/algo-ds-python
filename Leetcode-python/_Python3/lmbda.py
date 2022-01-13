'''
Lambda function in python 
'''

cube = lambda y : y*y*y
print(cube(2))


tables = [lambda x = x: x*10 for x in range(1, 11)]
for table in tables:
    print(table())
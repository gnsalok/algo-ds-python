'''
Problem :
# Get all substrings of string 
# Using list comprehension + string slicing 

Author : Alok Tripathi
'''

test_str = "Alok"

print("The original string is : " + str(test_str)) 

for i in range(len(test_str)):
	for j in range(i + 1, len(test_str) + 1):  #from 1 to str(len+1)
            print(list(test_str[i: j]))




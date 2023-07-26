'''
Left shift 
-------------------
7 = 0111 
Left shift by 1 :  1110  = 14

7 = 0111
left shift 2  : 011100 = 16 +8 + 4 = 28
'''
# Left Shift 

x = 7
x = x << 2
print(x)  # ans is 14



'''
Right shift 
-------------------
7 = 0111 
Right shift by 1 : 0110 = 

7 = 0111
Right shift 2  : 0001 = 16 + 8 + 4 = 28
'''

# Right Shift
x = 7
x = x >> 2
print(x)  # ans is 14


'''
XOR  
-------------------
8 4 2 1
-------------
A =  0100
B =  0010
----------------
XOR = 0110 = 6

'''

a = 4
b = 2
print(a^b)

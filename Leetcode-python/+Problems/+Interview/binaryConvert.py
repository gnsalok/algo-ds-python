'''
Convert no. in to binary.

9 => 1001 

'''
from typing import List

def getBinary(N):
    if(N > 1):
        # print(N)
        getBinary(N // 2)
    print(N%2, end = ' ')
    
   

getBinary(8)







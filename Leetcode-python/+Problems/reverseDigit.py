'''
max Int range in python 

[-2**31] to [(2**31) -1]

'''

class Solution:
    def reverse(self, x: int) -> int:
        isNegative = False
        reverseDigit = 0
        
        if(x < 0):
            isNegative = True
            x = -1 * x
        
        while(x > 0):
            lastDigit = x % 10
            reverseDigit =  reverseDigit * 10 + lastDigit 
            x = x//10
            
            
        if(isNegative):
            reverseDigit = -1 * reverseDigit
        
        if(reverseDigit < -2 ** 31 or reverseDigit > (2 ** 31) - 1 ):
            return 0
        return reverseDigit


if __name__ == "__main__":
    sl = Solution()
    result = sl.reverse(1234)
    print(result)
    
    
    
  
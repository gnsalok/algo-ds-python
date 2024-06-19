
"""
Link : https://www.youtube.com/watch?v=bNvIQI2wAjk

Problem : Design string to encode a string -> send encoded string over network -> decode back to original string.

input = ["lint", "code", "love", "you"]
output = ["lint", "code", "love", "you"]

Approach :
->One possible encode method is : 4#lint4#code4#love4#you  ; meaning you can count 4 char after #. 
so that you can keep track on origin string.

"""



class Solution:

    '''
    encode a string to a list of single string
    '''

    def encode(self, strs):
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s   
        return res
    
    '''
    decode string and return list of strings
    
    '''
    def decode(self, str):
        res, i = [], 0

        # decoding each string
        while i < len(str):
            j=i

            while(str[j]) != "#":
                j += 1

            # it will return the length of string from the encoded string ; 4#lint -> 4
            length =  int(str[i:j])

            res.append(str[j+1 : j+1+length])
            
            # repeat the same for the next string ; 4#code
            i = j + 1 + length

        return res



sl = Solution()
input = ["lint", "code", "love", "you"]

# get the encoded string with 4#lint etc.....
encodedStr = sl.encode(input)

# decoded str
decodedStr = sl.decode(encodedStr)

print(decodedStr)









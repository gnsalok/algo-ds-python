'''

This problem is using Binary search using range. Where you will not given arr and target.

https://leetcode.com/problems/guess-number-higher-or-lower/description/

READ the problem statement and write logic accordingly.

'''

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        l, r = 1 , n
       
        while(l <= r):
            mid = (l+r) // 2
            guess = guess(mid)
        
            if guess > 0 : # condition: if guess is lower then pick -> return -1
                l = mid + 1 
            elif guess < 0 : # condition: if guess is higher then pick -> return -1
                r = mid - 1
            else:
                return mid 
        
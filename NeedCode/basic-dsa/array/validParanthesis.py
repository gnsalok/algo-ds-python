'''

https://leetcode.com/problems/valid-parentheses/

Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

'''

class Solution:
    '''
    - Make all the closing brackets as key in the map 
    - Maintain a stack to keep track of top bracket (ie. opening bracket). 
    - If closing bracket it gets, and match with similar oping bracket, pop the the element from stack.
    - return True if stack is empty else, False.
    '''
    
    def isValid(self, s: str) -> bool:
        closeToOpen = {")":"(", "}":"{", "]":"["}
        stack = []

        for br in s:
            if br in closeToOpen:
                if stack and stack[-1] == closeToOpen[br]:
                    stack.pop()
                else:
                    return False 
            else:
                stack.append(br)

        return len(stack) == 0


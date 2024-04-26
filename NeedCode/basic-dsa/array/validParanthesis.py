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


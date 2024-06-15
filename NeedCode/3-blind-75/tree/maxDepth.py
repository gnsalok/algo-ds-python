
'''
https://leetcode.com/problems/maximum-depth-of-binary-tree/
'''

# DFS 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        
        
        
        
# BFS
from collections import deque

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        queue = []
        queue.append(root)
        level = 0

        while queue:
            for i in range(len(queue)): # to count value at each level
                cur = queue.pop(0)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            level += 1
        return level
                


        
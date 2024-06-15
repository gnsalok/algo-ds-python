'''
https://leetcode.com/problems/same-tree/description/
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        # Base cases:
        if not p and not q:  # Both trees are empty, considered identical
            return True
        if not p or not q:  # One tree is empty, not identical
            return False

        return True if p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right) else False
'''
Longest Univalue Path : https://leetcode.com/problems/longest-univalue-path/submissions/1625600743/


'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        self.max_lup = 0

        def dfs(node):
            if not node:
                return 0

            left_path = right_path = 0
            left = dfs(node.left)
            right = dfs(node.right)

            if node.left and node.left.val == node.val:
                left_path = left + 1
            if node.right and node.right.val == node.val:
                right_path = right + 1

            self.max_lup = max(self.max_lup, left_path + right_path)

            return max(left_path, right_path)

        dfs(root)
        return self.max_lup
        
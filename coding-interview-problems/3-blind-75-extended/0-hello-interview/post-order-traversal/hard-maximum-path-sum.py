'''

Problem : Maximum Path Sum
https://leetcode.com/problems/binary-tree-maximum-path-sum/
'''

from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = float('-inf')

        def dfs(node):
            if not node:
                return 0

            left_sum = max(dfs(node.left), 0)
            right_sum = max(dfs(node.right), 0)

            current_sum = node.val + left_sum + right_sum
            self.max_sum = max(self.max_sum, current_sum)

            return node.val + max(left_sum, right_sum)

        dfs(root)
        return self.max_sum
    

# Example usage:
if __name__ == "__main__":
    # Create a sample binary tree
    root = TreeNode(-10)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    # Calculate the maximum path sum of the binary tree
    solution = Solution()
    print("Maximum Path Sum of the binary tree:", solution.maxPathSum(root))  # Output: 42
    
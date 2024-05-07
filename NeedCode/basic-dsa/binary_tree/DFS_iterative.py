# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root:  # Handle empty tree case
            return None

        n = 0
        stack = [root]
        cur = root
        while cur  or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            # when we hit the NULL case, pop from stack
            cur = stack.pop()
            n += 1
            if n == k:
                return cur.val
            cur = cur.right
        
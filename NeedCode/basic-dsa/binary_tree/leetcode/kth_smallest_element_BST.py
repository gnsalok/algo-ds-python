# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # do inorder traversal and return if n == k
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        n = 0
        stack = []
        cur = root
        while cur and stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            # when we hit the NULL case, pop from stack
            # pop meaning visiting that node
            # - Check if that node is first kth smallest
            cur = stack.pop()
            n += 1 # each node processing just adding to a count and if it reaches to K, return it.
            if n == k:
                return cur.val
            cur = cur.right

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        cur = root
        stack = [(cur, False)]
        output= []

        while stack:
            cur, visited = stack.pop()
            if cur:
                if visited:
                    output.append(cur.val)
                else:
                    stack.append((cur,True))
                    stack.append((cur.right, False)) # first add right then left : <right> <left> <root>
                    stack.append((cur.left, False))
        return output
'''
https://leetcode.com/problems/binary-tree-right-side-view/description/
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        queue = [root]
        result = []

        while len(queue) > 0:
            qLengthAtLevel = len(queue)
            for i in range(qLengthAtLevel):
                cur = queue.pop(0)

                if i == qLengthAtLevel - 1:
                    result.append(cur.val)

                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)

        return result
'''
https://leetcode.com/problems/binary-tree-level-order-traversal/description/

'''
import collections

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = collections.deque()
        q.append(root)
        result = []

        while q:
            elementsAtEachLevel = []
            for i in range(len(q)):
                cur = q.popleft()
                if cur:
                    elementsAtEachLevel.append(cur.val)
                    q.append(cur.left)
                    q.append(cur.right)
            if elementsAtEachLevel:
                result.append(elementsAtEachLevel)
        return result
                





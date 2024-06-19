
'''
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/description/
Lowest Common Ancestor of a Binary Search Tree


'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''
Cases: 
1. if both p and q are less than root -> look in to left substree
2. if both p and q are greater than root -> look in to right substree
3. if 1 and 2, not satisfy it means there is split of p and q in left and right subtree. So return the cur as it will be LCS.
4. There can be a case where root can be equal to p or q. In that case also return root. As root is LCS of itself. 
    There is no way you can get CLS of root in left and right subtrees.

'''
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        cur = root 

        while cur:
            if p.val > cur.val and q.val > cur.val:
                cur = cur.right
            elif p.val < cur.val and q.val < cur.val:
                cur = cur.left
            else:
                return cur




        
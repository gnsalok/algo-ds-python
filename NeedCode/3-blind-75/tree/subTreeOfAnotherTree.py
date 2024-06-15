'''
https://leetcode.com/problems/subtree-of-another-tree/description/
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        
        if not subRoot:
            return True

        if self.isSameTree(root, subRoot):
            return True

        return (self.isSubtree(root.left, subRoot) or
                self.isSubtree(root.right, subRoot))


    def isSameTree(self, n1, n2):
        if not n1 and not n2:
            return True
        
        if n1 and n2 and n1.val == n2.val:
            return (self.isSameTree(n1.left, n2.left) and 
                    self.isSameTree(n1.right, n2.right))
        return False



        
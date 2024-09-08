# Definition for a binary tree node.
class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
class Solution:
    def isMirror(self, t1, t2):
        if(t1 is None and t2 is None):
            return True
        
        if(t1 is None or t2 is None):
            return False
        
        return (t1.val == t2.val) and self.isMirror(t1.left, t2.right) and self.isMirror(t1.right, t2.left)
        
        
    def isSymmetric(self, root) -> bool:
        return self.isMirror(root, root)
        
'''

        1
      /   \  
    2      2
   /  \    / \   
  4    5  5   4

'''

root = TreeNode(1)

root.left = TreeNode(2)
root.right = TreeNode(2)

root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

root.right.left = TreeNode(5)
root.right.right = TreeNode(4)



sl = Solution()
isSymmetric = sl.isSymmetric(root)
print("Is tree mirrored : ", isSymmetric)
         

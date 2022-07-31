# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

'''
max depth = height of tree + 1 ( {no. of edges on the longest downward path b/t root & leaf} + 1 )

        1
      /   \  
    2
   / \      3
  4   5
 /
6  

height = 3
maxDepth = 3 + 1 = 4

Generic Solution = 1 + max(leftSubtreeHeight, rightSubtreeHeight)

TC : Recursive : O(Height(N)) ; Level Order : O(N)
SP : O(N)
'''
class Solution:
    def maxDepth(self, root) -> int:
        if(root is None):
            return 0
        
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)

        print(left, " -- ", right, " Node : ", root.val, " -- Max Depth :", max(left, right) + 1)

        return max(left, right) + 1
        
        
        
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.left.left.left = TreeNode(6)

sl = Solution()
maxDepth = sl.maxDepth(root)
print("Max Depth of given Tree : ", maxDepth)
         

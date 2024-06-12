'''
Right View of binary Tree

https://leetcode.com/problems/binary-tree-right-side-view/

Hint : Solve by BFS while handling some base cases

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        # BFS and print last item of each level 
        result = []

        q = [root]

        while(q):
            rightSide = None

            for i in range(len(q)):
                node = q.pop(0)

                if node:
                    rightSide = node
                    q.append(node.left)
                    q.append(node.right)

            # verify if right side is not NULL        
            if rightSide:
                result.append(rightSide.val)
        return result
                

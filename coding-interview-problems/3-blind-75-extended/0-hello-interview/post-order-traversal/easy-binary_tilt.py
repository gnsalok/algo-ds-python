'''
Problem : Binary Tree Tilt
https://leetcode.com/problems/binary-tree-tilt/

'''
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def findTilt(root: Optional[TreeNode]) -> int:
    total_tilt = 0

    def dfs(node):
        nonlocal total_tilt

        if not node:
            return 0
        
        left_sum = dfs(node.left)
        right_sum = dfs(node.right)
        
        # Calculate the tilt for the current node
        total_tilt += abs(left_sum - right_sum)

        # Return the sum of values for the current subtree
        return node.val + left_sum + right_sum
    
    dfs(root)
    return total_tilt


# Example usage:
if __name__ == "__main__":

    # Create a sample binary tree
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(4)

    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
    root.right.right = TreeNode(7)


    # Calculate the tilt of the binary tree
    print("Tilt of the binary tree:", findTilt(root))  # Output: 9

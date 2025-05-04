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

    def postorder(node):
        nonlocal total_tilt
        if not node:
            return 0
        left_sum = postorder(node.left)
        right_sum = postorder(node.right)
        total_tilt += abs(left_sum - right_sum)
        return node.val + left_sum + right_sum
    
    postorder(root)
    return total_tilt


# Example usage:
if __name__ == "__main__":
    # Create a sample binary tree
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)

    # Calculate the tilt of the binary tree
    print("Tilt of the binary tree:", findTilt(root))  # Output: 1

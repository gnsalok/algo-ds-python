'''
search in BST
https://leetcode.com/problems/search-in-a-binary-search-tree/

TC : O log n ; * if tree is balanced
'''

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def search(root, target):
    # base case of recursive traversal
    if not root:
        return False 
    
    if target > root.val:
        return search(root.right, target)
    elif target < root.val:
        return search(root.left, target)
    else:
        return True
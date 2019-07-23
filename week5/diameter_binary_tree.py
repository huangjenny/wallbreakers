# Jenny Huang
# Wallbreakers Cohort #3
# Week 5
# Diameter of Binary Tree
# https://leetcode.com/problems/diameter-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        diameter = [0]
        return diameter[0]
        
# dfs
def get_depth(root, diameter):
    if root == None:
        return 0

    left = get_depth(root.left, diameter)
    right = get_depth(root.right, diameter)
    diameter[0] = max(diameter[0], left+right)
    return max(left, right)+1
# Jenny Huang
# Wallbreakers Cohort #3
# Week 5
# Longest Univalue Path
# https://leetcode.com/problems/longest-univalue-path/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """        
        self.longest = 0
        find_longest(self, root)
        return self.longest

def find_longest(self, root):
    if root == None:
        return 0
    
    left_root = root.left
    right_root = root.right
    
    left = find_longest(self, root.left)
    right = find_longest(self, root.right)
    
    left_val = 0
    right_val = 0
    
    if root.left != None and left_root.val == root.val:
        left_val = left + 1
    if root.right != None and right_root.val == root.val:
        right_val = right + 1
        
    self.longest = max(self.longest, left_val + right_val)
    return max(left_val, right_val)
# Jenny Huang
# Wallbreakers Cohort #3
# Week 5
# Find Bottom Left Tree Value
# https://leetcode.com/problems/find-bottom-left-tree-value/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        leftmost = root.val
        left_dict = {}
        get_leftmost(self, root, leftmost, 0, left_dict)

        # get leftmost node value
        if left_dict:
            return max(left_dict, key=left_dict.get)
        return root.val
        
def get_leftmost(self, root, leftmost, depth, left_dict):
    if root.left != None:
        current_depth = depth + 1
        if current_depth > depth:
            left_root = root.left
            leftmost = left_root.val
            # check depth is not dictionary
            if current_depth not in left_dict.values():
                left_dict[leftmost] = current_depth
            # recurse on child
            get_leftmost(self, root.left, leftmost, current_depth, left_dict)
    
    if root.right != None:
        current_depth = depth + 1
        if current_depth > depth and root.left == None:
            right_root = root.right
            leftmost = right_root.val
            # check depth is not dictionary
            if current_depth not in left_dict.values():
                left_dict[leftmost] = current_depth
        # recurse on child
        get_leftmost(self, root.right, leftmost, current_depth, left_dict)
    
    return leftmost
# Jenny Huang
# Wallbreakers Cohort #3
# Week 5
# Sum of Left Leaves
# https://leetcode.com/problems/sum-of-left-leaves/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        
        left_list = []
        get_left(self, root, left_list, False)
        return sum(left_list)

def get_left(self, root, left_list, left):
    # look to left
    if root.left != None:
        get_left(self, root.left, left_list, True)
        left = False # set back to False
        
    # look to right
    if root.right != None:
        get_left(self, root.right, left_list, False)
    
    else:
        # check for valid left leaf
        if left:
            left_list.append(root.val)
# Jenny Huang
# Wallbreakers Cohort #3
# Week 5
# Same Tree
# https://leetcode.com/problems/same-tree/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        # check if same
        if p == q:
            return True
        
        # check if valid trees
        elif p != None and q != None:
            p_list = [p.val]
            q_list = [q.val]
            create_tree(self, p, p_list)
            create_tree(self, q, q_list)
        
            if p_list == q_list:
                return True
            return False
        return False
        
def create_tree(self, root, tree_list):    
    # look for left child
    if root.left != None:
        left_root = root.left
        tree_list.append(left_root.val)
        create_tree(self, left_root, tree_list)
    
    # look for right child
    if root.right != None:
        right_root = root.right
        tree_list.append(right_root.val)
        create_tree(self, right_root, tree_list)
    
    # append null if no children
    else:
        tree_list.append("null")
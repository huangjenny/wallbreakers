# Jenny Huang
# Wallbreakers Cohort #3
# Week 5
# Leaf Similar Trees
# https://leetcode.com/problems/leaf-similar-trees/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        # base case
        if root1 == None or root2 == None:
            return False
        
        root1_list, root2_list = [], []
        get_children(self, root1, root1_list)
        get_children(self, root2, root2_list)
        
        # check lengths are same
        # check both lists are not empty
        if len(root1_list) == len(root2_list) and root1_list and root2_list:
            for i in range(len(root1_list)):
                if root1_list[i] != root2_list[i]:
                    return False
            return True
        return False
        
def get_children(self, root, root_list):
    og_root = root
    left, right = False, False

    # look for left child
    if root.left != None:
        left = True
        get_children(self, root.left, root_list)
    
    # look for right child
    if root.right != None:
        right = True
        get_children(self, root.right, root_list)    

    # no more children
    else:
        if not left and not right:
            root_list.append(root.val)
        elif root != og_root:
            root_list.append(root.val)
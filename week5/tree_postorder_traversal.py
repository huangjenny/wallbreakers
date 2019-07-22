# Jenny Huang
# Wallbreakers Cohort #3
# Week 5
# N-ary Tree Postorder Traversal
# https://leetcode.com/problems/n-ary-tree-postorder-traversal/

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        # base case
        if root == None:
            return root
        
        postorder_nodes = []
        get_children(self, [root], postorder_nodes)
        return postorder_nodes
        
def get_children(self, nodes, postorder_nodes):
    for i in nodes:
        # recurse on children
        if len(i.children) > 0:
            get_children(self, i.children, postorder_nodes)
        # add to list when there are no children
        postorder_nodes.append(i.val)
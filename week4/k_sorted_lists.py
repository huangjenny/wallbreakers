# Jenny Huang
# Wallbreakers Cohort #3
# Week 4
# Merge k Sorted Lists
# https://leetcode.com/problems/merge-k-sorted-lists/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """        
        nodes = []
        
        for i in lists:
            while i:
                nodes.append(i.val)
                i = i.next
                
        nodes.sort()
        
        # initiliaze head with node = 0
        head = ListNode(0)
        current = head
        for i in nodes:
            head.next = ListNode(i) # link current node as next
            head = head.next # move head to next node
        
        return current.next
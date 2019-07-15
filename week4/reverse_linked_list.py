# Jenny Huang
# Wallbreakers Cohort #3
# Week 4
# Reverse Linked List
# https://leetcode.com/problems/reverse-linked-list/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        previous = None
        current = head
        
        while current:
            next_node = current.next # save next node
            current.next = previous # switch directions
            previous = current
            current = next_node
        
        return previous
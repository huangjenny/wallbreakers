# Jenny Huang
# Wallbreakers Cohort #3
# Week 4
# Odd Even Linked List
# https://leetcode.com/problems/odd-even-linked-list/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return None
        
        odd = head
        even = head.next
        even_head = even # initiate linked list for evens
        
        # checks if there is a value
        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
            
        # connect odd linked list to even linked list
        odd.next = even_head
        
        return head
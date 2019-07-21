# Jenny Huang
# Wallbreakers Cohort #3
# Week 4
# Reverse Nodes in k-Group
# https://leetcode.com/problems/reverse-nodes-in-k-group/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        # base case
        if head is None or k == 1:
            return head
        
        # initialize placeholder to hold
        # reversed list in k group
        temp_head = ListNode(0)
        
        # intialize variables to reverse the list
        prev = temp_head
        current = head
        
        while current:
            n = k - 1
            start = current
            
            # get kth node
            while current and n:
                current = current.next
                n -= 1
            
            # get every kth group
            if current and n == 0:
                temp = current.next
                current.next = None
                
                # reverse
                new_head = reverseList(self,start)

                prev.next = new_head
                prev = start
                current = temp
            else:
                prev.next = start

        return temp_head.next
    
# reused code from reverse linked list
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
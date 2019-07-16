# Jenny Huang
# Wallbreakers Cohort #3
# Week 4
# Rotate Array
# https://leetcode.com/problems/rotate-array/

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        for i in range(k):
            nums.insert(0, nums[-1]) # move last element to front
            del nums[-1] # delete last element
            
        return nums
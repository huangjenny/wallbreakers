# Jenny Huang
# Wallbreakers Cohort #3
# Week 1
# Single Number
# https://leetcode.com/problems/single-number/

class Solution(object):
    def singleNumber(self, nums):
        # list to store unique numbers
        uniqueNums = []
        # list to store duplicate numbers
        duplicateNums = []
        
        # loop through list to sort numbers
        for num in nums:
            if num not in uniqueNums:
                uniqueNums.append(num)
            else:
                duplicateNums.append(num)
        
        # loop through duplicates list for unique number
        for num in duplicateNums:
            uniqueNums.remove(num)
        
        return uniqueNums[0]
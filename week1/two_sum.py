# Jenny Huang
# Wallbreakers Cohort #3
# Week 1
# Two Sum
# https://leetcode.com/problems/two-sum/

class Solution(object):
    def twoSum(self, nums, target):
        # loop through entire list
        for i in range(len(nums)):   
            # loop through entire list starting at second position
            for j in range(i+1,len(nums)):
                # check sum of two
                if nums[j] == target - nums[i]:
                    return [i, j]
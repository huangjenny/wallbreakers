# Jenny Huang
# Wallbreakers Cohort #3
# Week 3
# Array Partition 1
# https://leetcode.com/problems/array-partition-i/

class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sort_nums = sorted(nums)
        return sum(sort_nums[::2])
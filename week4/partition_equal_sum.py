# Jenny Huang
# Wallbreakers Cohort #3
# Week 4
# Partition Equal Subset Sum
# https://leetcode.com/problems/partition-equal-subset-sum/

class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) == 1:
            return False
        
        if sum(nums) % 2 != 0:
            return False
        
        total = sum(nums)/2
        nums.sort()
        return getPartitions(self, nums, total)
        
def getPartitions(self, nums, total):    
    if total == 0:
        return True
    
    # loop through nums list
    for i in range(len(nums)):
        if i > 0 and nums[i]==nums[i-1]: 
            continue
        # check if current num <= total
        # backtrack with new list and new total
        if nums[i] <= total and getPartitions(self, nums[i+1:],total-nums[i]):  
            return True

    return False
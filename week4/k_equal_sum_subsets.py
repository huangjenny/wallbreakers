# Jenny Huang
# Wallbreakers Cohort #3
# Week 4
# Parition to K Equal Sum Subsets
# https://leetcode.com/problems/partition-to-k-equal-sum-subsets/

class Solution(object):
    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        subset_sum = sum(nums)/k
        sums_list = [0]*k
        nums.sort(reverse=True) # start from largest num to smallest
        return subsetSum(self, 0, subset_sum, sums_list, nums, k)
        
def subsetSum(self, n, subset_sum, sums_list, nums, k):
    if n == len(nums):
        return True
    for i in range(k):
        sums_list[i] += nums[n]
        if sums_list[i] <= subset_sum and subsetSum(self, n + 1, subset_sum, sums_list, nums, k):
            return True
        sums_list[i] -= nums[n]
        # nums[i] is greater than subset_sum
        if sums_list[i] == 0:
            break
    return False
# Jenny Huang
# Wallbreakers Cohort #3
# Week 4
# Subsets
# https://leetcode.com/problems/subsets/

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        powerset = []
        subset = []
        generateSubsets(self, 0, nums, subset, powerset)
        return powerset
    
def generateSubsets(self, index, nums, subset, powerset):
    # append unique subset to powerset
    powerset.append(set(subset))
    for i in range(index, len(nums)):
        subset.append(nums[i])
        generateSubsets(self, i+1, nums, subset, powerset)
        del subset[-1]
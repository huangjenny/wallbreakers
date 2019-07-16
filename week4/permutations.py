# Jenny Huang
# Wallbreakers Cohort #3
# Week 4
# Permutations
# https://leetcode.com/problems/permutations/

#from itertools import permutations

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        #return permutations(nums)
        
        # initialize empty final list
        perm = [[]]
        
        for num in nums:
            # initialize empty subset list
            new_perm = []
            
            for i in perm:
                for j in range(len(i) + 1):
                    # add num in all possible positions 
                    # for each of the perm
                    new_perm.append(i[j:] + [num] + i[:j])
            perm = new_perm
        return perm
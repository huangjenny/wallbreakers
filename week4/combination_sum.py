# Jenny Huang
# Wallbreakers Cohort #3
# Week 4
# Combination Sum
# https://leetcode.com/problems/combination-sum/

class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if not candidates:
            return []
        
        output = []
        candidates.sort()
        
        backtracking(self, 0, output, [], 0, candidates, target)
        return output
        
def backtracking(self, start, output, subset, total, candidates, target):
    if start >= len(candidates):
        return
    
    # loop through array
    for i in range(start, len(candidates)):
        # check if sum = target
        if candidates[i] + total == target:
            # combine subset and candidates[i] and append to output
            output.append(subset + [candidates[i]])
            return
        # sum > target
        elif candidates[i] + total > target:
            return
        # recurse
        else:
            # start = i to look at candidates[start:]
            backtracking(self, i, output, subset + [candidates[i]], total + candidates[i], candidates, target)
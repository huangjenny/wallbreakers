# Jenny Huang
# Wallbreakers Cohort #3
# Week 3
# Peak Index in a Mountain Array
# https://leetcode.com/problems/peak-index-in-a-mountain-array/

class Solution(object):
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        max_a = max(A)
        max_a_index = A.index(max_a)

        if A[max_a_index-1] < max_a:
                return max_a_index
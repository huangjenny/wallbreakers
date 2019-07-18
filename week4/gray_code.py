# Jenny Huang
# Wallbreakers Cohort #3
# Week 4
# Gray Code
# https://leetcode.com/problems/gray-code/

class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        output = []
        # shift left by n places
        for i in range(1<<n):
            # shift right by 1 and get XOR
            output.append(i^(i>>1))      
        return output
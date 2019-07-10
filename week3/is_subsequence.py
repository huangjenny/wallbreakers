# Jenny Huang
# Wallbreakers Cohort #3
# Week 3
# Is Subsequence
# https://leetcode.com/problems/is-subsequence/

class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        new_s = list(s)
        new_t = list(t)
        
        # base case
        if len(s) == 0:
            return True
        if len(t) == 0:
            return False
        
        while len(new_s) > 0:
            for i in new_s:
                if i in new_t:
                    index = new_t.index(i)
                    new_t = new_t[index+1:]
                    del i
                else:
                    return False
            return True
        
            
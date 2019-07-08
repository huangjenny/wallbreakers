# Jenny Huang
# Wallbreakers Cohort #3
# Week 1
# Valid Anagram
# https://leetcode.com/problems/valid-anagram/

class Solution(object):
    def isAnagram(self, s, t):
        # convert inputs to lists
        listS = list(s)
        listT = list(t)
        
        # sort lists
        a = sorted(listS)
        b = sorted(listT)
        
        # base case
        if len(a) != len(b):
            return False
            
        # loop through inputs
        for i in range(len(a)):
            if a[i] == b[i]:
                continue
            else:
                return False
        return True
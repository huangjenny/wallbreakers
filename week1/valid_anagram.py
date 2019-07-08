# Jenny Huang
# Wallbreakers Cohort #3
# Week 1
# Valid Anagram
# https://leetcode.com/problems/valid-anagram/

import collections

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        t_counter = collections.Counter(t)
        s_counter = collections.Counter(s)
        
        if t_counter == s_counter:
            return True
        return False
# Jenny Huang
# Wallbreakers Cohort #3
# Week 2
# Isomorphic Strings
# https://leetcode.com/problems/isomorphic-strings/

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # base case
        if len(s) != len(t):
            return False
        
        # dictionary to map s characters to t characters
        # key = s characters
        # value = t characters
        s_t_dict = {}
        
        for i in range(len(s)):
            # key exists in dict
            if s[i] in s_t_dict.keys():
                # key, value exists in dict
                if s_t_dict[s[i]] == t[i]:
                    continue
                else:
                    return False
            elif len(s_t_dict) != 0:
                # value does not exist in dict
                if t[i] not in s_t_dict.values():
                    s_t_dict[s[i]] = t[i]
                else:
                    return False
            # add key, value to dict  
            s_t_dict[s[i]] = t[i]
            
        return True
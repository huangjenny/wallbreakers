# Jenny Huang
# Wallbreakers Cohort #3
# Week 2
# Word Pattern
# https://leetcode.com/problems/word-pattern/

class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """        
        split_str = str.split()
        
        # base case
        if len(pattern) != len(split_str):
            return False
        
        str_pattern_dict = {}
        
        for i in range(len(pattern)):
            # fill dictionary with first item
            if len(str_pattern_dict) == 0:
                str_pattern_dict[pattern[i]] = split_str[i]
                
            # key doesn't exist
            elif pattern[i] not in str_pattern_dict.keys():
                # value doesn't exist
                if split_str[i] not in str_pattern_dict.values():
                    # add key, value to dictionary
                    str_pattern_dict[pattern[i]] = split_str[i]
                # value exists, return False
                else:
                    return False
                
            # check if the key, value pair are equal
            elif str_pattern_dict[pattern[i]] == split_str[i]:
                continue
            
            else:
                return False
            
        return True
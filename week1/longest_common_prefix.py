# Jenny Huang
# Wallbreakers Cohort #3
# Week 1
# Longest Common Prefix
# https://leetcode.com/problems/longest-common-prefix/

class Solution(object):
    def longestCommonPrefix(self, strs):        
        # base case: no string in list
        if len(strs) < 1:
            return ""
        # base case: only 1 string in list
        elif len(strs) == 1:
            return strs[0]
        else:
            # set longest prefix as first string in list
            prefix = strs[0]
            # loop through list starting at second element in list
            for i in range(1, len(strs)):
                # base case: if string is empty
                if strs[i] == "":
                    return ""
                # check if the longest prefix is equal to element in list after index stripping it
                while prefix != strs[i][:len(prefix)]:
                    # decrease longest prefix by 1 if not equal and look again
                    prefix = prefix[:(len(prefix) - 1)]
                    # base case if string is empty
                    if prefix == "":
                        return ""
        return prefix
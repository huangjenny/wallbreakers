# Jenny Huang
# Wallbreakers Cohort #3
# Week 2
# Groups of Special-Equivalent Strings
# https://leetcode.com/problems/groups-of-special-equivalent-strings/

class Solution(object):
    def numSpecialEquivGroups(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        # initialize set to store the groups
        groups = set()
        
        for word in A:
            # store the even chars of the word as one string
            # store the odd chars of the word as one string
            # this ensures i%2==j%2 (order doesn't matter)
            
            # get every even char of the word
            even = ''.join(sorted(word[0::2]))
            # get every odd char of the word
            odd = ''.join(sorted(word[1::2]))
            
            # add combination set to groups set
            groups.add((even, odd))
        
        return len(groups)
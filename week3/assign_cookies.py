# Jenny Huang
# Wallbreakers Cohort #3
# Week 3
# Assign Cookies
# https://leetcode.com/problems/assign-cookies/

class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """        
        # look in reversed order
        new_g = sorted(g, reverse=True)
        new_s = sorted(s, reverse=True)
        
        happy = 0
        while len(new_g) > 0 and len(new_s) > 0:
            # check if there is a match
            if new_s[0] >= new_g[0]:
                happy += 1
                # remove cookie (already taken)
                del new_s[0]
            # remove child irregardless of match or not
            del new_g[0]
            
        return happy
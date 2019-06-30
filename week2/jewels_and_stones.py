# Jenny Huang
# Wallbreakers Cohort #3
# Week 2
# Jewels and Stones
# https://leetcode.com/problems/jewels-and-stones/

from collections import defaultdict

class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        listJ = list(J)
        listS = list(S)
        
        frequency_dict = defaultdict(int)
        
        # key = stone
        # value = how many stones
        for i in range(len(listS)):
            frequency_dict[listS[i]] += 1
        
        total = 0
        # loop through dictionary
        # if stone is in jewels list
        # take value and add it to total
        for key, value in frequency_dict.items():
            if key in listJ:
                total += value
        
        return total
# Jenny Huang
# Wallbreakers Cohort #3
# Week 2
# Distribute Candies
# https://leetcode.com/problems/distribute-candies/

from collections import defaultdict

class Solution(object):
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        # key = kind of candy
        # value = number of candy
        num_candy = defaultdict(int)
        
        for i in candies:
            num_candy[i] += 1
        
        total_candy = len(candies)
        total_candy_kind = len(num_candy)
        
        # num of candy/2 = total candy kinds
        if total_candy/2 == total_candy_kind:
            return total_candy_kind
        # num of candy/2 < total candy kinds
        elif total_candy/2 < total_candy_kind:
            return total_candy/2
        # num of candy/2 > total candy kinds
        else:
            return total_candy_kind
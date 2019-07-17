# Jenny Huang
# Wallbreakers Cohort #3
# Week 4
# Combinations
# https://leetcode.com/problems/combinations/

#from itertools import combinations

class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        num_list = []
        for i in range(n):
            num_list.append(i+1)
            
        #return combinations(num_list, k)
        return combination(self, num_list, k)

def combination(self, num_list, k):
    if k == 0:
        return [[]]
    if len(num_list) == k:
        return [num_list]
    
    # pick first item -> k-1 items from n-1 items left
    result = [[num_list[0]] + c for c in combinations(self, num_list[1:], k - 1)]
    # don't pick first item -> k items from n-1 items left
    result += combinations(self, num_list[1:], k)
    return result
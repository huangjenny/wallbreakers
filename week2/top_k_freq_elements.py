# Jenny Huang
# Wallbreakers Cohort #3
# Week 4
# Top K Frequent Elements
# https://leetcode.com/problems/top-k-frequent-elements/

import collections 

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # dictionary list of frequency of nums
        # key = num
        # value = freq of num
        counter = collections.Counter(nums)
        
        # return k largest elements from dictionary based on dictionary key
        return heapq.nlargest(k, counter.keys(), key=counter.get)
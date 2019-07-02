# Jenny Huang
# Wallbreakers Cohort #3
# Week 2
# Sort Characters By Frequency
# https://leetcode.com/problems/sort-characters-by-frequency/

from collections import defaultdict
from collections import OrderedDict

class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        # dictionary of characters and # of character occurrences
        # key = character
        # value = # of occurrences of character
        freq_s = defaultdict(int)
        
        # load data into dictionary
        for i in s:
            freq_s[i] += 1
        
        # order dictionary by value
        ordered_s = OrderedDict(sorted(freq_s.items(), key=lambda item:item[1], reverse=True))
        
        # create string
        sorted_string = ""
        for key, value in ordered_s.items():
            sorted_string = sorted_string + (key * value)
        
        return sorted_string
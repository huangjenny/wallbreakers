# Jenny Huang
# Wallbreakers Cohort #3
# Week 2
# Find the Difference
# https://leetcode.com/problems/find-the-difference/

from collections import defaultdict
from collections import OrderedDict

class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        # dictionary of characters and # of character occurrences
        # key = character
        # value = number of occurrences
        freq_s = defaultdict(int)
        freq_t = defaultdict(int)
        
        # load data into dictionaries
        for i in s:
            freq_s[i] +=1
            
        for i in t:
            freq_t[i] += 1
        
        # order dictionaries by key alphabetically 
        ordered_s = OrderedDict()
        ordered_t = OrderedDict()
        
        ordered_s = OrderedDict(sorted(freq_s.items(), key=lambda item: item[0], reverse=False))
        ordered_t = OrderedDict(sorted(freq_t.items(), key=lambda item: item[0], reverse=False))
        
        # loop through ordered_t because that length will either be
        # equal to or greater than ordered_s
        for key, value in ordered_t.items():
        	# check if key exists in ordered_s
            if key not in ordered_s.keys():
                return key
            # check if the value of key is equal to value of key in ordered_s
            if value != ordered_s.get(key):
                return key
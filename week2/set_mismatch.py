# Jenny Huang
# Wallbreakers Cohort #3
# Week 2
# Set Mismatch
# https://leetcode.com/problems/set-mismatch/

from collections import defaultdict
from collections import OrderedDict

class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # dictionary with a unique number and its corresponding # of occurrences
        # key = unique number
        # value = # of occurrences
        freq_nums = defaultdict(int)
        
        # load data in dictionary
        for i in nums:
            freq_nums[i] += 1
        
        # order the list by keys
        ordered_nums = OrderedDict(sorted(freq_nums.items(), key=lambda item: item[0], reverse=False))
    
        counter = 0
        missing_value = -1
        duplicate_num = -1
        min_value = ordered_nums.keys()[0]
        max_value = ordered_nums.keys()[-1]
        
        # base case
        # list does not start with 1
        if min_value != 1:
            for key, value in ordered_nums.items():
                if value == 2:
                    return [key,1]
        
        # base case
        # list contains 1 item of duplicates
        if len(ordered_nums.items()) == 1:
            if min_value != 1:
                return [(ordered_nums.keys()[0]), (ordered_nums.keys()[0])-1]
            return [(ordered_nums.keys()[0]), (ordered_nums.keys()[0])+1]
        
        for key, value in ordered_nums.items():
            counter += 1
            # no duplicate_num found and value == 2
            if duplicate_num == -1 and value == 2:
                duplicate_num = key
            # no missing_value found and counter != key
            if missing_value == -1 and counter != key:
                missing_value = counter
            # if both found, break out of loop
            if duplicate_num != -1 and missing_value != -1:
                break
        
        # check if missing_value is determined
        if missing_value == -1:
            if min_value != 1:
                missing_value = 1
            elif max_value != counter+1: 
                missing_value = (ordered_nums.keys()[-1])+1
            
        return [duplicate_num, missing_value]
# Jenny Huang
# Wallbreakers Cohort #3
# Week 2
# First Unique Character in a String
# https://leetcode.com/problems/first-unique-character-in-a-string/

from collections import defaultdict

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        # base case
        if len(s) == 0:
            return -1
        
        # sorted ordered dictionary
        freq_dict = defaultdict(int)
        
        # list of unique letters
        letter_list = []
        for i in range(len(s)):
            freq_dict[s[i]] += 1
            
            # if first occurrence and not in list of unique letters
            if freq_dict[s[i]] == 1 and s[i] not in letter_list:
                letter_list.append(s[i])
            
            # not first occurrence and in list of unique letters
            elif freq_dict[s[i]] > 1 and s[i] in letter_list:
                letter_list.remove(s[i])
        
        # check if there are letters in list
        if len(letter_list) > 0:
            return s.index(letter_list[0])
        else: 
            return -1
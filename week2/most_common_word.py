# Jenny Huang
# Wallbreakers Cohort #3
# Week 2
# Most Common Word
# https://leetcode.com/problems/most-common-word/

import re
from collections import defaultdict
from collections import OrderedDict

class Solution(object):    
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        # substitute punctuations with spaces    
        remove_punc = re.sub(r'[^\w\s]',' ',paragraph)
        # lower case paragraph text and split it in a list at the spaces
        new_paragraph = remove_punc.lower().split()
        
        # dictionary to contain occurrences of words
        # key = word
        # value = num of occurrences
        freq_word = defaultdict(int)

        # load data into dictionary
        for word in new_paragraph:
            freq_word[word] += 1
        
        # order the dictionary by highest word frequency
        ordered_freq = OrderedDict(sorted(freq_word.items(), key=lambda item: item[1], reverse=True))
        
        # loop through ordered dictionary
        for key in ordered_freq.keys():
            # check key not in banned list
            if key not in banned:
                return key
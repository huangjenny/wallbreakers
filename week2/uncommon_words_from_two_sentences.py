# Jenny Huang
# Wallbreakers Cohort #3
# Week 2
# Uncommon Words from Two Sentences
# https://leetcode.com/problems/uncommon-words-from-two-sentences/

from collections import defaultdict

class Solution(object):
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        # dictionaries to see how often words occur in sentences
        # key = word
        # value = number of times the word occurs
        freq_dict_a = defaultdict(int)
        freq_dict_b = defaultdict(int)
        
        # split the sentences into word lists
        split_a =  A.split()
        split_b = B.split()
        
        # populate data into dictionary
        for i in split_a:
            freq_dict_a[i] += 1
            
        for i in split_b:
            freq_dict_b[i] += 1
        
        # initialize sets
        set_a = set()
        set_a_more = set()
        set_b = set()
        set_b_more = set()
        
        for key, value in freq_dict_a.items():
            if value == 1:
                set_a.add(key)
            else:
                set_a_more.add(key)
                
        for key, value in freq_dict_b.items():
            if value == 1:
                if key not in set_a_more:
                    set_b.add(key)
                else:
                    set_b_more.add(key)
            else:
                set_b_more.add(key)
        
        # get difference between set_a and set_b_more to get true uncommon words
        diff_between_a_b_more = set_a.difference(set_b_more)

        # symmetric difference between diff and set_b
        uncommon_set = diff_between_a_b_more.symmetric_difference(set_b)
        
        return uncommon_set
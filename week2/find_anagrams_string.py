# Jenny Huang
# Wallbreakers Cohort #3
# Week 2
# Find All Anagrams in a String
# https://leetcode.com/problems/find-all-anagrams-in-a-string/

import collections

class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        index_list = []
        p_len = len(p)

        p_counter = collections.Counter(list(p))

        for i in range(len(list(s))):
            word = s[i:(p_len+i)]
            if len(word) == p_len:
                word_counter = collections.Counter(list(word))

                append = False
                if word_counter == p_counter:
                    append = True
                            
                if append:
                    index_list.append(i)

        return index_list
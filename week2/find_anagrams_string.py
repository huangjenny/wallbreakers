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

        p_counter = collections.Counter(p)

        # get first len(p) - 1 letters of s in a collection
        s_counter = collections.Counter(s[:len(p)-1])

        # index counter
        index = 0

        # loop through len(p) - 1 to len(s)
        for i in range(len(p) - 1, len(s)):
            # add first item seen to s_counter
            s_counter[s[i]] += 1

            # append index to list if counters are equal
            if s_counter == p_counter:
                index_list.append(index)

            # decrease the first item value in s_counter
            # can't just pop off the first item
            # even though it was seen because the 
            # value could be > 1
            s_counter[s[index]] -= 1

            # remove the first item if value = 0
            if s_counter[s[index]] == 0:
                del(s_counter[s[index]])

            index += 1
            
        return index_list
# Jenny Huang
# Wallbreakers Cohort #3
# Week 3
# Find All Anagrams in a String (Sorting)
# https://leetcode.com/problems/find-all-anagrams-in-a-string/

import bisect  

class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        sorted_p = sorted(p)
        string = list(s)
        output_list = []

        # initialize first 
        substring =  sorted(string[:len(p)])
        counter = 0 # index of string counter
        
        # loop through substring
        for i in range(len(p), len(s)):
            if len(substring) != len(p):
                return output_list
            if substring == sorted_p:
                output_list.append(counter)
            
            # get beginning of substring value at s[counter]
            head = s[counter]
            index = substring.index(head)

            # remove head of substring
            del substring[index]
            
            # add element with sorting
            bisect.insort(substring, s[i])    
            counter += 1
        
        # check last sorted substring
        if len(substring) == len(p) and substring == sorted_p:
            output_list.append(counter)
            
        return output_list          
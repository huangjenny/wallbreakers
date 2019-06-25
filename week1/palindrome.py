# Jenny Huang
# Wallbreakers Cohort #3
# Week 1
# Valid Palindrome
# https://leetcode.com/problems/valid-palindrome/

import re

class Solution(object):
    def isPalindrome(self, s):
        # define acceptable characters
        regex = re.compile('[^a-zA-Z0-9]')

        # strip non-alphanumeric characters and lowercase all letters
        newString = regex.sub('', s)
        newString = newString.lower()
        
        # convert string to a list to use reverse
        stringList = list(newString)
        stringList.reverse()

        # convert reversed string list back to a string
        reverseStringList = ''.join(stringList)
        
        # compare if reversed string list = stripped string
        if reverseStringList == newString:
            return True
        return False
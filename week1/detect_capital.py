# Jenny Huang
# Wallbreakers Cohort #3
# Week 1
# Detect Capital
# https://leetcode.com/problems/detect-capital/

class Solution(object):
    def detectCapitalUse(self, word):

    	# if word is all uppercase
        if word.isupper():
            return True
        # if word is all lowercase
        if word.islower():
            return True
        # if only first letter is uppercase
        if word[0].isupper() and word[1:].islower():
            return True
        return False
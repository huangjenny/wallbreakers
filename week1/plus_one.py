# Jenny Huang
# Wallbreakers Cohort #3
# Week 1
# Plus One
# https://leetcode.com/problems/plus-one/

class Solution(object):
    def plusOne(self, digits):
        # reverse list to add from the end 
        digits.reverse()
        addNext = False
        
        for i in digits:
            # add next digit if digit is 9
            if i == 9:
                digits[digits.index(i)] = 0
                addNext = True
            else:
                digits[digits.index(i)] = i + 1
                break # break out of loop
        
        # clean up
        if digits[-1] == 0:
            digits.append(1)
        
        # reverse list back
        digits.reverse()
        
        return digits
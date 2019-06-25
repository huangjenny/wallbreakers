# Jenny Huang
# Wallbreakers Cohort #3
# Week 1
# Sort Array By Parity
# https://leetcode.com/problems/sort-array-by-parity/

class Solution(object):
    def sortArrayByParity(self, A): 
        newArray = []

        # look at element in list
        for element in A:
            # if element is even, append to front
            if element % 2 == 0:
                newArray.insert(0, element)
            # if element is odd, append to end
            else:
                newArray.insert(len(newArray), element)
                
        return newArray
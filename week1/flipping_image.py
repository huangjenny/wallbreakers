# Jenny Huang
# Wallbreakers Cohort #3
# Week 1
# Flipping an Image
# https://leetcode.com/problems/flipping-an-image/

class Solution(object):
    def flipAndInvertImage(self, A):
        flippedAndInverted = []
        
        # flip array
        for x in A:
            flipped = []
            for y in x:    
                flipped.insert(0, y)
            flippedAndInverted.append(flipped)
        
        # invert flipped array    
        for x in flippedAndInverted:
            for y in range(len(x)):
                if x[y] == 1: # set 1 to 0
                    x[y] = 0
                else: # set 0 to 1
                    x[y] = 1

        return flippedAndInverted
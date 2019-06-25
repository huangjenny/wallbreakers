# Jenny Huang
# Wallbreakers Cohort #3
# Week 1
# Hamming Distance
# https://leetcode.com/problems/hamming-distance/

class Solution(object):
    def hammingDistance(self, x, y):
        # convert inputs to binary string lists
        binX = list(str(bin(x)[2:]))
        binY = list(str(bin(y)[2:]))
        
        # balance each set of string lists with equal number of digits
        if len(binY) > len(binX):
            for i in range(len(binY)-len(binX)):
                binX.insert(0,'0') # insert in beginning of list
        else: 
            for i in range(len(binX)-len(binY)):
                binY.insert(0,'0') # insert in beginning of list
        
        # counter
        output = 0

        # look for differences
        for i in range(len(binX)):
                if binX[i] != binY[i]:
                    output = output + 1

        return output
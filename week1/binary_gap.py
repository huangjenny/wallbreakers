# Jenny Huang
# Wallbreakers Cohort #3
# Week 1
# Binary Gap
# https://leetcode.com/problems/binary-gap/

class Solution(object):
    def binaryGap(self, N):
        # convert N to binary number list
        listN = list(bin(N)[2:])
        saveIndex = []
        
        for i in range(len(listN)):
            # save all the indexes that are 1
            if listN[i] == '1':
                saveIndex.append(i)
        
        distance = 0
        # loop through index list to find largest distance
        for i in range(len(saveIndex)-1):
            # determine if next index - current index > distance
            if saveIndex[i+1] - saveIndex[i] > distance:
                distance = saveIndex[i+1] - saveIndex[i]
        return distance
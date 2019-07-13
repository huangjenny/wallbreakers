# Jenny Huang
# Wallbreakers Cohort #3
# Week 3
# Partition Labels
# https://leetcode.com/problems/partition-labels/

class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        list_s = list(S)
        total = []
        index = 0
        while sum(total) != len(S):
            length = getLength(self, index, list_s[sum(total):])
            total.append(length)
            index = sum(total)   
        return total

# returns length of the first seen partition
def getLength(self, index, list_s):
    # base case
    if len(list_s) == 0:
        return 0
    if len(list_s) == 1:
        return 1
    if len(list_s) == 2:
        if list_s[0] == list_s[1]:
            return 2
        else:
            return 1

    # initialize
    prev_index = index
    output = list_s[0]

    # loop through list to find partition
    for i in range(1, len(list_s)):
        if list_s[i] in output:
            output = (list_s[:i+1])
        index = len(output)

    if index == 0:
        return 1
    
    return index
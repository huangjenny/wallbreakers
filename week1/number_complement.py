# Jenny Huang
# Wallbreakers Cohort #3
# Week 1
# Number Complement
# https://leetcode.com/problems/number-complement/

class Solution(object):
    def findComplement(self, num):
        # convert number to binary
        binaryNum = bin(num)[2:]

        binNumList = list(str(binaryNum))
        
        output = ""
        for i in range(len(binNumList)):
            if binNumList[i] == '1':
                binNumList[i] = '0'
            else:
                binNumList[i] = '1'
            output = output + binNumList[i]

        # convert binary to number
        return (int(output,2))
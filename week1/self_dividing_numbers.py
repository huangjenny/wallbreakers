# Jenny Huang
# Wallbreakers Cohort #3
# Week 1
# Self Dividing Numbers
# https://leetcode.com/problems/self-dividing-numbers/

class Solution(object):
    def selfDividingNumbers(self, left, right):
        output = []
        for num in range(left, right+1):
            appendToList = True
            
            # create list of single digits that compose of the number
            stringInt = []
            for digit in str(num):
                stringInt.append(int(digit))

            # check if each digit is self divisible
            for digit in stringInt:
                if (digit == 0) or (num % digit != 0):
                    appendToList = False

            # add number to output list if self divisible
            if appendToList:
                output.append(num)

        return output
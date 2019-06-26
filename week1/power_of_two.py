# Jenny Huang
# Wallbreakers Cohort #3
# Week 1
# Power of Two
# https://leetcode.com/problems/power-of-two/

class Solution(object):
    def isPowerOfTwo(self, n):
        while True:
            # base case
            if n < 1:
                return False
            # base case
            elif n == 1:
                return True
            # check if there is a remainder
            elif n % 2 != 0:
                return False
            # divide by 2 to get smaller number
            else:
                n = n / 2
# Jenny Huang
# Wallbreakers Cohort #3
# Week 2
# Happy Number
# https://leetcode.com/problems/happy-number/

class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        happyNum = False
        numSet = set()
        while not happyNum:
            # check if number is 1 (happy number)
            if (n != 1):
                n_list = list(str(n))
                n = self.squareNum(n_list)

                # if number not in set, add it
                if n not in numSet:
                    numSet.add(n)
                # if number is in set, it means it will loop endlessly
                # return false
                else:
                    return happyNum
            else:
                happyNum = True
        
        return happyNum
        
    def squareNum(self, n_list):
        new_n = 0        
        for num in n_list:
            new_n = new_n + int(num) ** 2
        return new_n
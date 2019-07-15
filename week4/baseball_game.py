# Jenny Huang
# Wallbreakers Cohort #3
# Week 4
# Baseball Game
# https://leetcode.com/problems/baseball-game/

class Solution(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        stack = []
        
        for i in ops:                
            if i == 'C':
                del stack[-1]
            elif i == 'D':
                stack.append(stack[-1] * 2)
            elif i == '+':
                stack.append(stack[-1] + stack[-2])
            else:
                stack.append(int(i))
        return sum(stack)
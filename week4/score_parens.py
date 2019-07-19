# Jenny Huang
# Wallbreakers Cohort #3
# Week 4
# Score of Parentheses
# https://leetcode.com/problems/score-of-parentheses/

class Solution(object):
    def scoreOfParentheses(self, S):
        """
        :type S: str
        :rtype: int
        """
        # initialize stack with 0
        stack = [0] 

        for i in S:
            if i == '(':
                stack.append(0)
            else:
                # remove last item to apply logic to
                last_item = stack.pop()
                # get max of new value (2*last_item ensures we don't get 0s)
                # add to last element
                stack[-1] += (max(2*last_item,1))
        return stack[-1]
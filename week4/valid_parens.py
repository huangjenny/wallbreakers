# Jenny Huang
# Wallbreakers Cohort #3
# Week 4
# Valid Parentheses
# https://leetcode.com/problems/valid-parentheses/

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # base case
        if len(s) == 0:
            return True
        if len(s) == 1:
            return False
        
        inside = False
        stack = []
        
        for i in s:
            if i =='(' or i == '[' or i == '{':
                stack.append(i)
                inside = True
            elif i == ')' or i == ']' or i == '}' and inside:
                if len(stack) == 0:
                    return False
                if i == ')':
                    if stack[-1] == '(':
                        del stack[-1]
                    else:
                        return False
                elif i == ']':
                    if stack[-1] == '[':
                        del stack[-1]
                    else:
                        return False
                elif i == '}':
                    if stack[-1] == '{':
                        del stack[-1]
                    else:
                        return False
        
        if len(stack) == 0:
            return True
        else:
            return False
# Jenny Huang
# Wallbreakers Cohort #3
# Week 4
# Generate Parentheses
# https://leetcode.com/problems/generate-parentheses/

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        output = []
        return parens(self, n, 0, '', output)
        
def parens(self, open, close, string, output):
    # no more parens
    if open == 0 and close == 0:
        output.append(string)
    
    # add open parens
    if open > 0:
        parens(self, open-1, close+1, string + "(", output)
    
    # add close parens
    if close > 0:
        parens(self, open, close-1, string + ")", output)
    
    return output
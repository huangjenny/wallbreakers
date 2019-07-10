# Jenny Huang
# Wallbreakers Cohort #3
# Week 3
# Best Time to Buy and Sell Stock - Recursion
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        return getMaxProfit(self, len(prices), prices)
    
def getMaxProfit(self, i, prices):
    if i == 0:
        return 0
    else:
        # recurse on each element in list
        total = getMaxProfit(self, i-1, prices)
        
        # loop through list
        for index in range(0, i):
            # get max of total, new profit
            total = max(total, prices[i-1] - prices[index])
        return total
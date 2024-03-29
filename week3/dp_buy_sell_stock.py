# Jenny Huang
# Wallbreakers Cohort #3
# Week 3
# Best Time to Buy and Sell Stock - Dynamic Programming
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # set default values to really high and really low numbers
        min_price = sys.maxint
        max_profit = 0
        
        for i in range(len(prices)):
            # set the min price @ smallest price
            if prices[i] < min_price:
                min_price = prices[i]
            # determine max profit @ given min price
            if prices[i] - min_price > max_profit:
                max_profit = prices[i] - min_price
        return max_profit
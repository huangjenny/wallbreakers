# Jenny Huang
# Wallbreakers Cohort #3
# Week 3
# Lemonade Change
# https://leetcode.com/problems/lemonade-change/

from collections import defaultdict

class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        # base case
        if bills[0] > 5:
            return False
        
        total = 0
        bill_count = defaultdict(int)
        for amount in bills:
            change = amount-5
            if change == 0:
                total = total + amount
                bill_count[amount] += 1
            elif change == 5:
                if change in bill_count:
                    bill_count[change] -= 1
                    bill_count[amount] += 1
                    total = total + amount - change
                else:
                    return False
            elif change == 15: # need 1 $10, 1 $5 or 3 $5
                print bill_count.get(10), bill_count.get(5)
                if bill_count.get(10) >= 1 and bill_count.get(5) >= 1:
                    bill_count[10] -= 1
                    bill_count[5] -= 1
                elif bill_count.get(5) >= 3:
                    bill_count[5] -= 3
                else:
                    return False
                bill_count[amount] += 1
                total = total + amount - change
        return True
                
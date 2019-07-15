# Jenny Huang
# Wallbreakers Cohort #3
# Week 3
# House Robber 2 - Recursion
# https://leetcode.com/problems/house-robber-ii/

# INCOMPLETE

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        cache = {}
        i = 0
        a = getLength(self, nums, i, cache)

def getLength(self, nums, i, cache):
    # if there is a cached value, then return it
    if i in cache:
        return cache[i]

    if len(nums) == 0:
        return 0
    elif len(nums) == 1:
        return nums[0]
    elif len(nums) == 2:
        return max(nums[0], nums[1])
    elif len(nums) > 2:
        cache[0] = nums[0]
        cache[1] = nums[1]

    # store length in cache
    length = max(getLength[i] + getLength[i-2], getLength[i-1])
    return length

    """
        # base cases
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        
        # create list with len(nums) elements
        dp = [0]*(len(nums)-1)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        # list from nums[0] to nums[n-1], where n is len(nums)
        nums1 = nums[:-1]
        
        dp2 = [0]*(len(nums)-1)
        dp2[0] = nums[1]
        dp2[1] = max(nums[1], nums[2])
        # list from nums[1] to nums[n], where n is len(nums)
        nums2 = nums[1:]
        
        # for nth items in nums, solve for nums[ith]
        for i in range(2,len(nums1)):
            dp[i] = max(nums1[i] + dp[i-2], dp[i-1])
        
        # for nth items in nums, solve for nums[ith]
        for i in range(2,len(nums2)):
            print i, nums2[i], dp2[i-2], dp2[i-1]
            dp2[i] = max(nums2[i] + dp2[i-2], dp2[i-1])
        
        # get the max from lists
        return max(dp[-1], dp2[-1])
    """
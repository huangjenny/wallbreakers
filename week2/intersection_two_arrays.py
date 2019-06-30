# Jenny Huang
# Wallbreakers Cohort #3
# Week 2
# Intersection of Two Arrays
# https://leetcode.com/problems/intersection-of-two-arrays/

class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # convert lists to sets to get unique elements
        nums1 = set(nums1)
        nums2 = set(nums2)
        
        # initialize new intersection set
        intersection_set = set()
        
        # built in method which provides same answer
        #intersection_set = nums1.intersection(nums2)

        # loop through each element in nums1
        for element in nums1:
            # if element is in nums2, add to intersection_list
            # this means the element exists in both nums1 and nums2
            if element in nums2:
                intersection_set.add(element)
        
        return intersection_set
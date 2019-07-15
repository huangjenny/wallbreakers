# Jenny Huang
# Wallbreakers Cohort #3
# Week 4
# Next Greater Element 1
# https://leetcode.com/problems/next-greater-element-i/

class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        output = []
        for i in range(len(nums1)):
            value = -1
            current = nums1[i]
            nums2_index = nums2.index(current)
            if nums2_index+1 < len(nums2):
                next_greater = nums2[nums2_index+1]
                # check if next greater is next to element
                if next_greater > current:
                    value = next_greater
                # parse the rest of nums2 for next greater
                else:
                    new_nums2 = nums2[nums2_index+1:]
                    for j in new_nums2:
                        if j > current:
                            value = j
                            break
            output.append(value)
        return output
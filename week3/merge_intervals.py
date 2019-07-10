# Jenny Huang
# Wallbreakers Cohort #3
# Week 3
# Merge Intervals
# https://leetcode.com/problems/merge-intervals/

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        # sort list
        intervals_sorted = sorted(intervals, key=lambda x: x[0])        
        
        temp_list = [] # list to hold new intervals
        len_interval_sorted = len(intervals_sorted)
        i = 0 # counter

        # base case
        if len_interval_sorted == 1:
            return intervals_sorted

        # loop through list
        for index in range(len_interval_sorted):
            # check if within list range
            if i < len_interval_sorted-1:
                if intervals_sorted[i+1][0] - intervals_sorted[i][1] <= 0:
                    #if intervals_sorted[i][1] > intervals_sorted[i+1][1]:
                        #temp_list.append([intervals_sorted[i][0],intervals_sorted[i][1]])
                    #else:
                        #temp_list.append([intervals_sorted[i][0],intervals_sorted[i+1][1]])
                    max_interval = max(intervals_sorted[i][1], intervals_sorted[i+1][1])
                    temp_list.append([intervals_sorted[i][0],max_interval])

                    # remove the interval pairs that will be merged
                    del intervals_sorted[i+1]
                    del intervals_sorted[i]
                    # add merged interval back into list
                    intervals_sorted.insert(i, temp_list[-1])
                    len_interval_sorted -= 1
                else:
                    # increment counter
                    i += 1
       
        return intervals_sorted
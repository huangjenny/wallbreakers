# Jenny Huang
# Wallbreakers Cohort #3
# Week 3
# Minimum Number of Arrows to Burst Balloons
# https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/

class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        # base case
        if len(points) == 0:
            return 0
        if len(points) == 1:
            return 1
        
        # sort by right coordinate of each pair
        sorted_points = sorted(points, key=lambda points: points[1])
        arrows = 1

        # initialize first x
        x = sorted_points[0][1]
        
        for i in range(1,len(sorted_points)):
            # if within range, do nothing
            if sorted_points[i][0] <= x and x <= sorted_points[i][1]:
                continue
            else:
                x = sorted_points[i][1]
                arrows += 1
                
        return arrows
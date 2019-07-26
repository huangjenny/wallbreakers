# Jenny Huang
# Wallbreakers Cohort #3
# Week 5
# Longest Increasing Path in a Matrix
# https://leetcode.com/problems/longest-increasing-path-in-a-matrix/

class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        # base case:
        if not matrix:
            return 0
        
        row = len(matrix)
        col = len(matrix[0])
        
        m = []
        for i in range(row):
            for j in range(col):
                m.append((matrix[i][j], i, j))
        
        # sort to start at min value
        m.sort()
        dp = [[0 for i in range(col)] for j in range(row)]
        bounds = [1,0],[0,1],[-1,0],[0,-1]
        for num, i, j in m:
            dp[i][j] = 1 # value looked at
            # look around
            for r, c in bounds:
                new_i = i + r
                new_j = j + c
                if 0 <= new_i < row and 0 <= new_j < col:
                    if matrix[i][j] > matrix[new_i][new_j]:
                        # get longest path
                        dp[i][j] = max(dp[i][j], 1 + dp[new_i][new_j])
        return max([dp[i][j] for i in range(row) for j in range(col)])
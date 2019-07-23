# Jenny Huang
# Wallbreakers Cohort #3
# Week 5
# Island Perimeter
# https://leetcode.com/problems/island-perimeter/

class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row = len(grid)        
        col = len(grid[0])
        counter = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1: # look for 1
                    # top row
                    if i == 0:
                        counter += 1
                    # bottom row
                    if i == row -1:
                        counter += 1
                    # left column
                    if j == 0:
                        counter += 1  
                    # right column
                    if j == col-1:
                        counter += 1
                    # look top 
                    if i > 0 and grid[i-1][j] == 0:
                        counter += 1
                    # look below
                    if i+1 < row and grid[i+1][j] == 0:
                        counter += 1
                    # look left
                    if j > 0 and grid[i][j-1] == 0:
                        counter += 1
                    # look right
                    if j+1 < col and grid[i][j+1] == 0:
                        counter += 1
        return counter
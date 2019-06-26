# Jenny Huang
# Wallbreakers Cohort #3
# Week 1
# Number of Islands
# https://leetcode.com/problems/number-of-islands/

class Solution(object):
    def numIslands(self, grid):
        row = len(grid)
        
        # base case: no input
        if row == 0:
            return 0
        
        col = len(grid[0])
        
        counter = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == '1': # look for land
                    counter = counter + 1
                    self.dfs(grid, row, col, i, j) # look around it
        print counter
        return counter
        
        
    def dfs(self, grid, row, col, i, j):
        # base case: i < 0 or j < 0 is off map -> return and look for more land
        # base case: i >= row or j >= col is edge or off the map -> return and look for more land
        # case 1: grid[i][j] == '0' is not land, so return and look for more land
        # order matters
        if i<0 or j<0 or row <= i or col <= j or grid[i][j] == '0':
            return
        grid[i][j] = '0' # change value to 0 because it's been visited
        self.dfs(grid, row, col, i + 1, j) # look to right
        self.dfs(grid, row, col, i - 1, j) # look to left
        self.dfs(grid, row, col, i, j + 1) # look to top
        self.dfs(grid, row, col, i, j - 1) # look to bottom
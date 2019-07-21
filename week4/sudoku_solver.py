# Jenny Huang
# Wallbreakers Cohort #3
# Week 4
# Sudoku Solver
# https://leetcode.com/problems/sudoku-solver/

class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        # convert all board[i][j] to string type
        for i in range(0,9):
            for j in range (0,9):
                #cell is unassigned
                if board[i][j] == '.':
                    board[i][j] = str(-1) # replace '.' with str(-1)
                else:
                    board[i][j] = str(board[i][j])
        solve(self, board)

def empty_square(self, board, row, col):
    empty_value = 0
    for i in range(0,9):
        for j in range (0,9):
            # get first unassigned cell
            if board[i][j] == str(-1):
                row = i
                col = j
                empty_value = 1
                x = [row, col, empty_value]
                return x
    x = [-1, -1, empty_value]
    return x

def is_valid(self, board, row, col, num):
    # check if the num is in row
    for i in range(0,9):
        if(board[row][i] == str(num)): 
            return False

    # check if the num is in col
    for i in range(0,9): 
        if(board[i][col] == str(num)): 
            return False

    row_start = (row//3)*3
    col_start = (col//3)*3
    # check if the num is in grid
    for i in range(row_start, row_start+3): # loop grid width
        for j in range(col_start, col_start+3): # loop grid height
            if(board[i][j] == str(num)): 
                return False
    return True
    
def solve(self, board):       
    row, col = 0, 0
    x = empty_square(self, board, 0,0)
    
    # if no empty squares
    if x[2] == 0:
        return True
    
    row=x[0]
    col=x[1]

    # try to insert #1-9 into empty grid
    for i in range(1,10):
        # check to assign i to square
        if is_valid(self, board, row, col, i):
            board[row][col] = str(i)

            if solve(self, board):
                return True
            
            # prev num doesn't work
            # try again
            board[row][col]=str(-1)
            
    # backtrack
    return False
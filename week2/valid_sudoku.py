# Jenny Huang
# Wallbreakers Cohort #3
# Week 2
# Valid Sudoku
# https://leetcode.com/problems/valid-sudoku/

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # check rows
        for row in board:
            row_set = set()
            # get each num per row
            for num in row:
                # check if num is in set
                if num not in row_set:
                    row_set.add(num)
                # ignore "."
                elif num == ".":
                    continue
                # return False if num is seen again
                else:
                    return False
        
        # check cols
        for i in range(len(board)):
            col_set = set()
            # get each num per col
            for j in range(len(board[i])):
                # check if num is in set
                if board[j][i] not in col_set:
                    col_set.add(board[j][i])
                # ignore "."
                elif board[j][i] == ".":
                    continue
                # return False if num is seen again
                else:
                    return False
                
        # check squares
        inc = -3
        # loop through rows every 3
        for i in range(0, len(board), 3):
            inc += 3 # incremental counter
            # loop through columns
            for j in range(len(board)):
                row = board[j]
                # create a new set per square                    
                if j == 0 or j % 3 == 0:
                    square_set = set()
                
                # get the 3 nums in each row
                three_nums = row[inc:(3+inc)]
                for num in three_nums:
                    # check if num is in set
                    if num not in square_set:
                        square_set.add(num)
                    # ignore "."
                    elif num == ".":
                        continue
                    # return False if num is seen again
                    else:
                        return False
        return True
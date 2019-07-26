# Jenny Huang
# Wallbreakers Cohort #3
# Week 5
# Word Search
# https://leetcode.com/problems/word-search/

class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        row = len(board)
        col = len(board[0])
        
        for i in range(row):
            for j in range(col):
                if dfs(self, i, j, board, 0, word):
                    return True
        
def dfs(self, i, j, board, index, word):
    if index == len(word):
        return True
    # check boundaries
    if i < 0 or j < 0 or i == len(board) or j == len(board[0]):
        return False
    if board[i][j] != word[index]: # look for word
        return False
    letter_found = board[i][j]
    board[i][j] = '0' # replace letter_found so we don't look at it again
    # look around for next letter
    a = dfs(self, i-1, j, board, index+1, word) or dfs(self, i+1, j,board, index+1, word) or dfs(self, i, j-1, board, index+1, word) or dfs(self, i, j+1, board, index+1, word) 
    # backtrack
    board[i][j] = letter_found
    return a
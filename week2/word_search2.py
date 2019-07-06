# Jenny Huang
# Wallbreakers Cohort #3
# Week 2
# Word Search II
# https://leetcode.com/problems/word-search-ii/

class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = {}
        self.end = "*"

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        current = self.head

        for char in word:
            if char not in current:
                current[char] = {}
            current = current[char]
            
        current[self.end] = word             

class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        # build trie of words
        trie = Trie()
        for word in words:
            trie.insert(word)
        
        output_words = []

        visited = []        
        # set each char in board with visited = False        
        for i in range(len(board)):
            visited_row = []
            for j in range(len(board[0])):
                visited_row.append(False)
            visited.append(visited_row)

        # loop through board and visit each char 
        # to check if trie is in board
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.visit(i, j, board, trie.head, output_words, visited)
                
        # return a set to remove duplicates
        return set(output_words)
    
    def visit(self, i, j, board, trie, output_words, visited):
        # already visited this char
        if visited[i][j]:
            return

        current_char = board[i][j]
        
        # character isn't in trie.head
        if current_char not in trie:
            return
        
        # visited char
        visited[i][j] = True
        
        # get the trie.head with current char
        trie = trie[current_char]
        
        if "*" in trie:
            word =  trie["*"]
            output_words.append(word)

        # get a list of [i,j] positions of neighbors of char
        neighbors = self.lookAround(i, j, board, visited)
        
        # visit neighbors
        for char in neighbors:
            self.visit(char[0], char[1], board, trie, output_words, visited)

        visited[i][j] = False
    
    # look around board for neighbors
    def lookAround(self, i, j, board, visited):
        neighbors = []
        # look above
        if (i > 0 and not visited[i-1][j]):
            neighbors.append([i-1,j])
        # look left
        if (j > 0 and not visited[i][j-1]):
            neighbors.append([i,j-1])
        # look down
        if (i < (len(board)-1) and not visited[i+1][j]):
            neighbors.append([i+1,j])
        # look right
        if (j < (len(board[0])-1) and not visited[i][j+1]):
            neighbors.append([i,j+1])
        return neighbors

# Jenny Huang
# Wallbreakers Cohort #3
# Week 2
# Longest Word in Dictionary
# https://leetcode.com/problems/longest-word-in-dictionary/

class TrieNode:
    def __init__(self):
        self.head = {}
        self.end = False
        
class Trie(object):
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word):
        # build Trie
        trie = self.root
        
        for i in range(len(word)):
            current = word[i]
            if current not in trie.head:
                    trie.head[current] = TrieNode()
            trie = trie.head[current]
        trie.end = True

class Solution(object):
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        # build trie 
        trie = Trie()
        for word in words:
            trie.insert(word)
        
        # dfs to look through trie
        return self.dfs(trie.root)
    
    def dfs(self, root):
        longest_word = ""

        for char in root.head:
            if root.head[char].end:
                long_word = char + self.dfs(root.head[char])
                # check which word is longer
                # if words are same length, return word
                # with smallest lexographical order
                if (len(longest_word) > len(long_word) or (len(longest_word) == len(long_word) and longest_word <= long_word)):
                    longest_word = longest_word
                else:
                    longest_word = long_word
        return longest_word
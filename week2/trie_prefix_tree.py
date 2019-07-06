# Jenny Huang
# Wallbreakers Cohort #3
# Week 2
# Implement Trie (Prefix Tree)
# https://leetcode.com/problems/implement-trie-prefix-tree/

class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = {}

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        #trie = self.root
        current = self.head
        
        for char in word:
            if char not in current:
                current[char] = {}
            current = current[char]
            
        current['*'] = True                

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        current = self.head
        
        for char in word: 
            if char not in current:
                return False
            current = current[char]
            
        if '*' in current:
            return True
        else:
            return False

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        current = self.head
        
        for char in prefix: 
            if char not in current:
                return False
            current = current[char]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

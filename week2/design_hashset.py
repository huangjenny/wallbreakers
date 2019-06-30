# Jenny Huang
# Wallbreakers Cohort #3
# Week 2
# Design HashSet
# https://leetcode.com/problems/design-hashset/

class MyHashSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.set = set()
        

    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        self.set.add(key)

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        self.set.discard(key)

    def contains(self, key):
        """
        Returns true if this set contains the specified element
        :type key: int
        :rtype: bool
        """
        if key in self.set:
            return True
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
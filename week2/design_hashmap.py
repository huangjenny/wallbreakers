# Jenny Huang
# Wallbreakers Cohort #3
# Week 2
# Design HashMap
# https://leetcode.com/problems/design-hashmap/

class MyHashMap(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dict = {}

    def put(self, key, value):
        """
        value will always be non-negative.
        :type key: int
        :type value: int
        :rtype: None
        """
        self.dict[key] = value

    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        """
        if key in self.dict.keys():
            return self.dict.get(key)
        else:
            return -1
        

    def remove(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        :type key: int
        :rtype: None
        """
        if key in self.dict.keys():
            del self.dict[key]

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
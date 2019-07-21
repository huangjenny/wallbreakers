# Jenny Huang
# Wallbreakers Cohort #3
# Week 4
# LRU Cache
# https://leetcode.com/problems/lru-cache/

# use OrderedDict to utilize move_to_end and popitem
from collections import OrderedDict

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.dict = OrderedDict()

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        # check if key exists
        if key in self.dict.keys():
            self.dict.move_to_end(key)
            return self.dict[key]
        return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        # insert key, value if exists
        if key in self.dict:
            self.dict.move_to_end(key)
            self.dict[key] = value
            
        # check capacity before inserting new key, value
        else:
            # capacity not reached yet
            # insert new key, value
            if len(self.dict) < self.capacity:
                self.dict[key] = value
            # capacity reached
            # remove LRU 
            else:
                # set last = False to pop in FIFO order
                self.dict.popitem(False)
                self.dict[key] = value     

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
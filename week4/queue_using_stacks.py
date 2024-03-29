# Jenny Huang
# Wallbreakers Cohort #3
# Week 4
# Implement Queue Using Stacks
# https://leetcode.com/problems/implement-queue-using-stacks/

class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = []

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        self.queue.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        if len(self.queue) > 0:
            return self.queue.pop(0)
        return None

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if len(self.queue) > 0:
            return self.queue[0]
        return None

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        if len(self.queue) > 0:
            return False
        return True


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
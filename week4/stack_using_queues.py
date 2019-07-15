# Jenny Huang
# Wallbreakers Cohort #3
# Week 4
# Implement Stack Using Queues
# https://leetcode.com/problems/implement-stack-using-queues/

class MyStack(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = []

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: None
        """
        self.stack.append(x)

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        if len(self.stack) > 0:
            return self.stack.pop(-1)

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        if len(self.stack) > 0:
            return self.stack[-1]
        return None

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        if len(self.stack) > 0:
            return False
        return True


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
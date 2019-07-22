# Jenny Huang
# Wallbreakers Cohort #3
# Week 1
# Friend Circles
# https://leetcode.com/problems/friend-circles/

class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        parents_list = [-1] * len(M)
        #print parents_list
        
        # union 2 friend circles into 1
        def union(parent_list, i, j):
            parent_i = get_parent(parent_list, i)
            parent_j = get_parent(parent_list, j)
            
            if parent_i != parent_j:
                parents_list[parent_i] = parent_j
        
        # check for unique parents
        def get_parent(parents_list, i):
            if parents_list[i] == -1:
                return i
            return get_parent(parents_list, parents_list[i])
    
        # look for friends
        for i in range(len(M)):
            for j in range(i+1, len(M)):
                if M[i][j] == 1:
                    union(parents_list, i, j)
        
        count = 0
        # count how many friend circles there are
        for i in range(len(parents_list)):
            if parents_list[i] == -1:
                count += 1
        
        return count
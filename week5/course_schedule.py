# Jenny Huang
# Wallbreakers Cohort #3
# Week 5
# Course Schedule
# https://leetcode.com/problems/course-schedule/

from collections import defaultdict

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        freq_dict = {}
        for i in range(numCourses):
            freq_dict[i] = 0
        adj=defaultdict(set)
        visited=False
        
        # create dictionaries for 
        # frequency of edge
        # and edges
        for i,j in prerequisites:
            freq_dict[i] +=1
            adj[j].add(i)
        
        ts = []
        for i in range(numCourses):
            if freq_dict[i] == 0:
                visited = True
                ts.append(i)
        
        # cycle is detected
        if visited == False:
            return False
        # no cycle
        # apply topological sorting
        else:
            while(ts):
                node = ts.pop()
                #print node
                for i in adj[node]:
                    freq_dict[i]-=1
                    if freq_dict[i]==0:
                        ts.append(i)
        
        # check frequency is 0
        # to ensure no cycles
        for i in range(numCourses):
            if freq_dict[i] > 0:
                return False
        return True
# Jenny Huang
# Wallbreakers Cohort #3
# Week 5
# Course Schedule 2
# https://leetcode.com/problems/course-schedule-ii/

from collections import defaultdict

class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        output = []
        if not prerequisites:
            for i in range(numCourses):
                output.append(i)
            output.sort(reverse=True)
            return output
        
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
            return []
        # no cycle
        # apply topological sorting
        else:
            while(ts):
                node = ts.pop()
                output.append(node)
                for i in adj[node]:
                    freq_dict[i]-=1
                    if freq_dict[i]==0:
                        ts.append(i)
        
        if len(output) != len(freq_dict.keys()):
            return []
        return output
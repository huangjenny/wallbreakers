# Jenny Huang
# Wallbreakers Cohort #3
# Week 5
# Is Graph Bipartite
# https://leetcode.com/problems/is-graph-bipartite/

class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        self.bipartite = True
        color = {}
        for i in range(len(graph)):
            if i not in color and self.bipartite:
                color[i] = 0
                color_dfs(self, i, graph, color)
        return self.bipartite

def color_dfs(self, i, graph, color):
    for j in graph[i]:
        if j not in color:
            color[j] = 1-color[i]
            color_dfs(self, j, graph, color)
        else:
            if color[j] == color[i]:
                self.bipartite = False
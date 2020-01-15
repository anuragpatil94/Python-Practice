"""
    This is the implementation of Dijkstra's Single source shortest path algorithm
"""
# from AdjacencyList import AdjacencyList
import math
import json


class Dijkstra:
    def __init__(self, graph, source):
        self.g = graph
        self.source = source
        pass

    def run(self):
        '''Time Complexity Vlog(E)'''
        # Initialize Parent Dictionary
        parent = {}
        # Initialize minDistance Dictionary
        minDistance = {}
        # Initalize Initial which represents the current state of the traversal
        initial = {}
        # Initialize each node to infinity, which means that the node is at that distance to source.
        for key in self.g:
            initial[key] = math.inf
        # Init Source Values
        initial[self.source] = 0
        parent[self.source] = None

        # Loop through initial that is all the nodes such that we always take minimum distance first.
        while initial:
            
            node = self.extractMin(initial)
            minDistance[node] = initial[node]
            initial.pop(node)
            for edge in g[node]:
                # Check if edge is in initial. This will make sure that we don't parse the node for which we have already found min distance
                if edge[0] in initial:
                    # Compare the distance
                    if minDistance[node] + edge[1] < initial[edge[0]]:
                        initial[edge[0]] = minDistance[node] + edge[1]
                        parent[edge[0]] = node
        return [parent, minDistance]

    def extractMin(self, initial):
        ''' Time Complexity : O(V) '''
        min = math.inf
        minIndex = None
        for key in initial:
            if initial[key] < min:
                minIndex = key
                min = initial[key]
        return minIndex


if __name__ == "__main__":
    # AdjList [edge,weight]
    g = {
        1: [[2, 2], [3, 1], [4, 9]],
        2: [[1, 2], [3, 4]],
        3: [[2, 4], [1, 1], [6, 4]],
        4: [[1, 9], [5, 7], [6, 6]],
        5: [[6, 2], [4, 7]],
        6: [[4, 6], [3, 4], [5, 2]],
    }
    d = Dijkstra(g, 1)
    print(d.run())

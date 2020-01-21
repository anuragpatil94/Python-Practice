"""
This algorithm uses DFS to do a topological sort for 1 round of Bellman Ford
"""
from AdjacencyList import AdjacencyList
import math


class SingleSourceShortestPath:
    def __init__(self, graph):
        self.graph = graph

    def listVertices(self):
        return list(self.graph.keys())

    def listAllEdges(self,):
        edgeList = []
        for key, edges in self.graph.items():
            for edge in edges:
                if edge:
                    edgeList.append(edge)
        return edgeList

    def findShortestPath(self, source):
        vertices = self.listVertices()
        distances = {}
        for vertex in vertices:
            distances[vertex] = math.inf

        distances[source] = 0

        edges = self.listAllEdges()
        print(edges)
        for i in range(0, len(vertices) - 1):
            for edge in edges:
                if distances[edge[1]] > distances[edge[0]] + edge[2]:
                    distances[edge[1]] = distances[edge[0]] + edge[2]

        for edge in edges:
            if distances[edge[1]] > distances[edge[0]] + edge[2]:
                print("Cycle Found")
                return -1
        return distances


if __name__ == "__main__":
    graph = {
        "A": [["A", "B", 2], ["A", "E", 4]],
        "B": [["B", "D", 3], ["B", "C", 5], ["B", "E", 1]],
        "C": [[]],
        "D": [["D", "F", 2], ["D", "G", 6]],
        "E": [["E", "D", 1]],
        "F": [["F", "C", 4]],
        "G": [[]],
    }
    S = SingleSourceShortestPath(graph)
    print(S.findShortestPath("A"))
    pass

from AdjacencyList import AdjacencyList
import json

class BFS:
    def BFS(self, source, list: AdjacencyList):
        level = {source: 0}
        parent = {source: None}
        levelNumber = 1
        frontier = [source]
        while frontier:
            next = []
            for u in frontier:
                current = list.getVertex(u)
                while current is not None:
                    if current.val not in level:
                        level[current.val] = levelNumber
                        parent[current.val] = u
                        next.append(current.val)
                    current = current.next
            frontier = next
            levelNumber+=1
        return level,parent

if __name__=="__main__":
    list = AdjacencyList()
    list.addVertex("a")
    list.addVertex("z")
    list.addVertex("s")
    list.addVertex("x")
    list.addVertex("d")
    list.addVertex("c")
    list.addVertex("f")
    list.addVertex("v")
    list.addEdge("a","z")
    list.addEdge("a","s")
    list.addEdge("s","x")
    list.addEdge("x","d")
    list.addEdge("x","c")
    list.addEdge("c","d")
    list.addEdge("c","f")
    list.addEdge("c","v")
    list.addEdge("f","v")
    list.addEdge("z","a")
    list.addEdge("s","a")
    list.addEdge("x","s")
    list.addEdge("d","x")
    list.addEdge("c","x")
    list.addEdge("d","c")
    list.addEdge("f","c")
    list.addEdge("v","c")
    list.addEdge("v","f")
    print(list.print_graph())
    print("--")
    bfs = BFS()
    level,parent = bfs.BFS("s",list)
    print(json.dumps(level,indent=4))
    print(json.dumps(parent,indent=4))
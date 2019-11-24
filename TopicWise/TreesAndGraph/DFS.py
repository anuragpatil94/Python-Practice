from AdjacencyList import AdjacencyList
import json


class DFS:
    def DFS_Visit(self, source, list, parent):
        current = list.getVertex(source)
        while current is not None:
            # print(current,current.val)
            if current.val not in parent:
                parent[current.val] = source
                self.DFS_Visit(current.val, list, parent)
            current = current.next

    def DFS(self, list):
        parent = {}
        for vertex in list:
            if vertex.val not in parent:
                parent[vertex.val] = None
                self.DFS_Visit(vertex.val, list, parent)
        return parent


if __name__ == "__main__":
    list = AdjacencyList()
    list.addVertex("a")
    list.addVertex("b")
    list.addVertex("c")
    list.addVertex("d")
    list.addVertex("e")
    list.addVertex("f")
    list.addEdge("a", "b")
    list.addEdge("a", "d")
    list.addEdge("b", "e")
    list.addEdge("d", "b")
    list.addEdge("e", "d")
    list.addEdge("c", "e")
    list.addEdge("c", "f")
    list.addEdge("f", "f")
    print(list.print_graph())
    print("--")
    dfs = DFS()
    # DFS_Visit("a",list)
    parent = dfs.DFS(list)
    print(json.dumps(parent, indent=4))

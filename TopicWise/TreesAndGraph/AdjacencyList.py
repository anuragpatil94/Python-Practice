class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class AdjacencyList:
    def __init__(self):
        self.list = []

    def getIndex(self, index):
        return self.list[index]

    def getVertex(self, vertex):
        for node in self.list:
            if node.val == vertex:
                return node

    def addVertex(self, val):
        newNode = Node(val)
        self.list.append(newNode)
        return newNode

    def addEdge(self, From, To):
        edge = None
        for vertex in self.list:
            if vertex.val == To:
                edge = vertex
                break
        if not edge:
            raise Exception
        edge = Node(To)
        for vertex in self.list:
            if vertex.val == From:
                current = vertex
                while current.next is not None:
                    current = current.next
                current.next = edge
                break

    def __iter__(self):
        self.start = 0
        return self

    def __next__(self):
        start = self.start
        # print("len =",start, len(self.list) )
        if self.start >= len(self.list):
            raise StopIteration
        self.start = start + 1
        return self.list[start]

    def __len__(self):
        return len(self.list)

    # Function to print the graph
    def print_graph(self):
        for i in range(len(self.list)):
            print("head", end="")
            temp = self.list[i]
            while temp:
                print(" -> {}".format(temp.val), end="")
                temp = temp.next
            print(" \n")


# if __name__ == "__main__":
#     list = AdjacencyList()
#     list.addVertex("A")
#     list.addVertex("B")
#     list.addVertex("C")
#     list.addVertex("D")
#     list.addVertex("E")
#     list.addVertex("F")
#     list.addVertex("G")

#     # for vertex in list:
#     #     print(vertex.val)

#     # for index in range(len(list)):
#     #     print(index)
#     # print( type(list))
#     # print(list.getIndex(1))
#     list.addEdge("A","B")
#     list.addEdge("A","D")
#     list.addEdge("A","C")
#     list.addEdge("B","A")
#     list.addEdge("C","E")
#     list.addEdge("C","A")
#     list.addEdge("D","E")
#     list.addEdge("D","F")
#     list.addEdge("D","G")
#     list.addEdge("E","D")
#     list.addEdge("F","G")
#     list.addEdge("G","F")
#     list.print_graph()

"""
4.6 Successor: 
Write an algorithm to find the "next" node (i.e., in-order successor) of a given node in a
binary search tree. You may assume that each node has a link to its parent. 
"""


class Node:
    def __init__(self, value=None):
        self.left = None
        self.right = None
        self.parent = None
        self.val = value


class Solution:
    def __init__(self):
        pass

    def successor(self, node: Node):
        if node.right:
            if not node:
                return None
            node = node.right
            while node.left is not None:
                node = node.left
            return node
        else:
            parent = node.parent
            current = node

            while parent is not None and parent.left is not current:
                current = parent
                parent = current.parent
            return parent


if __name__ == "__main__":
    s = Solution()

    # Create Tree
    A = Node("D")
    B = Node("B")
    C = Node("F")
    D = Node("A")
    E = Node("C")
    F = Node("E")
    G = Node("G")

    root = A
    A.left = B
    A.right = C

    B.left = D
    B.right = E
    B.parent = A

    C.left = F
    C.right = G
    C.parent = A

    D.parent = B
    E.parent = B

    F.parent = C
    G.parent = C

    print(" D -> ", (s.successor(A)).val)
    print(" B -> ", (s.successor(B)).val)
    print(" F -> ", (s.successor(C)).val)
    print(" A -> ", (s.successor(D)).val)
    print(" C -> ", (s.successor(E)).val)
    print(" E -> ", (s.successor(F)).val)
    print(" G -> ", (s.successor(G)))

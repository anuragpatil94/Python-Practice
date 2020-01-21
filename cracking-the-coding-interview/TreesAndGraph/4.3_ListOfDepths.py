"""
List of Depths: 
Given a binary tree, design an algorithm which creates a linked list of all the nodes at each depth 
(e.g., if you have a tree with depth D, you'll have D linked lists). 

Graph Traversal - BFS or DFS
"""


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None


def listOfDepths(root):
    d = dict()
    q = [root]
    level = 1
    while q:
        next = []
        for node in q:
            current = node
            if current is None:
                addToD(d, level, "null")
            else:
                if not current.left and not current.right:
                    pass
                else:
                    next.append(current.left)
                    next.append(current.right)
                addToD(d, level, current.data)
        q = next
        level += 1
    return d
    pass


def addToD(d, level, value):
    if level not in d:
        d[level] = ListNode(value)
    else:
        current = d[level]
        while current.next is not None:
            current = current.next
        current.next = ListNode(value)


if __name__ == "__main__":
    a = TreeNode(1)
    b = TreeNode(2)
    c = TreeNode(3)
    d = TreeNode(4)
    e = TreeNode(5)
    f = TreeNode(6)
    g = TreeNode(7)
    h = TreeNode(8)
    i = TreeNode(9)
    j = TreeNode(10)
    k = TreeNode(11)

    root = a
    root.left = b
    root.right = c
    b.left = d
    b.right = e
    c.left = f
    f.left = j
    f.right = k
    d.left = g
    d.right = h
    e.left = i

    y = listOfDepths(root)
    for key in y:
        x = y[key]
        print(key, end=" - ")
        while x is not None:
            print(x.data, end=" , ")
            x = x.next
        print()

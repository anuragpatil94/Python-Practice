"""
A linked list is given such that each node contains an additional random 
pointer which could point to any node in the list or null.

Return a deep copy of the list.

The Linked List is represented in the input/output as a list of n nodes. 
Each node is represented as a pair of [val, random_index] where:

val: an integer representing Node.val
random_index: the index of the node (range from 0 to n-1) where random 
pointer points to, or null if it does not point to any node.
 

Example 1:


Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]
Example 2:


Input: head = [[1,1],[2,1]]
Output: [[1,1],[2,1]]
Example 3:



Input: head = [[3,null],[3,0],[3,null]]
Output: [[3,null],[3,0],[3,null]]
Example 4:

Input: head = []
Output: []
Explanation: Given linked list is empty (null pointer), so return null.
 

Constraints:

    -10000 <= Node.val <= 10000
    Node.random is null or pointing to a node in the linked list.
    Number of Nodes will not exceed 1000.
"""


class Node:
    def __init__(self, x, next, random):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList1(self, head):
        # My Solution: O(n) O(n)
        current = head
        newHead = None
        d = {}
        q = []
        previous = None
        while current:
            newNode = Node(current.val)
            if previous:
                previous.next = newNode
            if not newHead:
                newHead = newNode
            d[current] = newNode
            if current.random:
                q.append((current, current.random))
            previous = newNode
            current = current.next

        while q:
            current = q.pop()
            start = d[current[0]]
            end = d[current[1]]
            start.random = end
        return newHead

    def copyRandomList2(self, head: "Node") -> "Node":
        self.copies = {}
        return self._copy(head)

    def _copy(self, node: "Node") -> "Node":
        if node is None:
            return None

        if node in self.copies:
            return self.copies[node]

        copy = Node(node.val)
        self.copies[node] = copy

        copy.next = self._copy(node.next)
        copy.random = self._copy(node.random)

        return copy

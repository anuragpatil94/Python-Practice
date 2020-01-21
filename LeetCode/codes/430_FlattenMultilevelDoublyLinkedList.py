class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Solution:
    def flatten(self, head: "Node") -> "Node":
        if not head:
            return head
        current = head
        l = list()
        while current:
            if current.child:
                if current.next:
                    l.append(current.next)
                current.next = current.child
                current.next.prev = current
                current.child = None
            else:
                if not current.next:
                    if len(l):
                        current.next = l.pop()
                        current.next.prev = current
                    else:
                        break
            current = current.next
        return head

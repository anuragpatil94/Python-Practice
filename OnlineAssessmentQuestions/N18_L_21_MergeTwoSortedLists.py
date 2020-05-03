"""

Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # Create a new Pointer
        h = x = ListNode(None)

        # Run Until One of them is NOne
        while l1 and l2:
            # The idea here is that the point l1 will always point to the lowest value so that everytime we add the lowest value to the pointer x and thenincrement it
            if l1.val > l2.val:
                l1, l2 = l2, l1
            x.next = l1
            # This herebasically starts from one point before so we are always adding a new value to the current max value.
            x = x.next
            l1 = l1.next
        cur = h
        x.next = l1 or l2
        return h.next

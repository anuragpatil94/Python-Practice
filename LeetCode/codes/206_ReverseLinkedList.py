"""
Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
Follow up:

A linked list can be reversed either iteratively or recursively. 
Could you implement both?

"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        """
        Time Complexity:O(n)
        Space Complexity:O(1)
        """
        prev = None
        current = head
        nextNode = None
        if current is None:
            return None
        if current.next is None:
            return current
        while current.next:
            nextNode = current.next
            current.next = prev
            prev = current
            current = nextNode
        current.next = prev
        return current

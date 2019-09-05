# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        ''' Time Complexity: O(n) Space Complexity O(1) '''
        slow = None
        fast = head
        prev = ListNode(None)
        
        while n > 1:
            if(fast.next is not None):
                fast = fast.next
                n-=1
        slow = head
        while fast.next is not None:
            fast = fast.next
            prev = slow
            slow = slow.next
        
        if slow.next is None:
            if(slow == head):
                return None
            prev.next = None
        else:
            slow.val = slow.next.val
            slow.next = slow.next.next
        
        return head
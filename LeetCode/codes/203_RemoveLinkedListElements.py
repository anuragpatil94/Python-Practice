'''

Remove all elements from a linked list of integers that have value val.

'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        '''
        Time Complexity: O(n)
        Space Complexity: O(1)
        '''
        while head  and head.val == val:
            head = head.next
        if not head:
            return head
        curr = head
        
        prev = None
        while curr:
            if curr.val == val:
                if not curr.next:
                    prev.next = None
                    curr = curr.next
                else:
                    curr.val = curr.next.val
                    curr.next = curr.next.next
            else:
                prev = curr
                curr = curr.next 
                
        return head
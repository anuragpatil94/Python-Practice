'''
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        '''Time and Space O(n)'''
        h = x = ListNode(None)
        while l1 and l2:
            if l1.val > l2.val: 
                l1,l2 =l2,l1
            x.next = l1
            x = x.next
            l1 = l1.next
        x.next = l1 or l2
        return h.next

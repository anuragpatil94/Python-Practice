'''

Given a linked list, return the node where the cycle begins. 
If there is no cycle, return null.

To represent a cycle in the given linked list, 
we use an integer pos which represents the position (0-indexed) 
in the linked list where tail connects to. If pos is -1, 
then there is no cycle in the linked list.

'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        Time Complexity: O(n) Space Complexity:O(1)
        """
        if not head:
            return None
        
        slow, fast = head, head
        
        while True:
            if not fast.next or not fast.next.next: # no loop
                return None
            
            slow, fast = slow.next, fast.next.next
            if slow == fast:    #meet
                break
        
        # has loop
        slow, fast = head, slow # second run
        index  = 0   
        while slow != fast:
            index += 1
            slow, fast = slow.next, fast.next
        return slow
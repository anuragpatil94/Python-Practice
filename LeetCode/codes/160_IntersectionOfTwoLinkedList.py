'''
Write a program to find the node at which the intersection of 
two singly linked lists begins.
'''

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        Time Complexity O(n + m)
        Space Complexity (1)
        """
        if not headA or not headB:
            return None
        currA = headA
        currB = headB
        tA = 0
        tB = 0
        while currA and currB:
            if tA > 1 and tB > 1:
                return None
            if currA == currB:
                return currA
            if not currA.next:
                currA = headB
                tA+=1
            else:
                currA = currA.next
            if not currB.next:
                currB = headA
                tB+=1
            else:
                currB = currB.next
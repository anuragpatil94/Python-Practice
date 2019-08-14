'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
'''
'''
SAME AS ./cracking-the-coding-interview/LinkedList/2.5
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        head = ListNode(0)
        current = head
        while l1 is not None or l2 is not None:
            x = 0 if l1 is None else l1.val
            y = 0 if l2 is None else l2.val
            
            sum = x + y + carry
            carry = sum//10

            current.next = ListNode(sum % 10)
            current = current.next

            # only iterate when l1 or l2 is not None. This will take care of the case when l1 and l2 doesn't have same length
            if l1 is not None:
                l1=l1.next
            if l2 is not None:
                l2=l2.next
        # If a Carry remains at the end of the addition.
        if(carry):
            current.next = ListNode(carry)
        # return next since we store the result from second node.
        return head.next
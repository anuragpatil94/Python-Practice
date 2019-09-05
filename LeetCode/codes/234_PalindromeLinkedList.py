'''

Given a singly linked list, determine if it is a palindrome.

Example 1:

Input: 1->2
Output: false
Example 2:

Input: 1->2->2->1
Output: true
Follow up:
Could you do it in O(n) time and O(1) space?

idea:
Reverse half of the linked list and then compare both half

'''

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        '''
        Time Complexity: O(n)
        Space Complexity: O(1)
        '''
        if not head:
            return True
        if head.next is None:
            return True
        slow = head
        fast = head.next
        aux = None
        prev = None
        
        while fast and fast.next:
            aux = slow.next
            slow.next = prev
            prev = slow
            slow = aux
            fast = fast.next.next
        
        if fast:
            aux = slow.next
            slow.next = prev
        else:
            slow = prev
            aux = aux.next
            
        while slow and aux:
            if slow.val == aux.val:
                slow = slow.next
                aux = aux.next
            else:
                return False
                
        if slow or aux:
            return False
        else:
            return True
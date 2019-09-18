'''
Given a linked list, rotate the list to the right by k places, where k is non-negative.

Example 1:

    Input: 1->2->3->4->5->NULL, k = 2
    Output: 4->5->1->2->3->NULL
    Explanation:
        rotate 1 steps to the right: 5->1->2->3->4->NULL
        rotate 2 steps to the right: 4->5->1->2->3->NULL

Example 2:

    Input: 0->1->2->NULL, k = 4
    Output: 2->0->1->NULL
    Explanation:
        rotate 1 steps to the right: 2->0->1->NULL
        rotate 2 steps to the right: 1->2->0->NULL
        rotate 3 steps to the right: 0->1->2->NULL
        rotate 4 steps to the right: 2->0->1->NULL

'''

class Solution:
    def rotateRight(head, k):
        '''
        Time Complexity: O(n)
        Space Complexity: O(1)
        '''
        if not head:
            return head

        fast = head
        slow = head
        length = 0
        
        # To get the length of the Linked List
        while slow:
            length += 1
            slow = slow.next
        
        slow = head
        
        # Total Moves required based on the length of Linked List
        newK = k%length

        # move fast pointer newK times ahead of the slow pointer
        while True:
            if newK:
                fast = fast.next
                newK -= 1
            else:
                break
        
        # move fast and slow at same time
        while fast.next:
            fast = fast.next
            slow = slow.next
        
        # Modify the links
        if slow.next:
            newHead = slow.next
            # Join last node with head 
            fast.next = head
            head = newHead
            # Disconnect the new last node
            slow.next = None

        return head
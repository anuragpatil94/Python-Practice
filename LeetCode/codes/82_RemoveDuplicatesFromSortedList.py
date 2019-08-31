'''

Given a sorted linked list, delete all duplicates such that each element appear only once.

Example 1:

Input: 1->1->2
Output: 1->2
Example 2:

Input: 1->1->2->3->3
Output: 1->2->3

Idea:
Keep track of the 1st Duplicate Node. If a Next node with different value is found link firstDuplicateNode to the next Node. For Comparing, compare current and next node.

Test Cases:
 1) [1,1,1,1,1,1]
 2) [1,1,2,2,3,4]
 3) [1]
 4) [1,2,3,3,3,3,3,3,3,4]
Missed Testcase:
 1) Empty List

'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    ''' Time O(n) Space O(1) '''
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        curr = head
        firstDuplicateNode = None
        while curr and curr.next:
            if not firstDuplicateNode and curr.val == curr.next.val:
                firstDuplicateNode = curr
            elif(firstDuplicateNode and curr.val != curr.next.val):
                firstDuplicateNode.next = curr.next
                firstDuplicateNode = None
            curr = curr.next
        
        if firstDuplicateNode:
            firstDuplicateNode.next = None
        return head
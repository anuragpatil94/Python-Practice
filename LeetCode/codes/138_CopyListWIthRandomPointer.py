'''

A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

Return a deep copy of the list.

Example 1:

Input:
{"$id":"1","next":{"$id":"2","next":null,"random":{"$ref":"2"},"val":2},"random":{"$ref":"2"},"val":1}

Explanation:
Node 1's value is 1, both of its next and random pointer points to Node 2.
Node 2's value is 2, its next pointer points to null and its random pointer points to itself.
 

Note:

You must return the copy of the given head as a reference to the cloned list.

'''

class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random

class Solution:
    def copyRandomList_MySolution(self, head: 'Node') -> 'Node':
        '''
            Time O(n)
            Space O(n)
        '''
        if not head:
            return head
        
        mapping = dict()
        
        newHead = Node(head.val, head.next,head.random)
        mapping[head] = newHead
        if head.next: 
            current = head.next
        else: 
            if newHead.random:
                newHead.random = mapping[head]
            return newHead
        
        newCurrent = newHead
        
        while current:
            newNode = Node(current.val,current.next,current.random)
            newCurrent.next = newNode
            mapping[current] = newNode
            current = current.next
            newCurrent = newCurrent.next
            
        newCurrent = newHead
        while newCurrent:
            if newCurrent.random:
                newCurrent.random = mapping[newCurrent.random]
            newCurrent =newCurrent.next
        
        return newHead
    

    def copyRandomList_BestSolution(self, head: 'Node') -> 'Node':
        '''
        Time O(n)
        Space O(1)
        '''
        if head == None:
            return None
        if head.next == None:
            new_head = Node(head.val, head.next, None)
            if head.random == head:
                new_head.random = new_head
            return new_head
        
        
        node = head
        while node != None:
            new_node = Node(node.val, None, None)
            
            tmp = node.next
            node.next = new_node
            new_node.next = tmp
            
            node = new_node.next
            
        node = head
        while node != None:
            new_node = node.next
            if node.random != None:
                new_node.random = node.random.next
            node = new_node.next
            
        new_head = head.next
        node1 = head
        node2 = new_head
        while node2.next != None:
            node1.next = node1.next.next
            node1 = node1.next
            
            node2.next = node2.next.next
            node2 = node2.next
            
        node1.next = node1.next.next
        return new_head
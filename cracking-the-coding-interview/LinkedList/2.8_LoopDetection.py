import sys
sys.path.insert(0, '../../')
from conceptual.linked_list import LinkedList
'''

2.8 Loop Detection: 
Given a circular linked list, implement an algorithm that returns the node at the beginning of the loop. 
DEFINITION 
    Circular linked list: A (corrupt) linked list in which a node's next pointer points to an earlier node, 
    so as to make a loop in the linked list. 
EXAMPLE 
    Input: A -> B -> C -> D -> E -> C [the same C as earlier] 
    Output: C 


Solution 1:
Take a set and store the new nodes in the set. Whenever a duplicate node, return that which will be the start of the loop.

TIME COMPLEXITY O(n)
SPACE COMPLEXITY O(n)`

Solution 2:
This is using Fast Pointer and Slow Pointer

''' 

def Solution1(head):
    s = set()
    current = head

    while(current.next is not None):
        if current not in s:
            s.add(current)
        else:
            return current.data
        current = current.next
    return -1
    pass

def Solution2(head):
    # This is using fast and slow pointer
    if not head:
        return -1

    s = head
    f = head

    while f.next:
        s = s.next
        f = f.next.next
        if s is f:
            s = head
            break
    
    while s and f:
        if s == f:
            return s.data
        s = s.next
        f = f.next
    return -1

if __name__ == "__main__":
    l = LinkedList()
    l.push(1)
    l.push(2)
    l.push(3)
    l.push(4)
    l.push(5)
    l.push(6)
    node = l.getNode_at(6)
    l.push_node(node)
    print(Solution1(l.head))

    print(Solution2(l.head))
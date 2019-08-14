import sys
sys.path.insert(0, '../../')
from conceptual.linked_list import LinkedList

'''
Important
2.7. Intersection
Given two linked lists, determine if the two lists intersect. Return the intersecting node, 
Note that the intersection is defined based on reference, not value. That is, if the kth node of 
the first linked list is the exact same node (by reference) as the jth node of the second linked list, 
then they are intersecting.
'''

def intersection():
    pass


if __name__ == "__main__":
    l1 = LinkedList()
    l1.push("A")
    l1.push("B")
    l1.push("C")
    l1.push("B")
    l1.push("A")
    l1.show()
    
    pass
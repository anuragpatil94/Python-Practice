import sys

sys.path.insert(0, "../../")
from conceptual.linked_list import LinkedList

"""
Important
2.7. Intersection
Given two linked lists, determine if the two lists intersect. Return the intersecting node, 
Note that the intersection is defined based on reference, not value. That is, if the kth node of 
the first linked list is the exact same node (by reference) as the jth node of the second linked list, 
then they are intersecting.

Algorithm:
traverse from both list and at the end of the list jump to the next list.

TIME COMPLEXITY: O(n+m) where n and m are length of the list
SPACE COMPLEXITY: O(1)
"""


def intersection(l1, l2):
    curr1 = l1
    curr2 = l2
    cycle1, cycle2 = 0, 0
    while cycle1 < 2 or cycle2 < 2:
        if curr1 is curr2:
            return curr1.data
        if curr1.next is None:
            cycle1 += 1
            curr1 = l2
        else:
            curr1 = curr1.next
        if curr2.next is None:
            cycle1 += 1
            curr2 = l1
        else:
            curr2 = curr2.next
    return -1
    pass


if __name__ == "__main__":
    l1 = LinkedList()
    l1.push("1")
    l1.push("2")
    l1.push("3")
    l1.push("4")
    l1.push("10")
    l1.push("11")
    inter = l1.getNode_at(6)
    l1.push("5")
    l1.push("6")
    l1.push("7")

    l2 = LinkedList()
    l2.push("8")
    l2.push("9")
    l2.push_node(inter)

    l1.show()
    l2.show()
    print(intersection(l1.head, l2.head))

    l1 = LinkedList()
    l1.push("1")
    l1.push("2")
    l1.push("3")
    l1.push("4")
    inter = l1.getNode_at(4)
    l1.push("5")
    l1.push("6")
    l1.push("7")

    l2 = LinkedList()
    l2.push("8")
    l2.push("9")
    l2.push("10")
    l2.push_node(inter)

    l1.show()
    l2.show()

    print(intersection(l1.head, l2.head))

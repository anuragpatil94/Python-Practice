import sys
import random

sys.path.insert(0, '../../')

from conceptual.linked_list import LinkedList

'''
2.4 Partition: 

Write code to partition a linked list around a value x, such that all nodes less than x come before all nodes greater than or equal to x. 
If x is contained within the list, the values of x only need to be after the elements less than x (see below). 
The partition element x can appear anywhere in the "right partition"; it does not need to appear between the left and right partitions.

'''


def partition(head, x):
    current = head
    lastGreater = head
    while current is not None:
        if current.data < x:
            if lastGreater is not current:
                current.data, lastGreater.data = lastGreater.data, current.data
            lastGreater = lastGreater.next
        current = current.next 
    return True
if __name__ == "__main__":
    linked_list = LinkedList()
    # for i in range(1,40):
    #     linked_list.push(random.randint(0,100))
    linked_list.push(3)
    linked_list.push(5)
    linked_list.push(8)
    linked_list.push(5)
    linked_list.push(10)
    linked_list.push(2)
    linked_list.push(1)

    linked_list.show()
    partition(linked_list.head,5)
    linked_list.show()

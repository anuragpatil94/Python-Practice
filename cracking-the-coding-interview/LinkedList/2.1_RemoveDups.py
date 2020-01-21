import sys

sys.path.insert(0, "../../")
from conceptual.linked_list import LinkedList


"""
Remove Dups: Write code to remove duplicates from an unsorted linked list. 

FOLLOW UP 

How would you solve this problem if a temporary buffer is not allowed? 
"""

# print(sys.path)


def remove_dups_without_buffer(l):
    """ Remove Duplicates from an Unsorted Array. This function takes O(n^2) Time but O(1) Space """
    if l.empty():
        print("Linked List is Empty.")
        return
    current = l.head
    while current.next is not None:
        look = current
        while look.next is not None:
            if current.data == look.next.data:
                look.next = look.next.next
            else:
                look = look.next
        current = current.next
    pass


def remove_dups_with_buffer(l):
    """ Remove Duplicates from an Unsorted Array. Using Set as a buffer. This function runs in O(n) Time but O(m) space where m is number of duplicates """
    if l.empty():
        print("Linked List is Empty.")
        return
    distinct = set()

    current = l.head
    distinct.add(current.data)
    while current is not None:
        if current.next is not None and current.next.data in distinct:
            if current.next.next is not None:
                current.next = current.next.next
            else:
                current.next = None
                current = current.next

        else:
            distinct.add(current.data)
            current = current.next


if __name__ == "__main__":

    print("Test Cases For Remove Duplicate with Buffer".center(55, "-"))
    print("Test Case 1")
    l = LinkedList()
    l.push(2)
    l.push(9)
    l.push(4)
    l.push(6)
    l.push(9)
    l.push(4)

    l.show()
    remove_dups_with_buffer(l)
    l.show()

    print("Test Case 2")
    l = LinkedList()
    l.push(2)
    l.push(9)
    l.push(4)
    l.push(6)
    l.push(9)
    l.push(4)
    l.push(7)
    l.push(3)
    l.show()
    remove_dups_with_buffer(l)
    l.show()

    print("Test Case 3 - Empty List")
    l = LinkedList()
    remove_dups_with_buffer(l)

    print("-" * 70)
    print("Test Cases For Remove Duplicate without Buffer".center(70, "-"))
    print("Test Case 1")
    l = LinkedList()
    l.push(2)
    l.push(9)
    l.push(4)
    l.push(6)
    l.push(9)
    l.push(4)

    l.show()
    remove_dups_without_buffer(l)
    l.show()

    print("Test Case 2")
    l = LinkedList()
    l.push(2)
    l.push(9)
    l.push(4)
    l.push(6)
    l.push(9)
    l.push(4)
    l.push(7)
    l.push(3)
    l.show()
    remove_dups_with_buffer(l)
    l.show()

    print("Test Case 3 - Empty List")
    l = LinkedList()
    remove_dups_with_buffer(l)

    pass

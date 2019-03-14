'''
Remove Dups: Write code to remove duplicates from an unsorted linked list. 

FOLLOW UP 

How would you solve this problem if a temporary buffer is not allowed? 
'''


class Node:
    def __init__(self, data=None):
        self.next = None
        self.data = data


class LinkedList:
    def __init__(self):
        self.head = None

    def empty(self):
        ''' Return True if Empty '''
        if self.head is None:
            return True
        return False

    def size(self):
        ''' Returns the size of the linked list. '''
        if self.empty():
            count = 0
        else:
            n = self.head
            count = 1
            while n.next is not None:
                count += 1
                n = n.next
        return count

    def push(self, data):
        ''' adds a node in the end of the linked list '''
        n = Node(data)
        if self.empty():
            self.head = n
            return

        l = self.head
        while l.next is not None:
            l = l.next
        l.next = n
        return

    def show(self):
        ''' Shows Linked List Representation for current Linked List '''
        if self.empty():
            return "Linked List is Empty"

        l = self.head
        while l is not None:
            print(l.data, end=" ----> ")
            l = l.next
        print()
        return

    def remove_dups_without_buffer(self):
        ''' Remove Duplicates from an Unsorted Array. This function takes O(n^2) Time but O(1) Space '''
        if(self.empty()):
            print("Linked List is Empty.")
            return
        current = self.head
        while current.next is not None:
            look = current
            while look.next is not None:
                if current.data == look.next.data:
                    look.next = look.next.next
                else:
                    look = look.next
            current = current.next
        pass

    def remove_dups_with_buffer(self):
        ''' Remove Duplicates from an Unsorted Array. Using Set as a buffer. This function runs in O(n) Time but O(m) space where m is number of duplicates '''
        if(self.empty()):
            print("Linked List is Empty.")
            return
        distinct = set()

        current = self.head
        distinct.add(current.data)
        while (current is not None):
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

    print("Test Cases For Remove Duplicate with Buffer".center(55, '-'))
    print("Test Case 1")
    l = LinkedList()
    l.push(2)
    l.push(9)
    l.push(4)
    l.push(6)
    l.push(9)
    l.push(4)

    l.show()
    l.remove_dups_with_buffer()
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
    l.remove_dups_with_buffer()
    l.show()

    print("Test Case 3 - Empty List")
    l = LinkedList()
    l.remove_dups_with_buffer()

    print("-"* 70)
    print("Test Cases For Remove Duplicate without Buffer".center(70, '-'))
    print("Test Case 1")
    l = LinkedList()
    l.push(2)
    l.push(9)
    l.push(4)
    l.push(6)
    l.push(9)
    l.push(4)

    l.show()
    l.remove_dups_without_buffer()
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
    l.remove_dups_with_buffer()
    l.show()

    print("Test Case 3 - Empty List")
    l = LinkedList()
    l.remove_dups_with_buffer()

    pass

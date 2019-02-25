'''
Linked List is a data structure which is written in such a way that every node is linked to next node using a pointer. It is a data storing data structure.
It removes the limitation of arrays of having fixed size. 
Secondly inserting an element in array is more texpensive.

Structure

(HEAD)
 NODE --------> Node --------> Node
       next            next    

functions to implement 
1)  size() - returns number of data nodes in linked list                            --- O(n)
2)  empty() - returns true if linked list is empty                                  --- O(1)
3)  value_at(index) - returns the value of the nth item (starting at 0 for first)   --- O(k) where k is kth element from head
4)  push_front(value) - adds an item to the front of the list                       --- O(1)
5)  pop_front() - remove front item and return its value                            --- O(1)
6)  push(value) - adds an item at the end                                           --- O(n)
7)  pop_back() - removes end item and returns its value                             --- O(n)
8)  front() - get value of front item                                               --- O(1)
9)  back() - get value of end item                                                  --- O(n)
10) insert(index, value) - insert value at index, so current item at that index     --- O(k) where k is the kth element from head
    is pointed to by new item at index 
11) erase(index) - removes node at given index                                      --- O(k) where k is the kth element from head
12) value_n_from_end(n) - returns the value of the node at nth position from 
    the end of the list 
13) reverse() - reverses the list 
14) remove_value(value) - removes the first item in the list with this value
'''
class Node:
    def __init__(self,data = None):
            self.next = None
            self.data = data 

class LinkedList:
    def __init__(self):
        self.head = None
    
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

    def value_at(self, index):
        ''' Returns the Value of the Node at certain index '''
        if self.empty():
            return "Linked List Empty"
        
        idx = 1
        l = self.head
        while l.next is not None:
            if idx is index:
                break
            
            l = l.next
            idx += 1
        return l.data

    def empty(self):
        ''' Return True if Empty '''
        if self.head is None:
            return True
        return False

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
    
    def push_front(self, data):
        ''' adds a node in the front of the linked list '''
        n = Node(data)
        if self.empty():
            self.head = n
            return
        
        l = self.head
        self.head = n
        n.next = l
        return
    
    def pop_front(self):
        ''' Removes a node from the front of the linked list and returns the removed element '''
        if self.empty():
            return "Linked List is Empty"
        
        h = self.head
        if h.next is None:
            self.head = None
            return h.data
        
        self.head = h.next
        return h.data
        
    def pop_back(self):
        ''' This will remove a node from the back of the LinkedList and returns the popped element '''
        if self.empty():
            return "Empty Linked List"
        
        h = self.head
        while h is not None:
            if(h.next.next is None):
                data = h.next.data
                h.next = None
                break
            h = h.next
        return data

    def front(self):
        ''' Returns head of the Linked List '''
        if(self.empty()):
            return "Linked List is Empty"
        return self.head.data

    def back(self):
        ''' Returns last Element of the Linked List '''
        if self.empty():
            return "Linked List is Empty"
        
        h = self.head
        while h.next is not None:
            h = h.next

        return h.data
    
    def insert(self, index, data):
        ''' Inserts a Value at given Index '''

        n = Node(data)

        if self.empty() and index is not 0:
            print("Linked List is Empty hence value cannot be added to index: ", index)
            return

        size = self.size()

        if index > size:
            print ("Size of the Linked List is less than the index")
            return

        if index is size:
            return self.push(data)

        idx = 0
        h = self.head
        previous = self.head
        while h.next is not None:
            if idx is index:
                if previous is not h:
                    prevous.next = n
                    n.next = h
                else:
                    self.head = n
                    self.head.next = h
                h = n
                return
            idx += 1
            prevous = h
            h = h.next
        
    def erase(self, index):
        ''' removes node at a given index and returns the value removed '''
        if self.empty():
            return "Linked List is empty"
        size = self.size()
        if index > size - 1:
            return "Size of the Linked List is less than the index"
        
        idx = 0
        h = self.head
        previous = self.head
        while h.next is not None:
            if idx is index:
                if previous is h:
                    data =h.data
                    self.head = h.next
                    return data
                else:
                    data = h.data
                    previous.next = h.next
                    h = None
                    return data
            idx += 1
            previous = h 
            h = h.next
        
        # Pop the last element
        data = previous.data
        previous.next = None
        return data

    def value_n_from_end(self, n):
        ''' returns the value of nth positon from the end of the list '''
        size = self.size()
        if n < 0:
            return "The value passed cannot be negative"
        if n > size:
            return "the value passed cannot be greater than the size"
        idx = 0
        h = self.head
        remainder = size - n
        while h is not None:
            if idx == remainder:
                return h.data
            idx += 1

            h = h.next
        pass

    def reverse(self):
        ''' Reverses the Linked List '''

        h = self.head
        previous = None
        while h is not None:
            next = h.next
            h.next = previous
            previous = h
            h = next

        self.head = previous

        # self.head.next = h
        # pass
    
    def remove_value(self, value):
        ''' Matches the Value and removes the first occurance of it from the Linked List and returns the index '''
        if self.empty():
            return "Linked List is empty"
        h = self.head
        previous = self.head
        idx = 0
        while h is not None:
            if h.data is value:
                if previous is h:
                    self.head = h.next
                    return idx
                else:
                    previous.next = h.next
                    h = None
                    return idx
            idx += 1
            previous = h
            h = h.next
            
        pass

    def show(self):
        ''' Shows Linked List Representation for current Linked List '''
        if self.empty():
            return "Linked List is Empty"

        l = self.head
        while l is not None:
            print(l.data , end =  " ----> ")
            l = l.next
        print()
        return
        

if __name__ == "__main__":
    l = LinkedList()
    print("----------------------------------------------------------------------------------")
    print("Push and Pop")
    l.push(2)
    l.push(3)
    l.push(5)
    l.push(1)
    l.push(6)
    l.push(2)
    l.push(7)
    l.push(9)

    l.push_front(10)
    l.push_front(81)


    l.show()
    print("Size of LinkedList: ", l.size())
    print("Value at 5th Position: ",l.value_at(5))

    
    print("Element Popped from Front:", l.pop_front())
    print("Element Popped from Back:", l.pop_back())

    l.show()
    print("Size of LinkedList: ", l.size())
    print("Value at 5th Position: ",l.value_at(5))
    print("front: ",l.front(), "back: ", l.back())
    print("----------------------------------------------------------------------------------")
    print("Insert")
    l.insert(0,12)
    print("Inserting 12 at 0th position")
    l.show()
    
    l.insert(4,19)
    print("Inserting 19 at 4th position")
    l.show()
    
    size = l.size()
    l.insert(size,20)
    print("Inserting 20 at last position")
    l.insert(17,21)
    l.show()
    
    print("Size of LinkedList: ", l.size())
    print("----------------------------------------------------------------------------------")
    print("Erase")
    print("Erased Index 0: ",l.erase(0))
    l.show()

    print("Erased Index 4: ",l.erase(4))
    l.show()
    
    size = l.size()
    print("Erased Index size: ",l.erase(size-1))
    l.show()
    print("Size of LinkedList: ", l.size())

    print("----------------------------------------------------------------------------------")
    print("nth value from end")
    l.show()
    size = l.size()
    print("4th Element from end", l.value_n_from_end(4))
    print("0th Element from end", l.value_n_from_end(0))
    print("1st Element from end", l.value_n_from_end(1))
    print("last Element from end", l.value_n_from_end(size))

    print("----------------------------------------------------------------------------------")
    print("Remove Value")
    l.show()
    index = l.remove_value(2)
    print("Index of removed vlaue:", index)
    l.show()

    print("----------------------------------------------------------------------------------")
    print("Reverse")
    l.push(8)
    l.reverse()
    l.show()
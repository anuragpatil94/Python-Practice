import sys
sys.path.insert(0, '../../')

from conceptual.linked_list import LinkedList

'''
    2.5 Sum Lists: You have two numbers represented by a linked list, where each node 
    contains a single digit. The digits are stored in reverse order, such that 
    the 1's digit is at the head of the list. Write a function that adds two numbers 
    and returns the sum as a linked list.
    Repeat if the digits are stored in forward order.
'''


def sumListsBackward(l1, l2):
    ''' This function takes 2 lists comprising of a number 
                            7 -> 1 -> 6      617
                            5 -> 9 -> 2      295
        and adds them to    2 -> 1 -> 9      912
    
    Time Complexity O(n), 
    Space Complexity O(n) can be changed to O(1) if output is saved in one of the linkedlist
    '''
    carry = 0
    output = LinkedList()
    while l1 is not None or l2 is not None:
        l1digit = 0 if l1 is None else l1.data
        l2digit = 0 if l2 is None else l2.data
        
        remainder = (l1digit + l2digit + carry) % 10
        carry =  (l1digit + l2digit + carry)//10
        output.push(remainder)

        l1 = l1.next if l1 is not None else None
        l2 = l2.next if l2 is not None else None
        if l1 is None and l2 is None and carry > 0:
            output.push(carry)
    return output

def sumListsForward(l1,l2):
    ''' This function takes 2 lists comprising of a number 
                            7 -> 1 -> 6         716
                            5 -> 9 -> 2         592
        and adds to    1 -> 3 -> 0 -> 8        1308
    
    Time Complexity O(n), 
    Space Complexity O(n)
    '''
    l3 = LinkedList()
    def _sumListsForward(l1,l2):
        if l1 is None and l2 is None: return 0
        carry = _sumListsForward(l1.next,l2.next)
        sumOfDigits = (l1.data+l2.data+carry)%10
        print(sumOfDigits,carry)
        l3.push_front(sumOfDigits)
        return (l1.data+l2.data+carry)//10

    l1size = l1.size()
    l2size = l2.size()
    if l1size < l2size:
        for i in range(l2size-l1size):
            l1.push_front(0)
    if l1size > l2size:
        for i in range(l1size-l2size):
            l2.push_front(0)
    
    carry = _sumListsForward(l1.head,l2.head)
    if carry > 0:
        l3.push_front(carry)
    return l3
    

if __name__ == "__main__":
    # l1 = LinkedList()
    # l2 = LinkedList()

    # l1.push(7)
    # l1.push(1)
    # l1.push(6)
    # print("INPUT: ",l1.show())

    # l2.push(5)
    # l2.push(9)
    # l2.push(2)
    # print("INPUT: ",l2.show())

    # output = sumListsBackward(l1.head,l2.head)
    # print("OUTPUT: ",output.show())

    l1 = LinkedList()
    l2 = LinkedList()

    l1.push(9)
    l1.push(7)
    l1.push(9)
    print("INPUT: ",l1.show())

    l2.push(2)
    l2.push(1)
    print("INPUT: ",l2.show())

    # output = sumListsBackward(l1.head,l2.head)


    # print("OUTPUT: ",output.show())

    # l1 = LinkedList()
    # l2 = LinkedList()

    # l1.push(6)
    # l1.push(1)
    # l1.push(7)
    # print("INPUT: ",l1.show())

    # l2.push(2)
    # l2.push(9)
    # l2.push(5)
    # print("INPUT: ",l2.show())
    
    output = sumListsForward(l1,l2)
    print("OUTPUT: ",output.show())

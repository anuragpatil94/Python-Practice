import sys
sys.path.insert(0, '../../')

from conceptual.linked_list import LinkedList

''' 
    Return Kth to Last: Implement an algorithm to find the kth to last element of a singly linked list. 

        Solution 1: parse through the list and get the size of the linked list. then find the (size - k)th element... O((3/2)n)
        Solution 2: parse through the list keeping a queue which will only store k elements. giving time complexity O(n)
        Solution 3: keep 2 pointers having them k elements apart. 
                    so that if pointer1 reaches the last element, the pointer2 will be at kth element

'''


def kth_element_to_last(head, k):
    ''' 
        # MY SOLUTION
        Solution 2: parse through the list keeping a queue which will only store k elements. giving time complexity O(n)
    '''
    if k < 1: return "Invalid! k cannot be less than 1"
    
    queue = list()
    current = head
    i = 0
    while current is not None:
        if len(queue) == k :
            queue.pop(0)
        queue.append(current.data)
        current = current.next
        i+=1

    if k > i : return "Invalid! k is greater than size of the linked list"

    return k,"th element is ", queue[0]
    pass


def kth_element_to_last_bs(head,k):
    '''
        # BS
        Solution 3: keep 2 pointers having them k elements apart. 
        so that if pointer1 reaches the last element, the pointer2 will be at kth element
    '''

    pointer1 = head
    pointer2 = head

    for element in range(1,k):
        pointer1 = pointer1.next

    while pointer1.next is not None:
        pointer1 = pointer1.next
        pointer2 = pointer2.next

    return pointer2.data
    pass

if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.push(2)
    linked_list.push(4)
    linked_list.push(6)
    linked_list.push(2)
    linked_list.push(8)
    linked_list.push(1)
    linked_list.push(9)
    linked_list.push(62)
    linked_list.push(95)
    linked_list.push(65)
    print(kth_element_to_last(linked_list.head,0))
    print(kth_element_to_last(linked_list.head,4))
    print(kth_element_to_last(linked_list.head,-1))
    print(kth_element_to_last(linked_list.head,15))


    print("BS - ",kth_element_to_last_bs(linked_list.head,4))

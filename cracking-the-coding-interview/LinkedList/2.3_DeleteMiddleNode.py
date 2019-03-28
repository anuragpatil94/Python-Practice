import sys
sys.path.insert(0, '../../')

from conceptual.linked_list import LinkedList

'''
    2.3 Delete Middle Node: Implement an algorithm to delete a node in the middle 
    (i.e., any node but the first and last node, not necessarily the exact middle) 
    of a singly linked list, given only access to that node. 

    Solution 1 - We have access to the node to be deleted hence we iterate from that node, 
    copy the data of next node to current node and in the end delete the last node.

    Solution 2 - Just Change the next pointer to next to next pointer 
'''


def delete_middle_node(delNode):
    while delNode.next is not None:
        delNode.data = delNode.next.data
        previous = delNode
        delNode = delNode.next
    previous.next = None

    pass

def delete_middle_node_bs(delNode):
    if delNode is None or delNode.next is None:
        return False
    
    delNode.data = delNode.next.data
    delNode.next = delNode.next.next

    return True

if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.push("a")
    linked_list.push("b")
    linked_list.push("c")
    linked_list.push("d")
    linked_list.push("e")
    linked_list.push("f")
    
    current = linked_list.head
    while current is not None:
        if current.data == "c":
            break
        current = current.next
    linked_list.show()
    delete_middle_node(current)
    linked_list.show()


    print("BOOK SOLUTION")
    linked_list = LinkedList()
    linked_list.push("a")
    linked_list.push("b")
    linked_list.push("c")
    linked_list.push("d")
    linked_list.push("e")
    linked_list.push("f")
    
    current = linked_list.head
    while current is not None:
        if current.data == "c":
            break
        current = current.next
    linked_list.show()
    delete_middle_node(current)
    linked_list.show()
import sys
sys.path.insert(0, '../../')
from conceptual.linked_list import LinkedList

'''
Important
2.6: Palindrome
    Implement a function to check if the linked list is the palindrome

    Solution: 
    - Get the Middle Element in Recursion
        - using the (length - 2) in the recussion which will make sure 
            when length is 0 the current_node will reach the middle for an even size Linkedlist and 
            when length is 1 the current_node will reach the middle for an odd size Linkedlist
        - Class Result - This is used to return 2 values and to update the values easily in the recursion.
'''
class Result:
    def __init__(self, node, isPalindrome):
        self.node = node
        self.isPalindrome = isPalindrome

    def __str__(self):
        return "node:"+self.node.data+", isPalindrome:"+str(self.isPalindrome)

def checkPalindrome(l, size):
    current = l.head
    result = _isPalindrome(current, size)
    return result.isPalindrome    

def _isPalindrome(current, length):
    if (length == 0):  return Result(current, True)
    elif(length == 1): return Result(current.next, True)

    result = _isPalindrome(current.next, length-2)

    if(not result.isPalindrome or result.node == None): return result
    result.isPalindrome = (result.node.data == current.data)        #Returns False if not equal
    result.node = result.node.next
    return result


if __name__ == "__main__":
    l = LinkedList()
    l.push("A")
    l.push("B")
    l.push("C")
    l.push("B")
    l.push("A")
    l.show()

    print(checkPalindrome(l, 5))

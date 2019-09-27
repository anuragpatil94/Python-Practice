'''
Three in One: 
    Describe how you could use a single array to implement three stacks. 

The Challenge here is how to not make stack of limited length

Solution 1: (My Solution) 
    Lets say we have a array A.
    Stack is a LIFO Data Structure, which means that the last element is the first to get popped.

    Now lets say we have 3 stacks K,L,M

    Since, we can only use one array,
    we can store the stacks in the following way
    K - 0,3,6,9,12.....
    L - 1,4,7,10,13....
    M - 2,5,8,11,14....



'''

class Stack:
    def __init__(self):
        self.arr = ['$']*50
        self.length1 = 0
        self.length2 = 0
        self.length3 = 0
    
    def _getMasterArrayLength(self) -> int:
        return len(self.arr)
        
    def getLengthOfStack1(self) -> int:
        """Returns Length of Stack 1"""
        return self.length1
    def getLengthOfStack2(self) -> int:
        """Returns Length of Stack 2"""
        return self.length2
    def getLengthOfStack3(self) -> int:
        """Returns Length of Stack 3"""
        return self.length3
    
    def _getLengthOfStack(self, stackNumber) -> int:
        """Returns Length of the stack{stackNumber}

        Keyword arguments:
        stackNumber - The Stack you want to push the Element (range(1,4))
        """
        if stackNumber == 1:
            return self.getLengthOfStack1()

        if stackNumber == 2:
            return self.getLengthOfStack2()
        
        if stackNumber == 3:
            return self.getLengthOfStack3()

    def _getIndex(self, stackNumber) -> int:
        """Returns Last Index of the stack{stackNumber}

        Keyword arguments:
        
            stackNumber - The Stack you want to push the Element (range(1,4))
        """
        return 3 * (self._getLengthOfStack(stackNumber)) + (stackNumber-1)

    def _incrementLength(self, stackNumber) -> None:
        if stackNumber == 1:
            self.length1+=1

        if stackNumber == 2:
            self.length2+=1
        
        if stackNumber == 3:
            self.length3+=1

    def _decrementLength(self, stackNumber) -> None:
        if stackNumber == 1:
            self.length1-=1

        if stackNumber == 2:
            self.length2-=1
        
        if stackNumber == 3:
            self.length3-=1

    def push(self, stackNumber, elem = None):
        """Push an element to the Stack

        Keyword arguments:
        stackNumber - The Stack you want to push the Element (range(1,4))
        elem - The Element that is to be pushed(Default = None)
        """
        if not elem:
            return

        self.arr[self._getIndex(stackNumber)] = elem
        self._incrementLength(stackNumber)

    def pop(self, stackNumber) -> int:
        """Removes last element from stack and returns the popped element

        Keyword arguments:
        stackNumber - The Stack you want to push the Element (range(1,4))
        """
        self.arr[self._getIndex(stackNumber) - 3] = '$'
        self._decrementLength(stackNumber)

    def show(self, stackNumber) -> list:
        for i in range(stackNumber-1,self._getMasterArrayLength(), 3):
            if self.arr[i] == '$':
                break
        return self.arr[stackNumber-1:i:3]
if __name__ == "__main__":
    s = Stack()
    s.push(1,1)
    s.push(1,2)
    s.push(1,3)
    s.push(1,4)
    s.push(1,5)
    s.push(1,6)


    s.push(2,7)
    s.push(2,8)
    s.push(2,9)
    s.push(2,10)
    s.pop(2)
    s.push(2,11)
    s.push(2,12)
    s.push(2,13)

    print(s.show(1))
    print(s.show(2))
"""

Stack of Plates: 
    Imagine a (literal) stack of plates. If the stack gets too high, it might topple. 
    Therefore, in real life, we would likely start a new stack when the previous stack exceeds some threshold. 
    Implement a data structure SetOfStacks that mimics this. 
    SetOfStacks should be composed of several stacks and should create a new stack once the previous one exceeds capacity. 
    SetOfStacks.push() and SetOfStacks.pop() should behave identically to a single stack (that is, pop () should return the same values as it would if there were just a single stack). 
    FOLLOW UP Implement a function popAt ( int index) which performs a pop operation on a specific sub-stack. 

"""


class StackOfPlates:
    def __init__(self, n):
        """n is the height of stack"""
        self.masterStack = []
        self.stackHeight = 0
        self.capacity = n

    def _createStack(self):
        self.masterStack.append([])
        pass

    def _isEmpty(self):
        if not len(self.masterStack):
            return True
        return False

    def _stackPacked(self):
        if not self._isEmpty() and len(self.masterStack[-1]) == self.capacity:
            return True
        return False

    def push(self, data):
        if self._isEmpty() or self._stackPacked():
            self._createStack()
        self.masterStack[-1].append(data)
        self.stackHeight += 1

    def pop(self):
        if len(self.masterStack[-1]) == 0:
            self.masterStack.pop()
        element = self.masterStack[-1].pop()
        self.stackHeight -= 1
        return element

    def popAt(self, index):
        """ Considering Index from 1 to number of Stacks"""
        index = index - 1
        if index > len(self.masterStack):
            print("Stack Number should be less than Number of Stacks")
            return
        if len(self.masterStack[index]) == 0:
            print("The Stack is Already Empty")
            return

        self.masterStack[index].pop()
        self.stackHeight -= 1

    def show(self):
        print(self.masterStack)


if __name__ == "__main__":
    s = StackOfPlates(5)

    s.push(1)
    s.push(1)
    s.push(1)
    s.push(1)
    s.push(1)
    s.show()

    s.pop()
    s.show()

    s.push(1)
    s.push(1)

    s.show()
    s.pop()
    s.show()

    s.push(1)
    s.push(1)
    s.push(1)
    s.push(1)
    s.push(1)
    s.push(1)
    s.push(1)

    s.show()
    print(s.stackHeight)

    s.popAt(2)
    s.show()
    print(s.stackHeight)

    s.popAt(3)
    s.popAt(3)
    s.popAt(3)

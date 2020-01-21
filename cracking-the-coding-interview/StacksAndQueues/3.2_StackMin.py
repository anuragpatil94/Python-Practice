"""

3.2 Stack Min: 
    How would you design a stack which, in addition to push and pop, has a function min which returns the minimum element? 
    Push, pop and min should all operate in 0(1) time. 

Idea:

Store one more array which will store the min everytime a element is pushed. When a elem is popped, an element is also popped from minStack

Improvement:
push to stack only if minimum

"""


class StackMin:
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val):
        """ Time Complexity: O(1) """
        self.stack.append(val)
        if len(self.stack) > 1:
            if val < self.minStack[-1]:
                self.minStack.append(min(val, self.minStack[-1]))
        else:
            self.minStack.append(val)

    def pop(self) -> int:
        """ Time Complexity: O(1) """
        x = self.stack.pop()
        if x <= self.minStack[-1]:
            self.minStack.pop()
        return x

    def min(self):
        """ Time Complexity: O(1) """
        return self.minStack[-1]

    def show(self):
        return self.stack


if __name__ == "__main__":
    s = StackMin()
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    s.push(5)
    s.push(-1)
    s.push(7)

    print(s.show())
    print("min:", s.min())
    print("pop:", s.pop())
    print(s.show())
    print("pop:", s.pop())
    print(s.show())
    print("min:", s.min())

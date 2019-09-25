class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.arr = []
        self.minArr = []

    def push(self, x: int) -> None:
        self.arr.append(x)
        if len(self.minArr):
            self.minArr.append(min(x,self.minArr[-1]))
        else:
            self.minArr.append(x)
        

    def pop(self) -> None:
        self.arr.pop()
        self.minArr.pop()
        

    def top(self) -> int:
        return self.arr[-1]
        

    def getMin(self) -> int:
        return self.minArr[-1]
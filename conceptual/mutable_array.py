from array import array


class MutableArray:
    def __init__(self, capacity):
        self.cap = capacity
        self.arr = array("b", [] * capacity)

    def size(self):
        return len(self.arr)

    def capacity(self):
        return self.cap

    def is_empty(self):
        return True if self.size() else False

    def at(self, index):
        if index > self.size() or index < 0:
            return "Error"
        return self.arr[index]

    def push(self, val):
        if self.size() < self.cap:
            self.arr.append(val)
            return
        else:
            self.cap = self.cap * 2
            self.push(val)

        print(self.arr)


if __name__ == "__main__":
    mutable = MutableArray(10)
    print(mutable)
    print(mutable.size(), mutable.capacity())
    mutable.push(1)
    mutable.push(2)
    mutable.push(3)
    mutable.push(4)
    mutable.push(5)
    mutable.push(6)
    mutable.push(7)
    mutable.push(8)
    mutable.push(9)
    mutable.push(10)
    print(mutable.size(), mutable.capacity())
    mutable.push(11)
    print(mutable.size(), mutable.capacity())
    print(mutable.at(4))

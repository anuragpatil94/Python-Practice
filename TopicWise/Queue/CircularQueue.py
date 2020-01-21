class CircularQueue:
    def __init__(self, capacity=10):
        self.head = 0
        self.tail = -1
        self.capacity = capacity
        self.queue = [None] * capacity
        self.size = 0

    def enqueue(self, data):
        if self.isFull():
            return False
        self.tail += 1
        self.tail = self.tail % self.capacity
        self.queue[self.tail] = data
        self.size += 1
        return True

    def dequeue(self):
        if self.isEmpty():
            return False
        self.head += 1
        self.head = self.head % self.capacity
        self.size -= 1
        return True

    def front(self):
        if self.isEmpty():
            return False
        return self.queue[self.head]

    def rear(self):
        if self.isEmpty():
            return False
        return self.queue[self.tail]

    def isEmpty(self):
        if self.size == 0:
            return True
        return False

    def isFull(self):
        if self.size == self.capacity:
            return True
        return False

    def show(self):
        return self.queue

import pytest
from TopicWise.Queue.CircularQueue import CircularQueue


class TestCircularQueue:
    def test_enqueue(self):
        cq = CircularQueue(5)
        cq.enqueue(1)
        assert cq.isEmpty() == False
        assert cq.isFull() == False
        assert cq.front() == 1
        assert cq.rear() == 1

    def test_queueEmpty(self):
        cq = CircularQueue(5)
        assert cq.isEmpty() == True
        cq.enqueue(1)
        assert cq.isEmpty() == False

    def test_queueFull(self):
        cq = CircularQueue(5)
        arr = [1, 2, 3, 4, 5]
        for num in arr:
            cq.enqueue(num)
        assert cq.isFull() == True
        assert cq.dequeue() == True
        assert cq.isFull() == False

    def test_queueFront(self):
        cq = CircularQueue(5)
        arr = [1, 2, 3, 4, 5]
        for num in arr:
            cq.enqueue(num)
        assert cq.front() == 1
        assert cq.dequeue() == True
        assert cq.front() == 2
        assert cq.dequeue() == True
        assert cq.front() == 3
        assert cq.dequeue() == True
        assert cq.front() == 4
        assert cq.dequeue() == True
        assert cq.front() == 5
        assert cq.dequeue() == True
        assert cq.front() == False

    def test_queueRear(self):
        cq = CircularQueue(5)
        arr = [1, 2, 3, 4, 5]
        for num in arr:
            cq.enqueue(num)
        assert cq.rear() == 5
        assert cq.dequeue() == True
        assert cq.rear() == 5
        assert cq.dequeue() == True
        assert cq.rear() == 5
        assert cq.dequeue() == True
        assert cq.rear() == 5
        assert cq.dequeue() == True
        assert cq.rear() == 5
        assert cq.dequeue() == True
        assert cq.rear() == False

    def test_circularEnqueue(self):
        cq = CircularQueue(5)
        arr = [1, 2, 3, 4, 5]
        for num in arr:
            cq.enqueue(num)
        assert cq.front() == 1
        assert cq.dequeue() == True

        cq.enqueue(78)
        assert cq.rear() == 78
        assert cq.show() == [78, 2, 3, 4, 5]

    def test_dequeue(self):
        cq = CircularQueue(5)
        arr = [1, 2, 3, 4, 5]
        for num in arr:
            cq.enqueue(num)
        assert cq.front() == 1
        assert cq.dequeue() == True
        assert cq.front() == 2

import pytest
from TopicWise.Queue.PriorityQueue import PriorityQ_Heap
from TopicWise.Queue.PriorityQueue import QElement


class TestPriorityQueue:
    def test_insert(self):
        q = PriorityQ_Heap()
        q.insert(2, 67)
        q.insert(1, 37)
        q.insert(4, 327)
        q.insert(1, 3547)
        q.insert(5, 637)
        assert q[0] == {"priority": 5, "data": 637}

    def test_empty(self):
        q = PriorityQ_Heap()
        assert q.empty() == True
        q.insert(2, 67)
        assert q.empty() == False

    def test_remove(self):
        q = PriorityQ_Heap()
        q.insert(2, 67)
        q.insert(1, 37)
        q.insert(4, 327)
        q.insert(1, 3547)
        q.insert(5, 637)
        assert q.remove() == QElement(5, 637)


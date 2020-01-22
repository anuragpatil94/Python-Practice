import heapq


class QElement:
    def __init__(self, priority, data):
        self.priority = priority
        self.data = data

    def __lt__(self, other):
        """This is used so that when heapq library uses comparison operator, instead of using it own function it will use __lt__ so that it knows which attribute to compare"""
        return self.priority < other.priority

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.priority == other.priority and self.data == other.data
        return False


class PriorityQ_Heap:
    """Implementation of Priority Queue using Heap. Storing the element as QElement(priority: int, data: any)"""

    def __init__(self):
        self.q = []

    def __getitem__(self, index):
        return {"priority": self.q[index].priority, "data": self.q[index].data}

    def empty(self):
        """checks if Queue is empty"""
        if len(self.q) == 0:
            return True
        return False

    def insert(self, priority, data):
        """Insert data with its priority to the Queue """
        self.priority = priority
        self.data = data
        element = QElement(self.priority, self.data)

        heapq.heappush(self.q, element)
        self.__heapqheapify()

        return True

    def __heapqheapify(self):
        heapq._heapify_max(self.q)

    def remove(self):
        """Removes Topmost element with highest Priority"""
        return heapq._heappop_max(self.q)


# if __name__ == "__main__":
#     q = PriorityQ_Heap()
#     q.insert(2, 67)
#     q.insert(1, 37)
#     q.insert(4, 327)
#     q.insert(1, 3547)
#     q.insert(5, 637)


class Heap:
    def __init__(self,A):
        # added a prefix element so that all calculations start from 1
        self.A = [-1] + A
        self.size = len(A)

    def Left(self, i):
        return 2*i
    def Right(self,i):
        return (2*i)+1
    
    def MaxHeapify(self, parentIndex):
        leftIndex = self.Left(parentIndex)
        rightIndex = self.Right(parentIndex)

        if leftIndex <= self.size and self.A[leftIndex] > self.A[parentIndex]:
            largest = leftIndex
        else:
            largest = parentIndex
        
        if rightIndex <= self.size and self.A[rightIndex] > self.A[largest]:
            largest = rightIndex
        
        if largest != parentIndex:
            self.A[parentIndex],self.A[largest] = self.A[largest],self.A[parentIndex]
            self.MaxHeapify(largest)

    def BuildMaxHeap(self):
        size = len(self.A)
        for i in range((size//2),0,-1):
            self.MaxHeapify(i)
        return self.A[1:]
        

    def HeapSort(self):
        sort = []
        self.BuildMaxHeap()
        for i in range(self.size,0,-1):
            sort.append(self.A[1])
            self.A[1],self.A[i] = self.A[i],self.A[1]

            self.size = self.size - 1
            self.MaxHeapify(1)
        
        return sort

if __name__=="__main__":
    #array= [1,2,03,4,5,6,7,08,9,10,11,12,13,14,15,16]
    array = [2,5,23,8,4,8,4,88,7, 5,34,76,33,66,21,35]
    heap = Heap(array)
    print(array)
    print(heap.BuildMaxHeap())
    print(heap.HeapSort())
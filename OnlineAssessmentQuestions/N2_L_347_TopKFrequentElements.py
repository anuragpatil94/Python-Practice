import heapq


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1

        heap = []
        for key, value in count.items():
            heapq.heappush(heap, (-value, key))

        return [heapq.heappop(heap)[1] for i in range(k)]


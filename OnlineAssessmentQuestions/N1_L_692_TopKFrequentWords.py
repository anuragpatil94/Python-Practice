import heapq


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        ans = {}
        for word in words:
            if word in ans:
                ans[word] += 1
            else:
                ans[word] = 1
        heap = []
        for key, value in ans.items():
            heapq.heappush(heap, (-value, key))

        return [element[1] for element in heap[:k]]


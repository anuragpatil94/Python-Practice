"""
Given n ropes of different lengths, we need to connect these ropes into one rope. We can connect only 2 ropes at a time. The cost required to connect 2 ropes is equal to sum of their lengths. The length of this connected rope is also equal to the sum of their lengths. This process is repeated until n ropes are connected into a single rope. Find the min possible cost required to connect all ropes.

Example 1:

Input: ropes = [8, 4, 6, 12]
Output: 58
Explanation: The optimal way to connect ropes is as follows
1. Connect the ropes of length 4 and 6 (cost is 10). Ropes after connecting: [8, 10, 12]
2. Connect the ropes of length 8 and 10 (cost is 18). Ropes after connecting: [18, 12]
3. Connect the ropes of length 18 and 12 (cost is 30).
Total cost to connect the ropes is 10 + 18 + 30 = 58
Example 2:

Input: ropes = [20, 4, 8, 2]
Output: 54
Example 3:

Input: ropes = [1, 2, 5, 10, 35, 89]
Output: 224
Example 4:

Input: ropes = [2, 2, 3, 3]
Output: 20
"""

"""
The idea is to get the 2 minimum length ropes everytime. in order to find the minimum cost
"""

from heapq import heappop, heappush, heapify


class Solution:
    def solution1(self, arr):
        # Time O(n log n) This solution will not work.
        arr.sort()
        j = 1
        total = 0
        sum = arr[0]
        while j < len(arr):
            sum = sum + arr[j]
            total += sum
            j += 1
        return total

    def solution2(self, ropes):
        if not ropes:
            return 0
        if len(ropes) == 1:
            return ropes[0]
        heapify(ropes)
        cost = 0
        while len(ropes) > 1:
            a, b = heappop(ropes), heappop(ropes)
            cost += a + b
            if ropes:
                heappush(ropes, a + b)
        return cost


if __name__ == "__main__":
    s = Solution()
    print(s.solution1([20, 4, 8, 2]))
    print(s.solution1([1, 2, 5, 10, 35, 89]))
    print(s.solution1([2, 2, 3, 3]))

    print(s.solution2([20, 4, 8, 2]))
    print(s.solution2([1, 2, 5, 10, 35, 89]))
    print(s.solution2([2, 2, 3, 3]))

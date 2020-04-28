"""
You have a map that marks the locations of treasure islands. 
Some of the map area has jagged rocks and dangerous reefs. 
Other areas are safe to sail in. There are other explorers trying to find the treasure
So you must figure out a shortest route to one of the treasure islands

Assume the map area is a two dimensional grid, represented by a matrix of characters
You must start from one of the starting point (marked as S) of the map and can move one block up, down, left or right at a time
The treasure island is marked as X
Any block with dangerous rocks or reefs will be marked as D
You must not enter dangerous blocks
You cannot leave the map area
Other areas O are safe to sail in
Output the minimum number of steps to get to any of the treasure islands

Example:

Input:
[['S', 'O', 'O', 'S', 'S'],
 ['D', 'O', 'D', 'O', 'D'],
 ['O', 'O', 'O', 'O', 'X'],
 ['X', 'D', 'D', 'O', 'O'],
 ['X', 'D', 'D', 'D', 'O']]

Output: 3
Explanation:
You can start from (0,0), (0, 3) or (0, 4)
The treasure locations are (2, 4) (3, 0) and (4, 0)
Here the shortest route is (0, 3), (1, 3), (2, 3), (2, 4).
"""


class Solution:
    # Total Time Complexity O(S*N)
    def solution1(self, arr):
        # Space O(1)
        m = len(arr)
        n = len(arr[0])
        adj = [(0, -1), (1, 0), (0, 1), (-1, 0)]
        minPath = m * n
        startQ = []

        # Time O(N)
        for rowIdx in range(m):
            for clmIdx in range(n):
                if arr[rowIdx][clmIdx] == "S":
                    startQ.append((rowIdx, clmIdx))
                pass

        # Time O(S)
        while startQ:
            # Space O(n)
            q = []
            start = startQ.pop(0)
            q.append([start, 0])
            visited = set()
            # Time O(mn or N)
            while q:
                (i, j), value = q.pop(0)
                visited.add((i, j))
                for co in adj:
                    nexti = i + co[0]
                    nextj = j + co[1]
                    if (
                        nexti < 0
                        or nextj < 0
                        or nexti >= m
                        or nextj >= n
                        or (nexti, nextj) in visited
                        or arr[nexti][nextj] == "D"
                    ):
                        continue

                    if arr[nexti][nextj] == "X":
                        minPath = min(minPath, value + 1)
                    q.append([(nexti, nextj), value + 1])
        return minPath


if __name__ == "__main__":
    s = Solution()
    a = [
        ["S", "O", "O", "S", "S"],
        ["D", "O", "D", "O", "D"],
        ["O", "O", "O", "O", "X"],
        ["X", "D", "D", "O", "O"],
        ["X", "D", "D", "D", "O"],
    ]
    s.solution1(a)

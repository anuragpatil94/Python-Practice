"""

You are given a m x n 2D grid initialized with these three possible values.

-1 - A wall or an obstacle.
0 - A gate.
INF - Infinity means an empty room. We use the value 2 31 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.
Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.

For example, given the 2D grid:

INF  -1  0  INF
INF INF INF  -1
INF  -1 INF  -1
  0  -1 INF INF
After running your function, the 2D grid should be:

  3  -1   0   1
  2   2   1  -1
  1  -1   2  -1
  0  -1   3   4

"""
import math


class Solution:
    def walls_dfs(self, arr):
        self.arr = arr
        self.solution = []

        for i in range(len(arr)):
            for j in range(len(arr[i])):
                if arr[i][j] == 0:
                    # self.dfs_visit(i, j)
                    self.dfs(i, j, 0)
        print(self.arr)
        pass

    def dfs(self, i, j, val):
        arr = self.arr
        if (
            i < 0
            or i >= len(arr)
            or j < 0
            or j >= len(arr[i])
            or arr[i][j] == -1
            or arr[i][j] < val
        ):
            return
        arr[i][j] = val
        self.dfs(i + 1, j, val + 1)
        self.dfs(i, j + 1, val + 1)
        self.dfs(i - 1, j, val + 1)
        self.dfs(i, j - 1, val + 1)

    def walls_bfs(self, arr):
        self.solution = []
        q = list()
        for i in range(len(arr)):
            for j in range(len(arr[i])):
                if arr[i][j] == 0:
                    q.append((i, j))
        co = [(0, -1), (-1, 0), (0, 1), (1, 0)]

        while q:
            current = q.pop(0)
            ci = current[0]
            cj = current[1]
            for k in co:
                i = ci + k[0]
                j = cj + k[1]
                if (
                    i < 0
                    or i >= len(arr)
                    or j < 0
                    or j >= len(arr[i])
                    or arr[i][j] < arr[ci][cj] + 1
                ):
                    continue
                arr[i][j] = arr[ci][cj] + 1
                q.append((i, j))
        print(arr)


if __name__ == "__main__":
    arr = [
        [math.inf, -1, 0, math.inf],
        [math.inf, math.inf, math.inf, -1],
        [math.inf, -1, math.inf, -1],
        [0, -1, math.inf, math.inf],
    ]
    s = Solution()
    s.walls_dfs(arr)
    arr = [
        [math.inf, -1, 0, math.inf],
        [math.inf, math.inf, math.inf, -1],
        [math.inf, -1, math.inf, -1],
        [0, -1, math.inf, math.inf],
    ]
    s.walls_bfs(arr)
    pass

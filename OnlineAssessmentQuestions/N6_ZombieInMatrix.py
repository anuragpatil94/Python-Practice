"""
Given a 2D grid, each cell is either a zombie 1 or a human 0. Zombies can turn adjacent (up/down/left/right) 
human beings into zombies every hour. Find out how many hours does it take to infect all humans?

Example:

Input:
[[0, 1, 1, 0, 1],
 [0, 1, 0, 1, 0],
 [0, 0, 0, 0, 1],
 [0, 1, 0, 0, 0]]

Output: 2

Explanation:
At the end of the 1st hour, the status of the grid:
[[1, 1, 1, 1, 1],
 [1, 1, 1, 1, 1],
 [0, 1, 0, 1, 1],
 [1, 1, 1, 0, 1]]

At the end of the 2nd hour, the status of the grid:
[[1, 1, 1, 1, 1],
 [1, 1, 1, 1, 1],
 [1, 1, 1, 1, 1],
 [1, 1, 1, 1, 1]]
"""


class Solution:
    def minHours(self, rows, columns, grid):
        q = []
        co = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        time = {}
        maxTime = 0
        for i in range(rows):
            for j in range(columns):
                if grid[i][j] == 1:
                    q.append((i, j))
                    time[(i, j)] = 0
        while q:
            current = q.pop(0)
            zi = current[0]
            zj = current[1]
            for next in co:
                i = zi + next[0]
                j = zj + next[1]
                if i < 0 or j < 0 or j >= columns or i >= rows:
                    continue
                if (i, j) in time:
                    time[(i, j)] = min(time[(i, j)], time[(zi, zj)] + 1)
                else:
                    time[(i, j)] = time[(zi, zj)] + 1
                    grid[i][j] = 1
                    q.append((i, j))
                maxTime = max(maxTime, time[(i, j)])
        return maxTime


if __name__ == "__main__":
    grid = [[0, 1, 1, 0, 1], [0, 1, 0, 1, 0], [0, 0, 0, 0, 1], [0, 1, 0, 0, 0]]
    # grid = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
    s = Solution()
    print(s.minHours(4, 5, grid))

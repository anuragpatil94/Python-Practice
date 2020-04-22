"""
In a given grid, each cell can have one of three values:

the value 0 representing an empty cell;
the value 1 representing a fresh orange;
the value 2 representing a rotten orange.
Every minute, any fresh orange that is adjacent (4-directionally) to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange.  If this is impossible, return -1 instead.

 

Example 1:
Input: [[2,1,1],[1,1,0],[0,1,1]]
Output: 4
Example 2:

Input: [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation:  The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
Example 3:

Input: [[0,2]]
Output: 0
Explanation:  Since there are already no fresh oranges at minute 0, the answer is just 0.
"""


class Solution:
    def orangesRotting(self, grid):
        q = []
        time = 0
        timeDict = {}
        co = [(-1, 0), (0, -1), (1, 0), (0, 1)]

        if not grid and not grid[0]:
            return time

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 2:
                    q.append((i, j))
                    timeDict[(i, j)] = time

        colLen = len(grid)
        rowLen = len(grid[0])
        # print(q)
        while q:
            # print(q, timeDict)
            current = q.pop(0)
            ri = current[0]
            rj = current[1]
            for next in co:
                i = ri + next[0]
                j = rj + next[1]
                if i < 0 or j < 0 or i >= colLen or j >= rowLen:
                    continue
                if (i, j) in timeDict and grid[i][j] == 2:
                    timeDict[(i, j)] = min(timeDict[(i, j)], timeDict[(ri, rj)] + 1)
                if grid[i][j] == 1:
                    timeDict[(i, j)] = timeDict[(ri, rj)] + 1
                    time = max(time, timeDict[(i, j)])
                    grid[i][j] = 2
                    q.append((i, j))
        # print(grid)
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    return -1
        return time

if __name__ == "__main__":
    s = Solution()
    # grid = [
    #     [2, 1, 1], 
    #     [1, 1, 0], 
    #     [0, 1, 1]
    # ]
    grid = [[2,1,1],[0,1,1],[1,0,1]]
    print (s.orangesRotting(grid))

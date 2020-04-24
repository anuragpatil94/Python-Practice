"""
At first when I started to think about thi, I had no freaking idea how to solve it. 
Not sure if it was gonna work, I just went with it. ONe thing after another I started following the answer and what was missing.


The Idea behind this was that we have to cover the area such that we have to make sure that the 1s are surrounded by 0s
by left down right up movement i checked each and every digit in matrix and making sure that i put that position to visited everytime i touched it.
Secondly,
suppose we start with (0,0) position which is 1
then i check left which is outside boundary which is technically 0 so I return 0 means it is passed. next is (1,0) down which is 1 hence we take it forward 
to the for loop. This means that whenever code reached for loop it means the area of the island is big. 
1 - go to for loop to check for its surrounding
0 - return back to previous found island area and check next direction.

In this way we only check immediate boundary of the island.
once all land is checked we go back to find next island checking only those 1 which are not visited
"""


class Solution:
    def numIslands(self, grid):
        c = [(0, -1), (1, 0), (0, 1), (-1, 0)]
        num = 0
        visited = set()
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1" and (i, j) not in visited:
                    visited.add((i, j))
                    num += 1
                    self.recur(grid, i, j,  c, visited)
        return num

    def recur(self, grid, i, j,  c, visited):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[i]) or grid[i][j] == "0":
            return 0
        for co in c:
            ci = i + co[0]
            cj = j + co[1]
            if (ci, cj) not in visited:
                visited.add((ci, cj))
                self.recur(grid, ci, cj,  c, visited)


if __name__ == "__main__":
    s = Solution()
    print(
        s.numIslands(
            [
                ["1","1","1","1","1","0","1","1","1","1","1","1","1","1","1","0","1","0","1","1"],
                ["0","1","1","1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","1","0"],
                ["1","0","1","1","1","0","0","1","1","0","1","1","1","1","1","1","1","1","1","1"],
                ["1","1","1","1","0","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],
                ["1","0","0","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],
                ["1","0","1","1","1","1","1","1","0","1","1","1","0","1","1","1","0","1","1","1"],
                ["0","1","1","1","1","1","1","1","1","1","1","1","0","1","1","0","1","1","1","1"],
                ["1","1","1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","0","1","1"],
                ["1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","1","1","1","1","1"],
                ["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],
                ["0","1","1","1","1","1","1","1","0","1","1","1","1","1","1","1","1","1","1","1"],
                ["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],
                ["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],
                ["1","1","1","1","1","0","1","1","1","1","1","1","1","0","1","1","1","1","1","1"],
                ["1","0","1","1","1","1","1","0","1","1","1","0","1","1","1","1","0","1","1","1"],
                ["1","1","1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","1","1","0"],
                ["1","1","1","1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","0","0"],
                ["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],
                ["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],
                ["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"]
            ]
        )
    )
    # print(
    #     s.numIslands(
    #         [
    #             ["1", "1", "1", "1", "0"],
    #             ["1", "1", "0", "1", "0"],
    #             ["1", "1", "0", "0", "0"],
    #             ["0", "0", "0", "0", "1"],
    #         ]
    #     )
    # )

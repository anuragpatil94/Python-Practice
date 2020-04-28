"""
You have a map that marks the location of a treasure island. 
Some of the map area has jagged rocks and dangerous reefs. 
Other areas are safe to sail in. 
There are other explorers trying to find the treasure. 
So you must figure out a shortest route to the treasure island.

Assume the map area is a two dimensional grid, represented by a matrix of characters. 
You must start from the top-left corner of the map and can move one block up, down, left or right at a time. 
The treasure island is marked as X in a block of the matrix. 
X will not be at the top-left corner. 
Any block with dangerous rocks or reefs will be marked as D. 
You must not enter dangerous blocks. 
You cannot leave the map area. Other areas O are safe to sail in. 
The top-left corner is always safe. 
Output the minimum number of steps to get to the treasure.

Example:

Input:
[['O', 'O', 'O', 'O'],
 ['D', 'O', 'D', 'O'],
 ['O', 'O', 'O', 'O'],
 ['X', 'D', 'D', 'O']]

Output: 5
Explanation: Route is (0, 0), (0, 1), (1, 1), (2, 1), (2, 0), (3, 0) The minimum route takes 5 steps.
"""


class Solution:
    def solution1(self, arr):
        adj = [(0, -1), (1, 0), (0, 1), (-1, 0)]
        found = len(arr) * len(arr[0])
        path = 0
        visited = set()
        found = self.recur(arr, adj, found, 0, 0, path, visited)
        return found
        pass

    def recur(self, arr, adj, found, i, j, path, visited):
        visited.add((i, j))
        # print(i, j, visited, path, found)
        for dir in adj:
            newi = i + dir[0]
            newj = j + dir[1]

            if (
                newi < 0
                or newj < 0
                or newi >= len(arr)
                or newj >= len(arr[i])
                or arr[newi][newj] == "D"
                or (newi, newj) in visited
            ):
                continue

            if arr[newi][newj] == "X":
                found = min(found, path + 1)
                # print("-----", found)
                return found
            elif arr[newi][newj] == "O":
                found = self.recur(arr, adj, found, newi, newj, path + 1, visited)
        return found

    def solution2_WOR(self, arr):
        adj = [(0, -1), (1, 0), (0, 1), (-1, 0)]
        q = []
        m = len(arr)
        n = len(arr[0])
        q.append((0, 0))
        visitedWithCount = {(0, 0): 0}
        parent = {(0, 0): None}
        path = m * n
        # visitedWithCount[(i, j)] = 0
        while q:
            # print(q)
            i, j = q.pop(0)
            if (i, j) not in visitedWithCount:
                visitedWithCount[(i, j)] = visitedWithCount[parent[(i, j)]] + 1
            # print(i, j, path, visitedWithCount, parent)
            for co in adj:
                newi = i + co[0]
                newj = j + co[1]
                if (
                    newi < 0
                    or newj < 0
                    or newi >= m
                    or newj >= n
                    or arr[newi][newj] == "D"
                    or (newi, newj) in visitedWithCount
                ):
                    continue

                if arr[newi][newj] == "X":
                    path = min(path, visitedWithCount[(i, j)] + 1)
                elif arr[newi][newj] == "O":
                    parent[(newi, newj)] = (i, j)
                    q.append((newi, newj))
        return path
        pass

    def solution3(self, m):
        ''' Time (m)  Space (m) '''
        if len(m) == 0 or len(m[0]) == 0:
            return -1  # impossible

        matrix = [row[:] for row in m]
        nrow, ncol = len(matrix), len(matrix[0])

        q = deque([((0, 0), 0)])  # ((x, y), step)
        matrix[0][0] = "D"
        while q:
            (x, y), step = q.popleft()

            for dx, dy in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                if 0 <= x+dx < nrow and 0 <= y+dy < ncol:
                    if matrix[x+dx][y+dy] == "X":
                        return step+1
                    elif matrix[x+dx][y+dy] == "O":
                        # mark visited
                        matrix[x + dx][y + dy] = "D"
                        q.append(((x+dx, y+dy), step+1))

        return -1

if __name__ == "__main__":
    s = Solution()
    a = [
        ["O", "O", "O", "O"],
        ["D", "O", "D", "O"],
        ["O", "O", "O", "O"],
        ["X", "D", "D", "O"],
    ]
    b = [
        ["O", "O", "O", "O"],
        ["D", "O", "D", "O"],
        ["O", "O", "O", "O"],
        ["X", "O", "D", "O"],
    ]
    c = [
        ["O", "O", "O", "X"],
        ["D", "O", "D", "O"],
        ["O", "O", "O", "O"],
        ["O", "O", "D", "O"],
    ]
    print(s.solution1(a))
    print(s.solution2_WOR(a))
    print(s.solution1(b))
    print(s.solution2_WOR(b))
    print(s.solution1(c))
    print(s.solution2_WOR(c))

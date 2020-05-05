"""
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.
Example:

Consider the following matrix:

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
Given target = 5, return true.

Given target = 20, return false.
"""


class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        self.steps = 0
        ans = self.search(matrix, len(matrix)-1, 0, target, False, set())
        print(self.steps)
        return ans

    def search(self, matrix, i, j, target, found, visited):
        self.steps += 1
        if (
            (i, j) in visited
            or i < 0
            or i >= len(matrix)
            or j < 0
            or j >= len(matrix[i])
        ):
            return found
        visited.add((i, j))
        if matrix[i][j] == target:
            found = True
        elif matrix[i][j] < target:
            return self.search(matrix, i, j + 1, target, found, visited) or self.search(
                matrix, i + 1, j, target, found, visited
            )
        else:
            return self.search(matrix, i, j - 1, target, found, visited) or self.search(
                matrix, i - 1, j, target, found, visited
            )
        return found


if __name__ == "__main__":
    s = Solution()
    a = [
        [1, 4, 7, 11, 15],
        [2, 5, 8, 12, 19],
        [3, 6, 9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30],
    ]
    s.searchMatrix(a, 5)
    print("--")
    s.searchMatrix(a, 13)
    print("--")
    s.searchMatrix(a, 26)
    print("--")
    s.searchMatrix(a, 15)

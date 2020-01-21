"""

Zero Matrix: Write an algorithm such that if an element in an MxN matrix is 0, its entire row and column are set to 0. 

Solution:
    Scan the matrix once to get the list of all 0 positions (Time:O(mn))
    then store it in 2 sets x and y individually (SPace: O(n))
    then again loop through the list to remove 0 (Time: O(m) + O(n))

    Time Complexity(O(m*n))
    Space Complexity (O(n))

Book Solution. 
    This can also be done in  Space O(1) where ever we find zeros we update the y,0 and 0,x value of the matrix to 0

    Time Complexity(O(m*n))
    Space Complexity (O(1))
"""


class Solution:
    def ZeroMatrix(self, arr):
        xlist = set()
        ylist = set()

        for y in range(len(arr)):
            for x in range(len(arr[0])):
                if arr[y][x] == 0:
                    xlist.add(x)
                    ylist.add(y)
        for num in xlist:
            index = 0
            while index < len(arr):
                arr[index][num] = 0
                index += 1
        for num in ylist:
            index = 0
            while index < len(arr[0]):
                arr[num][index] = 0
                index += 1
        return arr

    def ZeroMatrix_BS(self, arr):
        for y in range(len(arr)):
            for x in range(len(arr[0])):
                if arr[y][x] == 0:
                    arr[y][0] = 0
                    arr[0][x] = 0
        for y in range(len(arr)):
            if arr[y][0] == 0:
                for x in range(len(arr[y])):
                    arr[y][x] = 0
            if y <= x and arr[0][y] == 0:
                for x in range(len(arr)):
                    arr[x][y] = 0
        return arr


if __name__ == "__main__":
    print([[1, 1, 1, 1], [1, 1, 1, 1], [1, 0, 1, 1], [1, 0, 1, 1], [1, 1, 1, 1]])
    print(
        Solution().ZeroMatrix(
            [[1, 1, 1, 1], [1, 1, 1, 1], [1, 0, 1, 1], [1, 0, 1, 1], [1, 1, 1, 1]]
        )
    )
    print("---")
    print(
        Solution().ZeroMatrix_BS(
            [[1, 1, 1, 1], [1, 1, 1, 1], [1, 0, 1, 1], [1, 0, 1, 1], [1, 1, 1, 1]]
        )
    )

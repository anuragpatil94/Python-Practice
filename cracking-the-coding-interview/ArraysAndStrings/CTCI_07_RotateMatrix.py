"""
Rotate Matrix: 
    Given an image represented by an NxN matrix, where each pixel in the image is 4 bytes, 
    write a method to rotate the image by 90 degrees. 
    Can you do this in place?

Book Solution:
    The best way to do this would be to swap the nodes as we parse layer by layer.

Time Complexity: O(N²)
Space Complexity:O(1)
"""


class Solution:
    def RotateMatrix(self, arr, N):
        for layer in range(N // 2):
            y = layer  # first
            t = N - 1 - layer  # last
            for x in range(y, t):  # x == i
                offset = x - y  # Indexing from behind
                top = arr[y][x]
                arr[y][x] = arr[t - offset][y]
                arr[t - offset][y] = arr[t][t - offset]
                arr[t][t - offset] = arr[x][t]
                arr[x][t] = top
        return arr


if __name__ == "__main__":
    arr = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    print(arr)
    print(Solution().RotateMatrix(arr, 4))

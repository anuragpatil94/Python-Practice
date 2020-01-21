"""

Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.


In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]

TIME COMPLEXITY: O(n²)
SPACE COMPLEXITY: O(n²)


"""


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        """This is example of Dynamic Programming"""
        pascal = []
        for row in range(0, numRows):
            if row == 0:
                pascal.append([1])
            else:
                if len(pascal) > 1:
                    pattern = [1]
                    for i in range(0, len(pascal) - 1):
                        pattern.append(pascal[row - 1][i] + pascal[row - 1][i + 1])
                    pattern.append(1)
                else:
                    pattern = [1, 1]
                pascal.append(pattern)
        return pascal

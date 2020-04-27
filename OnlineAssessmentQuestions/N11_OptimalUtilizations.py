"""
Given 2 lists a and b. Each element is a pair of integers where the first integer represents the unique id and the second integer represents a value. Your task is to find an element from a and an element form b such that the sum of their values is less or equal to target and as close to target as possible. Return a list of ids of selected elements. If no pair is possible, return an empty list.

Example 1:

Input:
a = [[1, 2], [2, 4], [3, 6]]
b = [[1, 2]]
target = 7

Output: [[2, 1]]

Explanation:
There are only three combinations [1, 1], [2, 1], and [3, 1], which have a total sum of 4, 6 and 8, respectively.
Since 6 is the largest sum that does not exceed 7, [2, 1] is the optimal pair.
Example 2:

Input:
a = [[1, 3], [2, 5], [3, 7], [4, 10]]
b = [[1, 2], [2, 3], [3, 4], [4, 5]]
target = 10

Output: [[2, 4], [3, 2]]

Explanation:
There are two pairs possible. Element with id = 2 from the list `a` has a value 5, and element with id = 4 from the list `b` also has a value 5.
Combined, they add up to 10. Similarily, element with id = 3 from `a` has a value 7, and element with id = 2 from `b` has a value 3.
These also add up to 10. Therefore, the optimal pairs are [2, 4] and [3, 2].
Example 3:

Input:
a = [[1, 8], [2, 7], [3, 14]]
b = [[1, 5], [2, 10], [3, 14]]
target = 20

Output: [[3, 1]]
Example 4:

Input:
a = [[1, 8], [2, 15], [3, 9]]
b = [[1, 8], [2, 11], [3, 12]]
target = 20

Output: [[1, 3], [3, 2]]
"""


class Solution:
    def solution1(self, a, b, target):
        """Time Complexity - O(n2)"""
        ans = 0
        last = {}
        arr = []
        for x in a:
            for y in b:
                if x[1] + y[1] < target:
                    ans = max(ans, (x[1] + y[1]))
                    if ans not in last:
                        last[ans] = []
                    last[ans].append([x[0], y[0]])
                elif x[1] + y[1] == target:
                    arr.append([x[0], y[0]])
        if not arr:
            arr = last[ans]
        return arr

    def solution2(self, a, b, target):
        """Time - O(n log n)"""
        a = sorted(a, key=lambda x: x[1])
        b = sorted(b, key=lambda x: x[1])
        i = 0
        j = len(b) - 1
        arr = []
        m = 0
        while i < len(a) and j >= 0:
            num_a = a[i][1]
            num_b = b[j][1]
            sum = num_a + num_b
            if sum > target:
                j -= 1
            else:
                if sum > m:
                    m = sum
                    arr = []
                    arr.append([a[i][0], b[j][0]])
                elif sum == m:
                    arr.append([a[i][0], b[j][0]])
                else:
                    continue
                i += 1
        return arr


if __name__ == "__main__":
    s = Solution()
    a = [[1, 2], [2, 4], [3, 6]]
    b = [[1, 2]]
    target = 7
    assert s.solution1(a, b, target) == [[2, 1]], "Should be [[2,1]]"
    assert s.solution2(a, b, target) == [[2, 1]], "Should be [[2,1]]"

    a = [[1, 3], [2, 5], [3, 7], [4, 10]]
    b = [[1, 2], [2, 3], [3, 4], [4, 5]]
    target = 10
    assert s.solution1(a, b, target) == [[2, 4], [3, 2]], "Should be [[2, 4], [3, 2]]"
    assert s.solution2(a, b, target) == [[2, 4], [3, 2]], "Should be [[2, 4], [3, 2]]"

    a = [[1, 8], [2, 7], [3, 14]]
    b = [[1, 5], [2, 10], [3, 14]]
    target = 20
    assert s.solution1(a, b, target) == [[3, 1]], "Should be [[3, 1]]"
    assert s.solution2(a, b, target) == [[3, 1]], "Should be [[3, 1]]"

    a = [[1, 8], [2, 15], [3, 9]]
    b = [[1, 8], [2, 11], [3, 12]]
    target = 20
    assert s.solution1(a, b, target) == [[1, 3], [3, 2]], "Should be [[1, 3], [3, 2]]"
    assert s.solution2(a, b, target) == [[1, 3], [3, 2]], "Should be [[1, 3], [3, 2]]"

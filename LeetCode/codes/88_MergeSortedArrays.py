"""
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:

The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.
Example:

Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

Output: [1,2,2,3,5,6]

Idea: 

Here the idea is to go from back of the array and start comparing and replace 0 in nums1 based on that
"""


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        l1 = m
        l2 = n
        while n > 0 and m > 0:
            if nums2[n - 1] > nums1[m - 1]:
                nums1[(m + n) - 1] = nums2[n - 1]
                n -= 1
            else:
                nums1[(m + n) - 1] = nums1[m - 1]
                m -= 1
        while m > 0:
            nums1[(m + n) - 1] = nums1[m - 1]
            m -= 1

        while n > 0:
            nums1[(m + n) - 1] = nums2[n - 1]
            n -= 1

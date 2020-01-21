import unittest

"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

    Given nums = [2, 7, 11, 15], target = 9,

    Because nums[0] + nums[1] = 2 + 7 = 9,
    return [0, 1].
"""
""" 
PseudoCode: 
Initialize a empty dictionary
for each number in the list 
    if target-num is in the dictionary
        return the index of target-mun and index of num
    else
        add num to dictionary as key and index of num as value

"""


class Solution:
    def twoSum(self, nums, target: int):
        """ The Time Complexity of this algorithm is O(n) and the Space Complexity is O(n) because of use of dictionary """
        # This stores the new  number which was traversed in the loop with its index as value
        x = {}
        if not len(nums):
            return None
        for idx, num in enumerate(nums):
            if (target - num) in x:
                return [x[target - num], idx]
            else:
                x[num] = idx
        return None

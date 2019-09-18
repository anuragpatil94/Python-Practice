'''
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3
Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2
'''

class Solution:
    def majorityElement_WithBuffer(self, nums) -> int:
        counts = dict()
        max = 0
        maxNum = 0
        
        for num in nums:
            if num not in counts:
                counts[num] = 1
            else:
                counts[num]+=1
            if max < counts[num]:
                    max = counts[num]
                    maxNum = num
        return maxNum

    def majorityElement(self, nums):
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            print(num, candidate)
            count += (1 if num == candidate else -1)

        return candidate

if __name__ == "__main__":
    Solution().majorityElement([1,2,2,2,3,3,4,4,4,4,4,4,4,4])
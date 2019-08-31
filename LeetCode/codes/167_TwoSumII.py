'''

Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2.

Note:

Your returned answers (both index1 and index2) are not zero-based.
You may assume that each input would have exactly one solution and you may not use the same element twice.
Example:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.

Idea:
   Two Pointers Approach - Since the array is sorted.
   Take a pointer from start and second from end.

'''
class Solution:
    ''' Time Complexity is O(n) Space Complexity O(1)'''
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        j = len(numbers)-1
        i = 0
        while j > i:
            if(numbers[i]+numbers[j] > target):
                j-=1
            elif(numbers[i] + numbers[j] < target):
                i+=1
            else:
                return [i+1,j+1]
        return -1
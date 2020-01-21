class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        """
        i will iterate through numbers
        j will keep track of zeros
        foundZero - flag
        """
        i = j = 0
        foundZero = 0
        while i < len(nums) and j < len(nums):
            if nums[j] != 0:
                j += 1
            else:
                foundZero = 1
            if foundZero:
                if i > j and nums[i] != 0:
                    nums[i], nums[j] = nums[j], nums[i]
                    foundZero = 0
                    j += 1
                i += 1

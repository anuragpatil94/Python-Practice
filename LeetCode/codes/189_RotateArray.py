class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        for i in range(len(nums) // 2):
            nums[i], nums[~i] = nums[~i], nums[i]
        modK = k % len(nums)
        for i in range(0, (modK // 2)):
            nums[i], nums[modK - 1 - i] = nums[modK - 1 - i], nums[i]
        j = 0
        for i in range(modK, (modK + len(nums)) // 2):
            nums[i], nums[len(nums) - 1 - j] = nums[len(nums) - 1 - j], nums[i]
            j += 1

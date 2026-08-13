class Solution(object):
    def sortColors(self, nums):
        L = 0
        R = len(nums) - 1
        i = 0
        while i <= R:
            if nums[i] == 0:
                nums[i], nums[L] = nums[L], nums[i]
                L += 1
                i += 1
            elif nums[i] == 1:
                i += 1
            elif nums[i] == 2:
                nums[i], nums[R] = nums[R], nums[i]
                R -= 1
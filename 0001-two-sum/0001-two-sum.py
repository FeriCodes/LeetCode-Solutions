class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for index, num in enumerate(nums):
            complement = target - num
            if complement in nums:
                complement_index = nums.index(complement)
                if complement_index != index:
                    return [index, complement_index]


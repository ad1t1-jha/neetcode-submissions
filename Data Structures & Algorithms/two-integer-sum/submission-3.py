class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ptr1 = 0
        ptr2 = 1
        while ptr1 < len(nums):
            if ptr2 == len(nums):
                ptr1 += 1
                ptr2 = ptr1 + 1
            if ptr1 >= len(nums) - 1:
                return []
            if nums[ptr1] + nums[ptr2] == target:
                return [ptr1, ptr2]
            else:
                ptr2 += 1
        return []
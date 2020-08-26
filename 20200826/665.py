class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        invalid_num = 0
        for i in range(1, len(nums)):
            if nums[i-1] > nums[i]:
                invalid_num = invalid_num + 1
                if i+1 < len(nums) and i-2 >= 0:
                    if nums[i+1] < nums[i-1] and nums[i-2] > nums[i]:
                        return False
            if invalid_num > 1:
                return False
        return True
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0
        length = 1
        former = nums[0]
        for i in range(len(nums)):
            if nums[i] == former:
                continue
            else:
                nums[length] = nums[i]
                length = length + 1
                former = nums[i]

        return length

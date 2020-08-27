class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for i,num in enumerate(nums):
            print(hash_map.get(target - num))
            if hash_map.get(target - num) is not None:
                return [hash_map.get(target - num), i]
            hash_map[num] = i

# get可能会返回0，所以需要用is not None而不能不加
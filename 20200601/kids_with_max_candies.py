class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result = []
        max_candy_kid = max(candies)
        for kids in candies:
            result.append(max_candy_kid <= extraCandies + kids)
        return result
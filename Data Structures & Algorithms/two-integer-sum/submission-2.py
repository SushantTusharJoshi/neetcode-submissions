class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i,n in enumerate(nums):
            difference = target - n

            if diff in seen:
                return [seen[diff],i]

            seen[n] = i
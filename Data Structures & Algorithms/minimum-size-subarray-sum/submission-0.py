class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = r = 0
        total = 0
        res = float("inf")

        while r < len(nums):
            total +=  nums[r]                # 1. grow

            while total >= target:          # 2. if or while?
                res = min(res, r - l + 1)
                total -= nums[l]              #    drop the leftmost number
                l += 1

            r += 1                         # 3. next seat
        return 0 if res == float("inf") else res
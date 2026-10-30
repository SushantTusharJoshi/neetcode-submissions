class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        seen = { 0 : 1}

        total = 0
        res = 0

        for i,n in enumerate(nums):
            total += n
            diff = total - k
            
            if diff in seen:
                res += seen[diff]
            seen[total] = seen.get(total,0) + 1

        return res
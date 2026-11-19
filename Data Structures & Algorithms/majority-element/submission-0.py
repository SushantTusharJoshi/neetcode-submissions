class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cand, score = None, 0

        for x in nums:
            if score == 0:
                cand = x
            if x == cand:
                score += 1
            else:
                score -= 1
        return cand
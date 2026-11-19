class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        cand1, cand2, score1, score2 = None, None, 0, 0
        for x in nums:
            if x == cand1:
                score1 += 1
            elif x == cand2:
                score2 += 1
            elif score1 == 0:
                cand1 = x 
                score1 = 1
            elif score2 == 0:
                cand2= x 
                score2 = 1
            else:
                score1 -= 1
                score2 -= 1
        res = []
        if nums.count(cand1) > len(nums) //3:
            res.append(cand1)
        if nums.count(cand2) > len(nums) //3:
            res.append(cand2)
        
        return res

            
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l,r = max(weights), sum(weights)
        res = r


        while l <= r:   
            cap = l + (r - l) // 2
            ships , currMax = 1,0

            for w in weights:
                if currMax + w > cap:
                    ships += 1
                    currMax = w

                else:
                    currMax += w
                
            if ships <= days:
                res = min(res,cap)
                r = cap - 1
            else:
                l = cap + 1
        
        return res

        
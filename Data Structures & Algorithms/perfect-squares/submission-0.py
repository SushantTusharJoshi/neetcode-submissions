class Solution:
    def numSquares(self, n: int) -> int:
        dp = [float("inf")] * (n + 1)
        dp[0] = 0

        for amount in range(0, n + 1):
            s = 1
            while s * s <= amount:
                dp[amount] = min(dp[amount], dp[amount - s * s] + 1)
                s += 1

            
        return dp[n]
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1                         # one way to make 0: no coins
        for c in coins:                   # coins outside → combinations
            for a in range(c, amount + 1):
                dp[a] += dp[a - c]
        return dp[amount]
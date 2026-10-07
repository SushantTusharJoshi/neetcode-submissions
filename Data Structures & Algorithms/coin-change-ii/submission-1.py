class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins.sort()
        memo = [[-1] * (amount + 1) for _ in range(len(coins) + 1)]
        def dfs(i,n):
            if n == 0:
                return 1

            if i >= len(coins):
                return 0

            if memo[i][n] != -1:
                return memo[i][n]

            res = 0
            if n >= coins[i]:
                res = dfs(i + 1 , n)
                res += dfs(i, n - coins[i])

            memo[i][n] = res

            return res
        
        return dfs(0,amount)

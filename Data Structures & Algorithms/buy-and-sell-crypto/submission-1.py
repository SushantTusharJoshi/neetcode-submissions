class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Sliding window approach.

        Track the minimum price seen so far as the buy point.
        At each price, compute the potential profit and update
        the maximum. If the current price is lower than our
        buy point, shift the window by updating the buy point.

        Time:  O(n) - single pass through prices
        Space: O(1) - two variables
        """
        max_profit = 0
        min_price = prices[0]

        for price in prices[1:]:
            if price < min_price:
                min_price = price
            else:
                max_profit = max(max_profit, price - min_price)

        return max_profit

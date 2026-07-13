class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for i in range(len(prices)):
            buy_day = i
            sell_day = i

            while sell_day < len(prices):

                if buy_day == sell_day:
                    sell_day += 1
                    continue

                max_profit = max((prices[sell_day]-prices[buy_day]), max_profit)
                sell_day += 1

        return max_profit
        
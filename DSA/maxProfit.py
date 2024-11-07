from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # n = len(prices)
        # dp = [0] * n
        # for i in range(n):
        #     for j in range(i, n - 1):
        #         if prices[j + 1] > prices[i]:
        #             dp[i] = max(dp[i], prices[j+ 1] - prices[i])
        # return max(dp)

        buy_price = prices[0]
        profit = 0
        for p in prices[1:]:
            if buy_price > p:
                buy_price = p
            profit = max(profit, p - buy_price)

        return profit

    def maxProfitImmediate(self, prices: List[int]) -> int:
        # buy_price = prices[0]
        # profit = 0

        # for p in prices[1:]:
        #     if p > buy_price:
        #         profit += p - buy_price
        #     buy_price = p

        profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i - 1]
        return profit

        return profit

solution = Solution()
print(solution.maxProfit([7,1,5,3,6,4])) #5
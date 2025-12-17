class Solution:
    def maximumProfit(self, prices: List[int], k: int) -> int:
        l = k + 1
        profit,buy,sell = [0]*l,[-inf]*l,[-inf]*l
        for p in prices:
            prev_profit = profit[0]
            for i in range(1, l):
                i_profit = profit[i]
                profit[i] = max(profit[i], buy[i] + p, sell[i] - p)
                buy[i] = max(buy[i], prev_profit - p)
                sell[i] = max(sell[i], prev_profit + p)
                prev_profit = i_profit
        return max(profit)
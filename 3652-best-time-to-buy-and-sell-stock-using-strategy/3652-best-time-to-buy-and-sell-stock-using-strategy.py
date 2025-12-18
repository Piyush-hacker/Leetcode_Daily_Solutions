class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        n = len(prices)
        m = k // 2
        T = [s * p for s, p in zip(strategy, prices)]
        base_profit = sum(T)
        
        num_segments = n - k + 1
        if num_segments <= 0:
            return base_profit
            
        A_val = sum(prices[m:k])
        B_val = sum(T[:k])
        best_expr = A_val - B_val
        
        for L in range(1, num_segments):
            A_val = A_val - prices[L - 1 + m] + prices[L + k - 1]
            B_val = B_val - T[L - 1] + T[L + k - 1]
            current_expr = A_val - B_val
            if current_expr > best_expr:
                best_expr = current_expr
                
        return base_profit + max(0, best_expr)
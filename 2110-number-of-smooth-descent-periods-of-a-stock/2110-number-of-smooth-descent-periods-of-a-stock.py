class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        
        total = 0
        current_streak = 1

        for i in range(len(prices) - 1): 
            
            if prices[i] - 1 == prices[i + 1]: # extend sequence
                current_streak += 1

            else: # end sequence 
                # s_n = 0.5 * n * (n + 1)
                total +=  current_streak * (current_streak + 1)
                current_streak = 1

        total += current_streak * (current_streak + 1)

        # only divs once 
        return total // 2
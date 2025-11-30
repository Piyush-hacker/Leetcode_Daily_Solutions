class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total_sum = sum(nums) % p
        if total_sum == 0:
            return 0
            
        res = len(nums)
        dp = {0 : -1}
        curr = 0
        for i, s in enumerate(nums):
            curr = (curr + s) % p
            dp[curr] = i
            
            if (curr - total_sum) % p in dp:
                res = min(res, i - dp[(curr - total_sum) % p])
            
        return res if res < len(nums) else -1
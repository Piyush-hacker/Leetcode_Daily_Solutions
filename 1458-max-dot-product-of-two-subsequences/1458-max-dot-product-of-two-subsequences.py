class Solution:
    def maxDotProduct(self, nums1, nums2):
        n, m = len(nums1), len(nums2)
        NEG_INF = -10**9

        memo = [[None] * m for _ in range(n)]

        def dp(i, j):
            if i == n or j == m:
                return NEG_INF

            if memo[i][j] is not None:
                return memo[i][j]

            take = nums1[i] * nums2[j]

            res = max(
                take + dp(i + 1, j + 1),  
                take,                    
                dp(i + 1, j),             
                dp(i, j + 1)              
            )

            memo[i][j] = res
            return res

        return dp(0, 0)
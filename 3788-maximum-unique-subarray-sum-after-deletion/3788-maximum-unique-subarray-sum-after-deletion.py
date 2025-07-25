class Solution:
    def maxSum(self, nums: List[int]) -> int:
        return M if (M:=max(nums))<=0 else sum(x for x in set(nums) if x>0)
        
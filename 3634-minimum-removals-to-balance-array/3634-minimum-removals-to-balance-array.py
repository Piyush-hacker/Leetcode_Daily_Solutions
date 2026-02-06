class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        n=len(nums)
        if len(nums)==1:
            return 0
        nums.sort()
        i,mx_len=0,1
        for j in range(n):
            while nums[j]>k*nums[i]:
                i+=1
            mx_len=max(mx_len,j-i+1)
        return n-mx_len
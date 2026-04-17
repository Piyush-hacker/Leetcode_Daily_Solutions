class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        #Solution2 
        n = len(nums)
        ans = float("inf")
        hmap = dict()
        for i in range(n):
            num = nums[i]
            if num in hmap:
                ans = min(ans, i-hmap[num])
            rev_s=str(num)[::-1]
            rev_num=int(rev_s)
            hmap[rev_num]=i
        return -1 if ans == float("inf") else ans
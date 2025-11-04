class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        counts = {}
        for i in range(k-1):
            counts[nums[i]] = counts.get(nums[i],0) + 1

        def x_sum(d):
            return sum(a*b for a,b in sorted(d.items(),key=lambda p:(-p[1],-p[0]))[:min(x,len(d))])

        result = []
        for i in range(k-1,len(nums)):
            counts[nums[i]] = counts.get(nums[i],0) + 1
            result.append(x_sum(counts))
            counts[nums[i-k+1]] -= 1
        return result

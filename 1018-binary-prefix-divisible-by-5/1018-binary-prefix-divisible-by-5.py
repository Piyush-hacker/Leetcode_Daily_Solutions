class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        rem = 0
        return [(rem := (rem * 2 + val) % 5) == 0 for val in nums]
        
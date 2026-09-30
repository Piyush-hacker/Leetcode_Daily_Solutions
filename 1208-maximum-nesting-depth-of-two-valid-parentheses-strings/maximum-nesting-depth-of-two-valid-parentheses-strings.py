class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        return [*map(countOf, cycle('()'), seq)]
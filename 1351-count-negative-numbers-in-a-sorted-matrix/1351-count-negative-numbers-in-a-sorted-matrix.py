class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        return sum([bisect_right(row[::-1], -1) for row in grid])
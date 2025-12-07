class Solution:
    def countOdds(self, l: int, h: int) -> int:
        return -~h//2-l//2
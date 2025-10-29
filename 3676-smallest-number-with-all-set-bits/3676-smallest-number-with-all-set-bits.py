class Solution:
    def smallestNumber(self, n: int) -> int:
        result = 0
        i = 0
        while result < n:
            result += 2 ** i
            i += 1
        return result
class Solution(object):
    def differenceOfSums(self, n, m):
        return n * (n + 1) // 2 - m * (n // m) * (n // m + 1)
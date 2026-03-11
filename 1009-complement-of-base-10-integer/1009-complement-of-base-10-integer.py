class Solution:
    def bitwiseComplement(self, n: int) -> int:

        if n == 0: return 1
        ct, m = 1, n

        while m:
            m//= 2
            ct*= 2

        return n ^ (ct - 1)
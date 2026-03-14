class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        total = 3 * (2**(n - 1))
        if k > total:
            return ""

        res = []
        chars = ['a', 'b', 'c']

        for i in range(n):
            block = 2**(n - i - 1)
            for c in chars:
                if res and res[-1] == c:
                    continue
                if k > block:
                    k -= block
                else:
                    res.append(c)
                    break
        
        return "".join(res)
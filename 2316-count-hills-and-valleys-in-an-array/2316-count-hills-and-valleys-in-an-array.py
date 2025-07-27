class Solution:
    def countHillValley(self, a: List[int]) -> int:
        b = [v for v,_ in groupby(a)]
        return sum(l>m<r or l<m>r for l,m,r in zip(b,b[1:],b[2:]))
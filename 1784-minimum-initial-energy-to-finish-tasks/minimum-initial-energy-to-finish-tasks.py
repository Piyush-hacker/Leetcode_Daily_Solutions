class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:

        heap = []
        for i, j in tasks:
            heapq.heappush(heap, (-(j - i), i, j))

        ac = 0
        ans = 0
        while heap:
            t, a, r = heapq.heappop(heap)
            r = abs(r)
            a = abs(a) 
            
            
            if ac < r:
                ans += (r - ac)
                ac = r
                ac -= a
            else:
                ac -= a

        return(ans)
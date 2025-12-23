class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        events.sort()
        heap = []
        res, curr = 0, 0

        for start, end, value in events:
            while heap and heap[0][0] < start:
                    curr = max(curr, heapq.heappop(heap)[1])
            
            res = max(res, value + curr)
            heapq.heappush(heap, (end, value))
        
        return res
 
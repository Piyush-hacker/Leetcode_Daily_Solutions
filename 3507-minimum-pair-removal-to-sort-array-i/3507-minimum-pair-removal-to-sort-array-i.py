from typing import List
import heapq

class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0
        def is_non_decreasing():
            return all(nums[i] >= nums[i-1] for i in range(1, len(nums)))
        if is_non_decreasing():
            return 0
        left = list(range(-1, n))
        right = list(range(1, n + 1))
        alive = [True] * n
        heap = []
        for i in range(n - 1):
            heapq.heappush(heap, (nums[i] + nums[i + 1], i))
        ops = 0
        alive_count = n
        while alive_count > 1:
            while True:
                s, i = heapq.heappop(heap)
                j = right[i]
                if j < n and alive[i] and alive[j] and nums[i] + nums[j] == s:
                    break
            nums[i] = s
            alive[j] = False
            alive_count -= 1
            rj = right[j]
            right[i] = rj
            if rj < n:
                left[rj] = i
            li = left[i]
            if li >= 0 and alive[li]:
                heapq.heappush(heap, (nums[li] + nums[i], li))
            if right[i] < n and alive[right[i]]:
                heapq.heappush(heap, (nums[i] + nums[right[i]], i))
            ops += 1
            prev = -10**18
            ok = True
            k = 0
            while k < n:
                if alive[k]:
                    if nums[k] < prev:
                        ok = False
                        break
                    prev = nums[k]
                k += 1
            if ok:
                break
        return ops


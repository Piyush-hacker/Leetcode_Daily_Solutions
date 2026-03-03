from typing import List

class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        n = len(heights)
        ans = [0] * n
        stack = []  # decreasing stack of heights to the right

        for i in range(n - 1, -1, -1):
            count = 0

            # See all shorter people until a taller blocks the view
            while stack and stack[-1] < heights[i]:
                stack.pop()
                count += 1

            # If there's a taller person left, you can see them too
            if stack:
                count += 1

            ans[i] = count
            stack.append(heights[i])

        return ans